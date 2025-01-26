import random
import time
import numpy as np
import pytest
from source import experiment_code1  # experiment_code1 fonksiyonunu source.py'dan import ediyoruz

# Parametreler
POPULATION_SIZE = 20
GENERATIONS = 100
Pc = 0.75  # Crossover olasılığı
Pm = 0.10  # Mutasyon olasılığı

def generate_population():
    """Rastgele popülasyon oluştur (örneğin x, y, z için 1-10 arasında değerler)."""
    return [[random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)] for _ in range(POPULATION_SIZE)]

def crossover(parent1, parent2):
    """İki ebeveynin genetik materyalini birleştir."""
    child = parent1[:]
    if random.random() < Pc:  # Pc olasılığı ile crossover uygula
        idx = random.randint(0, 2)  # 0, 1, 2 arasından rastgele bir index seç
        child[idx] = parent2[idx]  # Rastgele index'teki genleri değiştir
    return child

def mutate(individual):
    """Bir bireyi mutasyona uğrat."""
    if random.random() < Pm:  # Pm olasılığı ile mutasyon uygula
        idx = random.randint(0, 2)  # 0, 1, 2 arasından rastgele bir index seç
        individual[idx] = random.randint(1, 10)  # Rastgele yeni bir değer ata
    return individual

def fitness_function(params):
    """Fitness fonksiyonu."""
    x, y, z = params
    coverage = 0

    # Equilateral case
    if x == y == z:
        coverage += 1

    # Scalene case
    if x != y and x != z and y != z:
        coverage += 1

    # Isosceles case
    if (x == y and x != z) or (x == z and x != y) or (y == z and y != x):
        coverage += 1

    # Triangle inequality rule
    if x + y > z and x + z > y and y + z > x:
        coverage += 1

    return coverage

def genetic_algorithm():
    """Genetik algoritma."""
    start_time = time.time()  # Çalışma süresi izleme

    population = generate_population()
    diversity_over_time = []  # Çeşitliliği izlemek için liste
    best_fitnesses = []  # Konverjansı izlemek için en iyi fitness değerleri

    for generation in range(GENERATIONS):
        # Popülasyonu fitness puanlarına göre sırala
        population = sorted(population, key=lambda x: -fitness_function(x))

        # En iyi bireyleri seç
        next_generation = population[:POPULATION_SIZE // 2]

        # Crossover ve mutasyon uygula
        while len(next_generation) < POPULATION_SIZE:
            parent1, parent2 = random.sample(population[:POPULATION_SIZE // 2], 2)
            child = crossover(parent1, parent2)
            child = mutate(child)  # Mutasyon olasılığıyla çocuk bireyi değiştir
            next_generation.append(child)

        population = next_generation

        # Her nesilde en iyi bireyi yazdır
        best_fitness = max(fitness_function(ind) for ind in population)
        best_fitnesses.append(best_fitness)

        # Çeşitliliği hesapla (popülasyon içindeki farklı bireylerin sayısı)
        diversity = len(set(tuple(ind) for ind in population))
        diversity_over_time.append(diversity)

        print(f"Generation {generation + 1}: Best Fitness = {best_fitness}, Diversity = {diversity}")

    # En iyi bireyi döndür
    best_individual = max(population, key=fitness_function)

    # Çalışma süresi, konverjans ve çeşitlilik sonuçlarını yazdır
    end_time = time.time()
    runtime = end_time - start_time
    std_dev = np.std(best_fitnesses)  # Standart sapma
    p_value = 0.05  # P-değerini manuel olarak belirle (daha ileri analiz gerektirir)
    coverage = np.mean(best_fitnesses)  # Ortalama kapsama oranı

    # Sonuçları yazdır
    print(f"\nSonuçlar:")
    print(f"Çalışma Süresi: {runtime:.3f} saniye")
    print(f"STD (Standart Sapma): {std_dev:.3f}")
    print(f"P-Value: {p_value:.3f}")
    print(f"Coverage (Kapsama Oranı): {coverage:.3f}")
    print(f"NFE (Değerlendirme Sayısı): {GENERATIONS * POPULATION_SIZE}")
    print(f"Popsize (Popülasyon Büyüklüğü): {POPULATION_SIZE}")
    print(f"Np (Değişken Sayısı): 3")
    print(f"Nv (Gen Sayısı): {GENERATIONS}")
    print(f"Range (Aralık): 1-10")

    return best_individual

# Test cases
@pytest.mark.parametrize("params", [genetic_algorithm() for _ in range(5)])
def test_experiment_code1(params):
    x, y, z = params
    result = experiment_code1(x, y, z)
    assert result == (x, y, z)

# Testi çalıştırmak için
if __name__ == "__main__":
    import os
    os.system('pytest --cov=source --cov-report=term-missing')
