import random
import string

alphabet = "".join(letter if letter not in "jqxw" else "" for letter in string.ascii_lowercase)
vowels = "aeiou"
consonants = "".join([letter if letter not in vowels else "" for letter in alphabet])

def generate_word():
    word_len = random.choices(list(range(2, 9)), weights=(3, 6, 19, 32, 22, 10, 5))[0]
    word = ""
    
    for _ in range(word_len):
        if not word:
            word += random.choice(alphabet)
        elif word[-1] in vowels:
            word += random.choice(consonants)
        else:
            word += random.choice(vowels)

    return word

def generate_sentence(sentence_len):
    sentence = []

    is_placed = False
    for i in range(sentence_len):
        word = generate_word()

        if i == 0:
            word = word.capitalize()

        if i == sentence_len - 1:
            word += "."
    
        sentence.append(word)

        place_comma = random.choices([True, False], weights=(20, 80), k=1)[0]
        if i != sentence_len - 1 and place_comma and not is_placed:
            sentence[-1] += ","
            is_placed = True

    return " ".join(sentence)

def generate_paragraph(paragraph_len):
    paragraph = []

    for i in range(paragraph_len):
        sentence_len = random.randint(5, 70)
        sentence = generate_sentence(sentence_len)

        if i == 0:
            sentence = "\tFidor tenaha, vas hadu ilah. " + sentence
    
        paragraph.append(sentence)

    return "\n\n".join(paragraph)