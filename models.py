from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

engine = create_engine('sqlite:///movie.db')
Session = sessionmaker(bind=engine)
session = Session()





class Actor(Base):
      __tablename__ = 'actors'

     
      name = Column(String,primary_key = True)
      age = Column(Integer)

      movies = relationship ('Movie', back_populates = 'actor')



class Director(Base):
      __tablename__ = 'directors'

      
      name = Column(String, primary_key =True)
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

    









