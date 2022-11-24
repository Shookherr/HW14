# ДЗ 14 Шумихин Алексей 24.11.22
from flask import Flask, jsonify
import utils

if __name__ == '__main__':

    app = Flask(__name__)

    app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


    @app.route('/')
    def main_page():
        return 'Main page'


    @app.route('/movie/<title>')
    def about_film(title):
        data_film = utils.film_to_title(title)
        return jsonify(data_film)


    @app.route('/movie/<int:year_beg>/to/<int:year_end>')
    def films_between_years(year_beg, year_end):
        data_films = utils.films_from_between_years(year_beg, year_end)
        return jsonify(data_films)

    @app.route('/rating/children')
    def shows_for_child():
        data_shows = utils.shows_with_rating("rating='G'")
        return jsonify(data_shows)


    @app.route('/rating/family')
    def shows_for_family():
        data_shows = utils.shows_with_rating("rating='G' OR rating='PG' OR rating='PG-13'")
        return jsonify(data_shows)


    @app.route('/rating/adult')
    def film_for_child():
        data_shows = utils.shows_with_rating("rating='R' OR rating='NC-17'")
        return jsonify(data_shows)


    @app.route('/genre/<genre>')
    def genre_top10(genre):
        data_shows = utils.shows_top10_new(genre)
        return jsonify(data_shows)


    app.run()
