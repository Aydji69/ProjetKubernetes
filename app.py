from flask import Flask, jsonify
import MySQLdb

app = Flask(__name__)

def get_db_connection():
    db = MySQLdb.connect(
        host='mysqldb',  
        user='root',
        password='Souleater11#',
        db='mydatabase'
    )
    return db

@app.route('/')
def index():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM mytable')  
    results = cursor.fetchall()
    cursor.close()
    connection.close()

    return jsonify(results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)