from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = env.str("BOT_TOKEN")  # Bot toekn
ADMINS = env.list("ADMINS")  # adminlar ro'yxati
CHANNELS = ['@blogca']

dbport = env.int('dbport')
dbhost = env.str('dbhost')
dbname = env.str('dbname')
dbuser = env.str('dbuser')
dbpassword = env.str('dbpassword')

DATABASE_URL = "postgres://{}:{}@{}:{}/{}".format(dbuser, dbpassword, dbhost, dbport, dbname)
