"""
D1:P2:F solution
"""
class SmartList:
    def __init__(self, input_words:list):
        self.words = input_words

    def get_answer(self):
        print("\n".join(sorted(self.words, key = lambda p : (len(p), p))))



def main():
    """
    Входная точка в приложение
    """
    n = int(input())
    current_words = []
    for _ in range(n):
        current_words.append(input())

    sl = SmartList(current_words)
    sl.get_answer()

if __name__ == "__main__":
    main()