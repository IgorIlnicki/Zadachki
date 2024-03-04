class Animal:
    def __init__(self, nickname, weight, color):
        self.nickname = nickname
        self.weight = weight
        self.color = color

    def change_color(self, col):
        self.color = col
    
    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight

first_animal = Animal("s1",12,"white") 
second_animal = Animal("s2",10,"white") 
first_animal.change_color("red")
print(f"    {first_animal.color}")
print(f"    {second_animal.color}")