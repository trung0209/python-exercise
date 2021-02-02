from imdb import IMDb
import re
# create an instance of the IMDb class
ia = IMDb()
try:
    # get a movie
    movie = ia.search_movie(title="Millions Game, The (Das Millionenspiel)")
    print(movie)
    year = re.search("\(\d{4}\)", str(movie))
    if year is not None:
        print(year)

except IMDb.IMDbError as e:
    print(e)
