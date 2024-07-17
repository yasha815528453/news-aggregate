from flask import request, jsonify

def configure_routes(app, db_repo):
    @app.route('/api/news/today', methods=['GET'])
    def get_today_news():
        """Get today's news"""
        date = request.args.get('date')
        news = db_repo.fetch_news(date)
        return jsonify(news)

    @app.route('/api/categories', methods=['GET'])
    def get_categories():
        """Get all categories"""
        categories = db_repo.fetch_categories()
        return jsonify(categories)

    @app.route('/api/subcategories/<category>', methods=['GET'])
    def get_subcategories(category):
        """Get subcategories for a given category"""
        subcategories = db_repo.fetch_subcategories(category)
        return jsonify(subcategories)
