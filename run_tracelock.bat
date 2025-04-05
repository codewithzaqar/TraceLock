@echo off
cd /d "%~dp0"
echo [TraceLock] Running username checker...

:: Change the username and output file below as needed
set USERNAME=codewithzaqar
set OUTPUT=results.txt

python main.py --username %USERNAME% --output %OUTPUT% 
pause