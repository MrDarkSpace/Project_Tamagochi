import sys
import time


class Tamagochi:     #Основной класс, от которо потом будем наследоваться
  face = ''
  state = 'OK'
  toi_number = 0
  all_time = 0
  part_food = 0
  part_cln = 0
  part_hea = 0
  feed_num = {'1': 5, '2': 10, '3': 20}


  def __init__(self, food=50, cleanness=50, health=100, age=0):
                                      #Задаем начальные значения характеристик
    self.Food = food  # Еда
    self.Cleanness = cleanness  # Чистота
    self.Health = health  # Здоровье
    self.Age = age  # Возраст
    print("You've sheltered your pet, congratulations!")

  def food_drop(self, st):  #Падение со временем Еды
    loss = ((time.time() - st + self.part_food)//1)//3
    if (loss != 0):
      self.Food = self.Food - int(loss)
      self.part_food = time.time() - st + self.part_food - loss*3
    else:
      self.part_food += (time.time() - st)

  def clnns_drop(self, st):   #Падение со временем Чистоты
    loss = ((time.time() - st + self.part_cln) // 1) // 3
    if (loss != 0):
      self.Cleanness = self.Cleanness - int(loss)*(1+self.toi_number)
      self.part_cln = time.time() - st + self.part_cln - loss * 3
    else:
      self.part_cln += (time.time() - st)

  def plus_age(self, st): #Рост Возраста
    self.all_time += time.time()-st
    self.Age = int(self.all_time//30)

  def health_drop(self, st): #Падение со временем Здоровья
    loss = (time.time() - st + self.part_hea) // 1
    loss1 = loss // 3
    loss2 = loss // 9
    if (loss1 != 0):
      if (self.Food <= 30) or (self.Cleanness <= 30):
        final_loss = loss1
        final_add = 3
      else:
        final_loss = loss2
        final_add = 9
      self.Health = self.Health - int(final_loss)
      self.part_hea = time.time() - st + self.part_hea - final_loss * final_add
    else:
      self.part_hea += (time.time() - st)


  def feed(self):    #Процесс Кормления
    feedtype = str(input('Choose serving size: \'1\' '
                         '(+5 Food), \'2\' (+10 Food) or \'3\' (+20 Food).\n'))
    while True:
      if feedtype in ('1', '2', '3'):
        self.Food += self.feed_num[feedtype]
        break
      else:
        feedtype = input('Sorry, but I don\'t '
                         'understand you :( Can you type one more time?\n')

  def wash(self):     #Процесс помывки
    self.Cleanness += 50
    if (self.Cleanness >= 100):
      self.Cleanness = 100

  def cure(self):     #Процесс Лечения
    self.Health += 30
    if (self.Health >= 100):
      self.Health = 100

  def toilet(self):   #Автопроцесс хождения в туалет
    self.toi_number += 1

  def clean_toilet(self):  #Процесс Очистки Туалета
    self.toi_number -= 1
    if self.toi_number < 0:
      self.toi_number = 0


class Cat(Tamagochi):
  face = '         ／＞　 フ \n　　　　　| 　_　 _| \n' \
         '　 　　　／`ミ _x 彡 \n　　 　 /　　　 　 | \n　　　 /　 ヽ　　 ﾉ \n' + \
         '　／￣|　　 |　|　| \n　| (￣ヽ＿_ヽ_)_) \n　＼二つ          '
  def __init__(self):
    super().__init__()
    print("Your tamagochi is a cute kitten!")


class Dog(Tamagochi):
  face = '  ╱▔▔▔▔▔╲  \n╭┫╭━╮┈╭━╮┣╮\n┃┃┃▇┃┈┃▇┃┃┃\n' \
         '┃┃╰╱▔▇▔╲╯┃┃\n┃┃▕╰┳┻┳╯▏┃┃\n╰╯╲╲╰━╯╱╱╰╯\n   ' \
         '┃▔▔▔ ╲  ╮\n   ┃    ╲ ┃\n' +\
         '   ┃┏┓┃ ╭ ╲╯\n   ┃┃┃┃╭┛  ┃\n   ┗┛┗┛┗━━━╯'
  def __init__(self):
    super().__init__()
    print("Your tamagochi is a beautiful puppy!")


class Goat(Tamagochi):
  face = '  ╱▔▔▔▔▔▔╲╲     \n ╱╳╱▔▔▔▔╲╳╲╲    \n╱╳╱     ▏╋▏▏   \n' \
         '▏╋▏  ▕▔╲▂▏╋▏▏   \n▏╋▏   ╲▂ ╭▅╮╲▂▂ \n╲╳╲▂╱▏ ╱▏     ▅▏\n' \
         + ' ╲╳╋╱ ╱ ╲   ╰━━▏\n  ▔▔ ╱   ╱▔╲╲▕▔ '
  def __init__(self):
    super().__init__()
    print("Your tamagochi is a funny goatling!")


def play():

  animaltype = input('Hello! I\'m very happy that '
                     'you\'re playing my game!\n' +
                 'You can choose your pet. '
                 'In our shelter there are cats, dogs '
                 'and goats. ' +
                 'Who would you like to shelter? '
                 '(print \'c\', \'d\' or \'g\')\n')

  an_create = {'c': Cat, 'd': Dog, 'g': Goat}
  while True:
    if animaltype in an_create:
      animal = an_create[animaltype]()
      break
    else:
      animaltype = input('Sorry, but I don\'t understand you :( '
                         'Can you type one more time?\n')



  animal.name = input('Now you should name your pet. Choose wisely.\n')
  print('Wow! Great name: ' + animal.name + '.\nSo, now we are starting '
                                            'our game! Be very attentive to '
                                            'your ' + animal.name + '!')

  start_time = time.time()
  feedback = ""

  while True:
    animal.plus_age(start_time)
    animal.food_drop(start_time)
    animal.clnns_drop(start_time)
    animal.health_drop(start_time)


    start_time = time.time()

    if all([animal.Food > 80, animal.Cleanness > 80,\
            animal.Health > 80]):
      animal.state = 'Delighted'
    elif all([animal.Food > 50, animal.Cleanness > 50, \
            animal.Health > 50]):
      animal.state = 'Happy'
    elif all([animal.Food > 30, animal.Cleanness > 30, \
            animal.Health > 30]):
      animal.state = 'OK'
    elif all([animal.Food > 0, animal.Cleanness > 0, \
            animal.Health > 0]):
      animal.state = 'Sad'
    else:
      print ("That\'s very awful! Your " + animal.name + ' Died!\nGame over!')
      break

    if (animal.Food > 95):
      animal.toilet()
      animal.Food = 95

    feedback = animal.face + animal.name + ' is ' + animal.state + \
               (" " + chr(128169))*animal.toi_number + "\n" +\
               str(animal.Food) + " Food  " + \
               str(animal.Cleanness) + " Cleanness  " + \
               str(animal.Health) + " Health  " + \
               str(animal.Age) + " years  "
    action = input(feedback + "\n")
    words = action.split()

    if len(words) > 0:
        command = words[0]
    else:
        command = ''

    if (command.upper() == 'FEED'):
      animal.feed()
    elif (command.upper() == 'WASH'):
      animal.wash()
    elif (command.upper() == 'CURE'):
      animal.cure()
    elif (command.upper() == 'CLEAN'):
      animal.clean_toilet()
    else:
      print('Strange command :( So, I\'ll just show you stats :)')


play()
