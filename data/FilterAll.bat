for /f "delims=|" %%f in ('dir /b .\in\') do FilterOne.bat "%%f"
pause
