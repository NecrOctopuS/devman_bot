### Devman bot

The program send notifications about verification lessons from [Devman](https://devman.org/).

### How to install

Then you need to deploy this project to [Heroku](https://heroku.com/)

On [Heroku](https://heroku.com/) you need create the app, and connect it to this project.

In Settings -> Config Vars you need add next variables

```text
DEVMAN_TOKEN='asda6d4a6d4a6s4d6' 
TELEGRAM_TOKEN='4645646:asd4a6dadawee4da6d4s'
TELEGRAM_ID='123456789'
```
DEVMAN_TOKEN can be take it from [Devman](https://dvmn.org/api/docs/).

TELEGRAM_TOKEN can be take it from [BotFather](https://telegram.me/BotFather) by type `/start`
`/newbot`.

TELEGRAM_ID can be take it from [userinfobot](https://telegram.me/userinfobot) by type `/start`.

After that in Resources you need turn on bot.

### How to run

In telegram you need to write to your bot any message.
When your lesson will be inspected you will get the message from your bot.



### Objective of the project

The code is written for educational purposes on the online course for web developers [dvmn.org](https://dvmn.org/).