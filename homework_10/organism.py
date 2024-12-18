import random
import time
from concurrent.futures import ThreadPoolExecutor


class Organism:
    """Клас для моделювання організму."""
    def __init__(self, id: int, energy: int):
        self.id = id
        self.energy = energy  # Поточний рівень енергії організму

    def eat(self):
        """Організм отримує енергію з харчування."""
        food_energy = random.randint(5, 20)
        self.energy += food_energy
        print(f"Організм {self.id} з'їв їжу: +{food_energy} енергії (загальна: {self.energy})")

    def reproduce(self):
        """Організм намагається розмножитися, якщо достатньо енергії."""
        if self.energy > 50:
            self.energy -= 30  # Витрати енергії на розмноження
            print(f"Організм {self.id} розмножився! (залишилось: {self.energy} енергії)")
            return True
        return False

    def survive(self):
        """Організм втрачає енергію через підтримку життєдіяльності."""
        survival_cost = random.randint(10, 15)
        self.energy -= survival_cost
        print(f"Організм {self.id} витратив {survival_cost} енергії на виживання (залишилось: {self.energy})")
        if self.energy <= 0:
            print(f"Організм {self.id} загинув.")
            return False
        return True


def evolve(organism: Organism):
    """Один крок еволюції для організму."""
    organism.eat()
    if not organism.survive():
        return None  # Організм не вижив
    organism.reproduce()
    return organism


def simulate_population(organisms, generations, max_workers=4):
    """Моделює еволюцію популяції."""
    for generation in range(1, generations + 1):
        print(f"\n=== Покоління {generation} ===")
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            results = list(executor.map(evolve, organisms))

        # Видаляємо загиблих організмів
        organisms = [org for org in results if org is not None]

        # Додаємо нових організмів від розмноження
        offspring = []
        for org in organisms:
            if org.reproduce():
                offspring.append(Organism(id=len(organisms) + len(offspring) + 1, energy=40))
        organisms.extend(offspring)

        print(f"Кількість організмів: {len(organisms)}")
        if not organisms:
            print("Популяція вимерла.")
            break
    return organisms


if __name__ == "__main__":
    initial_population = [Organism(id=i, energy=random.randint(20, 50)) for i in range(1, 11)]
    final_population = simulate_population(initial_population, generations=10, max_workers=4)
    print("\n=== Фінальний стан популяції ===")
    for org in final_population:
        print(f"Організм {org.id}: {org.energy} енергії")
