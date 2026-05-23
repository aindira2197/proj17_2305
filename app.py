from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shops.db'

db = SQLAlchemy(app)


class Shop(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))


@app.route('/')
def home():

    shops = Shop.query.all()

    text = ""

    for shop in shops:
        text += f"{shop.name}<br>"

    return text


@app.route('/add/<name>')
def add(name):

    shop = Shop(name=name)

    db.session.add(shop)
    db.session.commit()

    return "Shop Added"


if __name__ == '__main__':

    with app.app_context():
        db.create_all()

    app.run(debug=True)
