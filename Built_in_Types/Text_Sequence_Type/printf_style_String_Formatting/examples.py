print('%(language)s has %(number)03d quote types.' %
      {'language': "Python", "number": 2})  # Python имеет 002 типа кавычек.

print('%(language)r has %(number)-02i quote types.' %
      {'language': "Python", "number": 2})

print('%(language)a has %(number) 03o quote types.' %
      {'language': "Python", "number": 12})

print('%(language)s has %(number)03X quote types.' %
      {'language': "Python", "number": 12})

print('%(language)s has %(number)02e quote types.' %
      {'language': "Python", "number": 12})

print('%(language)s has %(number)02f quote types.' %
      {'language': "Python", "number": 12})

print('{} has {:04d} quote types.'.format('Python', 12))

print('%(language)a has %(number)03c quote types.' %
      {'language': "Python", "number": 12})

print('%(language)# has %(number)03a quote types.' %
      {'language': "Python", "number": 2})
