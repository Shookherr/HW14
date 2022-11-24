import sqlite3


def film_to_title(title):
    """
    Возвращает данные из БД по названию фильма
    """
    with sqlite3.connect("netflix.db") as con:
        cur = con.cursor()
        sqlite_query = ("SELECT title, country, release_year, listed_in, description "
                        "FROM netflix "
                        f"WHERE title LIKE '%{title}%' "
                        "AND type='Movie' " 
                        "ORDER BY release_year DESC")
        cur.execute(sqlite_query)
        executed_query = cur.fetchone()
        data = {"title": executed_query[0],
                "country": executed_query[1],
                "release_year": executed_query[2],
                "genre": executed_query[3],
                "description": executed_query[4]}
    return data


def films_from_between_years(year_start, year_stop):
    """
    Возвращает данные из БД по интервалу между двух годов выпуска
    """
    films = []

    with sqlite3.connect("netflix.db") as con:
        cur = con.cursor()
        sqlite_query = ("SELECT title, release_year "
                        "FROM netflix "
                        "WHERE type='Movie' "
                        f"AND release_year BETWEEN {year_start} AND {year_stop} "
                        "ORDER BY release_year ASC "
                        "LIMIT 100")
        cur.execute(sqlite_query)
        executed_query = cur.fetchall()

        for query in executed_query:
            film = {"title": query[0], "release_year": query[1]}
            films.append(film)
    return films


def shows_with_rating(str_rating):
    """
    Возвращает данные из БД по возрастному рейтингу
    str_rating должна иметь значения типа
    "rating='G'",
    "rating='G' OR rating='PG' OR rating='PG-13'" или
    "rating='R' OR rating='NC-17'"
    """
    with sqlite3.connect("netflix.db") as con:
        shows = []
        cur = con.cursor()
        sqlite_query = f"SELECT title, rating, description FROM netflix WHERE {str_rating}"
        cur.execute(sqlite_query)
        executed_query = cur.fetchall()

        for query in executed_query:
            show = {"title": query[0], "rating": query[1], "description": query[2]}
            shows.append(show)
    return shows


def shows_top10_new(genre):
    """
    Возвращает 10 самых свежих строк жанра из БД
    """
    with sqlite3.connect("netflix.db") as con:
        shows = []
        cur = con.cursor()
        sqlite_query = f"SELECT title, description FROM netflix WHERE listed_in LIKE '%{genre}%' " \
                       "ORDER BY release_year DESC LIMIT 10"
        cur.execute(sqlite_query)
        executed_query = cur.fetchall()

        for query in executed_query:
            show = {"title": query[0], "description": query[1]}
            shows.append(show)
    return shows


def get_actors(actor_1, actor_2):
    """
    Возвращает список актёров
    """
    with sqlite3.connect("netflix.db") as con:
        cur = con.cursor()
        sqlite_query = f"SELECT COUNT(netflix.cast), netflix.cast FROM netflix WHERE netflix.cast LIKE '%{actor_1}%' " \
                       f"AND netflix.cast LIKE '%{actor_2}%' GROUP BY netflix.cast"
        cur.execute(sqlite_query)
        executed_query = cur.fetchall()

    return executed_query


def find_show(show_type, release_year, genre):
    """
    Поиск записей по параметрам
    """
    with sqlite3.connect("netflix.db") as con:
        cur = con.cursor()
        sqlite_query = f"SELECT title, description FROM netflix WHERE type='{show_type}' AND " \
                       f"release_year={release_year}  AND listed_in LIKE '%{genre}%'"
        cur.execute(sqlite_query)
        executed_query = cur.fetchall()

    return executed_query
