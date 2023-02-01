from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = env.str("BOT_TOKEN")  # Bot token
ADMINS = env.list("ADMINS")  # adminlar ro'yxati
CHANNELS = ['@page_ea7']  # Majburiy kanallar ro'yhati

DB_USER = env.str("DB_USER") # PostgreSQL username
DB_PASS = env.str("DB_PASS") # PostgreSQL paroli
DB_NAME = env.str("DB_NAME") # PostgreSQL DB nomi
DB_HOST = env.str("DB_HOST") # PostgreSQL host