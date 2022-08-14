guess = ""
result = ""
words = []


with open('list.txt') as f:
    for line in f:
        words.append(line.strip())


print("Input a starter word of your choice. I recommend using SOARE, but feel free to use your own starter word.")


for guesses in range(6):

    guess = input("\n\nWord: ").lower()
    
    print("What Result Did Wordle Give You?")
    print("$ = Green, * = Yellow, # = Grey")
    result = input("Results: ")
    
    
    # if solved
    if result == "$$$$$":
        print("\n\nMission Acomplished: Wordle in", guesses+1)
        break


    tupleX = tuple(words)
    for word in tupleX:
        for i in range(5):

            #Logic 1: remove from list if word has grey letter
            if result[i] == "#" and guess[i] in word:
                words.remove(word)
                break

            #Logic 2: remove from list if word goes not have green letter in correct place
            elif result[i] == "$" and guess[i] != word[i]:
                words.remove(word)
                break

            #Logic 3: remove from list if word does not have yellow letter
            elif result[i] == "*" and guess[i] not in word:
                words.remove(word)
                break

            #Logic 4: remove from list if word has yellow letter in same place
            elif result[i] == "*" and guess[i] == word[i]:
                words.remove(word)
                break

                
    print("\nThese are a list of possible answers, use your judgement to select one.\n")
    print(words)
