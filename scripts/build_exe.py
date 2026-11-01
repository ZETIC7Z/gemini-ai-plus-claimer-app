"""
Build script to compile ZETICUZ AI PLUS GEN into a standalone Windows executable.
Usage: python scripts/build_exe.py
"""

import os
import sys
import subprocess
import shutil

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APP_SCRIPT = os.path.join(ROOT_DIR, "app", "zeticuz_ai_plus_gen.py")
ICON_FILE = os.path.join(ROOT_DIR, "images", "app_icon.ico")
DIST_DIR = os.path.join(ROOT_DIR, "dist")
BUILD_DIR = os.path.join(ROOT_DIR, "build")

def build():
    print("=" * 60)
    print("Building ZETICUZ AI PLUS GEN Portable Windows Executable...")
    print("=" * 60)

    ENGINE_DIR = os.path.join(ROOT_DIR, "app", "engine")
    IMAGES_DIR = os.path.join(ROOT_DIR, "images")

    cmd = [
        sys.executable,
        "-m",
        "PyInstaller",
        "--noconfirm",
        "--onedir" if "--onedir" in sys.argv else "--onefile",
        "--windowed",
        f"--name=Zeticuz AI Plus Gen",
        f"--icon={ICON_FILE}",
        f"--add-data={ICON_FILE};images",
        f"--add-data={ENGINE_DIR};engine",
        f"--add-data={IMAGES_DIR};images",
        "--collect-all=customtkinter",
        APP_SCRIPT
    ]

    print("Running command:", " ".join(cmd))
    res = subprocess.run(cmd, cwd=ROOT_DIR)
    if res.returncode == 0:
        print("\n[SUCCESS] Executable built successfully!")
        print(f"Check: {os.path.join(DIST_DIR, 'Zeticuz AI Plus Gen.exe')}")
    else:
        print(f"\n[ERROR] PyInstaller failed with code {res.returncode}")
        sys.exit(res.returncode)

if __name__ == "__main__":
    build()
