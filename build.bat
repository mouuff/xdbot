rmdir /s /q build
mkdir build
cd build
python -m PyInstaller -i ..\icon.ico --onefile ..\xdbot\__main__.py
move dist\__main__.exe xdbot.exe
xcopy ..\xdbot\res res
cd ..
