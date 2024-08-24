class Robot:

    def __init__(self,name,color,weight):
        self.name = name
        self.color = color
        self.weight = weight

    def introduce_self(self):
        print(f"My name is {self.name}")

robot_1 = Robot("Tom","blue",40)
robot_2 = Robot("Jerry","red",30)

robot_1.introduce_self()
robot_2.introduce_self()