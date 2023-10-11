import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **kwargs):
    self.contents = []
    for key, value in kwargs.items():
      for i in range(value):
        self.contents.append(key)

  def draw(self, num_balls):
    if num_balls < len(self.contents):
      selected_balls = []
      
      for n in range(num_balls):
        selected_ball = random.choice(self.contents)
        selected_balls.append(selected_ball)
        self.contents.remove(selected_ball)
        
      return selected_balls
      
    return self.contents

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  m = 0
  
  for n in range(num_experiments):
    all_match = True
    experiment_hat = copy.deepcopy(hat)
    result = experiment_hat.draw(num_balls_drawn)
    
    for key, value in expected_balls.items():
      if result.count(key) < value:
        all_match = False
        
    if all_match == True:
      m += 1
      
  probability = m / num_experiments
  return probability
