# GIS-dev-proj

GIS-E4030 - GIS Development


Useful things to remember

You can use py manage.py check to quickly see if code will run or has syntax errors or other fatal failures

Access the site locally by localhost:8000

^Need to run it from a git console first by py manage.py runserver
also use a private browsing mode like incognitoon chrome if you are making changes to static files

current admin account credentials
username: admin
password: ApinaVapina

Access admin page by appending /admin to url

git commands
git pull - downloads newest version from master branch
git status - see changes you've made
git add - add files to a commit
git commit -m "ebin :D" - creates a commit of added changes with the cited message 
git push - pushes made changes to master branch repository
git checkout <filepath> - permanently disregards changes in this file compared to master branch


you can install most python libraries by git console with the command:
pip install <library name>

database management
py manage.py makemigrations        <if changes in models have been made
py manage.py migrate               <after the one above to actually do the planned db changes

loading data to db by console using py manage.py shell and importing the read_lines function from mapapp/load.py. See that file for its use
