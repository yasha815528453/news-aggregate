from .sql_maker import SQLMaker
from .initialize import initialize_db
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class DBRepo:
    def __init__(self, app):
        self.app = app
        self.sql_maker = SQLMaker()
        initialize_db(app)

    def fetch_news(self, date):
        """Fetch news for a given date"""
        query = self.sql_maker.get_news_by_date(date)
        result = db.session.execute(query).fetchall()
        return result

    def insert_news(self, news_data):
        """Insert news data into the database"""
        query = self.sql_maker.insert_news(news_data)
        db.session.execute(query)
        db.session.commit()

    def fetch_categories(self):
        """Fetch all categories"""
        query = self.sql_maker.get_all_categories()
        result = db.session.execute(query).fetchall()
        return result

    def fetch_subcategories(self, category):
        """Fetch subcategories for a given category"""
        query = self.sql_maker.get_subcategories_by_category(category)
        result = db.session.execute(query).fetchall()
        return result
