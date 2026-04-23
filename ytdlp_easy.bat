@echo off
setlocal EnableDelayedExpansion
title YT-DLP Easy CLI

:start
cls
echo ==================================================
echo                YT-DLP Easy CLI
echo ==================================================
echo.

set /p "url=1. Enter the YouTube link to download: "
if "%url%"=="" (
    echo Error: URL cannot be empty.
    pause
    goto start
)

echo.
echo 2. What do you want to download?
echo    [1] Video (MKV)
echo    [2] Audio Only (MP3)
echo.
set /p "choice=Enter your choice (1 or 2): "

if "%choice%"=="1" goto video_menu
if "%choice%"=="2" goto audio_menu

echo Invalid choice.
pause
goto start

:video_menu
echo.
echo Select Video Quality:
echo    [1] 720p
echo    [2] 1080p
echo    [3] 2K (1440p)
echo    [4] 4K (2160p)
echo    [5] Best Quality Available
echo.
set /p "v_choice=Enter your choice (1-5): "

if "%v_choice%"=="1" set "format=bestvideo[height<=720]+bestaudio/best[height<=720]"
if "%v_choice%"=="2" set "format=bestvideo[height<=1080]+bestaudio/best[height<=1080]"
if "%v_choice%"=="3" set "format=bestvideo[height<=1440]+bestaudio/best[height<=1440]"
if "%v_choice%"=="4" set "format=bestvideo[height<=2160]+bestaudio/best[height<=2160]"
if "%v_choice%"=="5" set "format=bestvideo+bestaudio/best"

if not defined format set "format=bestvideo+bestaudio/best"

echo.
echo Starting video download...
yt-dlp -f "%format%" --merge-output-format mkv "%url%"
goto end

:audio_menu
echo.
echo Select Audio Quality:
echo    [1] 128 kbps
echo    [2] 192 kbps
echo    [3] 256 kbps
echo    [4] 320 kbps
echo    [5] Best Audio
echo.
set /p "a_choice=Enter your choice (1-5): "

if "%a_choice%"=="1" set "a_qual=128K"
if "%a_choice%"=="2" set "a_qual=192K"
if "%a_choice%"=="3" set "a_qual=256K"
if "%a_choice%"=="4" set "a_qual=320K"
if "%a_choice%"=="5" set "a_qual=0"

if not defined a_qual set "a_qual=0"

echo.
echo Starting audio download...
yt-dlp -f bestaudio --extract-audio --audio-format mp3 --audio-quality "%a_qual%" "%url%"
goto end

:end
echo.
echo Download process finished!
pause
goto start
