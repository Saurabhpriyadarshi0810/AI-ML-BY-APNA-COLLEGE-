# Student Enrolments

# Given a list of tuples with info(name, subject):

#  list all unique course

#  list students enrolled in English

#  create dictionary (student, set of courses)

info = [
("Alice", "Math"),
("Bob", "Science"),
("Alice", "Science"),
("Charlie", "Math"),
("Bob", "Math"),
("Alice", "English"),
("Charlie", "English"),
]


unique_course = set()

for i in info :
    unique_course.add(i[1])

x =list(unique_course)
print(x)


lis = []
for i in info :
    if i[1] == "English":
        lis.append(i[0])

print(lis)


dict = {}


for i in info :
    if dict.get(i[0]) == None :
        dict.update({i[0]:set()})
        dict[i[0]].add(i[1])
    else:
        dict[i[0]].add(i[1])


print(dict)