import math
import mysql.connector
from mysql.connector import Error
train_mass = 22680
train_acceleration = 10
train_distance = 100
c = 3*10**8

bomb_mass = 1
def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9
  return c_temp

def c_to_f(c_temp):
  f_temp = (c_temp * (9/5)) + 32
  return f_temp

def get_force(mass,acceleration):
  return mass*acceleration

def get_energy(mass):
    return mass*math.sqrt(c)

def get_work(mass,acacceleration,distance):
    force = get_force(mass,acacceleration)
    result = force*distance
    return result

train_work = get_work(mass=train_mass,distance=train_distance,acacceleration=train_acceleration)
train_force =  get_force(train_mass,train_acceleration)
bomb_energy = get_energy(bomb_mass)
print(f"The GE train does {train_work} Joules of work over {train_distance} meters.")
print(f"A 1kg bomb supplies {bomb_energy} Joules.")
print(f"the GE train supplies {train_force} Newtons of force.")
f100_in_celsius = f_to_c(100)
c0_in_fahrenheit = c_to_f(0)
print(2**10)


