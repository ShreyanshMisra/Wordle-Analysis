# Initializing variables and list
guess = ""
result = ""
guess_list = []


# Appending wordle words to list
try:
    with open('wordle_words.txt') as f:
        for line in f:
            guess_list.append(line.strip())
except FileNotFoundError:
    print("Word List Is Not In This Directory")


# Instructions
print("Type in a starter word of your choice")
print("My analysis concluded that SOARE is the best starter word, but feel free to use your own.")


for guesses in range(6):
    
    # Input 
    guess = input("\n\nWord: ").lower()
    
    # Result
    print("What Result Did Wordle Give You?")
    print("$ = Green, * = Yellow, # = Grey")
    result = input("Results: ")
    
    
    # Game over condition
    if result == "$$$$$":
        print("Mission Acomplished: Wordle in",guesses+1)
        break


    # Tuple Used As We Can't Iterate Over A Changing List
    tuple_1 = tuple(guess_list)
    for word in tuple_1:
        for i in range(5):


            #Logic 1: Remove From List If Word Has A Grey Letter
            if result[i] == "#" and guess[i] in word:
                guess_list.remove(word)
                break


            #Logic 2: Remove From List If Word Does Not Have Green In Correct Place
            elif result[i] == "$" and guess[i] != word[i]:
                guess_list.remove(word)
                break


            #Logic 3: Remove From List If Word Does Not Have Yellow Letter
            elif result[i] == "*" and guess[i] not in word:
                guess_list.remove(word)
                break


            #Logic 4: Remove From List If Word Has Yellow Letter In Same Place 
            elif result[i] == "y" and guess[i] == word[i]:
                guess_list.remove(word)
                break


    #Only Prints Ten Words Per Line
    counter = 0
    print("\nThese Are A List Of Possible Words. Use Your Judgement To Select One.")
    for word in guess_list:
        print(word,end=", ")
        counter+=1
        if counter == 10:
            print("")
            counter = 0
