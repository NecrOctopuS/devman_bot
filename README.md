### Devman bot

The program send notifications about verification lessons from [Devman](https://devman.org/) 

### How to install
 
The following data must be written to the `.env` file:
```text
DEVMAN_TOKEN='asda6d4a6d4a6s4d6' 
TELEGRAM_TOKEN='4645646:asd4a6dadawee4da6d4s'
TELEGRAM_ID='123456789'
```
DEVMAN_TOKEN can be take it from [Devman](https://dvmn.org/api/docs/)

TELEGRAM_TOKEN can be take it from [BotFather](https://telegram.me/BotFather) by type `/start`
`/newbot`

TELEGRAM_ID can be take it from [userinfobot](https://telegram.me/userinfobot) by type `/start`

Python3 should already be installed.
Then use `pip` (or` pip3`, there is a conflict with Python2) to install the dependencies:
```
pip install -r requirements.txt
```

### How to run

In telegram you need to write to your bot any message.
Run the script and when your lesson will be inspected you will get the message from your bot

### Objective of the project

The code is written for educational purposes on the online course for web developers [dvmn.org](https://dvmn.org/).