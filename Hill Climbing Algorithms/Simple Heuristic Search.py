import string
import random

def randomGen(goalList):
    characters = string.ascii_lowercase+" "
    randString =""
    for i in range(len(goalList)):
        randString = randString+characters[random.randrange(len(characters))]
    randList = [randString[i] for i in range(len(randString))]
    return randList

def scoreRand(goalList,randList):
    numScore = 0
    for i in range(len(goalList)):
        if goalList[i] == randList[i]:
            numScore = numScore+1
    return numScore / len(goalList)

def common_elements(clist,list1, list2):
    for i in range(len(list1)):
        if list1[i] == list2[i]:
            clist[i] = list1[i]
    return clist

def main():
    goal = input('Input a Goal State  ')
    goalList = [goal[i] for i in range(len(goal))]
    clist = [' ' for i in range(len(goal))]
    randList = randomGen(goalList)
    clist = common_elements(clist,goalList, randList)
    score = scoreRand(goalList,clist)
    totalIteration = 0
    while(score < 1):
        newrandList = randomGen(goalList)
        newclist = common_elements(clist,goalList, randList)
        newscore = scoreRand(goalList,clist)
        score = newscore
        randList = newrandList
        clist = newclist
        totalIteration = totalIteration+1
        print(score," : ",''.join(clist))
    print("Total iterations: ",totalIteration)

main()
