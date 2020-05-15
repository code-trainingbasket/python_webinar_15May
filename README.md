This is a basic introduction to flask framework along with a basic API implementation done during the python webinar session on 15 May 2020.

Steps to run this application:

* Have Python & git installed on your system and ensure its path is set in the environment variables
* Open command prompt and clone this Repository
* run pip install -r requirements.txt
* python wsgi.py (run in the command propmt)
* Open http://127.0.0.1:5000 in your browser

Steps for Deployment on heroku:

* Create a heroku account
* Download and install heroku cli (Ensure that the path is set in environment variables)
* Restart your cmd and goto to your project directory Run Below commands
* git init
* git add -A
* git commit -m "Your Commit message"
* heroku login
* heroku create "sitename" (Instead of "sitename" mentione the name of what you want the website to be named as) Ex: heroku create flasksimple
* heroku git:remote -a "sitename" Ex: heroku git:remote -a flasksimple
* git push heroku master
On success you can open the web application using www.sitename.herokuapp.com in your browser.
