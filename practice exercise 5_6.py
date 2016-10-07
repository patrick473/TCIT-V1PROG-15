studentgrades = [ [95, 92, 86],[66, 75, 54],[89, 72, 100],[34, 0, 0] ]
antwlist = []
antwo = []
def average_of_student(studentgrades) :
    for i in studentgrades :
        antwo.append((i[0]+ i[1]+ i[2]) / 3)

    return antwo

def average_of_all_students(studentgrades) :
    for i in studentgrades :
        antwlist.append( sum(i) / 3)
        antw = sum(antwlist) / 4

    return antw

print(average_of_student(studentgrades))
print(average_of_all_students(studentgrades))
