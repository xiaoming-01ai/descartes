# descartes

# Introduction

#### Nearest neighbor search algorithm descartes, based on fng, providing Python API.

# Install & Usage

## 1. **Installation**

### 1.1 Configure environment dependencies (recommended in the Docker container created by the Ubuntu image)
 ```bash
sudo apt update && sudo apt install -y git cmake g++ python3 python3-setuptools python3-pip libblas-dev liblapack-dev '''
```

### 1.2 Download code

```bash
git clone https://github.com/xiaoming-01ai/descartes.git
```

### 1.3 Configuration & installation

```bash
pip3 install descartes/descartes-*-linux_x86_64.whl
```

## 2. **Usage**

```python
python3 descartes.py
```

### The following describes the algorithm execution logic of descartes.py in steps

### 2.1 Data load
#### Method 1: Randomly generate data

```python
n, d = 10000, 128
X = np.random.randn(n, d)
```

#### Method 2: Load data from dataset (sift_base.fvecs as an example)

```python
def ivecs_read(fname):
    a = np.fromfile(fname, dtype='int32')
    d = a[0]
    return a.reshape(-1, d + 1)[:, 1:].copy()
def fvecs_read(fname):
    return ivecs_read(fname).view('float32')

X = fvecs_read("sift_base.fvecs")
```

### 2.2 Build Index

```python
index = py01ai.FNGIndex(metric="square_l2", dimension=dimension))
index.init(count=1000000, m=32, s=1, l=200)
index.add_vector(input=X)
```

### 2.3 Search
```python
v = np.random.randn(1, 128)
results = index.search(query=v, topk=10)
print(results)
```

## 3. **Performance**

glove-25-angular
-----------------
![glove-25-angular](https://github.com/xiaoming-01ai/descartes/blob/main/results/glove-25-angular_10_angular.png)

glove-50-angular
-----------------
![glove-50-angular](https://github.com/xiaoming-01ai/descartes/blob/main/results/glove-50-angular_10_angular.png)

glove-100-angular
-----------------
![glove-100-angular](https://github.com/xiaoming-01ai/descartes/blob/main/results/glove-100-angular_10_angular.png)

glove-200-angular
-----------------
![glove-200-angular](https://github.com/xiaoming-01ai/descartes/blob/main/results/glove-200-angular_10_angular.png)

sift-128-euclidean
------------------
![glove-100-angular](https://github.com/xiaoming-01ai/descartes/blob/main/results/sift-128-euclidean_10_euclidean.png)
fashion-mnist-784-euclidean
---------------------------

![fashion-mnist-784-euclidean](https://github.com/xiaoming-01ai/descartes/blob/main/results/fashion-mnist-784-euclidean_10_euclidean.png)

nytimes-256-angular
-------------------

![nytimes-256-angular](https://github.com/xiaoming-01ai/descartes/blob/main/results/nytimes-256-angular_10_angular.png)

gist-960-euclidean
-------------------

![gist-960-euclidean](https://github.com/xiaoming-01ai/descartes/blob/main/results/gist-960-euclidean_10_euclidean.png)


## 4. **Team members**
The team members come from 01AI: Xiaoming Peng, Gaofei Wang

