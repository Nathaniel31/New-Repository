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


    

##print(mostFrequentLetter("I am a boy"))

#using dictionary
def mostFrqLetter(s):
    s = s.lower()
    s = s.replace(" ","")
    count = dict()
    maxLetter = None
    maxCount = 0
    for i in s:
        if count.get(i,0) == 0:
            count[i] = 1
        else:
            count[i]+=1
        if count[i] >maxCount:
            maxCount = count[i]
            maxLetter=i
    return maxLetter

def testMostFrqLetter():
    print("testing mostFrqLetter....")
    assert mostFrqLetter("sjfhks") == "s"
    assert mostFrqLetter("AABBAA") == "a"
    assert mostFrqLetter("SAT reading") == "a"
    print("all passed")

testMostFrqLetter()
print(mostFrqLetter("sjfhks"))

