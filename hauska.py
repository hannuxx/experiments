#!/usr/bin/python3

class Test:
    g_num = 0

    def __init__(self, name):
        self.name = name
        Test.g_num += 1;

    def show(self):
        print(f'I am Test inst: {self.name}')

    @classmethod
    def G1(cls):
        print(f'Test class method G1: {cls.g_num}')

def hauska(n): return lambda n: n**n

l = [1,2,3,4,5,6,7]
s = "abcde"

for item in zip(l,s):
    print(f'Zipped: {item}')


sq = [x*x for x in l]
print(f"sq: {sq}")

#sq2 = [x*x*x for x in [10,20,30,40,50,60,70,80,90,100,200,300]]
sq2 = [x*x*x for x in range(1000, 2000, 50)]
print(f"sq2: {sq2}")

def main():
    f = hauska(7)

    print(f, f(14))

    t = Test("Kissa");
    t.show()
    Test.G1()
    t2 = Test("Koira");
    t.show()
    Test.G1()    

if __name__ == "__main__":
    main()
