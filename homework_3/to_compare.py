class Person(object):

    def __init__(self, name, age):
        """Initialization name and age"""
        self.name = name
        self.age = age

    def __lt__(self, other):
        """Comparison younger first than second"""
        return self.age < other.age

    def __eq__(self, other):
        """Age-matched comparison"""
        return self.age == other.age

    def __gt__(self, other):
        """Comparison older first than second"""
        return self.age > other.age

    def __repr__(self):
        """Deriving the answer"""
        return f"Відповідь: Ім'я {self.name}, вік {self.age}"


person = [
    Person("Anna", 25),
    Person("Dima", 35),
    Person("Kirill", 42),
    Person("Dasha", 36)
    ]
sorted_people = sorted(person)

for p in sorted_people:
    print(p)
