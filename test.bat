@REM @echo off
@REM chcp 65001
@REM python mykotlinc.py test.kt -w --no-rebuild --configuration-cache --parallel --daemon --build-cache --max-workers 6

@REM pyinstaller --onefile mykotlinc.py

@REM "./mykotlinc" test.kt

python mykotlinc.py test.kt -w --no-rebuild --configuration-cache --parallel --daemon --build-cache
