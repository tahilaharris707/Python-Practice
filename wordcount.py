# I will create a module that counts the number of times a word appears in a text.
# I will start with creating a def function.

def get_words_list(string):
    # I will creat a word list that will split the string.
    word_list=string.split()
    #I will creat a function that will return the word list.
    return word_list

# I will create an empty dictionary that will hold the words that are counted using a def function.

def get_counts(word_list):
    word_counts=dict()
    
    # I will create a for loop to search through the word list.
    for word in word_list:
        # I will use the in function to see if a word is in the word list.
        if not word in word_counts:
            word_counts[word]=1
        else:
            word_counts[word]+=1
     # I will create a funtion that will return the word_counts
    return word_counts
        


    