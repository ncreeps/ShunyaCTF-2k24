from flask import Flask, jsonify, render_template,request
import sqlite3,time
import base64

app = Flask(__name__)

def sleep_function(val):
    try:
        val = float(val)
        if val < 0:
            raise ValueError("Sleep time must be non-negative")
        time.sleep(val)
        return val
    except Exception as e:
        print(f"Error in sleep_function: {e}")

def create_random_table():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Generate a random table name
    random_string = 'oezxsbhh'
    table_name = f'secret_{random_string}_text'

    # Drop the table if it already exists
    cursor.execute(f"DROP TABLE IF EXISTS {table_name}")

    # Create a new table
    cursor.execute(f"""
        CREATE TABLE {table_name} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text TEXT NOT NULL
        )
    """)

    cursor.execute(f"INSERT INTO {table_name} (text) VALUES (?)", ('85862569322aff32d336432cb4fb423661c1de69dec2866c',))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/api/movies', methods=['POST'])
def get_movies():

    data = request.get_json()
    order_by = data.get('sequence', 'aWQgZGVzYw==')

    decode_order_by = base64.b64decode(order_by).decode()

    conn = get_db_connection()
    conn.create_function("zhopi", 1, sleep_function)
    query = f'SELECT * FROM movies ORDER BY {decode_order_by}'
    
    movies = conn.execute(query).fetchall()
    conn.close()
    
    return jsonify([dict(row) for row in movies])

@app.route('/api/goodforyou', methods=['POST'])
def goodforyou():
    return "Gotcha"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/time')
def timeStone():
    return render_template('time.html')

if __name__ == '__main__':
    create_random_table()

    app.run(host="0.0.0.0",port=80,debug=False)
