from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///qoutes.db'
db = SQLAlchemy(app)


class Qoutes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    qoute = db.Column(db.String(300), nullable=False)
    ref = db.Column(db.String(10))
    author = db.Column(db.String(100))

    def __repr__(self):
        return '<Qoute: %r>' % self.id


with app.app_context():
    db.create_all()


def get_qoute(id):
    with app.app_context():
        try:
            qoute = db.get_or_404(Qoutes, id)
            return qoute
        except:
            return 'An error occured'


@ app.route('/api/get/<int:id>')
def handle_get(id):
    data = get_qoute(id)
    data = {'qoute': data.qoute, 'reffrence': data.ref, 'author': data.author}
    response = jsonify({'response': data})
    return response


if __name__ == "__main__":
    app.run(debug=True)
