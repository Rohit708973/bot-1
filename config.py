import os
from dotenv import load_dotenv

# Load environment variables from .env file (for local development)
load_dotenv()

# Base URL for Vignan ECAP (Webpros)
BASE_URL = os.getenv("BASE_URL", "https://webprosindia.com/vignanit/")
LOGIN_URL = BASE_URL + "Login.aspx"
ATTENDANCE_URL = BASE_URL + "Academics/StudentAttendanceByDay.aspx"

# Bot Token - Load from environment variable (secure for deployment)
# Falls back to hardcoded value for local testing
BOT_TOKEN = os.getenv("BOT_TOKEN", "8035625648:AAGmrNXuYN9w121k9IiloB6ahx0YoherFkU")
