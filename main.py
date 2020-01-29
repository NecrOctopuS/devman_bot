import requests
import time
import telegram
import os
import logging
from dotenv import load_dotenv

if __name__ == '__main__':
    load_dotenv()
    devman_token = os.environ['DEVMAN_TOKEN']
    telegram_token = os.environ['TELEGRAM_TOKEN']
    telegram_id = int(os.environ['TELEGRAM_ID'])
    bot = telegram.Bot(token=telegram_token)


    class MyLogsHandler(logging.Handler):

        def emit(self, record):
            log_entry = self.format(record)
            bot.send_message(chat_id=telegram_id, text=log_entry)


    logger = logging.getLogger("MyLogsHandler")
    logger.setLevel(logging.ERROR)
    logger.addHandler(MyLogsHandler())
    logger.info("Бот запущен!")
    url = 'https://dvmn.org/api/long_polling/'
    headers = {
        'Authorization': 'Token ' + devman_token,
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
                        bot.send_message(chat_id=telegram_id,
                                         text=f"У вас проверили работу {attempt['lesson_title']} \n"
                                              f"https://dvmn.org{attempt['lesson_url']}\n"
                                              f"В работе нашлись ошибки")
                    else:
                        bot.send_message(chat_id=telegram_id,
                                         text=f"У вас проверили работу {attempt['lesson_title']} \n"
                                              f"https://dvmn.org{attempt['lesson_url']}\n"
                                              f"В работе нет ошибок")
            params = {
                'timestamp': json_data['last_attempt_timestamp']
            }
        except requests.exceptions.ReadTimeout as err:
            logger.error(err, exc_info=True)
            time.sleep(0.1)
        except requests.exceptions.ConnectionError as err:
            logger.error(err, exc_info=True)
            time.sleep(1)
        except ConnectionResetError as err:
            logger.error(err, exc_info=True)
            time.sleep(1)
        except requests.exceptions.HTTPError as err:
            logger.error(err, exc_info=True)
            time.sleep(360)
