@REM Parametro 1 = file.py da compilare
pyinstaller.exe .\%1 --clean --onefile --windowed --noconsole
rd /s /q build
set str=%1
set str=%str:~0,-3%
del %str%.spec
mkdir .\bin\
copy .\dist\%str%.exe .\bin\ /B
rd /s /q dist
