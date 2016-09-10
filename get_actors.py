import sys
from imdb import IMDb
import time

def get_actors(movie):
    pass

def get_movie(name):
    ia = IMDb()
    s_result = ia.search_movie(name)
    movie = s_result[0]
    ia.update(movie)
    print movie['long imdb canonical title']
    cast = movie['cast']
    male_female = [0, 0]
    print len(cast)
    for character in cast:
        person = ia.get_person(character.personID)
        male_female[person.has_key('actress')] += 1
        time.sleep(1)

    print "men:", male_female[0], "women:", male_female[1]

#get_movie(sys.argv[1])
#get_movie("Captain America")
get_movie("Gravity")