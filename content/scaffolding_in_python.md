Title: Scaffolding for Data Projects in Python
Date: 2024-07-04
Modified: 2024-07-18
Category: Articles
Tags: python, programming, software development, scaffolding
Slug: scaffolding-in-python
Authors: Juan José Farina, Tomás Vázquez
Summary: This article is a destiled version of the presentation "Scaffolding for Data Projects in Python" by Juan José Farina and Tomás Vázquez. It provides an overview of scaffolding in Python, including the definition of scaffolding, step-by-step instructions for setting up a Python project, and the use of Cookiecutter for scaffolding.
Keywords: scaffolding, python, development, engineering, pip, pipx, pipenv, cookiecutter

---

#### 1. Introduction
#### 2. Prerequisites
#### 3. Definition of Scaffolding
#### 4. Step-by-Step: How to Set Up a Python Project
#### 5. Using Cookiecutter for Scaffolding
#### 6. Bibliography

---

## Scaffolding for Data Projects in Python

### Introduction
This article introduces the concept of Scaffolding and its application within Data projects using Python. It highlights the importance of the topic and addresses key concepts.

We will follow a hands-on approach, building a Python project step-by-step, then using a Scaffolding tool to enable reuse.

After following this, you'll be able to make more informed decisions on creating Python projects and using Scaffolding tools to quickly focus on developing solutions.

### Prerequisites
For the purpose of this article, we will use the following tools:

- Visual Studio Code
- Python
- Pip

A basic understanding of each of them is required.

#### Preparation
1. Open Visual Studio Code in an empty directory.
2. Create a folder named “template”.
3. Open the terminal.
4. Verify Python installation by running `python -V`.
5. Verify Pip installation by running `pip --version`.

### Definition of Scaffolding

#### What is Scaffolding?
A scaffold is a structure used in construction to support the building process. Exactly the same is true for Sofrware Development, where scaffolding is an important concept that involves quickly setting up project structures to start development. This is useful because projects often share certain conventions in their structure and requirements.

#### Scaffolding Tools
- **PyScaffold:** Automates the creation of initial project structures with basic configurations for testing and distribution, using customizable templates.
- **Cookiecutter:** Generates projects from Jinja2 templates, allowing dynamic and complex customization. Ideal for projects with specific configurations and advanced integrations.
- **Kedro:** A framework for data pipelines in Python that provides an organized structure and tools for data management and reproducible data science experiments.

### Step-by-Step: How to Set Up a Python Project

#### Project Types
Each type of python project has its own requirements and structure. The most common types are:

- Library or CLI
- Data
- Web

#### Layout
There are three basic type of layouts:
- Flat: all code files are located in the root of the project.
- Src: all code files are located in a `src` folder.
- Package: all code files are located in a folder named after the project which contains a `__init__.py` file that initializes the directory as a Python package.

Starting with a package layout:
- Within the `template` folder, create a new folder `template`.
- Inside this folder, create two empty files: `__init__.py` and `main.py`.
- Back in the first `template` folder, create a new folder `tests`.
- Inside this folder, create an `__init__.py` file.

#### Project Configuration
One of the best ways to configure a modern Python project is through a `pyproject.toml` file, created in the project root (`template`).

Here’s a basic example to start with (refer to the documentation for all possible configurations):

```toml
[build-system]
requires = ["setuptools" >= 61.0.0"]
build-backend = "setuptools.build_meta"

[project]
name = "template"
version = "0.0.1"
authors = [
    {name = "Juan José Farina", email = "juanjosefarina@gmail.com"},
    {name = "Tomás Vázquez", email = "tomas.vazquez@gmail.com"},
]
readme = "README.md"
```

#### Dependency Management
For this we'll use a tool called `pipenv`, which creates a virtual environment for dependencies while fixing their versions and configuring execution scripts.

- Install pipenv using pip in the terminal: `pip install pipenv`.
- Enter the `template` (parent) folder and run `pipenv install`.

Pipenv will create a virtual environment and two new files: `Pipfile` and `Pipfile.lock`.

From now on, to install any dependency, run `pipenv install <dependency>`. For development dependencies, run `pipenv install --dev <dependency>`.

*It's a good practice to check the `Pipfile.lock` file to find out the installed version of each dependency and pin it in the `Pipfile`.*

#### Additional Files
Now create three more files in the project root: `.gitignore`, `MANIFEST.in`, and `README.md`:

- `.gitignore`: Tells git which files to ignore, useful for files that shouldn't be in the repository (e.g., `build/` and `dist/`).
- `MANIFEST.in`: Controls the files included or excluded in the package distribution (e.g., include `Pipfile` with `include Pipfile`).
- `README.md`: The first file a developer should see in a repository, containing important project information and instructions. `.md` stands for markdown.

#### Initializing Git
Git repositories are essential for tracking project changes. To initialize a git repository you can run `git init` in the terminal standing in the root of the project. Afterwards, you can already use some basic git commands:

- Use `git status` to check the repository status.
- Add new files with `git add .`.
- Commit changes with `git commit -m "<commit-message>"`.

*If you have a remote repository on GitHub or Azure DevOps, link your “local repository” and push changes with `git push`.*

#### Pre-commit
Finally, we can introduce an extra tool to improve code quality:

- **Pre-commit:** this helps maintain code quality by notifying and fixing format errors, syntax issues, typing errors, duplicate code, etc., before a commit. You can also configure other hooks to run pre-push.

Install pre-commit by running `pip install pre-commit` in the terminal.

To verify pre-commit installation you can run `pre-commit --version`.

Now create a `.pre-commit-config.yaml` file for configuring pre-commit to your preference. 

You can start a basic `.pre-commit-config.yaml` with the following lines:

```yaml
repos:
-   repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v3.2.0
    hooks:
    -   id: trailing-whitespace
    -   id: end-of-file-fixer
    -   id: check-yaml
    -   id: check-added-large-files
```

*`Note`: You can also run `pre-commit sample-config` in the terminal and copy the output.*

Execute `pre-commit install` to apply configurations.

### Using Cookiecutter for Scaffolding
Cookiecutter is a command-line tool for creating projects from templates called cookiecutters. You can install it running `pip install cookiecutter`.

Cookiecutter can use both remote (hosted on git repositories) and local templates. Let's start with a remote template:

#### Using Cookiecutter with a Remote Template
Standing in the parent directory of the previously created project, run in the terminal:

```bash
cookiecutter https://github.com/drivendataorg/cookiecutter-data-science -c v1
```

Enter the requested details, and you will have a complete project created immediatelly.

#### Using Cookiecutter with a Local Template
Let's modify our `template` project to be a Cookiecutter template. Place all your root files and folders inside a folder named `{{ cookiecutter.app_slug }}` and rename the internal `template` folder to `{{ cookiecutter.app_slug }}` too.

You should end with a directory structure like this:

```
template
├── {{ cookiecutter.app_slug }}
|   ├── {{ cookiecutter.app_slug }}
|   |   ├── __init__.py
|   |   ├── main.py
|   ├── tests
|   |   ├── __init__.py
|   ├── .gitignore
|   ├── MANIFEST.in
|   ├── Pipfile
|   ├── Pipfile.lock
|   ├── pyproject.toml
|   ├── README.md
├── cookiecutter.json (we'll create this file in the next step)
```

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
Use the declared variables in `cookiecutter.json` within your `pyproject.toml` file:

```toml
[build-system]
requires = ["setuptools" >= 61.0.0"]
build-backend = "setuptools.build_meta"

[project]
name = "{{ cookiecutter.app_slug }}"
version = "0.0.1"
authors = [
    {name = "{{ cookiecutter.app_author_name }}", email = "{{ cookiecutter.app_author_email }}"}
]
readme = "README.md"
```

Use Cookiecutter with the full path to the directory containing `cookiecutter.json`:

```bash
cookiecutter path/to/template
```

### Congratulations!
Your project should be generated ready for development!

## Bibliography
- Wikipedia Definition: [Wikipedia scaffold definition](https://en.wikipedia.org/wiki/Scaffold_(programming))
- Python Documentation:
    - [Python packaging](https://packaging.python.org/en/latest/overview/)
    - [Python virtualenvs](https://docs.python-guide.org/dev/virtualenvs/)
    - [Python pyproject.toml](https://packaging.python.org/en/latest/specifications/pyproject-toml/)
    - [Python layouts](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/)
- Cookiecutter:
    - [Cookiecutter documentation](https://cookiecutter.readthedocs.io/en/stable/)
    - [Cookiecutter templates](https://www.cookiecutter.io/templates)
    - [Cookiecutter data-science template](https://cookiecutter-data-science.drivendata.org/)
