@echo off
echo ==========================
echo Starting Ada System...
echo ==========================

REM Step 1: Launch Docker Desktop
echo Launching Docker Desktop...
start "" "C:\Program Files\Docker\Docker\Docker Desktop.exe"
timeout /t 10 >nul

REM Step 2: Navigate to Open WebUI folder
cd /d F:\MISC\CHET\ADA\open-webui

REM Step 3: Start containers silently
echo Starting Open WebUI + Ollama...
docker compose up -d >nul

REM Step 4: Open Ada in browser
start http://127.0.0.1:3000

echo ==========================
echo Ada is online 🖤
echo This window will close in 60 seconds...
timeout /t 60 >nul

exit
