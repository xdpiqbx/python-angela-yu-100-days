import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")

data_dict = {row.letter: row.code for (index, row) in data.iterrows()}


def convert_word_to_list_of_nato_code(word):
    return [data_dict[letter] for letter in word.upper() if letter in data_dict.keys()]


print(convert_word_to_list_of_nato_code(input("Enter a word: ")))

