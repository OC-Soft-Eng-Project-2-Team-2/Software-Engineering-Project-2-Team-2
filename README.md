# Software-Engineering-Project-2-Team-2: Course-Management System

*All command-line instructions in this file presume that you are operating inside VS Code and have a virtual environment that runs python 3.8.3*

To run any of the commands mentioned in this file:
--go to "View > Command Palette > Python: Select Interpreter" and select your virtual environment
--go to "View > Command Palette > Terminal: Set Default Shell" and select "Command Prompt"
--go to "View > Command Palette > Terminal: Create New Integrated Terminal" and enter the listed commands into the terminal that appears in the VS Code window

To install dependencies (django and any other libraries or modules we end up needing):
--cd into the Software-Engineering-Project-2-Team-2 directory
--run "pip install -r requirements.txt"

To add a dependency to that requirements file:
--copy the pip install command for that library/module/software WITH ITS VERSION NUMBER (e.g. "pip install django=3.0.8")
--make a new, blank line at the end of requirements.txt
--paste the command you copied onto the blank line you just made
--delete "pip install " from the beginning of that line

To apply database edits (this will be necessary any time models.py is edited in any way):
--cd into the outer cms_project folder
--run "python manage.py makemigrations"
--run "python manage.py migrate"

To run the server/site:
--cd into the outer cms_project folder
--run "python manage.py runserver"
--navigate in your browser to "127.0.0.1:8000" or "localhost:8000"
[If you encounter an error, your first line of defense should be to make sure you've applied all database edits (see above), especially if you've recently pulled from the remote repository]

To stop the server:
--click anywhere inside the terminal where you started the server with the above command
--type Ctrl+C (or whatever the BREAK command is on your system)

To access the built-in django admin interface:
--run the server (see above)
--navigate in your browser to "localhost:8000/admin"
--log in with admin or superuser credentials (see below)
[Users, authentication groups, and any other data in the site's database can be created, deleted, or have their permissions modified through this interface
Limited customization of the interfaces is also possible, primarily through edits to data models in the models.py file]

The superuser credentials for this site are:
--username: admin
--password: password
[Do not create additional superusers; only one should exist for any given project, and any other users who require administrative access should be created as admin users only]


======================================================================
Django Folder Structure, in Brief:
All things django live somewhere inside the outer cms_project folder.
--Things related to the site itself (like database models, html templates, views, site-specific page urls, etc.) live under the cms_application directory, in files and subfolders dictated by django conventions (explained in the official documentation)
--Things that are more overarching settings (like authentication, database management, django-admin interface urls, etc.) live under the inner cms_project directory