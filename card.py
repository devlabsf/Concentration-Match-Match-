class Card:
  
  def __init__(self, value, suit):
    self.value = value
    self.suit = suit

    if self.suit in ('hearts','diamonds'):
      self.color = "red"
    else:
      self.color = "black"

  def get_val(self):
    return self.color + self.value

  def get_file(self):
    return 'cards/' + self.value + '_' + self.suit + '.png'


