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

## 3. **Team members**
The team members come from 01AI: Xiaoming Peng, Gaofei Wang

