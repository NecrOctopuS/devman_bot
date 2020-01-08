import requests
import time
import telegram
from dotenv import load_dotenv
import os


load_dotenv()
DEVMAN_TOKEN = os.getenv('DEVMAN_TOKEN')
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
TELEGRAM_ID = int(os.getenv('TELEGRAM_ID'))
bot = telegram.Bot(token=TELEGRAM_TOKEN)


url = 'https://dvmn.org/api/long_polling/'
headers = {
    'Authorization': 'Token ' + DEVMAN_TOKEN,
}
response = requests.get(url, headers=headers)
while True:
    if response.json()['status'] == 'timeout':
        params = {
            'timestamp': response.json()['timestamp_to_request']
        }
    elif response.json()['status'] == 'found':
        attempts = response.json()['new_attempts']
        for attempt in attempts:
            bot.send_message(chat_id=TELEGRAM_ID, text=f"У вас проверили работу {attempt['lesson_title']} \n"
                                                       f" {'https://dvmn.org' + attempt['lesson_url']}")
            if attempt['is_negative']:
                bot.send_message(chat_id=TELEGRAM_ID, text=f"В работе нашлись ошибки")
            else:
                bot.send_message(chat_id=TELEGRAM_ID, text=f"В работе нет ошибок")
        params = {
            'timestamp': response.json()['new_attempts'][0]['timestamp']
        }
    try:
        response = requests.get(url, headers=headers, params=params)
    except requests.exceptions.ReadTimeout:
        time.sleep(5)
    except requests.exceptions.ConnectionError:
        time.sleep(5)
    except ConnectionResetError:
        time.sleep(5)
