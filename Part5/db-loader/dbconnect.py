import mysql.connector
import os
db_name = os.environ['DB_NAME']
db_user = os.environ['DB_USER']
db_pass = os.environ['DB_PASS']


def connection():
    # Edited out actual values
    conn = mysql.connector.connect( host='dbhost',
                            port=3306,
                            database='allergen_info',
                            user='pythonapp',
                            password='secretPass123!')
    c = conn.cursor()

    return c, conn