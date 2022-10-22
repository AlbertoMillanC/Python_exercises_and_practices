# "//hacer una lista  random"?
import random

dict = {
  "winter" : 10, 
  "summer" : 30, 
  "spring":  20, 
  "autumn" : 15
}

values = list(dict.values())

keys = list(dict.keys())

random = random.choice(values)

print(random)

print(keys[values.index(random)])


