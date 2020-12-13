"""
Хотим создать сервис для потокового воспроизведения фильмов.
Для того, чтобы сохранить фильм, нужно сохранить "критерии фильмовости".

Стало лучше, но проблема с контролем целостности хранилища еще не решена
К тому же, мы до сих пор не храним ФИЛЬМЫ
"""

titles = ['HP:1', 'LOTR:1', "HP:2"]
durations = [210, 999, 220]
ratings = [4.8, 4.8, 4.8]
actors_list = [
    ['Emma Watson', 'Friend1', 'Rupert Grin'],
    ['O Blum', 'Friend1', 'Friend2', 'Fritend3'],
    ['Emma Watson', 'Friend1', 'Rupert Grin']
]

# Добавление нового фильма выглядит теперь так
titles.append("LOTR:2")
durations.append(9999)
ratings.append(4.7)
actors_list.append(['O Blum', 'Friend1', 'Friend2', 'Fritend3'])