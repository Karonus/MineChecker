# MineChecker

Send notify to Telegram when a nickname is available.

### Envs
- `TELEGRAM_BOT_TOKEN`- Bot token from @BotFather
- `TEEGRAM_CHAT_ID` - Chat ID to send a notify
- `NICKNAMES` - Nicknames (comma separate) for check


Scripts:
- `background.py` - For background checking nicknames on your device.
- `for_ga.py` - For Github Actions, see [this](.github/workflows/checker.yml)


### Run checker on linux machine
1. Create a screen
```bash
screen -S mine_checker
```
2. Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```
3. Install requirements:
```bash
pip install -U pip
pip install -r requirements.txt
```
4. Create environ variables (see #Envs)
4. Run
```bash
python background.py
```
5. Detach from the screen, press `Ctrl+A+D`
