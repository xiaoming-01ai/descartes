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

### 1.3 File copy & Set permissions

```bash
sudo cp descartes/lib/* /usr/local/lib/
sudo cp descartes/bin/* /usr/local/bin/
sudo chmod a+x /usr/local/bin/* && chmod a+x descartes/*
```

### 1.4 Configuration & installation

```bash
ldconfig
pip3 install descartes/py01ai-*-linux_x86_64.whl
```

## 2. **Usage**

### The following describes the algorithm execution logic of descartes.py in steps

### 2.1 Data load

### 2.2 Build Index (Divided into FNG, QG)

#### 2.2.1 Build FNG

#### 2.2.3 Build QG


### 2.3 Search

## 3. **Team members**
The team members come from 01AI: Xiaoming Peng, Gaofei Wang

