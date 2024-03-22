

with open("books/frankenstein.txt") as f:
    file_contents = f.read()

def count_words(text):
    words = text.split()
    num_words = len(words)
    print(num_words)

# count_words(file_contents)

my_string = file_contents

    

my_dictionary = {}

i_count = 0

def count_letters(my_string):

    for i in range(0, len(my_string.split())):
        for j in range(0, i):
            if j == "c":
                i_count += 1
    print(i_count)



    