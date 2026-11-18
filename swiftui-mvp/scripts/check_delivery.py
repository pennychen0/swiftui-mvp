#!/usr/bin/env python3
"""Check the Xcode entry and 120 MB limits for a full folder and optional ZIP."""

import argparse
import os
from pathlib import Path, PurePosixPath
import stat
import sys
import zipfile


MAX_DELIVERY_BYTES = 120_000_000


def folder_files(project_dir, errors):
    """Count every file's logical bytes; do not omit caches or follow links."""
    sizes = {}

    def on_error(error):
        errors.append(f"無法完整量測資料夾：{error}")

    for directory, dirs, files in os.walk(project_dir, onerror=on_error, followlinks=False):
        for name in dirs + files:
            path = Path(directory) / name
            mode = path.lstat().st_mode
            if stat.S_ISLNK(mode):
                errors.append(f"交付必須自足，不可使用符號連結：{path}")
            elif stat.S_ISREG(mode):
                sizes[path.relative_to(project_dir).as_posix()] = path.stat().st_size
            elif not stat.S_ISDIR(mode):
                errors.append(f"交付含無法量測的一般檔案以外項目：{path}")
    return sizes


def check(project_dir, zip_path=None):
    errors = []
    if not project_dir.is_dir():
        return [f"專案資料夾不存在：{project_dir}"]
    if project_dir.is_symlink():
        errors.append("專案資料夾本身不可是符號連結。")
    children = sorted(project_dir.iterdir(), key=lambda path: path.name)
    print(f"第一層實際內容：{project_dir}")
    for child in children:
        print(f"  {child.name}{'/' if child.is_dir() else ''}")
    projects = [child for child in children if child.suffix == ".xcodeproj"]
    if not projects:
        errors.append("第一層找不到 .xcodeproj，請重整交付副本並修正引用。")
    for project in projects:
        if project.is_symlink() or not (project / "project.pbxproj").is_file():
            errors.append(f"不是完整的實體 Xcode 專案：{project.name}")
    for child in children:
        if child.suffix == ".xcworkspace":
            if child.is_symlink() or not (child / "contents.xcworkspacedata").is_file():
                errors.append(f"不是完整的實體 workspace：{child.name}")
    sizes = folder_files(project_dir, errors)
    folder_size = sum(sizes.values())
    print(f"完整專案資料夾大小：{folder_size} bytes")
    if folder_size > MAX_DELIVERY_BYTES:
        errors.append(f"完整專案資料夾超過 {MAX_DELIVERY_BYTES} bytes。")
    if zip_path is not None:
        try:
            size = zip_path.stat().st_size
            print(f"ZIP 實際大小：{size} bytes")
            if size > MAX_DELIVERY_BYTES:
                errors.append(f"ZIP 超過 {MAX_DELIVERY_BYTES} bytes。")
            with zipfile.ZipFile(zip_path) as archive:
                members = archive.infolist()
                names = set(info.filename for info in members)
                if len(names) != len(members):
                    errors.append("ZIP 內有重複路徑。")
                unpacked_size = sum(info.file_size for info in members)
                print(f"ZIP 內容未壓縮總量：{unpacked_size} bytes")
                if unpacked_size > MAX_DELIVERY_BYTES:
                    errors.append(f"ZIP 內容未壓縮總量超過 {MAX_DELIVERY_BYTES} bytes。")
                else:
                    bad_member = archive.testzip()
                    if bad_member:
                        errors.append(f"ZIP 完整性檢查失敗：{bad_member}")
                paths = [PurePosixPath(name) for name in names]
                if not paths or any(
                    path.is_absolute() or ".." in path.parts or not path.parts
                    for path in paths
                ) or any("\\" in name for name in names):
                    errors.append("ZIP 為空或含不安全的路徑。")
                if {path.parts[0] for path in paths if path.parts} != {project_dir.name}:
                    errors.append("ZIP 最外層必須只有一個與專案同名的資料夾。")
                if any(len(PurePosixPath(name).parts) == 1 and not name.endswith("/")
                       for name in names):
                    errors.append("ZIP 最外層不可有散落檔案。")
                for project in projects:
                    expected = f"{project_dir.name}/{project.name}/project.pbxproj"
                    if expected not in names:
                        errors.append(f"ZIP 缺少第一層的專案設定：{expected}")
                for info in members:
                    if stat.S_ISLNK(info.external_attr >> 16):
                        errors.append(f"ZIP 不可含符號連結：{info.filename}")
                prefix = project_dir.name + "/"
                packed_sizes = {
                    info.filename[len(prefix):]: info.file_size
                    for info in members
                    if not info.is_dir() and info.filename.startswith(prefix)
                }
                if packed_sizes != sizes:
                    errors.append("專案資料夾與 ZIP 的檔案清單或大小不一致，請檢查實際解壓副本。")
        except (OSError, zipfile.BadZipFile, RuntimeError, NotImplementedError) as error:
            errors.append(f"無法驗證 ZIP：{error}")
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project_dir", type=Path)
    parser.add_argument("--zip", dest="zip_path", type=Path)
    args = parser.parse_args()
    try:
        errors = check(args.project_dir, args.zip_path)
    except OSError as error:
        errors = [f"無法讀取專案：{error}"]
    if errors:
        for error in errors:
            print(f"FAIL: {error}", file=sys.stderr)
        return 1
    print("PASS: 第一層入口與 120 MB 大小檢查通過；引用、建置與互動仍須另行驗證。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
