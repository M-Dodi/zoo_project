# Marin Dodi


"""""
# Sistema di gestione dello zoo virtuale

Classi:

1. Zoo: questa classe rappresenta uno zoo. Lo zoo ha dei recinti fences e dei guardiani dello zoo, zoo_keepers.
2. Animal: questa classe rappresenta un animale nello zoo. Ogni animale ha questi attributi: name, species, age, height, width, preferred_habitat, health che è uguale a round(100 * (1 / age), 3).
3. Fence: questa classe rappresenta un recinto dello zoo in cui sono tenuti gli animali. I recinti possono contenere uno o più animali. I recinti possono hanno gli attributi area, temperature e habitat.
4. ZooKeeper: questa classe rappresenta un guardiano dello zoo responsabile della gestione dello zoo. I guardiani dello zoo hanno un nome, un cognome, e un id. Essi possono nutrire gli animali, 
pulire i recinti e svolgere altri compiti nel nostro zoo virtuale.

Funzionalità:
1. add_animal(animal: Animal, fence: Fence) (Aggiungi nuovo animale): consente al guardiano dello zoo di aggiungere un nuovo animale allo zoo. L'animale deve essere collocato in un recinto adeguato 
in base alle esigenze del suo habitat e se c'è ancora spazio nel recinto, ovvero se l'area del recinto è ancora sufficiente per ospitare questo animale.

2. remove_animal(animal: Animal, fence: Fence) (Rimuovi animale): consente al guardiano dello zoo di rimuovere un animale dallo zoo. L'animale deve essere allontanato dal suo recinto. 
Nota bene: L'area del recinto deve essere ripristinata dello spazio che l'animale rimosso occupava.

3. feed(animal: Animal) (Dai da mangiare agli animali): implementa un metodo che consenta al guardiano dello zoo di nutrire tutti gli animali dello zoo. Ogni volta che un animale viene nutrito, 
la sua salute incrementa di 1% rispetto alla sua salute corrente, ma le dimensioni dell'animale (height e width) vengono incrementate del 2%. Perciò, l'animale si può nutrire soltanto se il recinto
 ha ancora spazio a sufficienza per ospitare l'animale ingrandito dal cibo.

4. clean(fence: Fence) (Pulizia dei recinti): implementare un metodo che consenta al guardiano dello zoo di pulire tutti i recinti dello zoo. Questo metodo restituisce un valore di tipo 
float che indica il tempo che il guardiano impiega per pulire il recinto. Il tempo di pulizia è il rapporto dell'area occupata dagli animali diviso l'area residua del recinto. Se l'area residua è pari a 0,
 restituire l'area occupata.

5. describe_zoo() (Visualizza informazioni sullo zoo): visualizza informazioni su tutti i guardani dello zoo, sui recinti dello zoo che contengono animali. 

E.s.: Se abbiamo un guardiano chiamato Lorenzo Maggi con matricola 1234, e un recinto Fence(area=100, temperature=25, habitat=Continentale) con due animali
 Animal(name=Scoiattolo, species=Blabla, age=25, ...), Animal(name=Lupo, species=Lupus, age=14,...) ci si aspetta di avere una rappresentazione testuale dello zoo come segue:

Guardians:

ZooKeeper(name=Lorenzo, surname=Maggi, id=1234)

Fences:

Fence(area=100, temperature=25, habitat=Continent)

with animals:

Animal(name=Scoiattolo, species=Blabla, age=25)

Animal(name=Lupo, species=Lupus, age=14)
#########################

Fra un recinto e l'altro mettete 30 volte il carattere #.

"""
class Animal:
    
    def __init__(self, name: str, species: str, age: float, height: float, width:float, preferred_habitat:str) -> None:
        self.name: str = name
        self.species: str = species
        self.age: float = age
        self.height: float = height
        self.width: float = width
        self.preferred_habitat: str = preferred_habitat
        self.health: float = min(round(100 * (1/self.age), 3), 100)
        self.fence: Fence = None
        
    def area(self):
        return self.height * self.width
    
    def become_bigger(self, factor: float = 0.02) -> tuple[float, float]:
        height = self.height + self.height * factor
        width = self.width + self.width * factor
        return height, width
        
    def become_healthier(self, factor: float = 0.01):
        self.health = min(self.health + self.health * factor, 100)
        
    def __str__(self) -> str:
        return f'Animal(name={self.name}, species={self.species}, age={self.age}, height={round(self.height,3)}'\
            + f', width={round(self.width,3)}, habitat={self.preferred_habitat})'
    
class Fence:
    
    def __init__(self, area: float, temperature: float, habitat: str) -> None:
        self.area: float = area
        self.temperature: float = temperature
        self.habitat: str = habitat
        self.animals: list[Animal] = []
        
    def same_habitat(self, animal: Animal) -> bool:
        return animal.preferred_habitat.lower() == self.habitat.lower()
    
    def enough_space(self, animal_area: float) -> bool:
        return animal_area <= self.area
    
    def update_area(self, new_animal_area: float, old_animal_area: float):
        self.area += old_animal_area
        self.area -= new_animal_area
        
    def add_animal(self, animal: Animal):
        animal_area: float = animal.area()
        if self.same_habitat(animal) and self.enough_space(animal_area)\
            and animal not in self.animals:
            self.animals.append(animal)
            # elimino lo spazio del recinto che l'animale occupa
            self.area -= animal_area
            animal.fence = self
            
    def remove_animal(self, animal: Animal):
        if animal in self.animals:
            self.animals.remove(animal)
            animal_area: float = animal.area()
            # ripristino l'area occupata dall'animale
            self.area += animal_area
            animal.fence = None
            
    def feed(self, animal: Animal):
        new_height, new_width = animal.become_bigger()
        if self.enough_space((new_height * new_width) - animal.area()):
            # ripristina l'area vecchia occupata dall'animale
            self.area += animal.area()
            # faccio diventare l'animale più grande
            animal.height = new_height
            animal.width = new_width
            # levare al recinto l'area dell'animale più grande
            self.area -= animal.area()
            # incrementa la salute dell'animale
            animal.become_healthier()  
            
    def __str__(self) -> str:
        s: str = f"Fence(area={round(self.area,3)}, temperature={self.temperature}, habitat={self.habitat})"
        s += "\nWith Animals:\n"
        for animal in self.animals:
            s += animal.__str__() + "\n"
        return s[:-1]

class ZooKeeper:
    
    def __init__(self, name: str, surname: str, id: str) -> None:
        self.name: str = name
        self.surname: str = surname
        self.id: str = id
        
    def add_animal(self, animal: Animal, fence: Fence):
        fence.add_animal(animal)
        
    def remove_animal(self, animal: Animal, fence: Fence):
        fence.remove_animal(animal)
                
    def feed(self, animal: Animal):
        fence: Fence = animal.fence
        if fence:
            fence.feed(animal)
            
    def clean(self, fence: Fence) -> float:
        occupied_area: float = 0
        for animal in fence.animals:
            occupied_area += animal.area()
            
        if fence.area == 0:
            return occupied_area
        else:
            return occupied_area / fence.area
                
    def clean_all(self, zoo) -> float:
        cleaning_time = 0
        for fence in zoo.fences:
            cleaning_time += self.clean(fence)
        return cleaning_time
            
            
    def __str__(self) -> str:
        return f'ZooKeeper(name={self.name}, surname={self.surname}, id={self.id})'
    
class Zoo:
    
    
    def __init__(self, fences: list[Fence], zoo_keepers: list[ZooKeeper]):
        self.fences: list[Fence] = fences
        self.zoo_keepers: list[ZooKeeper] = zoo_keepers
        
    def describe_zoo(self):
        print("Guardians:")
        for zoo_keeper in self.zoo_keepers:
            print(zoo_keeper)
        print("Fences:")
        for fence in self.fences:
            print(fence)
            print("#" * 30)
    
    
    
simba = Animal(name="Simba", species="Leone", age=5, height=2, width=3, preferred_habitat="Savana")
simba1 = Animal(name="Simba", species="Leone", age=5, height=2, width=2, preferred_habitat="Giungla")

savana = Fence(area=100, temperature=27, habitat="Savana")
zoo_keeper = ZooKeeper(name="Bardh", surname="Prenkaj", id="PRNBDH95M09Z160W")

print(f"L'area del fence Savana è {savana.area}")
zoo = Zoo(fences=[savana], zoo_keepers=[zoo_keeper])
zoo_keeper.add_animal(simba, savana)
zoo_keeper.add_animal(simba1, savana)
print(f"L'area del fence Savana è {savana.area}")
old_area = 0
for i in range(1000):
    zoo_keeper.feed(simba)
    if old_area == round(simba.area(), 3):
        break
    print(f"It={i+1} --> L'area residua del recinto è {round(simba.fence.area, 3)}")
    print(f"It={i+1} --> Simba è diventato grande = {round(simba.area(), 3)}")
    old_area = round(simba.area(), 3)
    
pumba = Animal(name="Pumba", species="Porco", age=25, height=2, width=5, preferred_habitat="Savana")
zoo_keeper.add_animal(pumba, savana)


    

        















    











