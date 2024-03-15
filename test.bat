@REM @echo off
chcp 65001
@REM python mykotlinc.py test.kt -w --no-rebuild --configuration-cache --parallel --daemon --build-cache --max-workers 6

@REM pyinstaller --onefile mykotlinc.py

@REM "./mykotlinc" test.kt

python mykotlinc.py test.kt -w --no-rebuild --configuration-cache --parallel --daemon --build-cache

python mykotlinc.py test.kt

python mykotlinc.py test.kt clear

"./mykotlinc" test.kt

"./mykotlinc" test.kt -w --no-rebuild --configuration-cache --parallel --daemon --build-cache

"./mykotlinc" test.kt clear

python D:\学校作业及其他\考研\mykotlinc\mykotlincoutside.py D:\学校作业及其他\考研\mykotlinc\test.kt clear -w --no-rebuild --configuration-cache --parallel --daemon --build-cache --max-workers 6

python mykotlincoutside.py D:\学校作业及其他\考研\mykotlinc\test.kt

python mykotlincoutside.py D:\学校作业及其他\考研\mykotlinc\test.kt clear