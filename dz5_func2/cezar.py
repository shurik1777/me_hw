""" Написать две функции - шифратор и дешифратор Цезаря
Сначала сделать классику со сдвигом по алфавиту, а вот потом уже и свой попробовать """
alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'


def encrypt_caesar(clear_text, shift):
    cipher_text = ''
    for letter in clear_text:
        if letter in alphabet:
            shifted_index = (alphabet.index(letter) + shift) % len(alphabet)
            cipher_text += alphabet[shifted_index]
        else:
            cipher_text += letter
    return cipher_text


def decrypt_caesar(cipher_text, shift):
    clear_text = ''
    for letter in cipher_text:
        if letter in alphabet:
            shifted_index = (alphabet.index(letter) - shift) % len(alphabet)
            clear_text += alphabet[shifted_index]
        else:
            clear_text += letter
    return clear_text


text = 'много нового'
encrypted_text = encrypt_caesar(text, 3)
print(encrypted_text)
decrypted_text = decrypt_caesar(encrypted_text, 3)
print(decrypted_text)

# import string
#
#
# def cipher_decoder(text, key, characters=string.ascii_lowercase, decrypt=False):
#     if key < 0:
#         print('Ключ не может быть отрицательным')
#         return None
#     n = len(characters)
#     if decrypt == True:
#         key = n - key
#     table = str.maketrans(characters, characters[key:] + characters[:key])
#     translated_text = text.translate(table)
#     return translated_text
#
#
# character_set = string.ascii_lowercase + string.ascii_uppercase + string.digits + " " + string.punctuation
# print('Применяемые буквы, символы в процессе:\n', character_set)
# plain_text = 'My name is Alexander! I have been living and working in the Nizhny Novgorod' \
#              ' region of Uren since 2014, please keep it a secret!'
# encrypted = cipher_decoder(plain_text, 5, character_set, decrypt=False)
# print('Входящий текст:\n', plain_text)
# print('Зашифрованный или расшифрованный текст:\n', encrypted)
