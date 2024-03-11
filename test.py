import sqlite3

def search_database(username):
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username = '%s'" % username)
    result = c.fetchall()
    conn.close()
    return result

if __name__ == "__main__":
    username = input("Enter username to search: ")
    search_result = search_database(username)
    print(search_result)
