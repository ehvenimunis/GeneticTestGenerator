import random

# Üçgen sınıflandırma fonksiyonu (SUT: Software Under Test)
def classify_triangle(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return "Not a triangle"
    elif a == b == c:
        return "Equilateral"
    elif a == b or a == c or b == c:
        return "Isosceles"
    else:
        return "Scalene"

# Uygunluk fonksiyonu (fitness function)
def fitness_function(test_case):
    a, b, c = test_case
    result = classify_triangle(a, b, c)
    coverage = {
        "Not a triangle": 1,
        "Equilateral": 1,
        "Isosceles": 1,
        "Scalene": 1
    }
    return coverage.get(result, 0)

# Popülasyon oluşturma
def create_population(size, value_range):
    return [tuple(random.randint(*value_range) for _ in range(3)) for _ in range(size)]

# Çaprazlama operatörü (crossover)
def crossover(parent1, parent2):
    point = random.randint(1, len(parent1) - 1)
    return parent1[:point] + parent2[point:]

# Mutasyon operatörü (mutation)
def mutate(individual, value_range):
    index = random.randint(0, len(individual) - 1)
    mutated_value = random.randint(*value_range)
    return tuple(
        mutated_value if i == index else val for i, val in enumerate(individual)
    )

# Genetik algoritma
def genetic_algorithm(sut, population_size=20, generations=100, value_range=(1, 100)):
    population = create_population(population_size, value_range)
    for generation in range(generations):
        population = sorted(population, key=lambda x: -fitness_function(x))
        if fitness_function(population[0]) == 4:  # Tüm test durumlarını kapsayan birey
            break
        next_population = population[:2]  # Elitizm: En iyi 2 bireyi koru
        while len(next_population) < population_size:
            parent1, parent2 = random.sample(population[:10], 2)  # En iyi 10 bireyden seç
            child = mutate(crossover(parent1, parent2), value_range)
            next_population.append(child)
        population = next_population
    return population[0]  # En iyi birey

# Genetik algoritmayı çalıştırma
best_test_case = genetic_algorithm(classify_triangle)
print("En iyi test durumu:", best_test_case)
print("Sonuç:", classify_triangle(*best_test_case))
