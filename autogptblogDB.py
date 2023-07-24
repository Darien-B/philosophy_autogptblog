import sqlite3

def create_connection():
    conn = None;
    try:
        conn = sqlite3.connect('AutoGPTBlog.db')  # This will create a file named "AutoGPTBlog.db" in the current directory
        print(sqlite3.version)
    except sqlite3.Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except sqlite3.Error as e:
        print(e)

def main():
    database = r"AutoGPTBlog.db"

    sql_create_users_table = """CREATE TABLE IF NOT EXISTS users (
                                        id integer PRIMARY KEY,
                                        genre1 text NOT NULL,
                                        genre2 text NOT NULL,
                                        genre3 text NOT NULL
                                    );"""

    sql_create_memories_table = """CREATE TABLE IF NOT EXISTS memories (
                                        id integer PRIMARY KEY,
                                        memory_content text NOT NULL,
                                        memory_rank integer NOT NULL
                                    );"""

    # create a database connection
    conn = create_connection()

    # create tables
    if conn is not None:
        # create users table
        create_table(conn, sql_create_users_table)

        # create memories table
        create_table(conn, sql_create_memories_table)
    else:
        print("Error! cannot create the database connection.")

if __name__ == '__main__':
    main()
