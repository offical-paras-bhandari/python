# TODO 1. Create a dictionary in this format:
import pandas

NatoData = pandas.read_csv("nato_phonetic_alphabet.csv")

Nato_Dict = {row.letter: row.code for (index, row) in NatoData.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter a word: ").upper()
dict_user_input = [letter for letter in user_input]
output_list = [Nato_Dict[data] for data in Nato_Dict if data in dict_user_input]
print(output_list)
