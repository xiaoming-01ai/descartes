import py01ai
import numpy as np


n, d = 10000, 128
X = np.random.randn(n, d)

index = py01ai.FNGIndex(metric="square_l2", dimension=d))
index.init(count=n, m=32, s=1, l=200)
index.add_vector(input=X)

v = np.random.randn(1, 128)
results = index.search(query=v, topk=10)
print(results)

