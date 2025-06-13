from helper import all_movies, find_movie, create_movie

movie = all_movies()
for movi in movie:
    print(movi.title)

new_movie = create_movie('Cristina movieee', 2024, 'Salome', 'Tina')
print(new_movie)

movie = find_movie(1)
print(movie)
