# Dashboard-Subscriptions project

**_Version v1.0.0_**

![Python](https://img.shields.io/badge/Python-3.14-3776AB.svg?style=flat&logo=python&logoColor=white)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/fb6ab3ecc82d4750a86da843092f5cf8)](https://app.codacy.com/gh/NY-Daystar/Dashboard-Subscriptions/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade) [![Dashboard-CI](https://github.com/NY-Daystar/Dashboard-Subscriptions/actions/workflows/python.yml/badge.svg)](https://github.com/NY-Daystar/Dashboard-Subscriptions/actions/workflows/python.yml) [![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) [![Version](https://img.shields.io/github/tag/NY-Daystar/dashboard-subscriptions.svg)](https://github.com/NY-Daystar/dashboard-subscriptions/releases)

![GitHub repo size](https://img.shields.io/github/repo-size/ny-daystar/dashboard-subscriptions) ![GitHub language count](https://img.shields.io/github/languages/count/ny-daystar/dashboard-subscriptions) ![GitHub top language](https://img.shields.io/github/languages/top/ny-daystar/dashboard-subscriptions)

![GitHub issues](https://img.shields.io/github/issues/ny-daystar/dashboard-subscriptions) ![GitHub closed issues](https://img.shields.io/github/issues-closed-raw/ny-daystar/dashboard-subscriptions) ![GitHub commit activity (branch)](https://img.shields.io/github/commit-activity/m/ny-daystar/dashboard-subscriptions/main) [![All Contributors](https://img.shields.io/badge/all_contributors-1-blue.svg?style=circular)](#credits) [![Used By](https://img.shields.io/sourcegraph/rrc/github.com/NY-Daystar/Dashboard-Subscriptions.svg)](https://sourcegraph.com/github.com/NY-Daystar/Dashboard-Subscriptions)

![GitHub watchers](https://img.shields.io/github/watchers/ny-daystar/dashboard-subscriptions) ![GitHub forks](https://img.shields.io/github/forks/ny-daystar/dashboard-subscriptions) ![GitHub Repo stars](https://img.shields.io/github/stars/ny-daystar/dashboard-subscriptions)

Python project to handle your subscriptions like streaming platform or taxes
No data collected, all it's saved locally

Source code analysed with [Codacy](https://app.codacy.com)

Developped in python `v3.14`  
Using `poetry` as dependency manager

## Index

-   [Get Started](#get-started)
-   [How to contribute](#how-to-contribute)
-   [Unit tests](#unit-tests)
-   [Trouble-shootings](#trouble-shootings)
-   [Credits](#credits)

## Get Started

#### Native mode

**You have to get python and poetry on your computer**

1. Clone the repository

```bash
git clone https://github.com/NY-Daystar/Dashboard-Subscriptions.git
```

```bash
cd Dashboard-Subscriptions
```

2. Install dependencies with `poetry`

```bash
poetry install
```

3. Run the application

```bash
flask run
```

4. By default in your browser you can go on http://localhost:5000

#### Docker mode

**First you have to get docker in your computer**

TODO A FAIRE

## How to contribute

A METTRE POUR LES DEVELOPPERS

-   ajouter des rules of conduct.md
-   recherche une issue
-   creeer une branche depuis la branche main et proposer une pull requests

You need few requirements

-   Python (3.14 mini)
-   poetry and venv packages pre-installed

1. Setup virtual env

```bash
python -m venv .venv
```

2. Using poetry with virtual env

```bash
poetry env use .venv/Scripts/python.exe
```

3. Resolve dependencies

```bash
poetry install
```

## Unit tests

We use `pytest` for unit tests

```bash
pytest
```

To execute production tests

```bash
pytest --ignore=repositories --ignore=repositories_test --ignore=exe
```

## Trouble-shootings

If you have any difficulties, problems or enquiries please let me an issue [here](https://github.com/LucasNoga/Dashboard-Subscriptions/issues/new)

## Credits

Made by Lucas Noga  
Licensed under GPLv3.
