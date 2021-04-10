green = "\033[0;32;40m"
white = "\033[0;37;40m"
red = "\033[0;31;40m"

def findLettersInWord(word, letter):
    index = 0
    letterPositions = []
    letterList = ""
    for x in word:
        index = index + 1
        if (x == letter):
            letterPositions.append(str(index))
    for x in letterPositions:
        letterList = letterList + x + " "
    if (letterList == ""):
        return red + "That letter doesn't appear in the given word"
    else:
        return green+"That letter can be found at positions(s): "+letterList


word = input(green+"What word do you want? (hopefully its long)\n"+white+">> ")
letter = input(green + "Tell me a letter in the word.\n" + white + ">> ")
while (len(letter) != 1):
    letter = input(red + "That is not a letter. Please enter a 1-letter string.\n" + white + ">> ")
print(findLettersInWord(word, letter))