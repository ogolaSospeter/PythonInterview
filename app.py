import sqlite3
from flask import Flask, request, jsonify
import json
from flask_restful import Resource, Api



app = Flask(__name__)
api = Api(app)


users = [
    {
        "id": 1,
        "username": "john",
        "password": "1234",
        "email": "john1234@gmail.com"
    },
    {
        "id": 2,
        "username": "jane",
        "password": "5678",
        "email": "jane5678@gmail.com"
    },
    {
        "id": 3,
        "username": "joe",
        "password": "0000",
        "email": "joe0000@gmail.com"
    },
    {
        "id": 4,
        "username": "jill",
        "password": "1111",
        "email": "jill1111@gmail.com"
    },
    {
        "id": 5,
        "username": "jack",
        "password": "2222",
        "email": "jack2222@gmail.com"
    }
]

class Users(Resource):

    def get(self):
        return {'users': users}, 200


    def post(self):
        new_user = request.get_json()
        users.append(new_user)
        return {'users': users}, 201
api.add_resource(Users, '/users')




if __name__ == '__main__':
    app.run(debug=True)

    """
    def connection():
    conn = None
    try:
        conn = sqlite3.connect('PythonInterview.sqlite')
    except sqlite3.Error as e:
        print(e)
    return conn


@app.route('/users', methods=['GET', 'POST', 'PUT', 'DELETE'])
def users():
    if request.method == 'GET':
        conn = connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        users = [
            dict(id=row[0], username=row[1], password=row[2], email=row[3], created_at=row[4]) for row in rows
        ]
        if users is not None:
            return jsonify(users)
        conn.close()
        return jsonify(rows)

    elif request.method == 'POST':
        newusername = request.form['username']
        newpassword = request.form['password']
        newemail = request.form['email']
        newcreated_at = request.form['created_at']
        sql = /"/""INSERT INTO users (username, password, email, created_at) VALUES (?, ?, ?, ?)"/""
        
        conn = connection()
        cursor = conn.cursor()
        cursor.execute(sql, (newusername, newpassword, newemail, newcreated_at))
        conn.commit()
        return f"User {cursor.lastrowid} created successfully"


    elif request.method == 'PUT':
        conn = connection()
        cursor = conn.cursor()
        sql_query = ""/"UPDATE users SET username = ?, password = ?, email = ?, created_at = ? WHERE id = ?"/""
        cursor.execute(sql_query, (request.json['username'], request.json['password'], request.json['email'],
                                   request.json['created_at'], request.json['id']))
        conn.commit()
        conn.close()
        return "User updated successfully", 200

    elif request.method == 'DELETE':
        conn = connection()
        cursor = conn./cursor()
        sql_query = ""/"DELETE FROM users WHERE id = ?""/"
        cursor.execute(sql_query, (request.json['id'],))
        conn.commit()
        conn.close()
        return "User deleted successfully", 200
    """