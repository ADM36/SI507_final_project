# AaronDM NBA Statistics Final Project

Aaron Miller

[Link to this repository](https://github.com/ADM36/SI507_final_project)

---

## Project Description

This project allows a user to access statistics on people who have played in the National Basketball Association (NBA) through stats.nba.com. By accessing these statistics, a user can build their own database of key statistics on NBA players, as well as a list of NBA teams. A user can also retrieve, for viewing, information on NBA statistics "leaders" (e.g. most points, rebounds, etc.) from various NBA seasons.

## How to run

1. First, install all requirements with `pip install -r requirements.txt`.
2. Get familiar with the nba_api (https://github.com/swar/nba_api/blob/master/README.md) to understand how classes are working when pulling data from the API.
2. Second, you should ... (e.g. run `python programname.py runserver` or whatever else is appropriate)
3. Anything else

## How to use

1. A useful instruction goes here
2. A useful second step here
3. (Optional): Markdown syntax to include an screenshot/image: ![alt text](image.jpg)

## Routes in this application

- '/login' -> This is a login page, where a user can enter any password or username that isn't blank to get directed to the home page.

- `/` -> This is the home page, which plays an intro video for the 2019 NBA playoffs.

- `/teams` -> This route prints out a list of all NBA teams, and the city and state they are located. It also creates a table "nba_teams" for an external database.

- `/career_stats/<player_name>/` -> This route allows a user to input an NBA player name into the form to both print career, season statistics on the NBA player being searched, while also adding that data to a table "nba_players" for external data usage.

- `/leaders/<years>/<season_type>/<stat>/` -> This route has an input of an NBA season in the format XXXX-XX (e.g. 2003-04), season type (e.g. Regular Season) and a NBA player stat (e.g. PTS), which will print out data from the specified NBA season year and season type with NBA players who had the highest number of the specified statistic.

- '/bio/<player_name>/ -> This route allows a user to input a player name, and retrieve a print out of a short biography on the NBA player they searched.

## How to run tests
1. First... (e.g. access a certain directory if necessary)
2. Second (e.g. any other setup necessary)
3. etc (e.g. run the specific test file)
NOTE: Need not have 3 steps, but should have as many as are appropriate!

## In this repository:
- SI507_final_project
  - static
    - style.css
  - templates
    - analysis.html
    - all_teams.html
    - login.html
  - common_player.py
  - leauge_leader_nba.py
  - nba_507.py
  - nba_flask.py
  - nba_players.db
  - player_stats.py
  - README_template.md
  - requirements.txt
  - SI507project_final.py
  - SI507project_tools.py

---
## Code Requirements for Grading
Please check the requirements you have accomplished in your code as demonstrated.
- [x] This is a completed requirement.
- [ ] This is an incomplete requirement.

Below is a list of the requirements listed in the rubric for you to copy and paste.  See rubric on Canvas for more details.

### General
- [x] Project is submitted as a Github repository
- [x] Project includes a working Flask application that runs locally on a computer
- [ ] Project includes at least 1 test suite file with reasonable tests in it.
- [x] Includes a `requirements.txt` file containing all required modules to run program
- [ ] Includes a clear and readable README.md that follows this template
- [x] Includes a sample .sqlite/.db file
- [x] Includes a diagram of your database schema
- [x] Includes EVERY file needed in order to run the project
- [ ] Includes screenshots and/or clear descriptions of what your project should look like when it is working

### Flask Application
- [x] Includes at least 3 different routes
- [ ] View/s a user can see when the application runs that are understandable/legible for someone who has NOT taken this course
- [x] Interactions with a database that has at least 2 tables
- [x] At least 1 relationship between 2 tables in database
- [x] Information stored in the database is viewed or interacted with in some way

### Additional Components (at least 6 required)
- [x] Use of a new module
- [ ] Use of a second new module
- [ ] Object definitions using inheritance (indicate if this counts for 2 or 3 of the six requirements in a parenthetical)
- [ ] A many-to-many relationship in your database structure
- [x] At least one form in your Flask application
- [x] Templating in your Flask application
- [x] Inclusion of JavaScript files in the application
- [ ] Links in the views of Flask application page/s
- [ ] Relevant use of `itertools` and/or `collections`
- [ ] Sourcing of data using web scraping
- [x] Sourcing of data using web REST API requests
- [ ] Sourcing of data using user input and/or a downloaded .csv or .json dataset
- [ ] Caching of data you continually retrieve from the internet in some way

### Submission
- [ ] I included a link to my GitHub repository with the correct permissions on Canvas! (Did you though? Did you actually? Are you sure you didn't forget?)
- [ ] I included a summary of my project and how I thought it went **in my Canvas submission**!
