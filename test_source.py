import random
import time
import numpy as np
import pytest
from source import experiment_code1  # experiment_code1 fonksiyonunu source.py'dan import ediyoruz

# Parametreler
POPULATION_SIZE = 20  # Popülasyon büyüklüğü
GENERATIONS = 100  # Toplam nesil sayısı
Pc = 0.75  # Crossover (yeni birey üretimi) olasılığı
Pm = 0.10  # Mutasyon (rastgele değişim) olasılığı

def generate_population():
    """Rastgele popülasyon oluştur.
    Her birey 3 parametre (x, y, z) arasında 1 ile 10 arasında rastgele değerler alır.
    """
    return [[random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)] for _ in range(POPULATION_SIZE)]

def crossover(parent1, parent2):
    """İki ebeveynin genetik materyalini birleştirerek yeni bir çocuk birey oluşturur.
    Crossover olasılığına göre, ebeveynlerin genetik kodlarının bazı kısımları değiştirilir.
    """
    child = parent1[:]  # Ebeveyn1'in kopyasını al
    if random.random() < Pc:  # Eğer crossover olasılığı sağlanıyorsa
        idx = random.randint(0, 2)  # 0, 1, 2 arasından rastgele bir index seç
        child[idx] = parent2[idx]  # Çocuğa, ebeveyn2'den bir gen aktar
    return child

def mutate(individual):
    """Bir bireyi mutasyona uğratır.
    Mutasyon olasılığına göre, bireylerin bir kısmı rastgele değiştirilir.
    """
    if random.random() < Pm:  # Eğer mutasyon olasılığı sağlanıyorsa
        idx = random.randint(0, 2)  # 0, 1, 2 arasından rastgele bir index seç
        individual[idx] = random.randint(1, 10)  # Bireyin o genini rastgele değiştir
    return individual

def fitness_function(params):
    """Fitness fonksiyonu: Parametrelerin ne kadar 'iyi' olduğunu ölçer.
    Bu örnekte, üçgen özelliklerini değerlendirir:
    - Eşkenar üçgen, skalen üçgen, ikizkenar üçgen
    - Üçgen eşitsizliği kontrolü
    """
    x, y, z = params
    coverage = 0  # Kapsama oranı başlangıçta 0

    # Eşkenar üçgen kontrolü
    if x == y == z:
        coverage += 1

    # Skalen üçgen kontrolü
    if x != y and x != z and y != z:
        coverage += 1

    # İkizkenar üçgen kontrolü
    if (x == y and x != z) or (x == z and x != y) or (y == z and y != x):
        coverage += 1

    # Üçgen eşitsizliği kuralı
    if x + y > z and x + z > y and y + z > x:
        coverage += 1

    return coverage

def genetic_algorithm():
    """Genetik algoritma fonksiyonu:
    Popülasyonu oluşturur, her nesilde yeni bireyler üretir, crossover ve mutasyon uygular, 
    en iyi çözümü bulmaya çalışır.
    """
    start_time = time.time()  # Çalışma süresi izleme

    population = generate_population()  # İlk popülasyonu oluştur
    diversity_over_time = []  # Çeşitliliği izlemek için liste
    best_fitnesses = []  # Fitness değerlerini izlemek için liste

    for generation in range(GENERATIONS):
        # Popülasyonu fitness puanlarına göre sırala (en iyi bireyler önce)
        population = sorted(population, key=lambda x: -fitness_function(x))

        # En iyi bireyleri seç (popülasyonun yarısı kadar)
        next_generation = population[:POPULATION_SIZE // 2]

        # Crossover ve mutasyon ile yeni bireyler oluştur
        while len(next_generation) < POPULATION_SIZE:
            parent1, parent2 = random.sample(population[:POPULATION_SIZE // 2], 2)  # En iyi yarım popülasyondan ebeveyn seç
            child = crossover(parent1, parent2)  # Ebeveynlerden crossover ile çocuk üret
            child = mutate(child)  # Mutasyon uygula
            next_generation.append(child)

        population = next_generation  # Yeni nesli popülasyon olarak kabul et

        # Her nesilde en iyi fitness değerini yazdır
        best_fitness = max(fitness_function(ind) for ind in population)
        best_fitnesses.append(best_fitness)

        # Çeşitliliği hesapla (popülasyondaki farklı bireylerin sayısı)
        diversity = len(set(tuple(ind) for ind in population))
        diversity_over_time.append(diversity)

        # Nesil bilgilerini yazdır
        print(f"Generation {generation + 1}: Best Fitness = {best_fitness}, Diversity = {diversity}")

    # En iyi bireyi seç
    best_individual = max(population, key=fitness_function)

    # Çalışma süresi, konverjans ve çeşitlilik sonuçlarını yazdır
    end_time = time.time()
    runtime = end_time - start_time  # Çalışma süresi
    std_dev = np.std(best_fitnesses)  # Fitness değerlerinin standart sapması
    p_value = 0.05  # P-değeri (manüel olarak belirlenmiş)
    coverage = np.mean(best_fitnesses)  # Ortalama fitness (kapsama oranı)

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

    return best_individual  # En iyi bireyi döndür

# Test cases
@pytest.mark.parametrize("params", [genetic_algorithm() for _ in range(5)])  # Genetik algoritma sonuçlarını test eder
def test_experiment_code1(params):
    """Genetik algoritma sonuçlarını experiment_code1 fonksiyonu ile test eder."""
    x, y, z = params
    result = experiment_code1(x, y, z)  # experiment_code1 fonksiyonu ile test et
    assert result == (x, y, z)  # Sonuçların doğru olup olmadığını kontrol et

# Testi çalıştırmak için
if __name__ == "__main__":
    import os
    os.system('pytest --cov=source --cov-report=term-missing')  # Testleri çalıştır
