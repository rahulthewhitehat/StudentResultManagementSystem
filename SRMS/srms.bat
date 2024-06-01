@echo off
REM Run the Python login script

REM Set the path to the Python file
SET PYTHON_FILE=C:\Users\RAHUL\OneDrive\Desktop\SRMS\login.py

REM Check if the Python file exists
IF NOT EXIST "%PYTHON_FILE%" (
    echo The file %PYTHON_FILE% does not exist.
    exit /b 1
)

REM Run the Python file
python "%PYTHON_FILE%"

REM Check if the Python script ran successfully
IF %ERRORLEVEL% NEQ 0 (
    echo The Python script encountered an error.
    exit /b 1
)

echo The Python script ran successfully.
exit /b 0
