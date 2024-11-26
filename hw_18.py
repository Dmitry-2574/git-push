"""
ValueError - если очень большой сдвиг

Разное количество символов происходит из-за особенностей UTF-8 кодирования. Некоторые символы в UTF-8 могут занимать разное количество байт. При сдвиге мы можем попасть в диапазон, где символы представлены другим количеством байт. Но раскодируется корректно, потому что обратный сдвиг возвращает нас к исходным кодам символов.

Шестнадцатеричные значения появляются, когда мы попадаем в определенные диапазоны Unicode, где находятся специальные символы или управляющие последовательности. Раскодируется правильно по той же причине - математически операции сдвига и обратного сдвига компенсируют друг друга.

Ошибка при огромном сдвиге возникает, когда мы выходим за пределы допустимого диапазона Unicode (0x10FFFF или 1,114,111 в десятичной системе).
"""

STEP_CHANGE = 50 # На сколько сдвигать символы

user_input = 'aAbBCcDd'

users_words =  user_input.split()

# Обходим циклом каждое слово, каждую букву
# Получаем код буквы и сдвигаем на заданный шаг

encode_user_input = []
for word in users_words:
    # Переменная под слово
    encode_word = ''
    # Обходим буквы
    for letter in word:
        # Код буквы
        letter_code = ord(letter)
        # Сдвиг
        letter_code += STEP_CHANGE
        # Символ
        letter_encode = chr(letter_code)
        # Добавляем в слово
        encode_word += letter_encode
    
    # Добавляем в список
    encode_user_input.append(encode_word)

# Выводим результат
encode_user_input_string = ' '.join(encode_user_input)
print(encode_user_input_string)



# Обратный сдвиг
decode_user_input = []
for word in encode_user_input:
    # Переменная под слово
    decode_word = ''
    # Обходим буквы
    for letter in word:
        # Код буквы
        letter_code = ord(letter)
        # Обратный сдвиг
        letter_code -= STEP_CHANGE
        # Символ
        letter_decode = chr(letter_code)
        # Добавляем в слово
        decode_word += letter_decode
    
    # Добавляем в список
    decode_user_input.append(decode_word)

# Выводим результат
decode_user_input_string = ' '.join(decode_user_input)
print(decode_user_input_string)


