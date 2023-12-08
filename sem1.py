def find_paragraphs(filename, word):
    with open(filename, "r") as f:
        lines = f.readlines()

    paragraphs = []
    for line in lines:
        if line != "\n":
            paragraphs.append(line)

    for paragraph in paragraphs:
        if word in paragraph:
            print(paragraph)
        else:
            print("Помилка: слово " + word + " не знайдено в файлі " + filename)

while True:
    filename = "random.txt"
    word = input("Введіть слово для пошуку: ")
    if word.lower() == 'exit':
        break
    find_paragraphs(filename, word)