import random


LETTER_SCORES = {
    'А': 1,
    'Б': 3,
    'В': 1,
    'Г': 3,
    'Д': 2,
    'Е': 1,
    'Ё': 3,
    'Ж': 5,
    'З': 5,
    'И': 1,
    'Й': 4,
    'К': 2,
    'Л': 2,
    'М': 2,
    'Н': 1,
    'О': 1,
    'П': 2,
    'Р': 1,
    'С': 1,
    'Т': 1,
    'У': 2,
    'Ф': 10,
    'Х': 5,
    'Ц': 5,
    'Ч': 5,
    'Ш': 8,
    'Щ': 10,
    'Ъ': 10,
    'Ы': 4,
    'Ь': 3,
    'Э': 8,
    'Ю': 8,
    'Я': 3
}
all_scores = []

def get_random_letter():
    return random.choice(list(LETTER_SCORES.keys()))


def get_word_with_letter():
    while True:
        random_letter = get_random_letter()
        def calculate_score(word):
            all_scores = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
            while True:
                word = input(f"Введите слово на букву '{random_letter}': ").upper()
                if word[0] == random_letter:
                    break
                    # print("Условная канструкция сработала")
                elif word[0] != random_letter:
                    print(f"Слово должно начинатся на '{random_letter}'. Попробуйте снова.")
                # for letter in word:
                #     scores = LETTER_SCORES.get(letter.upper(), 0)
                #     all_scores.append(scores)
            

def main():
    get_word_with_letter()


if __name__ == "__main__":
    main()
