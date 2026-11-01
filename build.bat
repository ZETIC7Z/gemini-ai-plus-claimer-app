@echo off
echo ============================================================
echo   Compiling ZETICUZ AI PLUS GEN Windows Standalone Binary
echo   Developer: Sam Pangilinan (ZETICUZ)
echo ============================================================
python -m pip install -r app/requirements.txt
python scripts/build_exe.py
pause
