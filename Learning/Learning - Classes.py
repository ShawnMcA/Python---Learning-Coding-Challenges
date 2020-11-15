class Animal:
  def __init__(self, name, species, color):
    self.name = name
    self.species = species
    self.color = color

  def speak(self):
    print(f'{self.name} the {self.color} {self.species} makes a weird noise?')

class Dog(Animal):
  def __init__(self, name, color):
    Animal.__init__(self, name, 'dog', color)
    self.sound = 'bark bark!'
  
  def speak(self):
    print(f'Bark bark!!')


Unicorn = Animal('James', 'unicorn', 'white')

Unicorn.speak()

Kelly = Dog('Kelly', 'brown')

Kelly.speak()