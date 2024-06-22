from os import getenv,environ
from datetime import datetime
import pymysql


from dotenv import load_dotenv
load_dotenv()
DB_NAME = getenv('DB_NAME')
DB_HOST = getenv('DB_HOST')
DB_USER = getenv('DB_USER')
DB_PASSWORD = getenv('DB_PASSWORD')
print(DB_NAME, environ.get('DB_NAME'))

# connection = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD,)

# cursor = connection.cursor() 

# cursor.execute(f"SHOW DATABASES;")
# databases = cursor.fetchall()
# all_db = [i[0] for i in databases]

# if DB_NAME in all_db:
#     print(f"'{DB_NAME}' already exist! Try another name.")
# else:
#     cursor.execute(f"CREATE DATABASE {DB_NAME};")
#     print(f"{DB_NAME} database create at {datetime.now()}")


# # cursor.execute(f"CREATE DATABASE {DB_NAME};")
# # print('database created')
# # print(data)
