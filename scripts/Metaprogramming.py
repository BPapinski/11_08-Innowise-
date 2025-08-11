# Method to be added dynamically
def greet(self):
    print(f"Hello, my name is {self.name}!")

def set_name(self, name):
    self.name = name

def __init__(self, name=None, species="Human"):
    self.name = name
    self.species = species

# Create a new class dynamically using type()
Person = type(
    'Person',             # class name
    (object,),            # base classes
    {                     # attributes/methods dictionary
        '__init__': __init__,
        'species': 'Human',
        'greet': greet,
        'set_name': set_name
    }
)

# Create object
p = Person(species='something')

# Use dynamically added methods
p.set_name("Alice")
p.greet()                 # Hello, my name is Alice!
print(p.species)          # Human

# Check types
print(type(Person))       # <class 'type'>
print(type(p))            # <class '__main__.Person'>
