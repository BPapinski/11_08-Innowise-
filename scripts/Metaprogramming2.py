# Tworzymy klasę z minimalnym zestawem
Person = type('Person', (object,), {})

# Dodajemy __init__ po stworzeniu klasy
def __init__(self, name=None, species="Human"):
    self.name = name
    self.species = species

Person.__init__ = __init__

# Dodajemy inne metody
def greet(self):
    print(f"Hello, my name is {self.name}!")

Person.greet = greet

# Dodajemy kolejną metodę później
def set_name(self, name):
    self.name = name

Person.set_name = set_name

# Test
p = Person("Alice", "Elf")
p.greet()         # Hello, my name is Alice!
p.set_name("Bob")
p.greet()         # Hello, my name is Bob!
print(p.species)  # Elf


class MultiBases(type):
    # overriding __new__ method
    def __new__(cls, clsname, bases, clsdict):
        # if no of base classes is greater than 1 raise error
        if len(bases) > 1:
            raise TypeError("Inherited multiple base classes!!!")

        # else execute __new__ method of super class, ie. call __init__ of type class
        return super().__new__(cls, clsname, bases, clsdict)

#new jest wyoknywane w momencie tworzenia nowej klasy (nie obiektu)
# cls - sama metaklasa (chyba cos jak self)
# clsname - nazwa nowej klasy
# bases - klasy bazowe
# clsdict - slownik metod/strybutow nowej klasy

class Base(metaclass=MultiBases):
    pass


class A(Base):
    pass


class B(Base):
    pass


class C(A, B):
    pass