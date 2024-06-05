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

    def __int__(self,name: str, species: str,age: int, height: float, width: float,
                 preferred_habitat: str, health: float):
        
        self.name = name
        self.species = species  
        self.age = age
        self.height = height
        self.width = width
        self.preferred_habitat = preferred_habitat
        self.health = round(100 * (1 / age), 3)




class Fence:
    def __init__(self, area: float, temperature: float, habitat: str):  
        self.area = area
        self.temperature = temperature
        self.habitat = habitat
        self.animals = []  # Lista degli animali nel recinto

    def add_animal(self, animal):

        if animal.preferred_habitat == self.habitat and self.area >= animal.height * animal.width:
         self.animals.append(animal)
            
         return f"{animal.name} è stato aggiunto al recinto {self.habitat}."
        
        else:
         
         return f"Impossibile aggiungere {animal.name} al recinto {self.habitat}."

    def remove_animal(self, animal, fence):
        # Rimuovi animale
        if animal in fence.animals:
            self.animals.remove(animal)
            
            return f"{animal.name} è stato rimosso dal recinto {self.habitat}."
        
        else:
            return f"{animal.name} non è presente nel recinto {self.habitat}."


    
    def remaining_area(self):
        occupied_area = sum(animal.height * animal.width for animal in self.animals)
        return max(0, self.area - occupied_area)

class ZooKeeper:

    def __int__(self,name: str, surname: str, id_number: str): 
        self.name = name
        self.surname = surname
        self.id = id_number

    def feed_animal(self, animal):
        # Implementa la logica per nutrire l'animale
        # Incrementa la salute dell'animale del 1% e le dimensioni del 2%
        animal.health += animal.health * 0.01
        animal.height += animal.height * 0.02
        animal.width += animal.width * 0.02

        if self.check_space(animal, Fence):
            print(f"L'animale {animal.name} è stato nutrito con successo.")
        else:
            print(f"Non c'è abbastanza spazio nel recinto per nutrire l'animale {animal.name}.")
    # Ripristina la salute e le dimensioni dell'animale ai valori precedenti
            animal.health -= animal.health * 0.01 / 1.01
            animal.height -= animal.height * 0.02 / 1.02
            animal.width -= animal.width * 0.02 / 1.02

    def check_space(self, animal, fence):
        # Calcola l'area totale occupata dagli animali nel recinto
        total_occupied_area = sum(a.height * a.width for a in fence.animals)
        # Includi l'area che sarebbe occupata dall'animale dopo essere stato nutrito
        new_occupied_area = total_occupied_area + (animal.height * animal.width)
        # Controlla se l'area totale occupata supera l'area del recinto
        return new_occupied_area <= fence.area

    def clean_fence(self, fence):
        # Implementa la logica per pulire il recinto
        remaining_area = fence.remaining_area()
        
        if remaining_area == 0:
         
            return f"L'area occupata nel recinto {fence.habitat} è {fence.area}."
        
        cleaning_time = sum(animal.height * animal.width for animal in fence.animals) / remaining_area
        
        return cleaning_time
    



class Zoo:

    def __init__(self, fences: int, zoo_keepers: None):
        self.fences = []
        self.zoo_keepers = zoo_keepers

    def add_fence(self, fence):
        self.fences.append(fence)
   
    
def describe_zoo(self):
        print("Guardians:")
        for keeper in self.zoo_keepers:
            print(f"ZooKeeper(name={ZooKeeper.name}, surname={ZooKeeper.surname}, id={ZooKeeper.id_number})")
        print("\nFences:")    
        
        for fence in self.fences:
            print(f"Fence(area={fence.area}, temperature={fence.temperature}, habitat={fence.habitat})")
            print("with animals:")
            for animal in fence.animals:
                print(f"Animal(name={animal.name}, species={animal.species}, age={animal.age})")
            print("#" * 30)

    

zoo = Zoo(fences=[continent_fence], zoo_keepers=[lorenzo])
lorenzo = ZooKeeper('Lorenzo', 'Maggi', '1234')
continent_fence = Fence(100, 25, 'Continentale')
zoo.fences.append(continent_fence)
scoiattolo = ('Scoiattolo', 'Blabla', 25, 0.5, 0.3, 'Continentale')
lupo =('Lupo', 'Lupus', 14, 1.5, 0.8, 'Continentale')
continent_fence.animals.extend([scoiattolo, lupo])

# Visualizza informazioni sullo zoo
if __name__ == "__main__":
    zoo.describe_zoo()
        















    











