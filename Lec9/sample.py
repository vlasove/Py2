"""
D1:P2 G solution
"""

class BirthBook:
    """
    Класс для учета месяцев рождений друзей
    """
    def __init__(self):
        self.birth_dict = {}
        # {'янв' : ['Коля', 'Петя'], ...}

    def parse_string_and_add_new_person(self, message:str):
        """
        Пполучает на вход строку вида `Дима 12 янв` и по итогу добавляет в словарь
        self._berth_dict новые данные
        """
        sample = message.split() #['Дима', '12', 'янв']
        name = sample[0]
        month = sample[-1]

        """
        Добавление элемента и провекра на существование ключа
        """
        if month in self.birth_dict.keys():
            self.birth_dict[month].append(name)
        else:
            self.birth_dict[month] = [name]

    def get_persons_by_month(self, month_name:str):
        """
        Принимает на вход название месяца
        И отдает строку с именами людей у которыъ др в это время
        """
        answer = ""
        if month_name in self.birth_dict.keys():
            answer = " ".join(sorted(self.birth_dict[month_name]))  # sorted(['Витя', 'Вика', 'Петя'])
        return answer 


def main():
    """
    Входная точка в приложение
    """
    n = int(input())
    bb = BirthBook()
    for _ in range(n):
        bb.parse_string_and_add_new_person(input())
    
    n_request = int(input())
    for _ in range(n_request):
        print(bb.get_persons_by_month(input()))


if __name__ == "__main__":
    main()

# Дима 12 янв