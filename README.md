# GIS-E4030 - GIS Development #

## By: Juhani Heikkilä (353207), Bijay Karki (718648), Jhosimar Aguacia (661371) & Tekla Larinkoski (290483) ##

### How to set up, run and manage the Django server? ###

* Read the project documentation and also preferably some Django tutorial (or GeoDjango tutorial).

* Install all dependencies as described in https://docs.djangoproject.com/en/dev/ref/contrib/gis/install/.

* Also install django-leaflet with pip install. (In general you can install most python libraries by terminal with the command: 'pip install <library name>')

* After you've installed PostGIS make sure to define the database settings you chose in mapservice/settings.py.

* All of the instructions below are for using a Git Bash terminal on a Windows 10 installation. They should work for other terminals and other windows versions, but if you are using a different operating system something may work differently.

* All relevant commands start with 'python' or 'git'. The commands starting 'python' can be shortened to start with prefix 'py' instead, which is used here.

* You can use py manage.py check to quickly see if code will run or has syntax errors or other fatal failures. This is fastest way to spot fatal errors.
    - py manage.py check

* You will need to use the following commands for database management to create a table for the floor lines:
    - py manage.py makemigrations        
    - py manage.py migrate
    - The first one plans changes to the database and the second commits them. Needs to be run when new tables are added or existing ones edited. 

* To import the data for the floors of the buildings you will need to use a script from load.py. This is done by opening a python shell inside the project and then running the script with correct parameters (of folder and file name). The inputs below should work for the datafiles that were used for TIK and TUAS buildings.
    - py manage.py shell
    - from mapapp import load
    - load.read_lines('buildings_3851.shp', 'EPSG_building')

* You can run the server from terminal by 
    - py manage.py runserver

* Access the site locally by localhost:8000 in your browser.
* If you intend to do any developer work or simply edit something to test it out, a private browsing mode (ex. Google Chrome's Incognito) is recommended, as browsers often cache static files instead of refetching them when refreshing the page and as such newly made changes may not appear.

* Django offers an adminstration page to see and edit the database directly. This is not very useful in this project, as the only objects in the db are FloorLines, of which there will be plenty. But here are instructions how to access the adminstration panel. Create a new admin account in terminal by command below and fill in the email and password as requested.
    - py manage.py createsuperuser
* Then access admin page by appending /admin to url and logging in.


* Git commands:
    - git pull - downloads newest version from master branch
    - git status - see changes you've made
    - git add - add files to a commit
    - git commit -m "message" - creates a commit of added changes with the cited message
    - git push - pushes made changes to master branch repository
    - git checkout <filepath> - permanently disregards changes in this file compared to master branch




