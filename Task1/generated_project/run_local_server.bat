@echo off
cd /d "%~dp0"
call conda activate ai_in_se_chapter_04
python app\main.py
pause
