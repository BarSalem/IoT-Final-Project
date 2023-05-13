from prettytable import PrettyTable
import sqlite3

conn = sqlite3.connect("iot_final_project_light_data.db", check_same_thread=False, timeout=10)
cursor = conn.cursor()


def delete_table():
    cursor.execute("DROP TABLE IF EXISTS Light_Data")


def create_table(curs):
    curs.execute('''CREATE TABLE IF NOT EXISTS Light_Data
                      (id INTEGER PRIMARY KEY,
                       Light_Strength FLOAT,
                       Blinds_State string)''')


def print_db_data():
    cursor.execute("SELECT * FROM Light_Data")
    rows = cursor.fetchall()
    table = PrettyTable()
    table.field_names = [description[0] for description in cursor.description]
    for row in rows:
        table.add_row(row)
    print(table)


def insert_data_to_table(light_strength, blinds_state):
    cursor.execute("INSERT INTO Light_Data (Light_Strength, Blinds_State) VALUES (?, ?)", (light_strength, blinds_state))
    conn.commit()


create_table(cursor)
