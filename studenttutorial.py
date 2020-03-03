class students:
    def __init__(self, name, age):
                self.name = name
                self.age = age
    
    class_ = "student"
    
    def avescore(self):
        test1 = int(input("input test1 mark: "))
        test2 = int(input("input test2 mark: "))
        test3 = int(input("input test3 mark here: "))
        avescore = (test1 + test2 + test3)/3
        print(avescore)
mark = students("Mark", "30")
mark.avescore()