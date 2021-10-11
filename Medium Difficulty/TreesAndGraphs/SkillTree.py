

def getMinNumberOfSkills(Tarray,skills):


    necessarySkills = getDictionaryOfSkills(len(Tarray))

    for skill in skills:
        necessarySkills = updateNecessarySkills(Tarray,skill,necessarySkills)

    return sum(necessarySkills.values())



def updateNecessarySkills(Tarray,skill,necessarySkill):
    current = skill
    necessarySkill[current] = 1

    while current > 0:
        current = Tarray[current]
        necessarySkill[current] = 1

    return necessarySkill


def getDictionaryOfSkills(size):
    necessarySkills = dict()

    for i in range(size):
        necessarySkills[i] = 0

    return necessarySkills



print(getMinNumberOfSkills([0,0,1,1],[2]))
print(getMinNumberOfSkills([0,0,0,0,2,3,3],[2,5,6]))
print(getMinNumberOfSkills([0,0,1,2],[1,2]))
print(getMinNumberOfSkills([0,3,0,0,5,0,5],[4,2,6,1,0]))
