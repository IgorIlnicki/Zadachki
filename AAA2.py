class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight

class Cat(Animal):
    def __init__(self, voice, nickname, weight):
        super().__init__(nickname, weight)
        self.voice = voice
        # voice = "Meom"
        f"Cat Name: {self.nickname}, weight: {self.weight}"
        def say(self):
            voice = "Meow"
            return voice

# cat0 = Animal("Simon", 10)
cat = Cat(voice=Cat.say, nickname="Simon", weight=10)

print(f"   cat = {cat.nickname} {cat.weight} ")


