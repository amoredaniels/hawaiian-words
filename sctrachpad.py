#get input
word =  input('Enter a hawaiian word: ').lower()
#initialize input
validInput = True
#valid characters
validCh = "aeioupkhlmnw '"
consonants = 'pkhlmn'
vowels = {'a':'ah-','e':'eh-','i':'ee-','o':'oh-','u':'oo-'}
vowelGroups = {'ai':'eye-','ae':'eye-','ao':'ow-','au':'ow-',
                'ei':'ay-','eu':'eh-oo-','iu':'ew-','oi':'oy-',
                'ou':'ow-','ui':'ooey-'}
#vowelGroups = ['ai','ae','ao','au','ei','eu','iu','oi','ou','ui']
i = 0
#pronounce variable
keepGoing = True
#empty string for resulting string
result = ''

#special consonant function
def specialConsonant():
    # return the first instance of the letter 'w' and assign to currentCh
    currentCh = word.index('w')
    #assign previous ch to the ch before the first 'w'
    lastCh = currentCh - 1
    global result
    #if first letter is w, print w
    if word[0] == 'w':
        result +='w'
    #check if 'w' is after a vowel; it should not go to front of string
    if (word[currentCh] == 'w' and word[lastCh] == 'a') and word[0] != 'w':
        result+='w'
    # if w is after the letter 'i' print v
    if (word[currentCh] == 'w' and word[lastCh] == 'i') and word[0] != 'w':
        result +='v'
    # if w is after the letter 'e' print v  
    if (word[currentCh] == 'w' and word[lastCh] == 'e') and word[0] != 'w':
        result+='v'
    # if w is after the letter 'u' print w
    if (word[currentCh] == 'w' and word[lastCh] == 'u') and word[0] != 'w':
        result+='w' 
    #if w is after the letter 'o' print w
    if (word[currentCh] == 'w' and word[lastCh] == 'o') and word[0] != 'w':
        result+='w'


#validating input
while validInput == True:
    for ch in word:
        if ch not in validCh:
            print('{} is an invalid character. Try again!'.format(ch))
            word =  input('Enter a hawaiian word: ').lower()
        else:
            validInput = False


#getting pronounciation
if keepGoing == True:
    #CONSONANTS
    #for each ch in word
    for ch in word:
        #check if letter in consonants
        if ch in consonants:
            #add that letter to the resulting sting
            result += ch
        elif ch == 'w':
            # return the first instance of the letter 'w' and assign to currentCh
            currentCh = word.index('w')
            #assign previous ch to the ch before the first 'w'
            lastCh = currentCh - 1
            # global result
            #if first letter is w, print w
            if word[0] == 'w':
                result +='w'
            #check if 'w' is after a vowel; it should not go to front of string
            elif (word[currentCh] == 'w' and word[lastCh] == 'a') and word[0] != 'w':
                result+='w'
            # if w is after the letter 'i' print v
            elif (word[currentCh] == 'w' and word[lastCh] == 'i') and word[0] != 'w':
                result +='v'
            # if w is after the letter 'e' print v  
            elif (word[currentCh] == 'w' and word[lastCh] == 'e') and word[0] != 'w':
                result+='v'
            # if w is after the letter 'u' print w
            elif (word[currentCh] == 'w' and word[lastCh] == 'u') and word[0] != 'w':
                result+='w' 
            #if w is after the letter 'o' print w
            elif (word[currentCh] == 'w' and word[lastCh] == 'o') and word[0] != 'w':
                result+='w'

            #print(ch)
    #SINGLE VOWELS & VOWEL GROUPS
        elif ch in vowels:
            if ch == 'a':
                nextCh = word[i+1]
                if nextCh == 'i' or nextCh == 'e':
                    result+='eye-'
                    i+=1
                elif nextCh == 'o' or nextCh == 'u':
                    result+='ow-'
                    i+=1
                else:
                    result+='ah-'

            elif ch == 'e':
                nextCh = word[i+1]
                if nextCh == 'i':
                    result+='ay-'
                    i+=1
                elif nextCh == 'u':
                    result+= 'eh-oo'
                    i+=1
                else:
                    result+='eh-'

            elif ch == 'i':
                nextCh = word[i+1]
                if nextCh == 'u':
                    result+= 'ew-'
                    i+=1
                else:
                    result+= 'ee-'
            
            elif ch == 'o':
                nextCh = word[i+1]
                if nextCh == 'i':
                    result+='oy-'
                    i+=1
                elif nextCh == 'u':
                    result+='ow-'
                    i+=1
                else:
                    result+='oh-'

            elif ch == 'u':
                nextCh = word[i+1]
                i+=1
            else:
                result+='oo-'

print(word.upper(),'is pronounced',result.capitalize())

playAgain= input('Do you want to enter another word? (Y/YES/N/NO) ').upper()

if playAgain == 'YES' or 'Y':
    result = ''
    word = input('Enter a hawaiian word: ').lower()
    keepGoing = True
else:
    keepGoing = False