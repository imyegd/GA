import random

# 定义个体类
# class Individual:
#     def __init__(self, genes):
#         self.genes = genes
#         self.fitness = self.calculate_fitness()
#     def calculate_fitness(self):
#         # 计算适应度，这里简单假设排序后的基因与目标序列越接近，适应度越高
#         target_sequence = sorted(self.genes)
#         fitness = sum(1 for i, j in zip(self.genes, target_sequence) if i == j)
#         return fitness


# class Individual:
#     def __init__(self, genes):
#         self._genes = genes
#         self._fitness = self.calculate_fitness()

#     def calculate_fitness(self):
#         target_sequence = sorted(self._genes)
#         return sum(1 for i, j in zip(self._genes, target_sequence) if i == j)

#     @property
#     def genes(self):
#         return self._genes

#     @genes.setter
#     def genes(self, new_genes):
#         self._genes = new_genes
#         self._fitness = self.calculate_fitness()

#     @property
#     def fitness(self):
#         return self._fitness

# 定义个体类
class Individual:
    def __init__(self, genes):
        self.genes = genes
        # self.fitness = self.calculate_fitness()
    
    @property
    def fitness(self):
        # target_sequence = sorted(self.genes)
        target_sequence = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        return sum(1 for i, j in zip(self.genes, target_sequence) if i == j)
    
    # def calculate_fitness(self):
    #     # 计算适应度，这里简单假设排序后的基因与目标序列越接近，适应度越高
    #     target_sequence = sorted(self.genes)
    #     fitness = sum(1 for i, j in zip(self.genes, target_sequence) if i == j)
    #     return fitness

# 遗传算法类
class GeneticAlgorithm:
    def __init__(self, generarions_num, population_size, chromosome_length, mutation_rate):
        self.generations_num = generarions_num
        self.population_size = population_size
        self.chromosome_length = chromosome_length
        self.mutation_rate = mutation_rate

    def generate_initial_population(self):
        population = []
        for _ in range(self.population_size):
            original_list = list(range(0, self.chromosome_length))
            random.shuffle(original_list)
            # genes = random.sample(range(self.chromosome_length), self.chromosome_length)  # 生成随机排序的基因
            individual = Individual(original_list)
            population.append(individual)
        return population
    
    def pmx_crossover(self, parent1, parent2):
        size = len(parent1)

        cxpoint1, cxpoint2 = sorted(random.sample(range(size), 2))
        
        # 初始化后代
        offspring1 = [-1] * size
        offspring2 = [-1] * size
        
        # 复制交叉点之间的部分
        for i in range(cxpoint1, cxpoint2):
            offspring1[i] = parent1[i]
            offspring2[i] = parent2[i]
        
        # 处理交叉点之外的基因
        for i in range(size):
            if offspring2[i] == -1:
                value = parent1[i]
                while cxpoint1 <= parent2.index(value) < cxpoint2:
                    value = parent1[parent2.index(value)]
                offspring2[i] = value
                
            if offspring1[i] == -1:
                value = parent2[i]
                while cxpoint1 <= parent1.index(value) < cxpoint2:
                    value = parent2[parent1.index(value)]
                offspring1[i] = value
        
        return Individual(offspring1)

    def mutation(self, individual):
        random_number = random.random()
        if random_number < self.mutation_rate:
            length = len(individual.genes)
            i, j = random.sample(range(length), 2)
            individual.genes[i], individual.genes[j] = individual.genes[j], individual.genes[i]
        return individual

    def run(self):
        population = self.generate_initial_population()

        for generation in range(self.generations_num):
            # 选择
            population.sort(key=lambda x: x.fitness, reverse=True)
            selected_population = population[:self.population_size // 2]

            # 交叉和变异
            # new_population = []
            new_population = population[:self.population_size // 2]


            while len(new_population) < self.population_size:
                parent1, parent2 = random.sample(selected_population, 2)
                child = self.pmx_crossover(parent1.genes, parent2.genes)
                self.mutation(child)
                new_population.append(child)

            population = new_population

        # 输出最佳个体
        population.sort(key=lambda x: x.fitness, reverse=True)
        best_individual = population[0]
        print("Best individual:", best_individual.genes)
        print("fitness:", best_individual.fitness)
        return best_individual

# # 测试
sum_fit = 0
for _ in range(10):
    ga = GeneticAlgorithm(generarions_num=100, population_size=50, chromosome_length=30, mutation_rate=0.1)
    best_individual = ga.run()
    sum_fit += best_individual.fitness
print("sum_fitness:{}".format(sum_fit))



# import random

# # TARGET_SEQ = [5, 6, 8, 7, 9, 2, 1, 0, 4, 3]
# def generate_individual(length):
#     original_list = list(range(0, length))
#     random.shuffle(original_list)
#     return original_list


# def evaluate_fitness(individual):
#     # 计算适应度，这里简单假设排序后的基因与目标序列越接近，适应度越高
#     target_sequence = sorted(individual)
#     fitness = sum(1 for i, j in zip(individual, target_sequence) if i == j)
#     return fitness


# def pmx_crossover(parent1, parent2):
#     size = len(parent1)

#     cxpoint1, cxpoint2 = sorted(random.sample(range(size), 2))
    
#     # 初始化后代
#     offspring1 = [-1] * size
#     offspring2 = [-1] * size
    
#     # 复制交叉点之间的部分
#     for i in range(cxpoint1, cxpoint2):
#         offspring1[i] = parent1[i]
#         offspring2[i] = parent2[i]
    
#     # 处理交叉点之外的基因
#     for i in range(size):
#         if offspring2[i] == -1:
#             value = parent1[i]
#             while cxpoint1 <= parent2.index(value) < cxpoint2:
#                 value = parent1[parent2.index(value)]
#             offspring2[i] = value
            
#         if offspring1[i] == -1:
#             value = parent2[i]
#             while cxpoint1 <= parent1.index(value) < cxpoint2:
#                 value = parent2[parent1.index(value)]
#             offspring1[i] = value
    
#     return offspring1, offspring2


# def mutate(individual):
#     length = len(individual)
#     i, j = random.sample(range(length), 2)
#     individual[i], individual[j] = individual[j], individual[i]
#     return individual


# def genetic_algorithm(population_size, chromosome_length, generations):
#     population = [generate_individual(chromosome_length) for _ in range(population_size)]
#     for generation in range(generations):
#         new_population = []
#         while len(new_population) < population_size:
#             parent1 = random.choice(population)
#             parent2 = random.choice(population)
#             child1, child2 = pmx_crossover(parent1, parent2)
#             child1 = mutate(child1)
#             child2 = mutate(child2)
#             new_population.append(child1)
#             new_population.append(child2)
#         population = new_population
#     best_individual = max(population, key=evaluate_fitness)
#     return best_individual

# def test_algorithm():
#     parent1 = generate_individual(10)
#     parent2 = generate_individual(10)
#     fitness1 = evaluate_fitness(parent1)
#     fitness2 = evaluate_fitness(parent2)
#     parent1 = mutate(parent1)
#     child1, child2 = pmx_crossover(parent1, parent2)
#     child1_fitness = evaluate_fitness(child1)
#     child2_fitness = evaluate_fitness(child2)

#     print('test')

# # test_algorithm()
# chromosome_length = 10
# population_size = 500
# generations = 1000
# best_individual = genetic_algorithm(population_size, chromosome_length, generations)
# print("Best individual:", best_individual)
# print("Fitness", evaluate_fitness(best_individual))
