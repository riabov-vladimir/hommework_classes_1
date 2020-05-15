class Creature:
  age = 0 # новорождённое существо
  weight = 0 # у каждого существа есть вес
  hunger = 'hungry' # допустим каждое существо изначально голодное,
  # его можно покормить методом feed() и тогда оно станет сытым ('fed')
  vaccine = 'not vaccinated' # существа рождаются непривитыми, им можно делать прививки методом vaccinate()

  def __init__(self, name, gender):
    self.name = name
    self.gender = gender
    self.weight = weight

  def say_hi(self):
    print(f'{self.name} says "{self.talk}"')

  def feed(self):
    self.hunger = 'fed'
    print('Creature is fed!')

  def wash(self):
    self.clean_state = 'clean'
    print(self, 'is clean now!')

  def vaccinate(self):
    self.vaccine = 'vaccinated'
    print(self, 'is vaccinated now! More unlikely to get sick')


class Bird(Creature):
  eggs = None

  def nest(self):
    self.eggs += 1

  def gather_eggs(self):
    self.eggs = 0


class Animal(Creature):
  def get_milk(self):
    self.milk = 0

class Goose(Bird):
  name = None
  weight = 4
  eggs = 5
  talk = 'Ga-ga-ga!'

class Duck(Bird):
  weight = 3
  eggs = 10
  talk = 'Quack-quack!'

class Chicken(Bird):
  weight = 4
  eggs = 15
  talk = 'Co-co-co!'

class Sheep(Animal):
  weight = 120
  milk = 3
  talk = 'Beeee!'

class Goat(Animal):
  weight = 100
  milk = 5
  talk = 'Meeeeeh!'

class Cow(Animal):
  weight = 300
  milk = 10
  talk = 'Moooo!'



cow1 = Cow('Манька', 'female')
goat1 = Goat('Рога', 'male')
goat2 = Goat('Копыта', 'male')
sheep1 = Sheep('Барашек', 'male')
sheep2 = Sheep('Кудрявый', 'male')
chicken1 = Chicken('Ко-Ко', 'female')
chicken2 = Chicken('Кукареку', 'male')
duck1 = Duck('Кряква', 'female')
goose1 = Goose('Серый', 'male')
goose2 = Goose('Белый', 'male')


goose2.say_hi()

# creatures_list = [cow1, goat1, goat2, sheep1, sheep2, chicken1, chicken2, duck1, goose1, goose2]
#
# for creature in creatures_list:
#   print(creature.weight)