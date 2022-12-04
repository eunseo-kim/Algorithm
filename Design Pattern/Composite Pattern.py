class Component:
    def __init__(self, value):
        self.value = value

    def foo(self):
        pass


class Card:
    def __init__(self, value):
        self.card = Component(value)

    def foo(self):
        print("Card", self.card.value)


class Cardset:
    def __init__(self, title):
        self.cardset = Component(title)
        self.children = []

    def add(self, component: Component):
        self.children.append(component)

    def foo(self):
        print("Cardset", self.cardset.value)
        for component in self.children:
            component.foo()


cardset1 = Cardset("Java")

card1 = Card("자료형")
card2 = Card("반복문")
cardset2 = Cardset("객체지향")

cardset1.add(card1)
cardset1.add(card2)
cardset1.add(cardset2)

card3 = Card("OOP")
card4 = Card("다형성")
cardset2.add(card3)
cardset2.add(card4)

cardset1.foo()
