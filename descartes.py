import py01ai
import numpy as np


n, d = 10000, 128
X = np.random.randn(n, d)

index = py01ai.FNGIndex(metric="square_l2", dimension=dimension))
index.init(count=1000000, M=32, S=1, L=200)
index.add_vector(X)

v = np.random.randn(1, 128)
results = index.search(query=v, topk=10)
print(results)

