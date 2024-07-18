Title: Scaffolding in Python
Date: 2024-07-13
Modified: 2024-07-13
Category: Articles
Tags: python, development
Slug: scaffolding-in-python
Author: Juan José Farina
Summary: An article about my daily life as of now
Keywords: scaffolding, python, development, engineering, pip, pipx, pipenv, cookiecutter

# Scaffolding for Data Projects in Python

*Presented by Juan José Farina and Tomás Vázquez*  
*4th July 2024*

---

## 1. Introduction
## 2. Prerequisites
## 3. Definition of Scaffolding
## 4. Step-by-Step: How to Set Up a Python Project
## 5. Using Cookiecutter for Scaffolding
## 6. Bibliography

---

## Scaffolding for Data Projects in Python

### Introduction

**Presenters:**  
- Tomás Vázquez, MLOps Associate  
  Email: 
- Juan José Farina, MLOps Associate  
  Email: 

#### Idea
This presentation introduces the concept of Scaffolding and its application within Data projects using Python. It highlights the importance of the topic and addresses key concepts.

#### Methodology
We will follow a hands-on approach, building a Python project step-by-step, then using a Scaffolding tool to enable reuse. Time will be taken to address any issues encountered at each step.

#### Objectives
Equip attendees to make informed decisions on creating Python projects and using Scaffolding tools to quickly focus on developing solutions.

### Prerequisites

#### Necessary Tools
*Note: For any questions or issues with downloading or using these tools, feel free to ask.*
- Visual Studio Code
- Python
- Pip

#### Preparation
1. Open Visual Studio Code in an empty directory.
2. Create a folder named “template”.
3. Open the terminal.
4. Verify Python installation.
5. Verify Pip installation.

### Definition of Scaffolding

#### What is Scaffolding?
In software development, scaffolding is an important concept that involves quickly setting up project structures to start development. This is useful because projects often share certain conventions in their structure and requirements.

#### Scaffolding Tools
- **PyScaffold:** Automates the creation of initial project structures with basic configurations for testing and distribution, using customizable templates.
- **Cookiecutter:** Generates projects from Jinja2 templates, allowing dynamic and complex customization. Ideal for projects with specific configurations and advanced integrations.
- **Kedro:** A framework for data pipelines in Python that provides an organized structure and tools for data management and reproducible data science experiments.

### Step-by-Step: How to Set Up a Python Project

#### Project Types
- Library or CLI
- Data
- Web

#### Layout
Flat vs Src vs Package

Starting with a package layout:
- Within the `template` folder, create a new folder `template`.
- Inside this folder, create two empty files: `__init__.py` and `main.py`.
- Back in the first `template` folder, create a new folder `tests`.
- Inside this folder, create an `__init__.py` file.

*The `__init__.py` files are needed to initialize the directory as a Python package.*

#### Project Configuration
The correct way to configure a Python project is through a `pyproject.toml` file, created in the project root (`template`).

Here’s a basic example to start with; refer to the documentation for all possible configurations.

#### Dependency Management
We'll use a tool called `pipenv`, which creates a virtual environment for dependencies while fixing their versions and configuring execution scripts.
- Install pipenv using pip in the terminal.
- Enter the `template` (parent) folder and run `pipenv install`.

Pipenv creates a virtual environment and two new files: `Pipfile` and `Pipfile.lock`.

*From now on, to install any dependency, run `pipenv install <dependency>`. For development dependencies, run `pipenv install --dev <dependency>`.*

#### Additional Files
- `.gitignore`: Tells git which files to ignore, useful for files that shouldn't be in the repository (e.g., `build/` and `dist/`).
- `MANIFEST.in`: Controls the files included or excluded in the package distribution (e.g., include `Pipfile` with `include Pipfile`).
- `README.md`: The first file a developer should see in a repository, containing important project information and instructions. `.md` stands for markdown. Create a `README.md` for your project.

*Now create three more files in the project root: `.gitignore`, `MANIFEST.in`, and `README.md`.*

#### Initializing Git
Git repositories are essential for tracking project changes.
- Initialize a repository with `git init` in the terminal.
- Use `git status` to check the repository status.
- Add new files with `git add .`.
- Commit changes with `git commit -m "<commit-message>"`.

*If you have a remote repository on GitHub or Azure DevOps, link your “local repository” and push changes with `git push`, though this won’t be necessary for this presentation.*

#### Extra Tool: Pre-commit
Introduce an extra tool to improve code quality:
- **Pre-commit:** Helps maintain code quality by notifying and fixing format errors, syntax issues, typing errors, duplicate code, etc., before a commit.

Install pre-commit by running `pip install pre-commit` in the terminal.

*Verify pre-commit installation with `pre-commit --version`.*

Create a `.pre-commit-config.yaml` file for configuring pre-commit to your preference. Add the following lines:

`IMPORTANT NOTE`: Execute `pre-commit sample-config` in the terminal and copy the output.

Execute `pre-commit install` to apply configurations.

### Using Cookiecutter for Scaffolding

#### Using Cookiecutter for Scaffolding
First, let's clarify what Cookiecutter is: a command-line tool for creating projects from templates called cookiecutters.

#### Installation
*Preliminary step: Install pipx to install Cookiecutter and run it in an isolated environment.*  
Run in the terminal: `pip install pipx`.

Once installed, execute: `pipx run cookiecutter`.

Cookiecutter can use both remote (hosted on git repositories) and local templates. Let's start with a remote template:

#### Using Cookiecutter with a Remote Template
Run in the terminal:

```bash
cookiecutter https://github.com/drivendataorg/cookiecutter-data-science -c v1
```


Enter the requested details, and you will have a complete project created.

#### Using Cookiecutter with a Local Template
First, modify your `template` project to be a Cookiecutter template. Place your project inside a folder named `{{ cookiecutter.app_slug }}` and rename the internal `template` folder accordingly.

Create a `cookiecutter.json` file at the same level as the first folder, with this content:

```json
{
 "app_name": "Example App",
 "app_slug": "{{ cookiecutter.app_name|lower|replace(' ', '-')|replace('-', '_') }}",
 "app_author_name": "{{ 'Your full name' }}",
 "app_author_email": "{{ 'your_email@pwc.com' }}"
}
```

#### Final Details
Use the declared variables in `cookiecutter.json` within your `pyproject.toml` file.

Use Cookiecutter with the full path to the directory containing `cookiecutter.json`.

### Congratulations!
Your project should be generated as described.

## Bibliography
- Wikipedia Definition: wikipedia project definition
- Python Documentation:
    - Python Packaging
    - Python virtualenvs
    - Python pyproject.toml
    - Python layouts
- Cookiecutter:
    - Cookiecutter documentation
    - Cookiecutter templates
    - Cookiecutter data-science template
