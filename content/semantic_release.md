Title: Semantic Release
Date: 2023-10-02
Modified: 2024-07-20
Category: Articles
Tags: development, engineering, versioning, vcs, automation, python
Slug: semantic-release
Authors: Juan José Farina, Ezequiel Castaño
Summary: This article is a destiled version of the presentation "Semantic Release" by Juan José Farina and Ezequiel Castaño. It provides an overview of the Semantic Release tool and its benefits for versioning and automation in software development.
Keywords: semantic release, versioning, automation, software development, vcs, python

---

#### 1. Brief Introduction
#### 2. The Problem: Versioning
#### 3. Semantic Release
#### 4. Our Solution
#### 5. Live Demonstration

---

## Brief Introduction
When developing software and dealing with its versioning, a common topic that arises are the Git Branching Strategies.

These are a set of rules that define how branches are created, named, and merged. On this depends how the versioning and deploying of the software will be done too.

One of the most common branching strategies for the last 10 or so years has been GitFlow, which gives you a solid structure for your branches and releases, allowing you to easily manage the versioning of your software.

Although, GitFlow can be confusing and also add too much friction on the release process. It also makes versioning a very manual and tedious process.

An alternative to GitFlow and other branching strategies is Trunk-Based Development. This approach is based on the idea of having a single main branch (sometimes called trunk) and all development work is done on this branch.

Ezequiel came up with a variation to TBD, which is to have two long-lived branches: main and develop. This allows for a more streamlined development process and easier versioning, as well as having a robust CI/CD both for protecting the main branch and for deploying the software.

Yet, it still leaves versioning as a manual and tedious process.

## The Problem: Versioning
Versioning is the process of assigning unique version numbers to unique releases of a computer software (thanks Wikipedia!).

It is a very crucial aspect of software development, as it allows developers to keep track of changes and updates to their software, and also to communicate those changes to users.

When a software changes its APIs in a non-retrocompatible manner, this means another software that depends on it will need to be updated to work with the new version.

And when you have lots of dependencies that are not correctly versioned, it can be easy to fall into a situation called `Dependency Hell`.

## Semantic Versioning
Semantic Versioning is a widely used versioning system that is based on three numbers:

**MAJOR.MINOR.PATCH**

1. **MAJOR** means incompatible API changes
2. **MINOR** means backward compatible functionality
3. **PATCH** means backward compatible bug fixes

### The Good:
The system conveys meaning about the underlying code and what has been modified from one version to the next, and it’s also an industry standard used in many big companies.

### The Bad:
Semantic Versioning alone isn’t enough: it’s still manually updated, and still subjectively decided.

Furthermore, it doesn’t cover up the lack of documentation about changes in every version.

## The Solution: Semantic Releases

Semantic Release is a tool that automates the versioning process and the generation of the changelog.

1. **Enforced commits convention**
   - Using Pre-Commit, Commitizen, and Conventional Commits
2. **Commit parsing and version update**
   - Using Semantic Release and Azure Pipelines
3. **Generation of Changelog**
   - Using Semantic Release
4. **Azure Repo Git Tag generation**
   - Using Azure Pipelines
5. **Updating PR title and description**
   - Using Changelog Parser, Azure Pipelines, and API REST

## Live Demonstration

1. Push a `chore` to update to version `0.0.0`
2. Try to `commit` without using the right convention
3. Push a `fix` and Merge to update to version `0.0.1`
4. Push a `fix` and Merge to update to version `0.0.2`
5. Push a `feat` and Merge to update to version `0.1.0`
6. Push a `fix` and Merge to update to version `0.1.1`
7. Push a `feat!` to update to version `1.0.0`

## F.A.Q.

1. **Does Semantic Release enforce commits to be standardized with Conventional or other standards?**
   - Yes, Semantic Release can be configured to follow other standards.
2. **Can Semantic Release be used with other languages than Python?**
   - Yes, it only needs a configuration file in either TOML or JSON, but can also be configured from the command line.
3. **Does Semantic Release enforce Semantic Versioning?**
   - Yes, it enforces the format of Semantic Versioning.
4. **Does Semantic Release support multiple LTS versions?**
   - Yes, more info here: [Workflow Configuration](https://github.com/semantic-release/semantic-release/blob/master/docs/usage/workflow-configuration.md)
5. **Can the integration in Azure Pipelines to update the PR’s title and description be used across the board or is it project-specific?**
   - It’s completely agnostic, and can be used in any project.
6. **Does the CHANGELOG follow a specific standard like “Keep A Changelog”?**
   - No, the default changelog template is built-in using Jinja, but can be customized as needed.
7. **This still requires the user to know if they introduce a breaking change; can we automatically detect breaking changes?**
   - Yes, it’s possible to implement PyCracks to automatically detect when a change is a non-backward compatible change. [PyCracks](https://github.com/ELC/pycracks/)
