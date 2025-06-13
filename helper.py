from models import Movie
from models import Director
from models import Actor
from models import session


# Learning crud opertions
#  R
def all_movies():
    return session.query(Movie).all()

def all_directors():
    return session.query(Director).all()

def all_actors():
    return session.query(Actor).all()

#  Find

def find_movie():
    return session.query(Movie).filter(Movie.id == id ).first()

# Create

def create_movie(title,year,director_id, actor_id):
    movie  = Movie(title = title, year = year, director_id = director_id, actor_id = actor_id)

    session.add(movie)
    session.commit()
    return movie 

# update

def update_movie(id, title = None ,year = None ,director_id = None , actor_id = None )
    movie = find_movie(id)
    if movie :
        if title:
            movie.title = title
        if year:
            movie.year = year
        if director_id:
            movie.director_id = director_id
        if actor_id:
            movie.actor_id = actor_id
        session.commit()
        return movie
    
def delete_id(id):
    movie = find_movie(id)
    if movie:
        session.delete(movie)
        session.commit()
        return True
    return False








