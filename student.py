class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def welcome(self):
        print("Your Name is: ",self.name)
    def mark(self):
        print("Your marks are: ",self.marks)
    def total(self):
        sum=0
        for i in self.marks.values():
            sum=sum+i
        print("Total: ",sum)
    def avg(self):
        sum=0
        for i in self.marks.values():
            sum=sum+i
            p=len(self.marks)
        print("Average of yOUR marks : ",sum/p)
    

s1=Student("Messi",{"maths":90,"chem":80,"phy":100})
s1.welcome()
s1.mark()
s1.total()
s1.avg()
