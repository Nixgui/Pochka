Добро пожаловать!<br>
Перед заруском установить pyttsx3 "pip install pyttsx3"<br>
Если вотникнут проблемы с TTS переводом то установите pypiwin32 "pip install pypiwin32".<br>
Если установка пакета не помогла то перейдите в AppData.<br>
Откройте проводник и напишете в проводнике "%appdata%" и затем Enter<br>
Вы попадёте в папку AppData>Roaming<br>
Далее перейдите в каталог Python\Версия вашего питона\site-packages\pywin32_system32<br>
и найдите там pythoncom38.dll и pywintypes38.dll<br>
скопируйте эти 2 файла при помощи CTRL+C<br>
Далее переходим в папку Python\Python38\site-packages\win32\lib и копируем туда<br>
Плюс переходим в папку Python\Python38\site-packages\win32 и тоже копируем туда эти файлы<br>
После этих манипуляция всё должно заработать)<br>
