from datetime import date

class Snake:

    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age
        self.slithering = True
        self.date_added = date.today()
    


slippy = Snake('Slippy', 'Asshole Snake', 12)
bitey = Snake('Bitey', 'Colurful Snake', 4)
sneaky = Snake('Sneaky', 'Asshole Snake', 2)
killy = Snake('Sneaky', 'Colurful Snake', 5)
hunny = Snake('Hunny', 'Loner Snake', 5)

# for prop, value in slippy.__dict__.items():
#     print(f'{prop}: {value}')

class Fish:

    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age
        self.swimming = True
        self.date_added = date.today()
    


nemo = Fish('Nemo', 'Clown Fish', 5)
dory = Fish('Dory', 'Flat Fish', 8)
gill = Fish('Gill', 'Flat Fish', 9)
marvin = Fish('Phil', 'Clown Fish', 9)
finny = Fish('Finny', 'Flat Fish', 3)

# for prop, value in nemo.__dict__.items():
#     print(f'{prop}: {value}')

class Deer:

    def __init__(self, name, species, age, shift):
        self.name = name
        self.species = species
        self.age = age
        self.shift = shift
        self.walking = True
        self.date_added = date.today()
    


shika = Deer('Shika', 'Brown Deer', 2, 'midday')
bitey = Deer('Benny', 'White Head', 14, 'morning')
henry = Deer('Henry', 'Brown Deer', 2, 'morning')
craig = Deer('Craig', 'White Head', 11, 'midday')
scoot = Deer('Scoot', 'Brown Deer', 7, 'evening')

# for prop, value in shika.__dict__.items():
#     print(f'{prop}: {value}')
print(f'{shika.name} the {shika.species} is available to pet during the {shika.shift} shift.')