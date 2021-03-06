## Лекция 8. Стандартные методы

### Шаг 1. Переопределение функций
Поскольку интерпретатор читает модуль сверху-вниз, то в ситуации, если встречаются функции с одинаковыми ***именами***, то в итоге, валидной функцией с именем ```name``` будет та, которая встречалась ближе всего к моменту вызова этой функции:
```
def add(a:int, b:int):
    """
    a + b 
    """
    return a + b 



def add(a:int, b:int, c:int):
    """
    a**2 + b**2
    """
    return a**2 + b**2  + c**2



print(add(2,3,4))
```
Будет вызвана функция с сигнатурой ``` def add(a:int, b:int, c:int)```

### Шаг 2. Переопределение методов
Аналогичная история сопровождает и методы (поскольку метод является так же ***САМОЙ ОБЫЧНОЙ ФУНКЦИЕЙ***) то зависимость переопределения от имени метода - точно такая же как и у обычных функций:
```
class Calculator:
    def __init__(self, x:int, y:int):
        self.x_value = x 
        self.y_value = y 


    def calc(self):
        return self.x_value + self.y_value

    def calc(self):
        return self.x_value ** 2 + self.y_value ** 2


c = Calculator(2,10)
print(c.calc())
```

### Шаг 3. Спец методы. Откуда они взялись?
На самом деле при создании класса (ЛЮБОГО) все классы наделены (по умолчанию) набором специальных методов.
Для того, чтобы в этом убедиться давайте проведем эксперимент:
```
class MyClass:
    pass 

message = MyClass()
print(dir(message))
```
В итоге увидим :
```
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
```

Это равносильно тому, что при создании класса мы ***как-будто определяем этим методы в самом верху***.
```
class MyClass:
    def __class__(self):
        pass 

    def __init__(self):
        pass 

    def __str__(self):
        pass 
     
    def __init__(self, message:str):
        print(message)
```

Соответственно, когда я описываю свой констрктор в классе , я ***переопределяю*** стандартный конструктор.


### Шаг 3.1. Переопределение __init__
```__init__``` - это метод-конструктор. ***Вызывается*** на этапе инициализации объекта.Например, если у нас есть класс ```Point``` то вызов метода ```__init__``` произойдет, когда будет обращение к ```Point(...)```

```
class Point:
    def __init__(self, x, y):
        self.x_val = x 
        self.y_val = y 

p = Point(10, 20) # Здесь происходит вызов конструктора
print(dir(p))
```

* Данную функцию (метод) принято описывать в самом начале класса
* В данной функции (метод) принято указывать только оперделения атрибутов
* Данный метод у класса - только один


### Шаг 3.2 Переопределение __str__
***Проблема*** - когда хочу распечатать объект, вижу какую-то кваказябру.
```__str__``` - специальный метод, который позволяет создать ***строковое*** представление объекта. Это означает, что в результате вызова функции ```str()``` с вашим объектом ```str(p)``` появляется возможность создать контролируемое строковое описание:
* Было
```
class Point:
    def __init__(self, x, y):
        self.x_val = x 
        self.y_val = y 

p = Point(10, 20) 
print(p) #<__main__.Point object at 0x0000026AFD01FFD0>
```
* Стало
```
class Point:
    def __init__(self, x, y):
        self.x_val = x 
        self.y_val = y 
    def __str__(self):
        return "Point[X:" +  str(self.x_val) + "  Y:" +  str(self.y_val) +  "]"


p = Point(10, 20) 
print(p)

```

### Шаг 3.2.2 f-Строки
То, что написано выше - дико убого. Перепишем нормально.
```
class Point:
    def __init__(self, x, y):
        self.x_val = x 
        self.y_val = y 
    def __str__(self):
        return f"Point[X:{self.x_val}, Y:{self.y_val}]"
```

***Синтаксис*** - строка начинается с f"" или f'' . После чего внутри строки, в скобках {} указываются параметры для вставки.

### Шаг 3. Сравнение на равенство
***Проблема*** - создав 2 одинаковых объекта они сравниваются по адресу в памяти.  
```
class Point:
    def __init__(self, x, y):
        self.x_val = x 
        self.y_val = y 
    def __str__(self):
        return f"Point[X:{self.x_val}, Y:{self.y_val}]" # f-strings появлились в Python >= 3.6


p1 = Point(10, 20) 
p2 = Point(10, 20)
print(p1 == p2) # при таком сравнении по умолчанию сравниваются адреса в памяти
```

***Решение*** :  Необходимо переопределить базовое правило сравнения.
```
class Point:
    def __init__(self, x, y):
        self.x_val = x 
        self.y_val = y 
    def __str__(self):
        return f"Point[X:{self.x_val}, Y:{self.y_val}]" 
    
    def __eq__(self, other): # Данный метод вызывается, если мы хотим сравнить == 2 объекта
        return (self.x_val, self.y_val) == (other.x_val, other.y_val) 


p1 = Point(10, 20) 
p2 = Point(10, 20)
print(p1 != p2) # при таком сравнении по умолчанию сравниваются адреса в памяти
```
Метод ```__eq__``` если реализован, позволяет сравнивать между собой 2 объекта одного и того же класса как на равенство ```==```, так и ```!=```. Но если нужно свое правило сравнения на ```!=```  переопределить еще и ```__ne__(self, other)```( у препода в жизни за 10 лет такого не было ниразу).


### Шаг 4. Сравнение на больше (меньше)
```
class Point:
    def __init__(self, x, y):
        self.x_val = x 
        self.y_val = y 
    def __str__(self):
        return f"Point[X:{self.x_val}, Y:{self.y_val}]" 
    
    def __eq__(self, other): 
        return (self.x_val, self.y_val) == (other.x_val, other.y_val) 

    def __gt__(self, other): # Сравнение строго `>`. Аналог __lt__
        """
        greater than
        """
        return (self.x_val, self.y_val) > (other.x_val, other.y_val)
```

### Шаг 5. Сравнение на больше-или-равно (меньше-или-равно)
```
class Point:
    def __init__(self, x, y):
        self.x_val = x 
        self.y_val = y 
    def __str__(self):
        return f"Point[X:{self.x_val}, Y:{self.y_val}]" 
    
    def __eq__(self, other): 
        return (self.x_val, self.y_val) == (other.x_val, other.y_val) 

    def __gt__(self, other): # Сравнение строго `>`. Аналог __lt__
        """
        greater than
        """
        return (self.x_val, self.y_val) > (other.x_val, other.y_val)

    def __ge__(self, other): # Сравнение на `>=`. Важно, что `>=` это не `>` + `==`
        return (self.x_val, self.y_val) >= (other.x_val, other.y_val)
```

### Шаг 6. Подумаем
После введения сравнительных операций теперь у нас есть возможность проводить ***сортировки*** коллекций, содержащий объекты пользовательских классов!


### Шаг 7. Подумали.
Рассмотрим последний интересный нам метод ```__del___```. Но для начала необходимо немного поговорить об устройстве памяти в ```Python```.

### Шаг 7.1 Сборщик мусора
```Python``` это язык, в котором управление памятью возложено на плечи не разработчика, а некой программы, которая работает параллельно с нашим интерпретатором (***сборщик мусора*** - часть интерпретатора). Для передачи ***любого*** объекта во вледение сборщика мусора необходимо вызвать ```del``` у этого объекта. После передачи объекта сборщику мусора, данный объект нам более недоступен! Но высвобождение ресурсов памяти произойдет только тогда, когда ***сборщик мусора*** либо переполнит буффер (встроенный) , либо программа будет завершаться, либо придет аварийный сигнал от ОС. ***Главная мысль*** - высвобождение памяти происходит не сразу! Повляить на этот процесс без дополнительных утилит - очень сложно. 
```
class Point:
    def __init__(self, x, y):
        self.x_val = x 
        self.y_val = y 
    def __str__(self):
        return f"Point[X:{self.x_val}, Y:{self.y_val}]" 
    
    def __eq__(self, other): 
        return (self.x_val, self.y_val) == (other.x_val, other.y_val) 

    def __gt__(self, other): # Сравнение строго `>`. Аналог __lt__
        """
        greater than
        """
        return (self.x_val, self.y_val) > (other.x_val, other.y_val)

    def __ge__(self, other): # Сравнение на `>=`. Важно, что `>=` это не `>` + `==`
        return (self.x_val, self.y_val) >= (other.x_val, other.y_val)

    def __del__(self): # Этот метод вызывается в тот момент, когда происходит передача вашего объекта GC
        print("ЭТОТ ОБЪЕКТ ПЕРЕДАН ВО ВЛАЖНЫЕ ЛАДОШКИ СБОРЩИКА МУСОРА")
        print(self)

    


p = Point(10, 20)
1/0
p2 = Point(30, 40)
```

Главная идея состоит в том, что метод ```__del__``` вызывается в момент передачи объекта сборщику мусора. Этот процесс можно спровоцировать следующими способами:
* Вызвать явно через ```del object```
* Неявно, при заврешении работы программы (сборщик мусора сам заберет все существующие обхекты)
* Передача после выброса исключений (в любом случае, должна произойти очистка памяти, поэтому опять же - вызыввается сборщик мусора)

