import requests
import time
import telegram
import os
import logging

DEVMAN_TOKEN = os.environ['DEVMAN_TOKEN']
TELEGRAM_TOKEN = os.environ['TELEGRAM_TOKEN']
TELEGRAM_ID = int(os.environ['TELEGRAM_ID'])

if __name__ == '__main__':
    bot = telegram.Bot(token=TELEGRAM_TOKEN)


    class MyLogsHandler(logging.Handler):

        def emit(self, record):
            log_entry = self.format(record)
            bot.send_message(chat_id=TELEGRAM_ID, text=log_entry)


    logger = logging.getLogger("MyLogsHandler")
    logger.setLevel(logging.ERROR)
    logger.addHandler(MyLogsHandler())
    logger.info("Бот запущен!")
    url = 'https://dvmn.org/api/long_poll1ing/'
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
                        bot.send_message(chat_id=TELEGRAM_ID,
                                         text=f"У вас проверили работу {attempt['lesson_title']} \n"
                                              f"https://dvmn.org{attempt['lesson_url']}\n"
                                              f"В работе нашлись ошибки")
                    else:
                        bot.send_message(chat_id=TELEGRAM_ID,
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
            time.sleep(1)
