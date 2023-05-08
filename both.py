def both(number1, number2):
     return   (number1<= 0 and number2<= 0) or (number1>= 0 and number2>= 0)
print(both(6,2))
print(both(-1,2))
print(both(3,-12))