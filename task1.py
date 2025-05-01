from trie import Trie

# Клас Homework успадковує Trie і реалізує два методи:
# - count_words_with_suffix: підрахунок слів, що закінчуються на заданий суфікс
# - has_prefix: перевірка наявності хоча б одного слова з заданим префіксом
class Homework(Trie):
    
    def count_words_with_suffix(self, pattern) -> int:
        # Перевірка, що pattern — це рядок
        if not isinstance(pattern, str):
            raise TypeError(f"Illegal argument for countWordsWithSuffix: pattern = {pattern} must be a string")

        # Отримуємо всі слова з Trie, які були додані
        words = self._collect_words(self.root, "")

        # Рахуємо кількість слів, які закінчуються на вказаний суфікс (з урахуванням регістру)
        return sum(1 for word in words if word.endswith(pattern))

    # Рекурсивна допоміжна функція для збору всіх слів із Trie
    def _collect_words(self, node, prefix):
        results = []

        # Якщо вузол є кінцем слова (має значення) — додаємо слово
        if node.value is not None:
            results.append(prefix)

        # Рекурсивно проходимо по всіх дочірніх вузлах
        for char, child in node.children.items():
            results.extend(self._collect_words(child, prefix + char))

        return results

    def has_prefix(self, prefix) -> bool:
        # Перевірка, що prefix — непорожній рядок
        if not isinstance(prefix, str) or not prefix:
            raise TypeError(f"Illegal argument for has_prefix: prefix = {prefix} must be a non-empty string")

        current = self.root

        # Посимвольно проходимо по Trie, перевіряючи наявність префіксу
        for char in prefix:
            if char not in current.children:
                return False  # Якщо символа немає — префікс відсутній
            current = current.children[char]

        return True  # Після успішного проходження — префікс існує

# Приклад використання
if __name__ == "__main__":
    trie = Homework()
    
    # Додаємо слова у Trie з унікальними значеннями
    words = ["apple", "application", "banana", "cat"]
    for i, word in enumerate(words):
        trie.put(word, i)

    # Тести для перевірки підрахунку слів за суфіксом
    assert trie.count_words_with_suffix("e") == 1       # "apple"
    assert trie.count_words_with_suffix("ion") == 1     # "application"
    assert trie.count_words_with_suffix("a") == 1       # "banana"
    assert trie.count_words_with_suffix("at") == 1      # "cat"

    # Тести для перевірки наявності префіксів
    assert trie.has_prefix("app") == True               # "apple", "application"
    assert trie.has_prefix("bat") == False
    assert trie.has_prefix("ban") == True               # "banana"
    assert trie.has_prefix("ca") == True                # "cat"
