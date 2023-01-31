import random


class Person:
    def __init__(self,firstname,lastname,health,status):
        " initialize attributes to be used in/available for all \
           class methods in this class, and for class Objects created \
           by this class."
        self.firstname=firstname
        self.lastname=lastname
        self.health=health
        self.status=status
    def introduce(self):
        "All people intorduce themselves"
        print("Hi, I', {} {}".format(self.firstname,self.lastname))
    def emote(self):
        emotion=random.randrange(1,3)
        if emotion==1:
            print("{} is happy ".format(self.firstname))
        elif emotion==2:
            print("{} is sad right now".format(self.firstname))
        else:
            print("{} is neutral".format(self.firstname))
    def status_change(self):
        if self.health==100:
            print("{} is totally healthy".format(self.firstname))
        elif self.health>=76:
            print("{} is tired ".format(self.firstname))
        elif self.health>=50:
            print("{} should take a day off".format(self.firstname))
        elif self.health >= 40:
            print("{} goes to the doctor".format(self.firstname))

        else:
            print("{} is unconscious.".format(self.firstname))


Maria = Person("Maria", "Gutierrez", 95, status=True)
Rey = Person("Rey", "Jones", 88, status=False)
Lee = Person("Lee", "Williams", 72, status=True)

print("{} is my friend {}".format(Maria.firstname,Maria.status))
Maria.introduce()
Maria.emote()

Maria.status_change()
Rey.status_change()
Lee.status_change()


class Enemy(Person):
    def __init__(self, weapon, firstname, lastname, health, status):
        super().__init__(firstname, lastname, health, status)
        self.weapon = weapon

    def introduce(self):
        print("You are my mortal enemy!!!")

    def hurt(self, other):
        if self.weapon == 'rock':
            other.health -= 10

        elif self.weapon == 'stick':
            other.health -= 5

        print(other.health)
    def insult(self, other):
        if other.health <= 80:
            print("{}, you are tired and weak".format(other.firstname))

    def steal(self, other):
        print("ha ha ha, {}, I have your stuff!".format(other.firstname))

        if other.status == True:
            other.status = False


Alex = Enemy('rock', 'Alex', 'Wayne', 75, status = False)
Maria.introduce()
Rey.introduce()
Alex.introduce()
