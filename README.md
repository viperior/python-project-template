# python-project-template

This is a template for Python projects that provides a starting structure and a set of universally useful CI/CD configurations.

![build](https://github.com/viperior/python-project-template/actions/workflows/build.yml/badge.svg)

## What is this for?

This template can be used as a starting point for new Python projects to get up and running quickly with a standard set of CI/CD configurations and an organized project structure.

| Operation             | Solution Choice                                          |
| --------------------- | -------------------------------------------------------- |
| Linting               | flake8, pylint                                           |
| Testing               | pytest                                                   |
| Building              | setuptools                                               |
| Dependency management | pip-tools, dependabot                                    |
| Additional features   | changelog, example MIT license, dependabot configuration |

## How do I build it?

```bash
python -m build
```

## How do I run it?

```bash
python -m pip install -r requirements.txt
python -m callable
```

## How do I test it?

```bash
python -m pytest
```

## Project structure

``` text
project_root
├───games_of_chance
└───tests
```

## Resources

- Using GitHub template repositories <https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template>
- GitHub Actions <https://docs.github.com/en/actions>
- pylint <https://pylint.pycqa.org/en/latest/>
- flake8 <https://flake8.pycqa.org/en/latest/>
- pytest <https://docs.pytest.org/en/7.1.x/>
- setuptools <https://pypi.org/project/setuptools/>
- pip-tools <https://github.com/jazzband/pip-tools>
- dependabot <https://github.com/dependabot/dependabot-core>
- Changelog generation <https://github.com/github-changelog-generator/github-changelog-generator>
- MIT license <https://opensource.org/licenses/MIT>
