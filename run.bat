@echo off

cd C:\Users\david\Documents\Dev\ex2bib
ECHO Path Done!
if %ERRORLEVEL% neq 0 goto exit

call venv\Scripts\activate
if %ERRORLEVEL% neq 0 goto createVenv
goto runner

:createVenv
ECHO CREATING VENV
call python -m venv venv
call venv\Scripts\activate
call pip install -r requirements.txt

:runner
ECHO Running
venv\Scripts\python.exe ex2bib.py --david
pause
deactivate
