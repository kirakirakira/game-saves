# Game Saves
Project for Code Louisville Python Course (Django)

## Purpose
This app is a tracker that allows you to add video games that you own or want to play. You can also rate the games.

## How to run
You will need Python3 installed:
https://www.python.org/downloads/
To verify your Python3 version:
`python3 --version`

1. Clone or download the project files to your computer
2. In the terminal, navigate to the project folder (If cloned ../game-saves/ If downloaded ../game-saves-master/)
3. Create a virtual environment:
   1. Run `python3 -m venv myvenv`
   2. Activate the virtual environment by running `source myvenv/bin/activate`
4. Run the following command `pip install -r requirements.txt` to install necessary packages (If pip is not installed run `python3 -m pip install --user --upgrade pip`)
5. Run the following command `python3 manage.py runserver 0.0.0.0:8000` to start the server
  1. **Note**: A database (db.sqlite3) is checked into git. If you get a message asking you to run migrations, please do the following commands:
    `python3 manage.py makemigrations`
    `python3 manage.py migrate`
6. In the browser of your choosing, navigate to http://127.0.0.1:8000/

## Preview site
Can preview site at http://kirakirakira.pythonanywhere.com/

___

### To Do
- [X] Add developer to model
- [X] Preload game data (developers, publishers, platforms, genres)
- [X] Style!!!
- [X] Media queries!
- [ ] Integrate IGDB API?? (check if game exists, auto-populate data, prevent creating a game that doesn't exist (mismatched publisher/platform/genre) etc.)
- [ ] Add signup/login/logout/password change
- [X] Add randomness to Purchase next
- [X] Move the add game link somewhere else
- [X] Add a footer
- [ ] Change personal rating so you pick by clicking on stars
- [ ] Check whether a game is already added to your tracker and prevent it from being added again
- [X] Host project on pythonanywhere
