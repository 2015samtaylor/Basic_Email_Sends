@echo off
cd C:\Users\samuel.taylor\Desktop\Python_Scripts\Log_Sender
python.exe Log_Sender.py > Logs/batch_output.txt 2>&1

@REM virtual env example
@REM @echo off
@REM cd /d C:\Users\psadmin\Desktop\DW\NWEA
@REM pipenv run python Log_Sender.py
