#### Activate the virtualenv that contains the necessary libraries.
#### Install the pipenv library if it is not already installed using the command:
```angular2html
pip install pipenv  
```
#### Change the directory to the current project folder.
#### Create a new Pipenv environment using the command:
```angular2html
pipenv --python 3.x
```
#### Install all the libraries from your virtualenv into the Pipenv environment using the command:
```angular2html
pipenv install --ignore-pipfile
```
#### Create requirements.txt using the command:
```angular2html
pipenv lock -r > requirements.txt
```
#### Create Pipfile.lock using the command:
```angular2html
pipenv lock
```
#### Check if the libraries in Pipfile are installed using the command:
```angular2html
pipenv graph
```
#### If there are no libraries in requirements.txt, use the following command: 
```angular2html
pip freeze > requirements.txt
```
#### In the configuration, change the working directory to:
```angular2html
\...\CupidBot\main\src
```
#### Also, do not forget to set the appropriate interpreter and path to the main script as follows:
```angular2html
\...\CupidBot\main.py
```

##  Feedback

#### `If you have any questions or suggestions for the project, please feel free to contact me through my social media accounts:`
```
Discord: bladexses
```
```
Telegram: @BladeXses
```
##### `I am always happy to receive feedback from users to make the project better. Thank you for your attention!`