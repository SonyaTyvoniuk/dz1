def calculate_fuel(distance):
 fuel= distance * 10
   if fuel<100:
     fuel = 100
  return fuel
print(calculate_fuel(20))
print(calculate_fuel(35))
print(calculate_fuel(645))