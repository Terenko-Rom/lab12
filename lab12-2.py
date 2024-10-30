def count_vowels_in_file(filename):
    vowels = "aeiouAEIOU"
    count = 0  
    try:
        with open(filename, 'r') as file:
            text = file.read()
            for char in text:
                if char in vowels:
                    count += 1
    except FileNotFoundError:
        print("Файл не знайдено.")
        return None
        return count
filename = 'my_text_file.txt'
vowel_count = count_vowels_in_file(filename)
if vowel_count is not None:
    print(f"Кількість голосних літер у файлі: {vowel_count}")