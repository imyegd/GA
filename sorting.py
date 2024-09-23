import random

# 定义个体类
class Individual:
    def __init__(self, genes):
        self.genes = genes
        self.fitness = self.calculate_fitness()

    def calculate_fitness(self):
        # 计算适应度，这里简单假设排序后的基因与目标序列越接近，适应度越高
        target_sequence = sorted(self.genes)
        fitness = sum(1 for i, j in zip(self.genes, target_sequence) if i == j)
        return fitness

# 遗传算法类
class GeneticAlgorithm:
    def __init__(self, population_size, mutation_rate):
        self.population_size = population_size
        self.mutation_rate = mutation_rate

    def generate_initial_population(self):
        population = []
        for _ in range(self.population_size):
            genes = random.sample(range(10), 10)  # 生成随机排序的基因
            individual = Individual(genes)
            population.append(individual)
        return population

    def crossover(self, parent1, parent2):
        # 单点交叉
        crossover_point = random.randint(1, len(parent1.genes) - 1)
        child_genes = parent1.genes[:crossover_point] + parent2.genes[crossover_point:]
        return Individual(child_genes)

    def mutation(self, individual):
        # 随机变异
        for i in range(len(individual.genes)):
            if random.random() < self.mutation_rate:
                individual.genes[i] = random.randint(0, 9)

    def run(self):
        population = self.generate_initial_population()

        for generation in range(100):  # 迭代次数
            # 选择
            population.sort(key=lambda x: x.fitness, reverse=True)
            selected_population = population[:self.population_size // 2]

            # 交叉和变异
            new_population = []
            while len(new_population) < self.population_size:
                parent1, parent2 = random.sample(selected_population, 2)
                child = self.crossover(parent1, parent2)
                self.mutation(child)
                new_population.append(child)

            population = new_population

        # 输出最佳个体
        population.sort(key=lambda x: x.fitness, reverse=True)
        best_individual = population[0]
        print("Best individual:", best_individual.genes)

# 测试
ga = GeneticAlgorithm(population_size=100, mutation_rate=0.1)
ga.run()