## КиноБот
Поможет с выбором фильма на вечер. Просто укажите боту название фильма, а он подскажет похожие фильмы.

## Установка
- Создайте телеграм-бот
- Получите авторизационные данные gigachat
- Установите Python
- Создайте папку проекта
- Склонируйте репозиторий

```git clone https://github.com/lDenisKl/MovieBot.git```
- Создайте окружение командой

```python3 -m venv venv```
- Активируйте окружение командой:

Windows - ```venv/scripts/activate.ps1```

Linux - ```source venv/bin/activate```
- Установите зависимости командой

```pip install -r requirements.txt```
- Переименуйте файл ```secret.example.py``` в ```secret.py``` и внесите в него свои данные;
- Запустите ТГ-бот

```python main.py```
Для Linux используйте pip3 и python3

## Зависимости
Эта программа разрабатывалась на интепретаторе Python версии 3.8;

Использована бибиотека pyTelegramBotAPI версии 4.10;

Для работы бота необходим сертификат Минцифры, токен телеграмм-бота и авторизационные данные gigachat.