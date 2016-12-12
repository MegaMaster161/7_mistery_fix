from math import sqrt

#не хватает проверки условия. Дискриминант может быть больше/меньше нуля либо равно нулю

def get_roots(a, b, c):
    discriminant = b ** 2 - 4 * a * c
#    root1 = (-b - sqrt(discriminant)) / (2 * a)
#    root2 = (-b + sqrt(discriminant)) / (2 * a)
    if discriminant < 0:
        return None, None 
#Через elif не получилось, ругалось на NoneType в 3 местах.
    else:
      root1 = (-b - sqrt(discriminant)) / (2 * a)
      root2 = (-b + sqrt(discriminant)) / (2 * a)
    if discriminant == 0:
       return root1, None
    else:
       return root1, root2