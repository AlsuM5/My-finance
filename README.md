# My-finance
## Contribution
Файл ".pre-commit-config.yml" необходим для выполнения перед каждым commit следующих шагов:
переформатирование кода, согласно правилам переформатирования (black)
- проверка переформатирования на соответствие стандартам форматирования (flake8)
- удаление конечных пробелов (trailing-whitespace)

Как пользоваться:
- установить pre-commit с помощью команды "pip install pre-commit"
- клонировать проект
- запустить pre-commit install
- после изменений закоммитить

The ".pre-commit-config.yml" file is used before each commit for:
- code reformatting (black
- checking reformatting (flake8)
- remove trailing spaces (trailing-whitespace)

How used:
- install pre-commit with command "pip install pre-commit"
- clone a project
- run pre-commit install
- to commit after changing