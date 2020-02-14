students = []

firstname = input("Please Enter First Name (blank to quit): ").strip()
while firstname != "":
    student = {}
    student ["First Name"] = firstname
    lastname = input("Please Enter Last Name: ").strip()
    student["Last Name"] = lastname
    students.append(student)

    firstname = input("Please Enter First Name (blank to quit): ").strip()

print ("Here are the students you entered: ")
for currentstudent in students:
    print ("{} {}".format(currentstudent["First Name"], currentstudent["Last Name"]))
