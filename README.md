Добро пожаловать!<br>
Если вотникнут проблемы с TTS переводом то установите pypiwin32 "pip install pypiwin32".
Если установка пакета не помогла то
Перейдите в AppData.
Откройте проводник и напишете в проводнике "%appdata%" и затем Enter
Вы попадёте в папку AppData>Roaming
Далее перейдите в каталог Python\Версия вашего питона\site-packages\pywin32_system32
и найдите там pythoncom38.dll и pywintypes38.dll
скопируйте эти 2 файла при помощи CTRL+C
Далее переходим в папку Python\Python38\site-packages\win32\lib и копируем туда
Плюс переходим в папку Python\Python38\site-packages\win32 и тоже копируем туда эти файлы
После этих манипуляция всё должно заработать)
