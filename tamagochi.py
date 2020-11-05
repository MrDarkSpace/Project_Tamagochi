import sys
import time


class Tamagochi:
  face = ''
  state = 'OK'
  toi_number = 0
  def __new__(cls, food=50, cleanness=50, health=100, age=0):
    cls.Food = food
    cls.Cleanness = cleanness
    cls.Health = health
    cls.Age = age
    return super().__new__(cls)

  def __init__(self):
    print("You've sheltered your pet, congratulations!")

  def food_drop(self, st):
    self.Food = self.Food - int((time.time()-st)//3)

  def clnns_drop(self, st):
    self.Cleanness = self.Cleanness - int((time.time()-st)//3)*(1+self.toi_number)

  def plus_age(self, st):
    self.Age = self.Age + int((time.time()-st)//30)

  def health_drop(self, st):
    if (self.Food <= 30) or (self.Cleanness <= 30):
      self.Health = self.Health - int((time.time()-st)//3)
    else:
      self.Health = self.Health - int((time.time() - st) // 10)

  def feed(self):
    feedtype = str(input('Choose serving size: \'1\' (+5 Food), \'2\' (+10 Food) or \'3\' (+20 Food).\n'))
    while True:
      if (feedtype == '1') or (feedtype == '2') or (feedtype == '3'):
        self.Food += 5*int(feedtype) + (int(feedtype)//3)*5
        if (self.Food >= 100):
          self.Food = 100
        break
      else:
        feedtype = input('Sorry, but I don\'t understand you :( Can you type one more time?\n')

  def wash(self):
    self.Cleanness += 50
    if (self.Cleanness >= 100):
      self.Cleanness = 100

  def cure(self):
    self.Health += 30
    if (self.Health >= 100):
      self.Health = 100

  def toilet(self):
    self.toi_number += 1

  def clean_toilet(self):
    self.toi_number -= 1
    if self.toi_number < 0:
      self.toi_number = 0


class Cat(Tamagochi):
  face = '         ／＞　 フ \n　　　　　| 　_　 _| \n　 　　　／`ミ _x 彡 \n　　 　 /　　　 　 | \n　　　 /　 ヽ　　 ﾉ \n' + \
         '　／￣|　　 |　|　| \n　| (￣ヽ＿_ヽ_)_) \n　＼二つ          '
  def __init__(self):
    super().__init__()
    print("Your tamagochi is a cute kitten!")


class Dog(Tamagochi):
  face = '  ╱▔▔▔▔▔╲  \n╭┫╭━╮┈╭━╮┣╮\n┃┃┃▇┃┈┃▇┃┃┃\n┃┃╰╱▔▇▔╲╯┃┃\n┃┃▕╰┳┻┳╯▏┃┃\n╰╯╲╲╰━╯╱╱╰╯\n   ┃▔▔▔ ╲  ╮\n   ┃    ╲ ┃\n' +\
         '   ┃┏┓┃ ╭ ╲╯\n   ┃┃┃┃╭┛  ┃\n   ┗┛┗┛┗━━━╯'
  def __init__(self):
    super().__init__()
    print("Your tamagochi is a beautiful puppy!")


class Goat(Tamagochi):
  face = '  ╱▔▔▔▔▔▔╲╲     \n ╱╳╱▔▔▔▔╲╳╲╲    \n╱╳╱     ▏╋▏▏   \n▏╋▏  ▕▔╲▂▏╋▏▏   \n▏╋▏   ╲▂ ╭▅╮╲▂▂ \n╲╳╲▂╱▏ ╱▏     ▅▏\n' \
         + ' ╲╳╋╱ ╱ ╲   ╰━━▏\n  ▔▔ ╱   ╱▔╲╲▕▔ '
  def __init__(self):
    super().__init__()
    print("Your tamagochi is a funny goatling!")


def play():

  animaltype = input('Hello! I\'m very happy that you\'re playing my game!\n' +
                 'You can choose your pet. In our shelter there are cats, dogs and goats. ' +
                 'Who would you like to shelter? (print \'c\', \'d\' or \'g\')\n')

  while True:
    if (animaltype == 'c'):
      animal = Cat()
      break
    elif (animaltype == 'd'):
      animal = Dog()
      break
    elif (animaltype == 'g'):
      animal = Goat()
      break
    else:
      animaltype = input('Sorry, but I don\'t understand you :( Can you type one more time?\n')



  animal.name = input('Now you should name your pet. Choose wisely.\n')
  print('Wow! Great name: ' + animal.name + '.\nSo, now we are starting our game! Be very attentive to your ' +
        animal.name + '!')

  start_time = time.time()
  feedback = ""

  while True:
    animal.food_drop(start_time)
    animal.clnns_drop(start_time)
    animal.health_drop(start_time)
    animal.plus_age(start_time)

    start_time = time.time()

    if (animal.Food > 80) and (animal.Cleanness > 80) and (animal.Health > 80):
      animal.state = 'Delighted'
    elif (animal.Food > 50) and (animal.Cleanness > 50) and (animal.Health > 50):
      animal.state = 'Happy'
    elif (animal.Food > 30) and (animal.Cleanness > 30) and (animal.Health > 30):
      animal.state = 'OK'
    elif (animal.Food > 0) and (animal.Cleanness > 0) and (animal.Health > 0):
      animal.state = 'Sad'
    else:
      print ("That\'s very awful! Your " + animal.name + ' Died!\nGame over!')
      break

    if (animal.Food > 95):
      animal.toilet()
      animal.Food = 95

    feedback = animal.face + animal.name + ' is ' + animal.state + " 💩"*animal.toi_number + "\n" +\
               str(animal.Food) + " Food  " + \
               str(animal.Cleanness) + " Cleanness  " + str(animal.Health) + " Health  " + str(animal.Age) + " years  "
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
