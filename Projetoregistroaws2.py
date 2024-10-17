from flask import Flask, request, jsonify
import MySQLdb

app = Flask(__name__)

db = MySQLdb.connect(
    host = "database-1.c1sau2yc4mfy.us-east-2.rds.amazonaws.com",
    user = "admin",
    passwd = "teste123",
    db = "Registro"
)

@app.route('/registrer', methods = ['POST'])
def registrer_user():
    data = request.json
    name = data['name']
    email = data['email']
    
    cursor = db.cursor()
    cursor.execute("INSERT INTO users (name, email) values(%s, %s)", (name, email))
    db.commit()
    
    return jsonify({"message": "Usuário registrado com sucesso!"}), 201

if __name__ == '__main__':
    app.run(debug=True)
