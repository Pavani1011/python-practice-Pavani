# Python – Installation and Development Environment

## 1. What Is a Development Environment?

**Definition:**

A development environment is a setup of tools and software that developers use to write, run, test and debug programs.

### Main components

- Python interpreter
- IDE or code editor
- Terminal
- Python packages
- Virtual environment

---

## 2. What Is the Python Interpreter?

**Definition:**

The Python interpreter is software that executes Python code.

### Example

```python
print("Hello Pavani")
```

**Output:**

```text
Hello Pavani
```

### Explanation

1. We write Python code.
2. The interpreter processes and executes the code.
3. The output is displayed.

### Check the Python version

**Mac command:**

```bash
python3 --version
```

**Example output:**

```text
Python 3.13.15
```

---

## 3. What Is an IDE?

**Definition:**

IDE stands for **Integrated Development Environment**.

An IDE is an application that provides tools to write, run, test and debug code in one place.

### Popular Python development tools

| Tool | Description |
|---|---|
| PyCharm | A Python-focused IDE with debugging and code completion features |
| VS Code | A lightweight code editor that supports Python through extensions |
| Jupyter Notebook | An interactive environment for writing and executing code in cells |
| Google Colab | A browser-based notebook environment for running Python code |

### PyCharm

PyCharm provides:
- Code editor
- Code completion
- Run and debug tools
- Project management
- Python interpreter configuration

---

## 4. What Is a Terminal?

**Definition:**

A terminal is a text-based interface where users enter commands to interact with their computer.

### Example commands on Mac

Check Python version:

```bash
python3 --version
```

Check the current directory:

```bash
pwd
```

List files and folders:

```bash
ls
```

Change directory:

```bash
cd folder_name
```

---

## 5. What Is a Virtual Environment?

**Definition:**

A virtual environment is an isolated Python environment used to install project-specific packages without affecting other projects.

### Why do we use virtual environments?

Imagine two projects:

- Project A requires Pandas version 2.
- Project B requires Pandas version 3.

Using separate virtual environments helps prevent package version conflicts.

### Virtual environment lifecycle

#### Step 1: Create a virtual environment

**Mac:**

```bash
python3 -m venv my_env
```

This creates an environment named `my_env`.

#### Step 2: Activate the environment

**Mac:**

```bash
source my_env/bin/activate
```

After activation, the terminal prompt usually displays the environment name.

Example:

```text
(my_env) pav@MacBook-Air %
```

#### Step 3: Deactivate the environment

```bash
deactivate
```

This exits the active virtual environment.

### Important note

PyCharm can automatically create a virtual environment for a project.

A common environment folder name is `.venv`.

---

## 6. What Is PIP?

**Definition:**

PIP is Python's package installer. It is used to install and manage additional Python packages.

A package is reusable code that provides additional functionality.

### Essential PIP commands

| Command | Description |
|---|---|
| `pip install pandas` | Installs Pandas |
| `pip uninstall pandas` | Removes Pandas |
| `pip list` | Lists installed packages |
| `pip freeze` | Displays installed packages with versions |
| `pip show pandas` | Displays information about Pandas |
| `pip install -r requirements.txt` | Installs packages listed in a requirements file |

### Example: Install Pandas

```bash
python3 -m pip install pandas
```

### Example: Check installed packages

```bash
python3 -m pip list
```

### Example: Display package versions

```bash
python3 -m pip freeze
```

---

## 7. What Is a Python Package?

**Definition:**

A Python package is a collection of reusable Python modules that provide related functionality.

### Examples

| Package | Purpose |
|---|---|
| Pandas | Data manipulation and analysis |
| NumPy | Numerical computing |
| Matplotlib | Data visualization |
| Requests | Making HTTP requests |

---

## 8. What Is requirements.txt?

**Definition:**

`requirements.txt` is a text file commonly used to list the Python packages and versions required by a project.

### Example

```text
pandas==3.0.5
numpy==2.3.3
```

### Generate requirements.txt

```bash
python3 -m pip freeze > requirements.txt
```

This saves the installed packages and their versions into a file.

### Install packages from requirements.txt

```bash
python3 -m pip install -r requirements.txt
```

This installs the listed packages into the active Python environment.

---

## 9. How Python Development Tools Work Together

1. **IDE:** Write and edit Python code.
2. **Python interpreter:** Executes the code.
3. **Virtual environment:** Isolates project-specific packages.
4. **PIP:** Installs and manages packages.
5. **Terminal:** Runs commands and starts programs.

### Example workflow

```text
Create a Python project
          |
          v
Set up a virtual environment
          |
          v
Install required packages
          |
          v
Write Python code in PyCharm
          |
          v
Run code using the interpreter
          |
          v
View and verify output
```

---

## 10. Practical Commands for Mac

| Task | Command |
|---|---|
| Check Python version | `python3 --version` |
| Check PIP version | `python3 -m pip --version` |
| Create environment | `python3 -m venv my_env` |
| Activate environment | `source my_env/bin/activate` |
| Deactivate environment | `deactivate` |
| Install Pandas | `python3 -m pip install pandas` |
| List packages | `python3 -m pip list` |
| Save package versions | `python3 -m pip freeze > requirements.txt` |

---

## 11. Interview Questions

**Q1. What is an IDE?**

An IDE is an Integrated Development Environment that provides tools for writing, running, testing and debugging programs.

**Q2. What is a Python interpreter?**

A Python interpreter is software that executes Python code.

**Q3. What is a virtual environment?**

A virtual environment is an isolated Python environment used to manage project-specific packages.

**Q4. Why do we use virtual environments?**

To isolate project dependencies and avoid package version conflicts between projects.

**Q5. What is PIP?**

PIP is Python's package installer, used to install and manage packages.

**Q6. What is the difference between an IDE and a Python interpreter?**

An IDE provides a development workspace and tools. An interpreter executes Python code.

**Q7. What is requirements.txt?**

It is a file that lists the packages and versions required by a Python project.

**Q8. What is the difference between PyCharm and Jupyter Notebook?**

PyCharm is a full IDE designed for software development. Jupyter Notebook is an interactive environment that executes code in individual cells, commonly used for data exploration and analysis.

---

## 12. Quick Revision

- **Development environment:** Tools and software used to develop programs.
- **Python interpreter:** Executes Python code.
- **IDE:** Provides tools for writing, running and debugging code.
- **Terminal:** Interface for entering system commands.
- **Virtual environment:** Isolated space for project dependencies.
- **PIP:** Installs and manages Python packages.
- **Package:** Reusable code that adds functionality.
- **requirements.txt:** Lists project dependencies and their versions.
- **`.venv`:** A common name for a project's virtual environment folder.
