# Changelog

## Unreleased

### New features

### Improvements

- Limit code line length to 80 characters (closes [#73](https://github.com/viperior/python-project-template/issues/73))

## [1.1.0](https://github.com/viperior/python-project-template/tree/v1.1.0) (2022-06-27)

### New features

- Configure dependabot to update GitHub Actions (closes [#64](https://github.com/viperior/python-project-template/issues/64))

### Issues fixed

- Resolve the pylint import error encountered during the GitHub Action workflow execution (closes [#58](https://github.com/viperior/python-project-template/issues/58))

### Improvements

- Move the tests related to the example module into example/tests (closes [#36](https://github.com/viperior/python-project-template/issues/36))
- Improve the project structure documentation
- Rename the `build` workflow to `test` (closes [#52](https://github.com/viperior/python-project-template/issues/52))
- Simplify the import statement in the coin flip test case
- Ignore `.venv` directory when linting with flake8 (closes [#53](https://github.com/viperior/python-project-template/issues/53))
- Dependency updates

## [1.0.0](https://github.com/viperior/python-project-template/tree/v1.0.0) (2022-05-06)

### New features

* Configure the `setuptools` build tool by creating the required metadata files

### Improvements

* Move pylint usage from the pytest test suite to a GitHub Actions workflow
* Document universally important project aspects in readme (closes [#13][i13])
* Update reference to build.yaml file in badge URL (closes [#38][i38])

[i13]: https://github.com/viperior/python-project-template/issues/13
[i38]: https://github.com/viperior/python-project-template/issues/38

## [0.7.0](https://github.com/viperior/python-project-template/tree/v0.7.0) (2022-02-26)

### Improvements

* Measure code coverage using `coverage` and require 100% code coverage to pass PR checks (closes [#9][i9])

### Testing

* Improve the design of the `test_flip_coins_function` to use parametrized test input data and run multiple times with a range of coin count inputs
* Exclude pylint success/failure reporting from code coverage measurement
* Achieve 100% code coverage ???

[i9]: https://github.com/viperior/python-project-template/issues/9

## [0.6.0](https://github.com/viperior/python-project-template/tree/v0.6.0) (2022-02-25)

### Improvements

* Enforce Flake8 Rules (closes [#11][i11])
* Modify max code line length to 100 characters in `flake8` command

[i11]: https://github.com/viperior/python-project-template/issues/11

## [0.5.0](https://github.com/viperior/python-project-template/tree/v0.5.0) (2022-02-25)

### Improvements

* Fail faster when running the `pytest` test suite by running the test suite asynchronously and halting on the first error encountered using pytest's `-x` option (closes [#12][i12])
* Bump pylint from 2.12.1 to 2.12.2 ([#16][p16])
* Bump pytest from 6.2.5 to 7.0.1 ([#17][p17])

[i12]: https://github.com/viperior/python-project-template/issues/12
[p16]: https://github.com/viperior/python-project-template/pull/16
[p17]: https://github.com/viperior/python-project-template/pull/17

## [0.4.0](https://github.com/viperior/python-project-template/tree/v0.4.0) (2022-02-25)

### New features

* Configure Dependabot to automate the management of the project's dependencies (closes [#10][i10])

[i10]: https://github.com/viperior/python-project-template/issues/10

## [0.3.0](https://github.com/viperior/python-project-template/tree/v0.3.0) (2022-02-25)

### New features

* Changelog template with standard categories and PR/issue footnotes (closes [#8][i8])

[i8]: https://github.com/viperior/python-project-template/issues/8

## [0.2.0](https://github.com/viperior/python-project-template/tree/v0.2.0) (2022-02-25)

### New features

* Configure a `FUNDING.yml` that integrates with GitHub's Sponsors functionality ([#2][p2])
* Configure a GitHub Action that runs the test suite using `pytest` ([#3][p3])
* Display a badge in the project readme with the status of the latest GitHub Actions build workflow ([#6][p6])
* Configure a GitHub Actions workflow that performs CodeQL analysis ([#7][p7])

### Issues fixed

* Remove static reference to project name ([#5][p5])

### Improvements

* Rename the GitHub actions workflow to `build` from `Python application`

[p2]: https://github.com/viperior/python-project-template/pull/2
[p3]: https://github.com/viperior/python-project-template/pull/3
[p5]: https://github.com/viperior/python-project-template/pull/5
[p6]: https://github.com/viperior/python-project-template/pull/6
[p7]: https://github.com/viperior/python-project-template/pull/7

## [0.1.0](https://github.com/viperior/python-project-template/tree/v0.1.0) (2021-11-28)

### New features

* Starting structure that can be leveraged to start a new Python project
* `requirements.in` file used with the `pip-compile` command from `pip-tools` to auto-generate `requirements.txt`
* Automatic linting via `pylint` is automatically executed when the `pytest` command is invoked
