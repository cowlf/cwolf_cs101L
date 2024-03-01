wordcount = int(0)
subcount = 0
longestword = ''
usertext = ''
usersub = ''
# This function counts the words in the user- supplied string.
# I used the split() method to create a list i could iterate over to count the words.
def word_count(text):
    wordcount = int(0)
    counttext = text.split(' ')
    for i in counttext:
        wordcount += 1
    return wordcount
# This function will return the longest word from the user's string.
# I also used the split() method here.
# The for loop and if statement are used to update the longest word as the list is iterated over.
def find_longest_word(text):
    longcount = 0
    longestword = ''
    longlist = text.split(' ')
    for i in longlist:
        wordlength = len(i)
        if wordlength > longcount:
            longcount = wordlength
            longestword = i
    return longestword
# This function counts the number of times a user- input substring occurs in the original string.
# I used the count() method here.
def count_substring(text, sub):
    subcount = 0
    subcount = text.count(sub)
    return subcount
# I was not able to find a way for this function to work, I made a few seperate files to test things but nothing worked out.
def extract_unique_words():
    print('I could not find a way to get this to work :(')
# Here is the main function. This executes the other functions and repeats via a while loop.
def main():
    print('Welcome to this text processing test!')
    usertext = input('Please enter text:\n')
    print(f"Original text: {usertext}")
    selectoption = 0
    while selectoption != 5:
        print(f"Text Analysis Options: \n"
              f"1. Word Count\n"
              f"2. Longest Word\n"
              f"3. Count of Substring\n"
              f"4. Unique Words\n"
              f"5. Exit")
        selectoption = int(input('Enter the number of the desired analysis:\n'))
        if selectoption == 1:
            wordcount = word_count(usertext)
            print(f"Word count: {wordcount}")
        elif selectoption == 2:
            longestword = find_longest_word(usertext)
            print(f"Longest word: {longestword}")
        elif selectoption == 3:
            usersub = input('Please input substring to count:\n')
            subcount = count_substring(usertext, usersub)
            print(f"Substring count: {subcount}")
        elif selectoption == 4:
            extract_unique_words()
        elif selectoption == 5:
            print('Thank you for using this program!')
            break
        else:
            selectoption = input('Please enter a valid number 1-5\n')

main()
        
        
    
