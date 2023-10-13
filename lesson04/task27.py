# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.

# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells

# Output: 13

# Вариант 1
text = """She sells sea shells on the sea
shore The shells that she sells are sea
shells I'm sure So if she sells sea shells
on the sea shore I'm sure that the shells are sea shore shells"""
text = text.split()
unique_words = set()

for word in text:
    unique_words.add(word.lower())
    
print(len(unique_words))

# Вариант 2

text = """She sells sea shells on the sea
shore The shells that she sells are sea
shells I'm sure So if she sells sea shells
on the sea shore I'm sure that the shells are sea shore shells"""

print(len(set(text.lower().split())))
