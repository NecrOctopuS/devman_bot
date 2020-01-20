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
params = {}
while True:
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        json_data = response.json()
        if json_data['status'] == 'found':
            attempts = json_data['new_attempts']
            for attempt in attempts:
                if attempt['is_negative']:
                    bot.send_message(chat_id=TELEGRAM_ID, text=f"У вас проверили работу {attempt['lesson_title']} \n"
                                                               f"https://dvmn.org{attempt['lesson_url']}\n"
                                                               f"В работе нашлись ошибки")
                else:
                    bot.send_message(chat_id=TELEGRAM_ID, text=f"У вас проверили работу {attempt['lesson_title']} \n"
                                                               f"https://dvmn.org{attempt['lesson_url']}\n"
                                                               f"В работе нет ошибок")
        params = {
            'timestamp': json_data['last_attempt_timestamp']
        }
    except requests.exceptions.ReadTimeout:
        time.sleep(0.1)
    except requests.exceptions.ConnectionError:
        time.sleep(1)
    except ConnectionResetError:
        time.sleep(1)
    except requests.exceptions.HTTPError as exception:
        print(exception.response.text)
        time.sleep(1)
