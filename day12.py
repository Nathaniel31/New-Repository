def mostFrequentLetter(Letter):

    Letter = Letter.lower()
    Letter = Letter.replace(" ","")
    maxCount = 0
    for i in range(0,len(Letter)):
        if Letter.count(Letter[i])> maxCount:
            maxCount = Letter.count(Letter[i])
            maxLetter = Letter[i]
        if Letter.count(Letter[i]) == maxCount:
            if Letter[i]< maxLetter:
                maxLetter = s[i]
    return maxLetter


    

print(mostFrequentLetter("I am a boy"))

