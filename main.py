from abc import ABC, abstractmethod

class Creature(ABC):

  weight = 0 # у каждого существа есть вес
  hunger = 'голоден(на)' # допустим каждое существо изначально голодное, их можно покормить методом feed()
  vaccine = 'не привит(а)' # существа рождаются непривитыми, им можно делать прививки методом vaccinate()

  def __init__(self, name, gender, weight):
    self.name = name
    self.gender = gender
    self.weight = weight

  def say_hi(self):
    print(f'{self.name} говорит "{self.talk()}"')

  def feed(self):
    self.hunger = 'сыт(а)'
    print(f'{self.name} накормлен(а)!')

  def vaccinate(self):
    self.vaccine = 'привит(а)'
    print(self.name, 'теперь привит(а)! Существенно снижена вероятность заболеть')

  @abstractmethod
  def gather(self):
    '''
    этот метод будет реализован у классов дающих ОДИНАКОВЫЕ продукты
    (например для всех птиц как класса он будет реализован, а для животных он всё ещё будет абстрактным,
    так как некоторые животные дают молоко, а некоторые шерсть)
    '''
    pass

  @abstractmethod
  def goods(self):
    pass

  def __gt__(self, other): # метод для сравнения создания с другим созданием
    return self.weight > other.weight

  def __add__(self, other): # метод для сложения созданий по их весу
    return self.weight + other.weight


class Bird(Creature):

  def talk(self):
    pass

  def gather(self): #
    self.eggs = 0

  def goods(self):
    return self.eggs

class Animal(Creature):

  def talk(self): # метод "Подай голос"
    pass

  def goods(self): # метод отображает сколько продукта напопило животное
    pass

  def gather(self): # метод сбора накопленных продуктов
    pass


class Goose(Bird):
  eggs = 5
  def talk(self):
    return 'Ga-ga-ga!'


class Duck(Bird):
  eggs = 10
  def talk(self):
    return 'Quack-quack!'


class Chicken(Bird):
  eggs = 15
  def talk(self):
    return 'Co-co-co!'


class Sheep(Animal):
  wool = 20

  def talk(self):
    return 'Beeee!'

  def goods(self):
    return self.wool

  def gather(self):
    self.wool = 0


class Goat(Animal):
  milk = 5

  def talk(self):
    return 'Meeeeeh!'

  def gather(self):
    self.milk = 0

  def goods(self):
    return self.milk

class Cow(Animal):
  milk = 10
  def talk(self):
    return 'Moooo!'

  def gather(self):
    self.milk = 0

  def goods(self):
    return self.milk

cow1 = Cow('Манька', 'female', 300)
goat1 = Goat('Рога', 'male', 89)
goat2 = Goat('Копыта', 'male', 92)
sheep1 = Sheep('Барашек', 'male', 118)
sheep2 = Sheep('Кудрявый', 'male', 109)
chicken1 = Chicken('Ко-Ко', 'female', 3)
chicken2 = Chicken('Кукареку', 'male', 4)
duck1 = Duck('Кряква', 'female', 3)
goose1 = Goose('Серый', 'male', 5)
goose2 = Goose('Белый', 'male', 5)

creatures_list = [cow1, goat1, goat2, sheep1, sheep2, chicken1, chicken2, duck1, goose1, goose2]

def main():

  while True:
    user_input = input('Что мне сделать, дядюшка Джо? ')
    if user_input == 'hi':
      hi(class_instances)
    elif user_input == 'is hungry':
      check_hunger(class_instances)
    elif user_input == 'feed':
      dinner(class_instances)
    elif user_input == 'gather':
      gather(class_instances)
    elif user_input == 'check goods':
      goods(class_instances)
    elif user_input == 'stats':
      stats(creatures_list)
    elif user_input == 'check vaccine':
      check_vaccination(class_instances)
    elif user_input == 'vaccinate':
      vaccination(class_instances)
    elif user_input == 'bye':
      print('Спасибо за помощь! Увидимся следующим летом!')
      break

def stats(creatures_list):
  print(f'Самое тяжелое из них - {max(creatures_list).name}, {max(creatures_list).weight} кг')
  total_weight = []
  for creature in creatures_list:
    total_weight.append(creature.weight)
  print(f'Общий вес всех животных - {sum(total_weight)}')


def hi(creatures=creatures_list):

  for creature in creatures:
    creature.say_hi()
  print('А я им в ответ: "Привет зверушки!"')

def check_hunger(creatures=creatures_list):
  for creature in creatures:
    print(f'{creature.name} - {creature.hunger}')

def dinner(creatures=creatures_list):
  for creature in creatures:
    creature.feed()

def gather(creatures=creatures_list):
  for creature in creatures:
    creature.gather()

def goods(creatures=creatures_list):
  for creature in creatures:
    creature.goods()

def vaccination(creatures=creatures_list):
  for creature in creatures:
    creature.vaccinate()

def check_vaccination(creatures=creatures_list):
  for creature in creatures:
    print(f'{creature.name} - {creature.vaccine}')

    def filtered_creature_list(target_class):
      class_instances = []
      for creature in creatures_list:
        if isinstance(creature, target_class) == True:
          class_instances.append(creature)
          print('Работаем с:', *map(lambda x: x.name, class_instances), sep=', ')
          return class_instances

def filter_creatures_list():
  print('Для начала выберем класс, c которым хотим взаимодействовать.\nВарианты: млекопитающие, птицы, утки, гуси, '
        'куры, коровы, овцы, козы.\nДля взаимодействия со всеми сразу напишите "все" или нажмите ENTER')
  user_input = input('--> ')

  while True:
    if user_input == 'млекопитающие':
      target_class = Animal
      break
    elif user_input == 'птицы':
      target_class = Bird
      break
    elif user_input == 'коровы':
      target_class = Cow
      break
    elif user_input == 'козы':
      target_class = Goat
      break
    elif user_input == 'овцы':
      target_class = Sheep
      break
    elif user_input == 'гуси':
      target_class = Goose
      break
    elif user_input == 'утки':
      target_class = Duck
      break
    elif user_input == 'курицы':
      target_class = Chicken
      break
    elif user_input == 'все':
      target_class = Creature
      break
    else:
      target_class = Creature
      break
  return target_class

def class_list(creatures_list, target_class):

  class_instances = []
  for creature in creatures_list:
    if isinstance(creature, target_class) == True:
      class_instances.append(creature)
  print(*map(lambda x: x.name, class_instances))
  return class_instances


target_class = filter_creatures_list()

class_instances = class_list(creatures_list, target_class)

main()

# filter(lambda x, y: isinstance(x, y),