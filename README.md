# task-done


## Set Up:
1) Fork this repo and creating a clone of it on your local machine
2) Open the repo in your text editor 
3) In the terminal, create a virtual environment:
```
python -m venv .venv
```
4) Activate the virtual environment
```
source .venv/bin/activate  <!--- macOS -->
./.venv/Scripts/Activate.ps1 <!--- Windows -->
```
5) Update pip
```
python -m pip install --upgrade pip
```
6) Install all the dependencies in the requirements.txt file
```
pip install -r requirements.txt
```
7) Create a brand new requirements.txt file from the installed pip packages
```
pip freeze > requirements.txt
```
8) Apply all migrations to your database
```
python manage.py migrate
```
9) Now you're ready to start using the app. Start up your server:
```
python manage.py runserver
```
- Note: The app is configured to run in your browser on localhost:8000
- Note: In order to deactivate the virtual environment at any point in time, enter `deactivate` in the terminal
- Note: If you want the server to stop running press Control + C in your text editor.
