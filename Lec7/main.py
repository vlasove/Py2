"""
D1:P2: E : Solution
"""
class Sequence:
    def __init__(self, input_message:str):
        self.message = input_message

    def find_max(self):
        """
        Находит максимальную подпоследовательность символов "о" в строке
        и возвращает длину такой подполседовательности
        """
        return len(max(self.message.split("р"))) # len(max(["", "", "o", "ooooo", "o", ""])) == len("ooooo")

def main():
    """
    Входная точка в приложение
    """
    seq = Sequence(input())  # Sequnce("pppooopoopoppp")
    print(seq.find_max())

if __name__ == "__main__":
    main()


# """
# D1:P2 : Solution
# """
# class Sequence:
#     def __init__(self, input_message:str):
#         self.message = input_message

#     def find_max(self):
#         return len(max(self.message.split("р"))) # len(max(["", "", "o", "ooooo", "o", ""])) == len("ooooo")


# seq = Sequence(input())  # Sequnce("pppooopoopoppp")
# print(seq.find_max())