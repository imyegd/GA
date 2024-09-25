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

# class Circle:
#     def __init__(self, radius):
#         self._radius = [radius, 10]

#     @property
#     def radius(self):
#         return self._radius
    
#     @property
#     def area(self):
#         return 3.14 * self._radius[0] * self._radius[0]
    
#     @radius.setter
#     def radius(self, value):
#         if value < 0:
#             raise ValueError("Radius cannot be negative.")
#         self._radius = [value]

# c = Circle(-2)
# print(c.area)
# print(c.radius)
# c.radius[0] = -20
# print(c.radius)
# print(c._radius)

import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# # 生成一些随机日期
# np.random.seed(42)
# date_range = pd.date_range(start='2023-01-01', end='2024-09-25')
# dates1 = np.random.choice(date_range, size=10)
# dates2 = np.random.choice(date_range, size=10)

# # 创建 DataFrame
# df = pd.DataFrame({'date1': dates1, 'date2': dates2})

# # 将 DataFrame 保存为 xls 文件
# df.to_excel('two_columns_dates.xls', index=False)

# df = pd.read_excel('two_columns_dates.xlsx')
# print(df)




import pandas as pd

# 读取 xls 文件
df = pd.read_excel('two_columns_dates.xlsx')

# 假设两列日期的列名分别为 'date1' 和 'date2'
def calculate_loss(row):
    date1 = row['date1']
    date2 = row['date2']
    if date1 < date2:
        return (date2 - date1).days
    else:
        return (date1 - date2).days * 100

# 应用函数计算损失
df['loss'] = df.apply(calculate_loss, axis=1)

# 打印结果
print(df['loss'].sum())


# import pandas as pd
# import numpy as np
# from datetime import datetime, timedelta

# # 生成一些随机日期
# np.random.seed(42)
# date_range = pd.date_range(start='2023-01-01', end='2024-09-25')
# dates1 = np.random.choice(date_range, size=10)
# dates2 = np.random.choice(date_range, size=10)

# # 创建 DataFrame
# df = pd.DataFrame({'date1': dates1, 'date2': dates2})

# # 定义序列 seq
# # seq = np.arange(1, 11)
# seq = [6, 7, 8, 9, 10, 1, 2, 3, 4, 5]
# print(df)
# # 根据 seq 对 row['date1']进行排序
# new_df = df.iloc[np.argsort(df['date1'].map(lambda x: seq[np.where(df['date1'].values == x)[0][0]]))].reset_index(drop=True)
# merged_df = pd.DataFrame({'date1': new_df['date1'], 'date2': df['date2']})
# # 打印结果
# print(merged_df)

# import pandas as pd
# import numpy as np

# # 生成一些随机日期
# np.random.seed(42)
# date_range = pd.date_range(start='2023-01-01', end='2024-09-25')
# dates1 = np.random.choice(date_range, size=10)
# dates2 = np.random.choice(date_range, size=10)

# # 创建 DataFrame
# df = pd.DataFrame({'date1': dates1, 'date2': dates2})

# # 定义序列 seq
# # seq = [2, 1, 3, 4, 5]
# seq = [1, 2, 3, 4, 5]

# # 创建一个新的索引列表，根据 seq 对原始索引进行重新排序
# new_index_order = [df.index[i - 1] if i > 0 else df.index[0] for i in seq]

# # 使用新的索引顺序重新排列 DataFrame
# new_df = df.iloc[new_index_order]

# # 打印结果
# print(new_df)