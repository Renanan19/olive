@echo off
REM Lance le generateur depuis le dossier du projet, quel que soit le repertoire
REM courant. %~dp0 = dossier de ce fichier .bat.
cd /d "%~dp0"
python generate_atlas_video.py %*
echo.
pause
