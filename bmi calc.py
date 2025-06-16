

def request_height ():
    float(input("Please enter your height in Meters above:"))



def bmi (height,weight):
    return(weight/request_height)^2
from enum import Enum
import math


class Ethnicity(Enum):
  BLACK = 'black'
  CHINESE = "chinese"
  WHITE = 'white'


ethnicity_list = [eth.value for eth in Ethnicity]


# so that we can use it multiple times
def request_ethnicity():
  ethnicity_str = input('Please enter your ethnicity: ')
  is_supported_ethnicity = ethnicity_str in ethnicity_list
  # instead of having long if statement add them to an array and check if they are all true or false
  conditions = [
      ethnicity_str is not None,
      len(ethnicity_str) > 0, is_supported_ethnicity
  ]
  # will return true if all are true
  is_ethnicity_valid = all(conditions)

  if is_ethnicity_valid is False:
    print(f"{ethnicity_str} is not supported.")
    return request_ethnicity()
  return ethnicity_str


def request_bimometric(message: str):
  # The errors that you see in your console when something goes wrong is an exception
  # try and except is a way to handle errors
  try:
    input_val = input(message)
    return float(input_val)
  except ValueError:
    print("Please enter a valid number")
    return request_bimometric(message)


def calc_bmi(w: float, h: float, ethnicity: str):
  # if height or width or not floats throw an error
  if any(isinstance(dim, float) for dim in [w, h]) is False:
    raise ValueError('Height or width or not numbers')
  # rounds it down/up
  return math.ceil(w / (h * h))


height = request_bimometric("Please enter your height in CM: ")
weight = request_bimometric("Please enter your weight in KG: ")
ethnicity = request_ethnicity()

#if ethnicity is None or len(ethnicity) == 0 or ethinicty is not a member of Ethnicity:

person_bmi = calc_bmi(height, weight, ethnicity)
print(f"Your approx BMI is {person_bmi}")
