class Circle:
    def pattern(self):
        
        circle=[(13,2),(15,2),(17,3),(18,4),(19,6),(19,7),(18,9),(17,10),(15,11),
                (13,11),(11,10),(10,9),(9,7),(9,6),(10,4),(11,3)]

        for i in range(20):
            for j in range(15):
                if (i,j) in circle:
                    print('*',end='')
                else:
                    print('  ',end='')
            print()
            
class Ellipse:
    def pattern(self):
        
        circle=[(13,2),(15,2),(17,3),(18,4),(19,6),(19,7),(18,9),(17,10),(15,11),
                (13,11),(11,10),(10,9),(9,7),(9,6),(10,4),(11,3)]

        for i in range(20):
            for j in range(15):
                if (i,j) in circle:
                    print('*',end='')
                else:
                    print(' ',end='')
            print()

class Triangle:
    def pattern(self):
            
        for i in range(10):
            print((10-i)*' '+i*' *')
        print()

class RightTriangle:
    def pattern(self):
            
        for i in range(10):
            print(i*' *')
        print()

class Heart:
    def pattern(self):
        d=[(1,4),(1,5),(1,6),(1,10),(1,11),(1,12),(2,3),(2,7),(2,9),(2,13),(3,3),(3,8),(3,13),(4,4),(4,12),(5,6),(5,10),
           (6,8)]
        for i in range(7):
            for j in range(14):
                if (i,j) in d:
                    print('*',end=' ')
                else:
                    print(' ',end=' ')
            print()
class Scalene:
    def pattern(self):
        for i in range(10):
            print(i*' ',i*'*')
        print()
class Square:
    def pattern(self):
        for i in range(10):
            print(10*' *')
        print()
class Rectangle:
    def pattern(self):
        for i in range(10):
            print(20*' *')
        print()
class Rhombus:
    def pattern(self):
        n=5
        for i in range(0,n):
            for j in range(0,n):
                if (i+j==2) or (i-j==2) or (j-i==2) or (i+j==6):
                    print('*',end=' ')
                else:
                    print(' ',end=' ')
            print()
class Parallelogram:
    def pattern(self):
        for i in range(10):
            print((10-i)*' '+20*' *')
        print()
class Trapezium:
    def pattern(self):
        trap=[(1,3),(1,4),(1,5),(1,6),(1,7),(1,8),(1,9),(2,10),(3,11),(3,10),(3,9),(3,8),(3,7),
              (3,6),(3,5),(3,4),(3,3),(3,2),(3,1),(2,2)]
        for i in range(5):
            for j in range(12):
                if (i,j) in trap:
                    print('*',end=' ')
                else:
                    print(' ',end=' ')
            print()

class Hexagon:
    def pattern(self):
        hex=[(1,4),(1,9),(1,5),(1,6),(1,7),(1,8),(2,10),(3,11),(4,10),(5,9),(5,8),(5,7),(5,6),(5,5),(5,4),(4,3),(3,2),(2,3)]
        for i in range(6):
            for j in range(12):
                if (i,j) in hex:
                    print('*',end='')
                else:
                    print(' ',end='')
            print()

class Pentagon:
    def pattern(self):
        pent=[(1,4),(2,6),(3,7),(4,6),(5,5),(5,4),(5,3),(4,2),(3,1),(2,2)]
        for i in range(6):
            for j in range(9):
                if (i,j) in pent:
                    print('*',end=' ')
                else:
                    print(' ',end=' ')
            print()

class Octagon:
    def pattern(self):
        oct=[(1,4),(1,5),(1,6),(2,7),(3,8),(4,8),(5,8),(6,7),(7,6),(7,5),(7,4),(6,3),(5,2),(4,2),(3,2),(2,3)]
        for i in range(10):
            for j in range(10):
                if (i,j) in oct:
                    print('*',end=' ')
                else:
                    print(' ',end=' ')
            print()

class Star:
    def pattern(self):
        star=[(1,6),(2,5),(2,6),(2,7),(3,1),(3,2),(3,3),(3,4),(3,5),(3,6),(3,7),(3,8),(3,9),(3,10),(3,11),(4,2),(4,3),
              (4,4),(4,5),(4,6),(4,7),(4,8),(4,9),(4,10),(5,3),(5,4),(5,5),(5,6),(5,7),(5,8),(5,9),(6,2),(6,3),(6,9),(6,10),
              (7,1),(7,11)]
        
        for i in range(10):
            for j in range(15):
                if (i,j) in star:
                    print('*',end=' ')
                else:
                    print(' ',end=' ')
            print()

class Fourstar:
    def pattern(self):
        star=[(1,6),(2,5),(2,7),(3,4),(3,8),(4,2),(4,10),(5,1),(5,11),(6,2),(6,10),(7,4),(7,8),(8,5),(8,7),(9,6)]
        for i in range(10):
            for j in range(15):
                if (i,j) in star:
                    print('*',end=' ')
                else:
                    print(' ',end=' ')
            print()
class Sixstar:
    def pattern(self):
        star=[(1,7),(2,6),(2,7),(2,8),(3,3),(3,4),(3,5),(3,6),(3,7),(3,8),(3,9),(3,10),(3,11),(4,4),(4,5),(4,6),(4,7),(4,8),
              (4,9),(4,10),(5,3),(5,4),(5,5),(5,6),(5,7),(5,8),(5,9),(5,10),(5,11),(6,6),(6,7),(6,8),(7,7)]
        for i in range(10):
            for j in range(15):
                if (i,j) in star:
                    print('*',end=' ')
                else:
                    print(' ',end=' ')
            print()
class Decagon:
    def pattern(self):
        d=[(1,13),(1,15),(1,17),(2,19),(3,21),(5,22),(7,23),(9,22),(11,21),(12,19),(13,17),(13,15),(13,13),(12,11),(11,9),
           (9,8),(7,7),(5,8),(3,9),(2,11)]
        for i in range(14):
            for j in range(25):
                if (i,j) in d:
                    print('*',end=' ')
                else:
                    print(' ',end=' ')
            print()
class Heptagon:
    def pattern(self):
        d=[(3,13),(4,11),(4,15),(5,9),(5,17),(7,8),(7,18),(9,7),(9,19),(11,8),(11,18),(13,10),(13,12),(13,14),(13,16)]
        for i in range(14):
            for j in range(20):
                if (i,j) in d:
                    print('*',end=' ')
                else:
                    print(' ',end=' ')
            print()
class Nonagon:
    def pattern(self):
        d=[(1,13),(2,11),(2,15),(3,8),(3,18),(5,7),(5,19),(7,6),(7,20),(9,6),(9,20),(11,6),(11,20),(12,8),
           (12,18),(13,10),(13,12),(13,14),(13,16)]
        for i in range(14):
            for j in range(21):
                if (i,j) in d:
                    print('*',end=' ')
                else:
                    print(' ',end=' ')
            print()
n=1
while n!=0:
    
    print('Please find the options for patterns below: ')
    print('1.Circle 2.Ellipse 3.Triangle 4.Heart 5.Pentagon 6.Hexagon 7.Heptagon 8.Octagon 9.Nonagon 10.Decagon')
    print('11.Right triangle 12.Scalene triangle 13.Square 14.Rectangle 15.Parallelogram 16.Trapezium 17.Rhombus')
    print('18. Four pointed star 19.Five pointed star 20.Six pointed star, Press 0 to exit')
    n=int(input('Enter your option: '))
    if n==1:c=Circle()
    if n==2:c=Ellipse()
    if n==3:c=Triangle()
    if n==4:c=Heart()
    if n==5:c=Pentagon()
    if n==6:c=Hexagon()
    if n==7:c=Heptagon()
    if n==8:c=Octagon()
    if n==9:c=Nonagon()
    if n==10:c=Decagon()
    if n==11:c=RightTriangle()
    if n==12:c=Scalene()
    if n==13:c=Square()
    if n==14:c=Rectangle()
    if n==15:c=Parallelogram()
    if n==16:c=Trapezium()
    if n==17:c=Rhombus()
    if n==18:c=Fourstar()
    if n==19:c=Star()
    if n==20:c=Sixstar()
    if n==0:break

    notn=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    if n not in notn:
        print('Invalid input')
        continue
    c.pattern()
    
