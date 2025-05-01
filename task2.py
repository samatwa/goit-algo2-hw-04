from trie import Trie

# Клас LongestCommonWord наслідує Trie і реалізує метод для знаходження найдовшого спільного префікса
class LongestCommonWord(Trie):
    def find_longest_common_word(self, strings) -> str:
        # Перевіряємо, що strings — список рядків
        if not isinstance(strings, list) or not all(isinstance(s, str) for s in strings):
            raise TypeError("Illegal argument for find_longest_common_word: strings = {strings} must be a list of strings")

        # Якщо список порожній — повертаємо порожній рядок
        if not strings:
            return ""

        # Якщо у списку лише один рядок — він і є спільним префіксом
        if len(strings) == 1:
            return strings[0]

        # Додаємо всі рядки у Trie з унікальними значеннями
        for i, word in enumerate(strings):
            self.put(word, i)

        # Обчислюємо довжину найкоротшого слова, бо префікс не може бути довшим за нього
        min_len = min(len(word) for word in strings)

        current = self.root  # Починаємо з кореня Trie
        prefix = ""          # Змінна для збереження результату — префікса

        # Поки глибина не перевищує мінімальну довжину
        for _ in range(min_len):
            # Якщо в поточному вузлі більше одного нащадка або він є кінцем слова —
            # ми досягли межі спільного префікса
            if len(current.children) != 1 or current.value is not None:
                break

            # Отримуємо єдиного нащадка цього вузла
            char, next_node = next(iter(current.children.items()))
            prefix += char           # Додаємо символ до префікса
            current = next_node      # Переходимо глибше в Trie

        return prefix  # Повертаємо найдовший знайдений спільний префікс
    
if __name__ == "__main__":
    # Тести
    trie = LongestCommonWord()
    strings = ["flower", "flow", "flight"]
    assert trie.find_longest_common_word(strings) == "fl"

    trie = LongestCommonWord()
    strings = ["interspecies", "interstellar", "interstate"]
    assert trie.find_longest_common_word(strings) == "inters"

    trie = LongestCommonWord()
    strings = ["dog", "racecar", "car"]
    assert trie.find_longest_common_word(strings) == ""