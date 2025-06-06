
class Pet:
    all = []
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]

    def __init__(self, name, pet_type, owner= None):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)


        if pet_type not in self.PET_TYPES:
            raise Exception(f"Invalid pet type: {pet_type}. Must be one of {self.PET_TYPES}")

class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise TypeError("Pet is not of type Pet")
        pet.owner = self
         
    
    def print_pets(self):
        if not self.pets():
            print(f"{self.name} has no pets.")
        else:
            print(f"{self.name}'s pets:")
            for pet in self.pets():
                print(f"Pet name: {pet.name}, Pet type: {pet.pet_type}")


    def get_sorted_pets(self):
      owned_pets = self.pets()
      if not all(isinstance(pet, Pet) for pet in owned_pets):
          raise TypeError("All pets must be Pet instances")
      return sorted(owned_pets, key = lambda pet: pet.name)
    


        

owner = Owner("Jerome")
owner1 = Owner("Lina")
pet1 = Pet("Fido", "dog", owner)
pet2 = Pet("Jerry", "reptile", owner1)
pet3 = Pet("Dico", "dog", owner1)
pet4 = Pet("Echo", "cat", owner)
# print(f"Pet name: {pet1.name}\nType: {pet1.pet_type}\nOwner: { pet1.owner}")
# print(Pet.all)

for pet in Pet.all:
    print(f"Pet name: {pet.name}, Pet type: {pet.pet_type}, Pet Owner: {pet.owner} ")
owner.print_pets()
owner1.print_pets()



sorted_pets = owner.get_sorted_pets()
sorted_pets = owner1.get_sorted_pets()

for pet in sorted_pets:
    print(f"Pet name: {pet.name}, Pet type: {pet.pet_type}, Owner: {pet.owner.name if pet.owner else 'None'}")





