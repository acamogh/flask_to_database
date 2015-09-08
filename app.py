
from flask import Flask, jsonify
from flask.ext.sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://amogh:amogh@localhost/fire'
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = "setpoints_test"

    id       = db.Column(db.Integer, primary_key=True)
    wing = db.Column(db.String(128), index=True)
    sensor = db.Column(db.String(128))

    def __init__(self, data):
        self.wing = data['wing']
        self.sensor = data['sensor']

    def __repr__(self):
       
        return '{}-{}'.format(self.wing, self.sensor)
        
db.create_all()

@app.route('/')
def index():
    # This is a dummy list, 2 nested arrays containing some
    # params and values
    list = [
        {'wing': 'left', 'sensor': 'fff2'},
        {'wing': 'right', 'sensor': 'fff0'}
    ]
    # jsonify will do for us all the work, returning the
    # previous data structure in JSON
    print list
    db.session.add(User(list[1]))
    db.session.commit()
    posts=db.session.query(User).all()
    print posts
    return jsonify(results=list)
    



if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)
