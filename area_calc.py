# area_calc.py
from area.rectangle import Rect
from area.square import Square

if __name__ == '__main__':
    sq1 = Square(5)
    print(sq1)
    print(sq1.area())

    rect1 = Rect(5, 10)
    rect2 = Rect(7, 9)
    print(rect1)
    print(rect2)
