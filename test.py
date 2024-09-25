# import random

# def pmx_crossover(parent1, parent2):
#     # 定义交叉点
#     size = len(parent1)
#     # cxpoint1 = random.randint(0, size)
#     # cxpoint2 = random.randint(0, size - 1)
#     # if cxpoint2 >= cxpoint1:
#     #     cxpoint2 += 1
#     # else:  # Swap the two cx points
#     #     cxpoint1, cxpoint2 = cxpoint2, cxpoint1

#     cxpoint1, cxpoint2 = sorted(random.sample(range(size), 2))
#     print(cxpoint1, cxpoint2)
    
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

# # 示例用法

# def generate_individual(length):
#     original_list = list(range(0, length))
#     random.shuffle(original_list)
#     return original_list

# parent1 = generate_individual(10)
# parent2 = generate_individual(10)

# offspring1, offspring2 = pmx_crossover(parent1, parent2)
# print("Offspring 1:", offspring1)
# print("Offspring 2:", offspring2)

class Circle:
    def __init__(self, radius):
        self._radius = [radius, 10]

    @property
    def radius(self):
        return self._radius
    
    @property
    def area(self):
        return 3.14 * self._radius[0] * self._radius[0]
    
    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative.")
        self._radius = [value]

c = Circle(-2)
print(c.area)
print(c.radius)
c.radius[0] = -20
print(c.radius)
print(c._radius)