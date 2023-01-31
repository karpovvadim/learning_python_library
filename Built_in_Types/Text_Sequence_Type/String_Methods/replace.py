"""str.replace(old, new[, count])"""   # заменять
# Возвращает копию строки, в которой все вхождения старой подстроки заменены новой.
# Если задан необязательный аргумент count, заменяются только первые экземпляры count.

song = 'cold, cold heart'
print(song.replace('cold', 'hurt'))  # replacing 'cold' with 'hurt'
song = 'Let it be, let it be, let it be, let it be, let it be'
print(song.replace('let', "don't let", 2))  # replacing only two occurences of 'let'
song = 'cold, cold heart'
replaced_song = song.replace('o', 'e')
print('Original string:', song)  # The original string is unchanged
print('Replaced string:', replaced_song)
