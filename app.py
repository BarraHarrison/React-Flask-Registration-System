from flask import Flask, request, jsonify
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = "mariadb+pymysql://root:@localhost:3306/userDB"  # Updated to userDB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


bcrypt = Bcrypt(app)
jwt = JWTManager(app)
CORS(app)
db = SQLAlchemy(app) 


class User(db.Model):
    __tablename__ = 'users'  # Explicitly tell SQLAlchemy to use 'users' table
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)



with app.app_context():
    db.create_all()


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        
        user = User.query.filter_by(username=username).first()

        if not user:
            return jsonify({"msg": "User not found"}), 404

        
        if bcrypt.check_password_hash(user.password, password):
            access_token = create_access_token(identity=username)
            return jsonify(access_token=access_token), 200
        else:
            return jsonify({"msg": "Bad credentials"}), 401
    
    if request.method == 'GET':
        return "This is the login route. Please use POST to submit login credentials."



@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')  

    
    if User.query.filter_by(username=username).first():
        return jsonify({"msg": "Username already exists"}), 400
    if User.query.filter_by(email=email).first():
        return jsonify({"msg": "Email already exists"}), 400

    
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

    
    new_user = User(username=username, password=hashed_password, email=email)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"msg": "User registered successfully"}), 201


if __name__ == '__main__':
    app.run(debug=True)
