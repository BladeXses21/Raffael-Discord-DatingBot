#### Активуйте virtualenv, який містить потрібні бібліотеки.
#### Встановіть бібліотеку pipenv, якщо вона ще не встановлена, за допомогою команди:
```angular2html
pip install pipenv  
```
#### Змініть директорію на поточну папку проекту.
#### Створіть нове середовище Pipenv, використовуючи команду:
```angular2html
pipenv --python 3.x
```
#### Встановіть всі бібліотеки з вашого virtualenv в середовищі Pipenv, використовуючи команду:
```angular2html
pipenv install --ignore-pipfile
```
#### Створіть requirements.txt, використовуючи команду
```angular2html
pipenv lock -r > requirements.txt
```
#### Створіть Pipfile.lock, використовуючи команду:
```angular2html
pipenv lock
```
#### Перевірте, чи є у Pipfile бібліотеки, використовуючи команду:
```angular2html
pipenv graph
```
#### Якщо в requirements.txt немає бібліотек використайте наступну команду: 
```angular2html
pip freeze > requirements.txt
```
#### В конфігурації робочу дерикторію змініть за шляхом:
```angular2html
\...\CupidBot\main\src
```
#### Також не забудьте виставити потрібний інтерпритатор та шлях до головного скрипту за шляхом:
```angular2html
\...\CupidBot\main.py
```