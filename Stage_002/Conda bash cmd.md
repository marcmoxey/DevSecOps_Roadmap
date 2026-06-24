
# 🟢 Setup / Check Conda

```
conda --version
```

```
conda info
```

---

# 🟦 Environment Management

### List environments

```
conda env list
```

```
conda info --envs
```

### Create environment

```
conda create -n [name]
```

### Create with Python version

```
conda create -n [name] python=3.12
```

### Create with packages

```
conda create -n [name] python=3.12 numpy pandas
```

### Create environment in folder

```
conda create -p ./env python=3.12
```

---

# 🟣 Activate / Exit Environment

### Activate

```
conda activate abspython
```

### Deactivate

```
conda deactivate
```

---

# 🟡 Package Management

### Install package

```
conda install package_name
```

Example:

```
conda install numpy pandas matplotlib
```

### Install using pip

```
pip install package_name
```

Example:

```
pip install flask requests
```

### List installed packages

```
conda list
```

### Find package

```
conda search package_name
```

---

# 🟠 Update

### Update Conda

```
conda update conda
```

### Update all packages

```
conda update --all
```

### Update one package

```
conda update package_name
```

---

# 🔵 Save / Restore Environments

### Export environment

```
conda env export > environment.yml
```

### Create from file

```
conda env create -f environment.yml
```

### Update from file

```
conda env update -f environment.yml
```

---

# 🔴 Delete / Remove

### Delete environment

```
conda remove -n abspython --all
```

### Delete folder environment

```
conda remove -p ./env --all
```

---

# ⚫ Cleanup

### Clear cache

```
conda clean --all
```

---

# ⭐ Typical Daily Workflow

```
conda activate abspythonconda listconda install package_namepython app.pyconda deactivate
```

---

# 🚀 New Project Workflow

```
conda create -n myproject python=3.12conda activate myprojectconda install numpy pandas jupyterpip install extra-packageconda env export > environment.yml
```
