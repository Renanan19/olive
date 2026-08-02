@echo off
REM Lance le generateur couleur depuis le dossier du projet, quel que soit le
REM repertoire courant. %~dp0 = dossier de ce fichier .bat.
cd /d "%~dp0"
python generate_atlas_video_couleur.py %*
echo.
pause
