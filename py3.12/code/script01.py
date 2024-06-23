import math
def calc_area(n):
    return math.pi * n**2

if __name__ == '__main__':
    n = 10
    area = calc_area(n)
    print(f"the area of {n} is {area}")
