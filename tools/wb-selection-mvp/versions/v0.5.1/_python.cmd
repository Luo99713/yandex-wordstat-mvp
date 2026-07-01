@echo off
setlocal
set "PYTHON_EXE="
where py >nul 2>nul
if not errorlevel 1 (
  for /f "delims=" %%P in ('py -3 -c "import sys; print(sys.executable)" 2^>nul') do set "PYTHON_EXE=%%P"
)
if not defined PYTHON_EXE (
  where python >nul 2>nul
  if not errorlevel 1 (
    for /f "delims=" %%P in ('python -c "import sys; print(sys.executable)" 2^>nul') do set "PYTHON_EXE=%%P"
  )
)
if not defined PYTHON_EXE (
  echo Python was not found. Please install Python 3.8+ and add it to PATH.
  exit /b 1
)
set "PYTHONUTF8=1"
set "PYTHONIOENCODING=utf-8"
"%PYTHON_EXE%" %*
