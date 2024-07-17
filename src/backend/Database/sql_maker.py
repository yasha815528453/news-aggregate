class SQLMaker:
    def get_news_by_date(self, date):
        """Get news by date"""
        return f"SELECT * FROM news WHERE date = '{date}';"

    def insert_news(self, news_data):
        """Insert news into the database"""
        return f"""
            INSERT INTO news (title, content, date, category, subcategory, sentiment)
            VALUES ('{news_data['title']}', '{news_data['content']}', '{news_data['date']}',
                    '{news_data['category']}', '{news_data['subcategory']}', '{news_data['sentiment']}');
        """

    def get_all_categories(self):
        """Get all categories"""
        return "SELECT DISTINCT category FROM news;"

    def get_subcategories_by_category(self, category):
        """Get subcategories by category"""
        return f"SELECT DISTINCT subcategory FROM news WHERE category = '{category}';"
