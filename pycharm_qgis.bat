@echo off
chcp 65001 >nul
setlocal enabledelayedexpansion

REM Устанавливаем корневую папку QGIS
set "QGIS_ROOT=D:\Programs\QGIS 3.40.13"
set "PYCHARM_PATH=C:\Program Files\JetBrains\PyCharm Community Edition 2024.3.2\bin\pycharm64.exe"

echo ============================================
echo Настройка окружения QGIS 3.40.13 для PyCharm
echo ============================================

REM 1. Полностью очищаем и устанавливаем правильные пути (БЕЗ пробелов в конце!)
set "PATH=%QGIS_ROOT%\bin"
set "PATH=%PATH%;%QGIS_ROOT%\apps\qgis-ltr\bin"
set "PATH=%PATH%;%QGIS_ROOT%\apps\Python312"
set "PATH=%PATH%;%QGIS_ROOT%\apps\Python312\Scripts"
set "PATH=%PATH%;%QGIS_ROOT%\apps\Qt5\bin"
set "PATH=%PATH%;%WINDIR%\system32"
set "PATH=%PATH%;%WINDIR%"
set "PATH=%PATH%;%WINDIR%\system32\WBem"

echo Путь PATH установлен

REM 2. Критически важные переменные QGIS (БЕЗ пробелов в конце!)
set "QGIS_PREFIX_PATH=%QGIS_ROOT:\=/%/apps/qgis-ltr"
set "GDAL_FILENAME_IS_UTF8=YES"
set "VSI_CACHE=TRUE"
set "VSI_CACHE_SIZE=1000000"
set "QT_PLUGIN_PATH=%QGIS_ROOT%\apps\qgis-ltr\qtplugins"

REM 3. Python настройки (ВАЖНО: без пробелов!)
set "PYTHONHOME=%QGIS_ROOT%\apps\Python312"
set "PYTHONPATH=%QGIS_ROOT%\apps\qgis-ltr\python"

REM 4. Проверка импорта QGIS
echo.
echo Проверка импорта QGIS из командной строки...
echo import sys > "%TEMP%\qgis_test.py"
echo print("PYTHONHOME:", sys.prefix) >> "%TEMP%\qgis_test.py"
echo print("PYTHONPATH:", sys.path) >> "%TEMP%\qgis_test.py"
echo sys.path.insert(0, r'%QGIS_ROOT%\apps\qgis-ltr\python') >> "%TEMP%\qgis_test.py"
echo try: >> "%TEMP%\qgis_test.py"
echo     from qgis.core import * >> "%TEMP%\qgis_test.py"
echo     print('УСПЕХ: QGIS', Qgis.QGIS_VERSION, 'загружен в командной строке!') >> "%TEMP%\qgis_test.py"
echo except Exception as e: >> "%TEMP%\qgis_test.py"
echo     print('ОШИБКА в командной строке:', e) >> "%TEMP%\qgis_test.py"

"%QGIS_ROOT%\apps\Python312\python.exe" "%TEMP%\qgis_test.py"
del "%TEMP%\qgis_test.py"

REM 5. Создаем скрипт для запуска PyCharm БЕЗ PYTHONHOME (это вызывает проблемы)
echo.
echo Создание окружения для PyCharm...

echo @echo off > "%TEMP%\pycharm_env.bat"
echo chcp 65001 ^>nul >> "%TEMP%\pycharm_env.bat"
echo echo ============================================ >> "%TEMP%\pycharm_env.bat"
echo echo PyCharm запускается с окружением QGIS >> "%TEMP%\pycharm_env.bat"
echo echo ============================================ >> "%TEMP%\pycharm_env.bat"
echo. >> "%TEMP%\pycharm_env.bat"

echo REM Устанавливаем переменные окружения (БЕЗ PYTHONHOME!) >> "%TEMP%\pycharm_env.bat"
echo set PATH=%PATH% >> "%TEMP%\pycharm_env.bat"
echo set PYTHONPATH=%PYTHONPATH% >> "%TEMP%\pycharm_env.bat"
echo set QGIS_PREFIX_PATH=%QGIS_PREFIX_PATH% >> "%TEMP%\pycharm_env.bat"
echo set QT_PLUGIN_PATH=%QT_PLUGIN_PATH% >> "%TEMP%\pycharm_env.bat"
echo. >> "%TEMP%\pycharm_env.bat"

echo REM Проверяем окружение >> "%TEMP%\pycharm_env.bat"
echo echo Путь к Python: %QGIS_ROOT%\apps\Python312\python.exe >> "%TEMP%\pycharm_env.bat"
echo echo PYTHONPATH: %%PYTHONPATH%% >> "%TEMP%\pycharm_env.bat"
echo echo. >> "%TEMP%\pycharm_env.bat"

echo REM Запускаем PyCharm >> "%TEMP%\pycharm_env.bat"
echo start "PyCharm with QGIS" /B "%PYCHARM_PATH%" >> "%TEMP%\pycharm_env.bat"

REM 6. Запускаем PyCharm
echo.
echo ============================================
echo Запуск PyCharm...
echo ============================================

start "QGIS Environment" /MIN cmd /c "%TEMP%\pycharm_env.bat"

timeout /t 3 >nul
echo PyCharm должен был запуститься.
echo.
echo Важно: Не создавайте виртуальное окружение автоматически!
echo При создании проекта выберите:
echo 1. "Previously configured interpreter"
echo 2. Или добавьте вручную: D:\Programs\QGIS 3.40.13\apps\Python312\python.exe
echo.
echo Нажмите любую клавишу для завершения...
pause >nul