import kivy

class course:
    @staticmethod
    def findCourse():
        lines = []
        majors = ["BE","EC","ME"]
        for i in range(0,2):
            line = input()
            if line and i == 0:

                def validMajor():
                    for M in majors:
                        if line.upper() == M.upper():
                            return True
                    return False

                while line.__len__() != 2 or not validMajor():
                    print("major not valid, try again")
                    print("please enter BE, EC, or ME")
                    line = input()

                lines.append(line.upper()) 

            elif line and i == 1:
                def getOrdSum(stringVal):
                    cumsum = 0
                    for c in stringVal:
                        cumsum += ord(c)  
                    return cumsum

                sum = getOrdSum(line)

                while sum < 144 or sum > 171:
                    print("course number not valid, try again")
                    print("please enter course number between 000-999")
                    line = input()
                    sum = getOrdSum(line)

                lines.append(line)
                break
            else:
                break
        coursenum = lines.pop()
        dep = lines.pop()
        return {"Department": dep, "Course" : coursenum}

if __name__ == "__main__":
    courses = list()
    print("how many classes this semester?")
    numC = input()
    for i in range(int(numC)):
        courses.append(course.findCourse())
    print(courses)
