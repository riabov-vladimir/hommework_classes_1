# коз 2 "Рога" и "Копыта"
# корову "Маньку"
# овец 2 "Барашек" и "Кудрявый"
# кур 2 "Ко-Ко" и "Кукареку"
# утку "Кряква"
# гусей 2 "Серый" и "Белый"

class Creature:

  age = 0 # новорождённое существо
  weight = 0 # у каждого существа есть вес
  hunger = 'hungry' # допустим каждое существо изначально голодное,
  # его можно покормить методом feed() и тогда оно станет сытым ('fed')
  says = None # какие звуки издаёт существо
  location = None
  vaccine = 'not vaccinated' # существа рождаются непривитыми, им можно делать прививки методом vaccinate()
  clean_state = 'dirty' # ну существо допустим изначально у нас грязненькое такое


  def feed(self):
    self.hunger = 'fed'
    print('Creature is fed!')
  pass

  def wash(self):
    self.clean_state = 'clean'
    print(self, 'is clean now!')

  def vaccinate(self):
    self.vaccine = 'vaccinated'
    print(self, 'is vaccinated now! More unlikely to get sick')

class Bird(Creature):
  # крылья
  # несёт яйца
  # можно собрать яйца
  pass

class Animal(Creature):
  # даёт молоко
  # можно доить

  pass

class Goose(Bird):
  pass

class Duck(Bird):
  pass

class Chicken(Bird):
  pass

class Sheep(Animal):
  pass

class Goat(Animal):
  pass

class Cow(Animal):
  pass

print('moo')

creature1 = Creature()
creature2 = Creature()

print(creature1.vaccine)
print(creature2.vaccine)

creature2.vaccinate()

print(creature1.vaccine)
print(creature2.vaccine)