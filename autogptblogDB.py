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

def get_memories():
    # Create a connection to the SQLite database
    conn = sqlite3.connect('AutoGPTBlog.db')

    # Create a cursor
    cursor = conn.cursor()

    # Perform a query to retrieve the memories
    cursor.execute('SELECT memory_content FROM memories ORDER BY memory_rank DESC')

    # Fetch all the results
    memories = cursor.fetchall()

    # Close the connection
    conn.close()

    # The function should return a list of memory contents
    return [memory[0] for memory in memories]

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



def add_user(conn, user_id, top_3_philosophies):
    # Splitting the top 3 philosophies
    philosophy1, philosophy2, philosophy3 = top_3_philosophies.split(', ')
    
    # SQL query to insert preferences into the "users" table
    sql = '''INSERT INTO users (id, genre1, genre2, genre3) VALUES (?, ?, ?, ?)'''
    
    # Executing the query
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (user_id, philosophy1, philosophy2, philosophy3))
        conn.commit()
    except sqlite3.Error as e:
        print(e)

# SQL queries to update the "memories" table for memory scoring
update_memories_table_query = """
ALTER TABLE memories ADD COLUMN novelty INTEGER NOT NULL DEFAULT 0;
ALTER TABLE memories ADD COLUMN usefulness INTEGER NOT NULL DEFAULT 0;
ALTER TABLE memories ADD COLUMN accuracy INTEGER NOT NULL DEFAULT 0;
ALTER TABLE memories ADD COLUMN community_engagement INTEGER NOT NULL DEFAULT 0;
ALTER TABLE memories ADD COLUMN total_score INTEGER NOT NULL DEFAULT 0;
"""

# Function to update the memories table structure
def update_memories_table():
    # Connecting to the SQLite database
    conn = sqlite3.connect('AutoGPTBlog.db')
    cursor = conn.cursor()

    # Executing the queries to update the "memories" table
    cursor.executescript(update_memories_table_query)

    # Committing the changes and closing the connection
    conn.commit()
    conn.close()
