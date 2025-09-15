class Animal:

    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.health = health
        self.name = name
        self.hidden = False
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (f'{{Name: {self.name},'
                f' Health: {self.health},'
                f' Hidden: {self.hidden}}}')


class Herbivore(Animal):

    def hide(self) -> None:
        if not self.hidden:
            self.hidden = True
        else:
            self.hidden = False


class Carnivore(Animal):

    def bite(self, obj: Animal) -> None:
        if obj.health > 0:
            if isinstance(obj, Herbivore) and not obj.hidden:
                obj.health -= 50
        if obj.health <= 0:
            Animal.alive.remove(obj)
