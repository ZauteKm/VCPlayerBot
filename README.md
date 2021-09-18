# Telegram VCVideoPlayBot

- An Telegram Bot By [@ZauteKm](https://t.me/ZauteKm) To Stream Videos in Telegram Voice Chat.

---

## NOTE:

- Make sure you have started a VoiceChat in your Group/Channel before deploying.

---

## Features

<details>
  <summary><b>Show the Features</b></summary>
<br/>

- Playlist, queue.
- Supports Play from Youtube Playlist.
- Change VoiceChat title to current playing song name.
- Supports Live streaming from youtube
- Play from telegram file supported.
- Starts Radio after if no songs in playlist.
- Automatically downloads audio for the first two tracks in the playlist to ensure smooth playing
- Automatic restart even if heroku restarts.
- Support exporting and importing playlist.

</details>

---

## Variables
<details>
  <summary><b>See Variables</b></summary>
<br/>

<b>Mandatory Vars</b>
1. `API_ID` : Get From [my.telegram.org](https://my.telegram.org/)
2. `API_HASH` : Get from [my.telegram.org](https://my.telegram.org)
3. `BOT_TOKEN` : [@Botfather](https://telegram.dog/BotFather)
4. `SESSION_STRING` : Generate From here [![GenerateStringName](https://img.shields.io/badge/repl.it-generateStringName-yellowgreen)](https://replit.com/@ZauteKm/GenerateStringSession)
5. `CHAT` : ID of Channel/Group where the bot plays Music.

<b>Optional Vars</b>
1. `LOG_GROUP` : Group to send Playlist, if CHAT is a Group()
2. `ADMINS` : ID of users who can use admin commands.
3. `STARTUP_STREAM` : This will be streamed on startups and restarts of bot. You can use either any STREAM_URL or a direct link of any video or a Youtube Live link. You can also use YouTube Playlist.Find a Telegram Link for your playlist from [PlayList Dumb](https://telegram.dog/DumpPlaylist) or get a PlayList from [PlayList Extract](https://telegram.dog/GetAPlaylistbot). The PlayList link should in form `https://t.me/DumpPlaylist/xxx`.
4. `REPLY_MESSAGE` : A reply to those who message the USER account in PM. Leave it blank if you do not need this feature. 
5. `ADMIN_ONLY` : Pass `Y` If you want to make /play command only for admins of `CHAT`. By default /play is available for all.
6. `HEROKU_API_KEY` : Your heroku api key. Get one from [here](https://dashboard.heroku.com/account/applications/authorizations/new)
7. `HEROKU_APP_NAME` : Your heroku apps name.

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
<a href="https://railway.app/new/template?template=https%3A%2F%2Fgithub.com%2FZauteKm%2FVCVideoPlayBot"
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
$ git clone https://github.com/ZauteKm/VCVideoPlayBot.git
$ cd VCVideoPlayBot
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
