from flask import Flask
from configs import Configuration
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object(Configuration)
SQLALCHEMY_DATABASE_URI = 'postgresql://testuser:123456@localhost:5432/postgrestest'
db = SQLAlchemy(app)
migrate = Migrate(app, db)


from views import bp
app.register_blueprint(bp)
