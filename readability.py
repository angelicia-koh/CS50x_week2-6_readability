def main():

    while True:
        text = input("Text: ")  # Prompt the user for some text
        if len(text) < 1:
            print("Invalid")
        else:
            break
    # Count the number of letters, words, and sentences in the text
    numof_letters = letters(text)
    numof_words = words(text)
    numof_sentences = sentences(text)

    L = numof_letters / numof_words * 100.0
    S = numof_sentences / numof_words * 100

    index = 0.0588 * L - 0.296 * S - 15.8  # Compute the Coleman-Liau index

    # Print the grade level
    if round(index) > 16:  # more than 16
        print("Grade 16+")

    elif 1 <= round(index) <= 16:  # between 1 to 16
        print(f"Grade {round(index)}")

    elif round(index) < 1:  # less than 1
        print("Before Grade 1")

    else:
        print("Error")


def letters(text):

    count_letters = 0
    for char in text:
        if char.isalpha():
            count_letters += 1

    return count_letters


def words(text):

    count_words = 1
    for char in text:
        if char == " ":
            count_words += 1

    return count_words


def sentences(text):

    count_sentences = 0
    for char in text:
        if char == "." or char == "?" or char == "!":
            count_sentences += 1

    return count_sentences


main()
