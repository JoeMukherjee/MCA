class student:
            def getStudent(self):
                        self.name=input("Enter student name: ")
                        self.roll=input("Enter student roll: ")
            def putStudent(self):
                        print("Student name is " + self.name+ " and roll is " + self.roll)
class marks:
            def getMarks(self):
                        s=[]
                        n=[]
                        m=input("Enter number of subjects")
                        for i in m:
                                    s[i]=input("Enter " +i+" no. subject name")
                                    self.n[i]=input("Enter marks obtained in this subject")
                                    
a=student()
print(help(a.getStudent()))