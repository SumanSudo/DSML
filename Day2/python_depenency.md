# Python Dependency Management Cheat Sheet

## Virtual Environment (`virtualenv`)

### Install

```bash
pip install virtualenv
```

### Create

```bash
virtualenv myenv
```

### Activate

**Windows**

```powershell
myenv\Scripts\Activate.ps1
```

**macOS / Linux**

```bash
source myenv/bin/activate
```

### Install Packages

```bash
pip install requests
pip install numpy pandas
```

### List Installed Packages

```bash
pip list
```

### Export Dependencies

```bash
pip freeze > requirements.txt
```

### Install from `requirements.txt`

```bash
pip install -r requirements.txt
```

### Deactivate

```bash
deactivate
```

### Remove Environment

**Windows (PowerShell)**

```powershell
Remove-Item -Recurse -Force myenv
```

**Windows (CMD)**

```cmd
rmdir /s myenv
```

**macOS / Linux**

```bash
rm -rf myenv
```

---

## Conda Environment

### Create

```bash
conda create --name myenv python=3.13
```

### Activate

```bash
conda activate myenv
```

### Install Packages

```bash
conda install numpy
```

Install from the `conda-forge` channel:

```bash
conda install -c conda-forge scikit-learn
```

### Export Environment

```bash
conda env export > environment.yml
```

### Create from `environment.yml`

```bash
conda env create -f environment.yml
```

### Update a Package

```bash
conda update numpy
```

### List Environments

```bash
conda env list
```

### Remove Environment

```bash
conda env remove --name myenv
```

---

## `requirements.txt` vs `environment.yml`

| `requirements.txt`                         | `environment.yml`                                                    |
| ------------------------------------------ | -------------------------------------------------------------------- |
| Used with `pip`                            | Used with `conda`                                                    |
| Stores Python packages only                | Stores Python packages, Conda packages, channels, and Python version |
| Generate: `pip freeze > requirements.txt`  | Generate: `conda env export > environment.yml`                       |
| Install: `pip install -r requirements.txt` | Install: `conda env create -f environment.yml`                       |

---

## Typical Workflow

### Using `virtualenv`

```text
Create Project
      ↓
Create Virtual Environment
      ↓
Activate Environment
      ↓
Install Packages
      ↓
Develop Project
      ↓
pip freeze > requirements.txt
      ↓
Share / Push to GitHub
      ↓
pip install -r requirements.txt
```

### Using `conda`

```text
Create Environment
      ↓
Activate Environment
      ↓
Install Packages
      ↓
Develop Project
      ↓
conda env export > environment.yml
      ↓
Share / Push to GitHub
      ↓
conda env create -f environment.yml
```
