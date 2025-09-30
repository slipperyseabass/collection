import random as rd
import matplotlib.pyplot as plt
import time as t
a = 0
e = 0
x = []
y = []
corners = []
corners2 = []
corners3 = []
corners4 = 0
zeroes = []
zeroes2 = []
zeroes3 = []
zeroes4 = 0
edges = []
edges2 = []
edges3 = []
edges4 = 0
hundreds = []
hundreds2 = []
hundreds3 = []
hundreds4 = 0
hundcorners = []
hundcorners2 = []
hundcorners3 = []
hundcorners4 = 0
equals = []
equals2 = []
equals3 = []
equals4 = 0
repeats = []
repeats2 = []
repeats3 = []
repeats4 = 0
blanks = []
blanks2 = 0
endx = []
d = 1
choosing = True
for i in range(500):
    endx.append(d)
    d+=1

while choosing:
    choice = input("do you want it to repeat every 500 (y/n)\n> ")
    if choice.lower() == "y":
        loop = True
        choosing = False
    elif choice.lower() == "n":
        loop = False
        choosing = False
        e = "inf"
    else:
        print("type y or n")

while True:
    a += 1
    b = rd.randint(-a,a)
    c = rd.randint(-a,a)
    if b == a and c == a:
        corners.append(b)
        corners2.append(c)
        corners4 += 1
        plt.title(f"{e}-{a} ({b},{c});max on both axis")
        print("max on both")
    elif b == -a and c == -a:
        corners.append(b)
        corners2.append(c)
        corners4 += 1
        plt.title(f"{e}-{a} ({b},{c});max on both axis")
        print("max on both")
    elif b == a and c == -a:
        corners.append(b)
        corners2.append(c)
        corners4 += 1
        plt.title(f"{e}-{a} ({b},{c});max on both axis")
        print("max on both")
    elif b == -a and c == a:
        corners.append(b)
        corners2.append(c)
        corners4 += 1
        plt.title(f"{e}-{a} ({b},{c});max on both axis")
        print("max on both")
    elif b == a or b == -a or c == a or c == -a:
        edges.append(b)
        edges2.append(c)
        edges4 += 1
        plt.title(f"{e}-{a} ({b},{c});max on 1 axis")
        print("max on 1")
    elif b in x and c in y:
        repeats.append(b)
        repeats2.append(c)
        repeats4 += 1
        plt.title(f"{e}-{a} ({b},{c});repeated value")
        print("i hate re-runs")
    elif b in corners and c in corners2:
        repeats.append(b)
        repeats2.append(c)
        repeats4 += 1
        plt.title(f"{e}-{a} ({b},{c});repeated value")
        print("i hate re-runs")
    elif b in edges and c in edges2:
        repeats.append(b)
        repeats2.append(c)
        repeats4 += 1
        plt.title(f"{e}-{a} ({b},{c});repeated value")
        print("i hate re-runs")
    elif b in zeroes and c in zeroes2:
        repeats.append(b)
        repeats2.append(c)
        repeats4 += 1
        plt.title(f"{e}-{a} ({b},{c});repeated value")
        print("i hate re-runs")
    elif b in equals and c in equals2:
        repeats.append(b)
        repeats2.append(c)
        repeats4 += 1
        plt.title(f"{e}-{a} ({b},{c});repeated value")
        print("i hate re-runs")
    elif b in hundcorners and c in hundcorners2:
        repeats.append(b)
        repeats2.append(c)
        repeats4 += 1
        plt.title(f"{e}-{a} ({b},{c});repeated value") 
        print("i hate re-runs")
    elif b in hundreds and c in hundreds2:
        repeats.append(b)
        repeats2.append(c)
        repeats4 += 1
        plt.title(f"{e}-{a} ({b},{c});repeated value")
        print("i hate re-runs")
    elif b in repeats and c in repeats2:
        repeats.append(b)
        repeats2.append(c)
        repeats4 += 1
        plt.title(f"{e}-{a} ({b},{c});repeated value")
        print("i hate re-runs")
    elif b == 0 and c == 0:
        zeroes.append(b)
        zeroes2.append(c) 
        zeroes4 += 1
        plt.title(f"{e}-{a} ({b},{c})")
        print("(0,0)")
    elif b == c:
        equals.append(b)
        equals2.append(c)
        equals4 += 1
        plt.title(f"{e}-{a} ({b},{c});equal x and y")
        print("equal")
    elif b % 100 == 0 and c == b:
        hundcorners.append(b)
        hundcorners2.append(c)
        hundcorners4 += 1
        plt.title(f"{e}-{a} ({b},{c});multiple of same 100")
        print("two of the same 100")
    elif b % 100 == 0 or c % 100 == 0:
        if b != 0 and c != 0:
            hundreds.append(b)
            hundreds2.append(c)
            hundreds4 += 1
            plt.title(f"{e}-{a} ({b},{c});multiple of 100")
            print("multiple of 100")
        else:
            x.append(b)
            y.append(c)
            blanks2 += 1
            plt.title(f"{e}-{a} ({b},{c});nothing")
    else:
        x.append(b)
        y.append(c)
        blanks2 += 1
        plt.title(f"{e}-{a} ({b},{c});nothing")
    corners3.append(corners4)
    equals3.append(equals4)
    edges3.append(edges4)
    zeroes3.append(zeroes4)
    hundcorners3.append(hundcorners4)
    hundreds3.append(hundreds4)
    repeats3.append(repeats4)
    plt.scatter(x,y, color= '#6102f0')
    plt.scatter(edges,edges2, color= '#16f083')
    plt.scatter(zeroes,zeroes2, color= 'r')
    plt.scatter(corners,corners2, color= 'g')
    plt.scatter(hundreds,hundreds2, color= '#72e4ff')
    plt.scatter(hundcorners,hundcorners2, color= 'm')
    plt.scatter(equals,equals2,color= 'y')
    plt.scatter(repeats,repeats2,color= '#fdacf4')
    plt.grid(linestyle= '--')
    plt.xlim(-a,a)
    plt.ylim(-a,a)
    plt.xlabel('the """""""x""""""" """""""axis"""""""')
    plt.ylabel('the """""""y""""""" """""""axis"""""""')
    plt.minorticks_on()
    plt.show()
    if a == 500 and loop == True:
        a = 0
        plt.plot(endx,edges3, color= '#16f083')
        plt.plot(endx,zeroes3, color= 'r')
        plt.plot(endx,corners3, color= 'g')
        plt.plot(endx,hundreds3, color= '#72e4ff')
        plt.plot(endx,hundcorners3, color= 'm')
        plt.plot(endx,equals3,color= 'y')
        plt.plot(endx,repeats3,color= '#fdacf4')
        plt.grid(linestyle= '--')
        plt.xlim(1,500)
        plt.title(f"stuffs this 500; {blanks2} normals")
        plt.ylabel("amount")
        plt.xlabel("graph number")
        plt.legend(["max on one","(0,0)s", "max on both", "multiples of 100s", "2 multiples of the same 100", "equal values", "repeated values"], loc= 'upper left')
        plt.minorticks_on()
        plt.show()
        e += 1
        x = []
        y = []
        corners = []
        corners2 = []
        corners3 = []
        corners4 = 0
        zeroes = []
        zeroes2 = []
        zeroes3 = []
        zeroes4 = 0
        edges = []
        edges2 = []
        edges3 = []
        edges4 = 0
        hundreds = []
        hundreds2 = []
        hundreds3 = []
        hundreds4 = 0
        hundcorners = []
        hundcorners2 = []
        hundcorners3 = []
        hundcorners4 = 0
        equals = []
        equals2 = []
        equals3 = []
        equals4 = 0
        repeats = []
        repeats2 = []
        repeats3 = []
        repeats4 = 0
        blanks = []
        blanks2 = 0