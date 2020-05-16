class Creature:
  age = 0 # новорождённое существо
  weight = 0 # у каждого существа есть вес
  hunger = 'hungry' # допустим каждое существо изначально голодное,
  # его можно покормить методом feed() и тогда оно станет сытым ('fed')
  vaccine = 'not vaccinated' # существа рождаются непривитыми, им можно делать прививки методом vaccinate()

  def __init__(self, name, gender):
    self.name = name
    self.gender = gender
    # self.weight = weight

  def say_hi(self):
    print(f'{self.name} says "{self.talk}"')

  def feed(self):
    self.hunger = 'fed'
    print('Creature is fed!')

  def vaccinate(self):
    self.vaccine = 'vaccinated'
    print(self, 'is vaccinated now! More unlikely to get sick')

  def gather(self):
    if isinstance(self, Bird):
      self.eggs = 0
    elif isinstance(self, Cow or Goat):
      self.milk = 0
    elif isinstance(self, Sheep):
      self.wool = 0


class Bird(Creature):

  eggs = None
  class_name = 'Птица'
  def nest(self):
    self.eggs += 1

  def gather_eggs(self):
    self.eggs = 0


class Animal(Creature):
  class_name = 'Млекопитающее' # прикольно было бы срезом менять окончание при выводе
  def get_milk(self):
    self.milk = 0

class Goose(Bird):
  class_name = 'Гусь'
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
  wool = 20
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

creatures_list = [cow1, goat1, goat2, sheep1, sheep2, chicken1, chicken2, duck1, goose1, goose2]
classes_list = [Animal, Bird, Cow, Goat, Sheep, Duck, Chicken, Goose]
def main():
  user_input = input('Что мне сделать, дядюшка Джо?')
  while True:
    if user_input == 'hi':
      hi_everyone(creatures_list)
    elif user_input == 'bye':
      print('Спасибо за помощь! Увидимся следующим летом!')

def hi_everyone(class_list):

  for creature in creatures_list:
    creature.say_hi()

  print('А я им в ответ: "Привет зверушки!"')

def dinner(creatures=creatures_list):
  for creature in creatures:
    creature.feed()
  print('')

def class_list(creatures_list, target_class): # если не сделаю классный инпут, реализую через main()
  # target_class = classes_list[input('Class index: ')]
  class_instances = []
  for creature in creatures_list:
    if isinstance(creature, target_class) == True:
      class_instances.append(creature)

  print(*map(lambda x: x.name, class_instances), sep=', ')

# class_list(creatures_list, Bird) # подсчёт птиц без user_input !WORKS OK!

