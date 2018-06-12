lottery_player_dict = {
  'name': 'Chris',
  'numbers': (5, 9, 12, 3, 1, 21)
}

class LotteryPlayer:
  def __init__(self, name):
    self.name = name
    self.numbers = (5, 9, 12, 3, 1, 21)

player_one = LotteryPlayer('Chris')
player_two = LotteryPlayer('Katelyn')

print(player_one.name == player_two.name)