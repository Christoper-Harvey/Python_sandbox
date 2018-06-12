lottery_player_dict = {
  'name': 'Chris',
  'numbers': (5, 9, 12, 3, 1, 21)
}

class LotteryPlayer:
  def __init__(self, name):
    self.name = name
    self.numbers = (5, 9, 12, 3, 1, 21)

player_one = LotteryPlayer('Chris')
player_one.numbers = (1, 2, 4, 21, 48, 5)
player_two = LotteryPlayer('Katelyn')

print(player_one.name == player_two.name)

class Student:
  def __init__(self, name, school):
    self.name = name
    self.school = school
    self.marks = []

  def average(self):
    return sum(self.marks) / len(self.marks)

anna = Student('Anna', 'MIT')
anna.marks.append(56)
anna.marks.append(72)
anna.marks.append(98)
print(anna.marks)
print(anna.average())