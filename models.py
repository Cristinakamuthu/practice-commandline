from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from . import Base




class Actor(Base):
      __tablename__ = 'actors'

      id = Column(Integer,primary_key = True)
      name = Column(String)
      age = Column(Integer)

      movies = relationship ('Movie', back_populates = 'actor')



class Director(Base):
      __tablename__ = 'directors'

      id = Column(Integer,primary_key = True)
      name = Column(String)
      age = Column(Integer)

      movies = relationship ('Movie', back_populates = 'director')


class Movie(Base):
    __tablename__ = 'movies'

    id = Column(Integer,primary_key = True)
    title = Column(String)
    year = Column(Integer)
    director_id = Column(String, ForeignKey('directors.name'))
    actor_id = Column(String, ForeignKey('actors.name'))

    director = relationship('Director', back_populates= 'movies')
    actor = relationship('Actor',back_populates ='movies')

    









