from datetime import date

class Snake:

    def __init__(self, name, species, age, food):
        self.name = name
        self.species = species
        self.age = age
        self.slithering = True
        self.food = food
        self.date_added = date.today()
    
    def feed(self):
        x = (f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
        return x


slippy = Snake('Slippy', 'Asshole Snake', 12, 'rats')
bitey = Snake('Bitey', 'Colurful Snake', 4, 'rats')
sneaky = Snake('Sneaky', 'Asshole Snake', 2, 'rats')
killy = Snake('Sneaky', 'Colurful Snake', 5, 'rats')
hunny = Snake('Hunny', 'Loner Snake', 5, 'rats')

# for prop, value in slippy.__dict__.items():
#     print(f'{prop}: {value}')

class Fish:

    def __init__(self, name, species, age, food):
        self.name = name
        self.species = species
        self.age = age
        self.swimming = True
        self.food = food
        self.date_added = date.today()
    
    def feed(self):
        x = (f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
        return x
    


nemo = Fish('Nemo', 'Clown Fish', 5, 'Fish flakes')
dory = Fish('Dory', 'Flat Fish', 8, 'Fish flakes')
gill = Fish('Gill', 'Flat Fish', 9, 'Fish flakes')
marvin = Fish('Phil', 'Clown Fish', 9, 'Fish flakes')
finny = Fish('Finny', 'Flat Fish', 3, 'Fish flakes')

print(dory.feed())
# for prop, value in nemo.__dict__.items():
#     print(f'{prop}: {value}')

class Deer:

    def __init__(self, name, species, age, shift, food):
        self.name = name
        self.species = species
        self.age = age
        self.shift = shift
        self.walking = True
        self.food = food
        self.date_added = date.today()
    
    def feed(self):
        return(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

shika = Deer('Shika', 'Brown Deer', 2, 'midday', 'pellets')
bitey = Deer('Benny', 'White Head', 14, 'morning', 'pellets')
henry = Deer('Henry', 'Brown Deer', 2, 'morning', 'pellets')
craig = Deer('Craig', 'White Head', 11, 'midday', 'pellets')
scoot = Deer('Scoot', 'Brown Deer', 7, 'evening', 'pellets')

for prop, value in dory.__dict__.items():
    print(f'{prop}: {value}')
