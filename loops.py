import time


def sixty_second_count():
  x = 60
  while True:
    if x <= 0:
      print("Time's up.")
      break
    if x > 0:
      x -= 1
      print(x)
    time.sleep(1)

def all_even():
  x = 0
  while True:
    x += 2
    print(x)

def all_odd():
  x = 1
  print(x)
  while True:
    x += 2
    print(x)