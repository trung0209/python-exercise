from imdb import IMDb

# create an instance of the IMDb class
ia = IMDb()

# get a movie
# movie = ia.get_movie('0133093')
#
# # print the names of the directors of the movie
# print('Directors:')
# for director in movie['directors']:
#     print(director['name'])
#
# # print the genres of the movie
# print('Genres:')
# for genre in movie['genres']:
#     print(genre)

# search for a person name
movie = ia.get_movie("6149532")
print(movie)