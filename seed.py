from models import Base, engine, session
from models import Movie
from models import Actor
from models import Director


Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

actor1 = Actor(name='Cristina Nyawira', age=24)
actor2 = Actor(name='Francisca Kamuthu', age=30)

director1 = Director(name='Marion Wangare', age=45)

movie1 = Movie(title='Rise of the Devs', year=2025, director=director1, actor=actor1)
movie2 = Movie(title='Codebound', year=2025, director=director1, actor=actor2)

session.add_all([actor1, actor2, director1, movie1, movie2])
session.commit()
