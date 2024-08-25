import functions.funds
voteList:list[int] = []
newvoteList:list[int] = []
ind:int = 0
maxPosVote:int = 0
maxNegVote:int = 0
maxNonVote:int = 0
indFirstPos:int = 0
indLastNeg:int = 0
while ind < 8:
    try:
        voteList.append(functions.funds.enterInteger("enter the next vote"))
        if voteList[ind] not in [1, 2, 3, 4 ]:
            print("the vote is illegal, try again")
            voteList.pop()
            continue
        if voteList[ind] == 4:
            print(f"the vote number {ind + 1} voted vetto")
            voteList.pop()
            break
        maxPosVote += 1 if voteList[ind] == 1 else 0
        ###print("votelist", voteList, "voteList[ind]", voteList[ind], "maxPosVote", maxPosVote)
        maxNegVote += 1 if voteList[ind] == 2 else 0
        maxNonVote += 1 if voteList[ind] == 3 else 0
        ind += 1
    except Exception as e:
        print("you entered a wrong number", e, "try again")
        continue

print("votelist", voteList)

print(f"positive votes: {maxPosVote} negative votes: {maxNegVote} not voted: {maxNonVote}")
try:
    indFirstPos = voteList.index(1) + 1
    print(f"the first country to vote positive is: {indFirstPos} end = " "")
except Exception as e:
    print("there was no positive vote")
try:
    newvoteList = list(reversed(voteList))  # iterator
    indLastNeg = len(newvoteList) - newvoteList.index(2)
    print(f"the last country to vote negative: {indLastNeg}")
except Exception as e:
    print("there was no negative vote")

