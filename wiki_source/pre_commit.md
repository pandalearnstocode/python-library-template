# Pre-commit hooks

Before pushing some changes in the git repository we need to check some stuff. We are implementing this using pre-commit hook. `.pre-commit-config.yaml` file in te project root directory will have all the hooks configure. Notes, these hooks are order dependent. Here is the pre-commit hook files content,


```
repos:
- repo: https://github.com/commitizen-tools/commitizen
  rev: v2.19.0
  hooks:
    - id: commitizen
      stages: [commit-msg]
- repo: https://github.com/myint/autoflake
  rev: v1.4
  hooks:
    - id: autoflake
      exclude: &fixtures tests/functional/|tests/input|tests/extensions/data|tests/regrtest_data/|tests/data/
      args:
        - --in-place
        - --ignore-init-module-imports
        - --remove-all-unused-imports
        - --expand-star-imports
        - --remove-duplicate-keys
        - --remove-unused-variables
- repo: https://github.com/nbQA-dev/nbQA
  rev: 1.1.1
  hooks:
   - id: nbqa-black
     additional_dependencies: [black==21.7b0]
   - id: nbqa-pyupgrade
     additional_dependencies: [pyupgrade==2.7.3]
   - id: nbqa-isort
     additional_dependencies: [isort==5.6.4]
-   repo: https://github.com/ambv/black
    rev: 21.9b0
    hooks:
    - id: black
      language_version: python3.8
-   repo: https://gitlab.com/pycqa/flake8
    rev: 3.9.2
    hooks:
    - id: flake8
- repo: https://github.com/pycqa/pylint
  rev: v2.11.1
  hooks:
    - id: pylint
      name: pylint
      entry: pylint
      language: system
      types: [python]
- repo: https://github.com/pre-commit/mirrors-mypy
  rev: v0.910-1
  hooks:
    - id: mypy
      name: mypy
      entry: mypy
      language: python
      types: [python]
      args: []
      require_serial: true
      additional_dependencies:
        ["platformdirs==2.2.0", "types-pkg_resources==0.1.3", "types-toml==0.1.3"]
      exclude: tests/functional/|tests/input|tests(/.*)*/data|tests/regrtest_data/|tests/data/|tests(/.*)+/conftest.py|doc/|bin/

```


Here, first we are checking commit rules using commitizen. To know about this project more check [this](https://commitizen-tools.github.io/commitizen/) url. 