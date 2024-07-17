from flask import Flask
from .routes import configure_routes
from ..Database.db_repo import DBRepo

app = Flask(__name__)
db_repo = DBRepo(app)
configure_routes(app, db_repo)

if __name__ == '__main__':
    app.run(debug=True)
