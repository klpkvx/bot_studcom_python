# Telegram Bot

A Telegram bot for dormitory management and information services.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set up environment variables:
```bash
export GOOGLE_SHEETS_API_KEY="your_google_sheets_api_key_here"
```

3. Configure the bot token in `src/config.py`:
```python
TOKEN = 'your_bot_token_here'
```

4. Run the bot:
```bash
cd src
python main.py
```

## Recent Bug Fixes

### 1. Security Fix - API Key Protection
- **Issue**: Google Sheets API key was hardcoded in the source code
- **Fix**: Moved API key to environment variable `GOOGLE_SHEETS_API_KEY`
- **Location**: `src/utils/create_bot.py`

### 2. Logic Fix - Floor Selection
- **Issue**: Missing return statement in floor selection for buildings Г, Е, Ж, Д
- **Fix**: Added proper return statement for the missing case
- **Location**: `src/utils/client.py:158-162`

### 3. Performance Fix - Database Connections
- **Issue**: Inefficient database connection management
- **Fix**: Added explicit commit and improved connection handling
- **Location**: `src/utils/sqlite_db.py:47-52`

## Security Notes

- Never commit API keys or tokens to version control
- Use environment variables for sensitive configuration
- Regularly rotate API keys and tokens