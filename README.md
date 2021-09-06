# Telegram vcVideoPlayer

- An Telegram Bot By [@ZauteKm](https://t.me/ZauteKm) To Stream Videos in Telegram Voice Chat.

---

## NOTE:

- Make sure you have started a VoiceChat in your Group/Channel before deploying.

---

## Features

<details>
  <summary><b>Show the Features</b></summary>
<br/>

- Supports Live Streaming
- Supports YouTube Streaming
- Supports Live Radio Streaming
- Supports Video Files Streaming
- Supports YouTube Live Streaming
- Customizable Userbot Protection (PM Guard)

</details>

---

## Variables
<details>
  <summary><b>See Variables</b></summary>
<br/>

<b>Pre Requisites (Config Vars)</b>
- `API_ID` : Get from [my.telegram.org](https://my.telegram.org/app) or [@UseTGzKBot](https://telegram.dog/UseTGzKBot)
- `API_HASH` : Get from [my.telegram.org](https://my.telegram.org/app) or [@UseTGzKBot](https://telegram.dog/UseTGzKBot)
- `BOT_TOKEN` : Get From [@Botfather](https://telegram.dog/BotFather)
- `BOT_USERNAME` : Your Telegram Bot Username, get it from @Botfather XD
- `SESSION_STRING` : Generate From here [![GenerateStringName](https://img.shields.io/badge/repl.it-generateStringName-yellowgreen)](https://replit.com/@ZauteKm/GenerateStringSession)
- `CHAT_ID` : ID of Channel/Group where the bot will works or stream videos.
- `AUTH_USERS` : ID of Users who can use Admins commands (for multiple users seperated by space).
- `REPLY_MESSAGE` : A reply to those who message the USER account in PM. Leave it blank if you do not need this feature. 

</details>

---

## Deploy Now

<details><summary><b>Deploy to Heroku</b></summary>
<p>
<br>
<a href="https://heroku.com/deploy?template=https://github.com/ZauteKm/vcVideoPlayer">
  <img src="https://www.herokucdn.com/deploy/button.svg" alt="Deploy">
</a>
</p>
</details>

<details>
  <summary><b>Deploy to Railway</b></summary>
<br/>

<p align="left">
<a href="https://railway.app/new/template?template=https%3A%2F%2Fgithub.com%2FZauteKm%2FvcVideoPlayer&envs=API_ID%2CAPI_HASH%2CBOT_TOKEN%2CSESSION_STRING%2CCHAT_ID%2CAUTH_USERS%2CBOT_USERNAME%2CREPLY_MESSAGE&optionalEnvs=REPLY_MESSAGE&API_IDDesc=User+Account+Telegram+API_ID+get+it+from+my.telegram.org%2Fapps&API_HASHDesc=User+Account+Telegram+API_HASH+get+it+from+my.telegram.org%2Fapps&BOT_TOKENDesc=Your+Telegram+Bot+Token%2C+get+it+from+%40Botfather+XD&SESSION_STRINGDesc=Pyrogram+Session+String+of+User+Account%2C+get+it+from+%4https://replit.com/@ZauteKm/GenerateStringSession&CHAT_IDDesc=ID+of+your+Channel+or+Group+where+the+bot+will+works+or+stream+videos&AUTH_USERSDesc=ID+of+Auth+Users+who+can+use+Admin+commands+%28for+multiple+users+seperated+by+space%29&BOT_USERNAMEDesc=Your+Telegram+Bot+Username+without+%40%2C+get+it+from+%40Botfather+XD&REPLY_MESSAGEDesc=A+reply+message+to+those+who+message+the+USER+account+in+PM.+Make+it+blank+if+you+do+not+need+this+feature.&REPLY_MESSAGEDefault=Hello+Sir%2C+I%27m+a+bot+to+stream+videos+on+telegram+voice+chat%2C+not+having+time+to+chat+with+you+%F0%9F%98%82%21&referralCode=,ZAUTEKM"
">
     <img height="30px" src="https://railway.app/button.svg">
  </a>
</p>

</a>
</p>

</details>

<details>
  <summary><b>Deploy in your VPS</b></summary>
<br/>

```sh
$ git clone https://github.com/ZauteKm/vcVideoPlayer.git
$ cd vcVideoPlayer
$ sudo apt-get install python3-pip ffmpeg
$ pip3 install -U pip
$ pip3 install -U -r requirements.txt
# <create .env variables appropriately>
$ python3 main.py
```

</details>

---

## Requirements
- Python 3.6 or Higher.
- [Telegram API key](https://docs.pyrogram.org/intro/quickstart#enjoy-the-api).
- Latest [FFmpeg Python](https://www.ffmpeg.org/).
- Pyrogram [String Session](https://replit.com/@ZauteKm/GenerateStringSession) of the account.
- The User Account Needs To Be An Admin In The Channel/Group.

---

## License
```sh
vcVideoPlayer, Telegram Video Chat Bot
Copyright (c) 2021 Zaute Km

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
```

