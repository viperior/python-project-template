# Changelog

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
