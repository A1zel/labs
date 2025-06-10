import re


def process_file_regex(filename):
    content = read_file(filename)
    if not content:
        return

    # Регулярное выражение для поиска четных чисел до 5 цифр
    pattern = r'\b[02468][0-9]{0,4}\b'
    matches = re.findall(pattern, content)

    for i, match in enumerate(matches):
        print(f"Исходное число: {match}")
        if (i + 1) % 2 == 1:  # Нечетная позиция
            print(f"Преобразованное число: {' '.join(digit_to_word[digit] for digit in match)}")
        else:
            print(f"Преобразованное число: {match}")
        print("-" * 30)


if __name__ == "__main__":
    filename = input("Введите имя файла: ")
    print("Результаты без использования регулярных выражений:")
    process_file(filename)
    print("\nРезультаты с использованием регулярных выражений:")
    process_file_regex(filename)
