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
## Tests
Файл "tests.py" необходим для проверки правильности выполнения кода.

Как пользоваться:
- перед использование должен быть установлен pytest с помощью команды "pip install pytest"
- по завершении изменений в основном файле необходимо запустить "pytest tests.py"

The "tests.py" file is necessary to check the correctness of code execution.

How used:
- before use pytest, must be installed using the "pip install pytest" command
- after completing the changes in the main file, you need to run "pytest tests.py"