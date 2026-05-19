from flask import Flask
from models import db
from routes import api

app = Flask(__name__)
app.json.ensure_ascii = False

# الاتصال بكونتينر بوستجر الشغال عندك
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://ahmeddb:123456@db:5432/hospital_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
app.register_blueprint(api)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # بناء الجداول لو مش موجودة
    app.run(host='0.0.0.0', debug=True, port=5000)