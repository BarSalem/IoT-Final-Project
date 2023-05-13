from prettytable import PrettyTable
import sqlite3
# Bar Salem 207351784
conn = sqlite3.connect("iot_final_project.db", check_same_thread=False, timeout=10)
cursor = conn.cursor()


def delete_table():
    cursor.execute("DROP TABLE IF EXISTS DHT_Data")


def create_table(curs):
    curs.execute('''CREATE TABLE IF NOT EXISTS DHT_Data
                      (id INTEGER PRIMARY KEY,
                       Temperature FLOAT,
                       Humidity FLOAT,
                       AC_State string)''')


def print_db_data():
    cursor.execute("SELECT * FROM DHT_Data")
    rows = cursor.fetchall()
    table = PrettyTable()
    table.field_names = [description[0] for description in cursor.description]
    for row in rows:
        table.add_row(row)
    print(table)


def insert_data_to_table(temp, hum, ac_state):
    cursor.execute("INSERT INTO DHT_Data (Temperature, Humidity, AC_State) VALUES (?, ?, ?)", (temp, hum, ac_state))
    conn.commit()


create_table(cursor)
