@echo off
cd /d "%~dp0"
echo [TraceLock] Running multihreaded username scan with colored output...

:: Change the username and output file below as needed
set USERNAME=zaqar
set OUTPUT=results.json

python main.py --username %USERNAME% --output %OUTPUT% 
pause