#есть класс собаки, сделать наследование в нём домашние или бродячие собаки, в классе должно быть кличка порода окрас и прочее, пользователь должен встретиться либо с бродячей либо с домашней собакой, и взависимости от этого прописать методы(например для бродечей укусила, а для домашней дала погладить)
class Dog:
    def __init__(self):
        self.name = ""
        self.breed = ""
        self.color = ""
        self.age = ""
    
    def meet(self):
        print(f"Вы встретили собаку")

class PetDog(Dog):
    def __init__(self):
        self.name = input("Кличка собаки: ")
        self.breed = input("Порода: ")
        self.color = input("Окрас: ")
        self.age = input("Возраст: ")
        self.owner = input("Хозяин: ")

    def meet(self):
        print("Вы встретили домашнюю собаку")
        print(f"Кличка {self.name}")
        print(f"Порода {self.breed}")
        print(f"Окрас {self.color}")
        print(f"Возраст {self.age} лет")
        print(f"Хозяин {self.owner}")

    def pet(self):
        print(f"{self.name} дала себя погладить, {self.owner} смотрит и улыбается!")
        print("Вы погладили собаку")
    
    def feed(self):
        print(f"Вы дали собаке по имени {self.name} еду")
        print(f"Собака радостно виляет хвостом, хозяин {self.owner} смотрит и улыбается")

class StrayDog(Dog):
    def __init__(self):
        self.color = input("Окрас: ")
        self.age = input("Примерный возраст: ")
        self.location = input("Где встретили: ")
    
    def meet(self):
        print(f"Вы встретили бродячую собаку")
        print(f"Окрас: {self.color}")
        print(f"Примерный возраст: {self.age} лет")
        print(f"Место: {self.location}")
    
    def bite(self):
        print("Собака укусила вас!")
        print("Нужно сделать укол от бешенства")
    
    def run_away(self):
        print("Собака убежала от вас")
        print("Вы в безопасности")

def main():
    while True:
        print("Вы пошли гулять")
        print("=== ВСТРЕЧА СОБАКИ ===")
        print("1. Домашняя собака")
        print("2. Бродячая собака")
        print("3. Уйти домой")
    
        choice = input("Кого вы встретили? (1 или 2): ")
    
        if choice == "1":
            dog = PetDog()
            dog.meet()
        
            print("Что делать?")
            print("1. Погладить")
            print("2. Покормить")
        
            action = input("Ваш выбор: ")
        
            if action == "1":
                dog.pet()
            elif action == "2":
                dog.feed()
            else:
                print("Вы ничего не сделали")
    
        elif choice == "2":
            dog = StrayDog()
            dog.meet()
        
            print("Что делать?")
            print("1. Попытаться погладить")
            print("2. Отойти подальше")
        
            action = input("Ваш выбор: ")
        
            if action == "1":
                dog.bite()
            elif action == "2":
                dog.run_away()
            else:
                print("Вы застыли на месте")
                print("Собака ушла сама")

        elif choice == "3":
            print("Вы ушли домой")
            break

        else:
            print("Вы не встретили собаку")

if __name__ == "__main__":
    main()