movie_rate = {'Titanic':9.0, 'Star Wars':8.9, 'The Matrix':8.7}
print(hash('Inception'))
print(hash(movie_rate['Star Wars']))
print(movie_rate.keys())
print(movie_rate.values())
print(movie_rate.items())
print(movie_rate.get('Titanic', 0))
print(movie_rate.get('Titanici', 0))
print(movie_rate.get('Titanicis'))

movie_rate.update({'Titanic':9.1})
print(movie_rate)

popVal = movie_rate.pop('Titanic')
print(movie_rate)
print(popVal)

movie_rate.clear()
print(movie_rate)
