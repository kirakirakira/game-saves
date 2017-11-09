# game-saves
Project for Code Louisville Python Course (Django)

# Purpose
This app is a tracker that allows you to add video games that you own or want to play. You can also rate the games. 

# How to run
1. Clone or download the project files to your computer
2. In the terminal, navigate to the project folder (../game-saves/)
3. Run the following command `pip install -r requirements.txt` to install necessary packages
4. Run the following command `python3 manage.py runserver 0.0.0.0:8000` to start the server
5. In the browser of your choosing, navigate to http://127.0.0.1:8000/


## To Do
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
- [ ] Host project on pythonanywhere
