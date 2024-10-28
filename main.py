# Самостоятельная работа по уроку "Произвольное число параметров"
# Цель: закрепить знание использования параметров *args/ **kwargs на практике.

def single_root_words(root_word, *other_words):
    same_words = []
    upper_root = root_word.upper()
    for word in other_words:
        upper_word = word.upper()
        if upper_root in upper_word or upper_word in upper_root:
            same_words.append(word)
    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
print(result1)

result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result2)
