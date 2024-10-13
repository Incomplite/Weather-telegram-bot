# Weather Telegram Bot

Этот проект представляет собой Telegram-бота, который позволяет пользователям узнать текущую погоду в любом городе. Бот использует **API OpenWeatherMap** для получения данных о погоде и предоставляет их в удобном формате.

## Функциональность
- **Проверка погоды**: Пользователи могут ввести название города, чтобы получить информацию о текущей погоде, включая температуру, влажность и описание погодных условий.



## Установка и запуск

1. Клонирование репозитория

```bash
git clone https://github.com/Incomplite/Weather-telegram-bot.git
cd Weather-telegram-bot
```

2. Создание виртуального окружения

```bash
python3 -m venv venv
venv/Scripts/activate
```

3. Установка зависимостей

```bash
pip3 install -r requirements.txt
```

6. Создайте файл **.env** и добавьте туда свои токены

```bash
BOT_TOKEN = 'Ваш_Telegram_Bot_Token'
WEATHER_API_KEY = 'Ваш_OpenWeatherMap_API_Key'
```

7. Запуск бота.

```bash
python main.py
```

## Поддержка
Если у вас возникли сложности или вопросы по использованию, создайте 
[обсуждение](https://github.com/Incomplite/Weather-telegram-bot/issues/new/choose) в данном репозитории или напишите на электронную почту <blocktapok@gmail.com>.
