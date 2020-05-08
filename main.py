"""
Concentration, aka Match Match, card game.
John Berliner, DEV / Lab
All rights reserved.
Feel free to reproduce if credit is given.
5/8/2020 
"""

import tkinter as tk
from card import Card
from random import shuffle
from time import sleep

def reset(btn):
  btn.configure(image=card_back)
  btn.image = card_back

def clear(btn):
  btn.configure(image=blank)
  btn.image = blank
  btn.configure(borderwidth='0')
  btn["state"] = "disabled"

def game_over():
  if deck.count('') >= 52:
    return True
  return False

def reveal(num):
  global first_card, turns
  if num == first_card:
    status.configure(text="You can't match a card against itself!")
    return False
  card_img = tk.PhotoImage(file=deck[num].get_file())
  button_clicked = deck_buttons[num]
  button_clicked.configure(image=card_img)
  button_clicked.image = card_img
  if first_card == '':
    first_card = num
  else:
    turns += 1
    turns_indicator.configure(text="Turns: " + str(turns))
    this_card_val = deck[num].get_val()
    first_val = deck[first_card].get_val()
    if this_card_val == first_val:
      status.configure(text="Match found!")
      deck[num] = deck[first_card] = ''
      root.update()
      sleep(DELAY)
      clear(button_clicked)
      clear(deck_buttons[first_card])
    else:
      status.configure(text="No match. Try again.")
      root.update()
      sleep(DELAY)
      reset(button_clicked)
      reset(deck_buttons[first_card])
    first_card = ''
  if game_over():
    status.configure(text="Good job! You did it!")

CARDS = ('2','3','4','5','6','7','8','9','10','jack','queen','king','ace')
SUITS = ('hearts','diamonds','clubs','spades')
COLOR="coral"
DELAY = 3
deck = []  # global state = bad, I know
deck_buttons = []
first_card = ''
turns = 0

for card in CARDS:
  for suit in SUITS:
    deck.append(Card(card,suit))
shuffle(deck)

root = tk.Tk()
root.geometry("690x440")
root.configure(bg=COLOR)
root.rowconfigure(0, pad=10)
root.rowconfigure(1, pad=5)
root.rowconfigure(2, pad=5)
root.rowconfigure(3, pad=5)
root.rowconfigure(4, pad=5)
root.rowconfigure(5, pad=5)
card_back = tk.PhotoImage(file="cards/card_back.png")
blank = tk.PhotoImage(file="cards/blank.png")

# set up playing area
banner = tk.Label(text="Concentration (Match Match)", font=("Arial",24), bg=COLOR)
banner.grid(row=0, columnspan=13)

for y in range(1,5):
  for x in range(13):
    i = (y-1)*13 + x
    btn = tk.Button(image=card_back, highlightthickness='0', bg=COLOR, command=lambda i=i: reveal(i))
    btn.image = card_back
    deck_buttons.append(btn)
    btn.grid(row=y,column=x)

turns_indicator = tk.Label(text="Turns: 0", font=("Arial",16), bg=COLOR)
turns_indicator.grid(row=5, columnspan=2)

status = tk.Label(text="Click any card to start", font=("Arial",16), bg=COLOR)
status.grid(row=5, columnspan=13)

root.mainloop()