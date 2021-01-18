#!/usr/bin/python3

class Person:
    g_count = 0

    def __init__(self, name):
        self.name = name
        Person.g_count += 1;

    def show(self):
        print(f'I am Person inst: {self.name}')

    @classmethod
    def showCount(cls):
        print(f'Test class method showCount: {cls.g_count}')

class Hero(Person):
    def __init__(self, name, hero_name):
        super().__init__(name);
        self.hero_name = hero_name

    def show(self):
        super().show()
        print(f'...and I am Hero inst with: {self.hero_name}')

def main():
    p = Person('Corey')
    h = Hero('Hannu', 'Power')
    p.show()
    h.show()
    
if __name__ == "__main__":
    main()
