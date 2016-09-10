import sys
from imdb import IMDb

def get_actors(movie):
    pass

def get_movie(name):
    ia = IMDb()
    s_result = ia.search_movie(name)
    movie = s_result[0]
    ia.update(movie)
    print movie['long imdb canonical title']
    cast = movie['cast']
    for character in cast:
        print character.personID

#get_movie(sys.argv[1])
#get_movie("Captain America")
get_movie("Gravity")