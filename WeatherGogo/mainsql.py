# import pymysql
# from config import host, user, password, db_name
#
# try:
#     connection = pymysql.connect(
#         host=host,
#         port=3306,
#         user=user,
#         password=password,
#         database=db_name,
#         cursorclass=pymysql.cursors.DictCursor
#     )
#     print("successfully connected")
#     print("#" * 20)
#
#     try:

        # with connection.cursor() as cursor:
        #     insert_query = "INSERT INTO member (username, age, email, password) VALUES ('dfgdfg', 20, 'anna@mail.ru', '{}');"
        #     # insert_query = "INSERT INTO member (username, age, email, password) VALUES ('Anna', 20, 'anna@mail.ru', 'hello236');"
        #     cursor.execute(insert_query)
        #     connection.commit()

#         with connection.cursor() as cursor:
#             select_query = "SELECT * FROM image"
#             cursor.execute(select_query)
#             result = cursor.fetchall()
#             print('>', result)
#
#     finally:
#         connection.close()
# except Exception as ex:
#     print("Connection refused")
#     print(ex)

# import sqlite3
#
# db = sqlite3.connect('gogo_db')
#
# c = db.cursor()

# c.execute("""CREATE TABLE user (
#     id INTEGER PRIMARY KEY autoincrement,
#     username VARCHAR,
#     age TINYINT,
#     email VARCHAR,
#     password BINARY
# )""")

    # c.execute("INSERT INTO outfit (img) VALUES ('https://imgur.com/IKV42LS')")
    # c.execute("INSERT INTO outfit (img) VALUES ('https://imgur.com/Fsu8Zys')")
    # c.execute("INSERT INTO outfit (img) VALUES ('https://imgur.com/ZzVZrGB')")
    # c.execute("INSERT INTO outfit (img) VALUES ('https://imgur.com/bSdTwPG')")
    # c.execute("INSERT INTO outfit (img) VALUES ('https://imgur.com/HWoCusU')")


# select_query = "SELECT * FROM user"
# c.execute(select_query)
# result = c.fetchall()
# print(result)
#
# db.commit()
#
# db.close()

