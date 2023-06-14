# MineChecker

Send notify to Telegram when a nickname is available.

Envs:
- `TELEGRAM_BOT_TOKEN`- Bot token from @BotFather
- `TEEGRAM_CHAT_ID` - Chat ID to send a notify
- `NICKNAMES` - Nicknames (comma separate) for check


Scripts:
- `background.py` - For background checking nicknames on your device.
- `for_ga.py` - For Github Actions, see [this](.github/workflows/checker.yml)
