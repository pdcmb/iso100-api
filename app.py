from flask import Flask
from api import db, ma
from api.route.camera import camera_api
from api.route.producer import producer_api
import os



# Init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
ma.init_app(app)
db.init_app(app)

@app.before_first_request
def initialize_database():
    db.create_all()

# DB config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite3')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Register blueprints
app.register_blueprint(camera_api)
app.register_blueprint(producer_api)

# Run server
if __name__ == "__main__":
    app.run(debug=True)

