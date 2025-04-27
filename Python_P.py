import sqlite3
from datetime import datetime
import time
import sys

def print_usage():
    print("Input a number between 1-3")
def main():
    if len(sys.argv) != 1:
        print_usage()
        sys.exit(1)
        

conn = sqlite3.connect('table_update.db')
cursor = conn.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS data_table (
    id INTEGER PRIMARY KEY,
    info TEXT,
    updated_at TIMESTAMP
)
''')
conn.commit()


def insert_row(id, info, current_time):
    current_time = datetime.now()
    cursor.execute("INSERT INTO data_table (id, info, updated_at) VALUES (?, ?, ?)", [id, info, current_time])

    conn.commit()
    formatted_date = current_time.strftime("%Y-%m-%d %H:%M:%S")
  

def select_all_data():
     cursor.execute("SELECT * FROM data_table")
     rows = cursor.fetchall()
     return rows

def main():
    while True:
      
        print("1. Add data ")
        print("2. View data")
        print("3. Exit")
        option = input("Choose an option: ")

        if option == '1':
           id = input("Enter the id: ")
           info = input("Enter name: ")
           insert_row(id, info, current_time=datetime.now())
        elif option== '2':
           
            print(select_all_data())
        elif option== '3':
           break
        else:
            print_usage()

if __name__ == "__main__":
      main()
      conn.close()

