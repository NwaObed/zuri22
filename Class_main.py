class Student:
    # [assignment] Skeleton class. Add your code here

    T = ['MA']
    
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score
    
    def change_name(self, name):
        self.name

    def change_age(self, age):
        self.age

    # def get_track(self):
    #     return self.tracks

    def add_track(self, track):
        T = self.tracks
        T.append(track)
        return self.tracks
    
    def get_score(self):
        return self.score


Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

#Expected methods  and Check
new_name = Bob.change_name("Peter")
new_age = Bob.change_age(34)
new_track = Bob.add_track("UI/UX")
Stu_score = Bob.get_score()


print("""Student name has changed from {} to {}. The new age also changed from {} to {}. The student updated the
learning track to {} but the score remained at {}""".format(Bob.name, new_name, Bob.age, new_age, new_track,Stu_score))

#print(new_track)

