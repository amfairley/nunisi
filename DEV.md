![Website logo](/documentation/site_logo.png)

---

# Development and Deployment

See [README.md](/README.md) for information on project goals, user stories, security, future developments, technologies used, user feedback, credits, and acknowledgements. <br>
See [DESIGN.md](/DESIGN.md) for information on the five planes of UX design, site map, database schema, and features. <br>
See [TESTING.md](/TESTING.md) for information on the test driven development of the website, manual and automated testing of the site, bugs encountered, and website analytics. <br>

---
## Table Of Contents
1. [CI/CD](#cicd)
2. [Development Environment](#development-environment)
    - [Creating a GitHub Repository](#creating-a-github-repository)
    - [Cloning the GitHub Repository Locally](#cloning-the-github-repository-locally)
    - [Setting up my IDE](#setting-up-my-ide)
    - [Project Requirements](#project-requirements)
    - [Getting the Project up and Running](#getting-the-project-up-and-running)
    - [Coding in Python and PEP8](#coding-in-python-and-pep8)
3. [Local Development](#local-development)
4. [Apps](#apps)
5. [Deployment](#deployment)

## CI/CD
The philosophy of continuous integration and continuous deployment was at the forefront of my mind during the development of this project.<br>
Version control was achieved using Git and all the information for this project has been stored in this repository on GitHub. Though not strictly continuous integration, version control and continuous integration are synergistic and have a large overlap in terms of project management. The repository was not shared with any other developers for this single developer project, so a shared repository and necessary continuous integration practices such as automated builds were not require, although automated tests were implemented as part of the Test Driven Development of this website and would be a key part of CI/CD for a team of developers.<br>
Please see my [GitHub Project](https://github.com/users/amfairley/projects/9) for the tracking of tasks across the project. GitHub projects was used to track the development of this website, allowing tasks to be created, converted to an issue to link them to the GitHub repository and to assign a member of the team the task. As this project was completed as a single developer team, I assigned all of the tasks to myself. In a multi-developer team, this software would allow the scrum leader to assign tasks and ensure that no two developers are working on the same aspect of the project in isolation. <br>
To create a GitHub project, you will need a [GitHub](https://github.com/) account. From your profile page you can access your projects from the taskbar at the top. It is the third selection after “Overview” and “Repositories”. Help with creating a project can be found [here](https://docs.github.com/en/issues/planning-and-tracking-with-projects/creating-projects/creating-a-project). When assigning tasks in my project I used the [MoSCoW](https://www.marketing-logic.com/salesforce/the-moscow-method/) method; a way of prioritising tasks by assigning them Must, Should, Could, or Would. This allowed me to concentrate on core components of the project and build up from there.

## Development Environment
Here are the steps that I took to set up my local development environment in order to provided guidance to unfamiliar users with how to set up their own local development environment. 

### Creating a GitHub Repository
In order to create your own repository you will also need a GitHub account. From your profile page, you can access your repositories from the taskbar at the top. It is the second selection, after “Overview”.<br>
![Github taskbar](/documentation/development_github_taskbar.png)<br>
From this tab, select the green “New” button to open the new repository creation form.<br>
![New repository button](/documentation/development_new_repo.png)<br>
In this form you can enter details for your own repository. The values that I used were:
-	Repository template: No template
-	Owner: Selecting myself from the dropdown menu
-	Repository name: nunisi
-	Description: A full stack python backed hotel management web app
-	Public: I toggled public so that this is available to you, however you may want to select Private if you do not wish other users to have access to your repository
-	Add a README file: Ticked, so that I can explain my process and code to facilitate users getting up and running with my project or create a project of their own.
-	.gitignore template: None, I will create my own .gitignore file
-	License: None
Then I clicked the green create repository button and was redirected to the new repository.<br>
![Create new repository](/documentation/development_create_repo.png)<br>
For any troubleshooting tips or help with creating your own repository, GitHub provides this handy [quick start guide](https://docs.github.com/en/repositories/creating-and-managing-repositories/quickstart-for-repositories).

### Cloning the GitHub Repository Locally
My IDE of choice for this project is [Visual Studio Code](https://code.visualstudio.com/), as it has strong support for many coding and markup languages and I will be utilising HTML, CSS, JavaScript, and Python to create my website. With help setting up Git in VSCode, please see the [VSCode Git documentation](https://code.visualstudio.com/docs/sourcecontrol/intro-to-git).
The steps that I took to clone my project to deploy it locally were:
-	Open my repository page in GitHub
-	Click the bright green “<> Code” button located below the Pin/Watch/Fork/Star toolbar and above the repository file list.
-	Selected my cloning option which was to clone from the web URL using HTTPS and clicked the copy URL to keyboard button.
-	![Repository Clone Options](/documentation/development_clone_options.png)
-	Other options for cloning include using a password protected SSH key using SSH, working in the official GitHub CLI with GitHub CLI, or downloading the repository in a .zip folder
-	In VSCode, I clicked on the Source Control icon located on the left hand side beneath the explorer and search button
-	![Source Control Icon](/documentation/development_source_control_icon.png)
-	I selected “Clone Repository”, which redirects the user to the search bar at the top of VSCode. This is where I pasted in my web URL copied from my GitHub repository and clicked enter, ensuring that the “Clone from URL” option was highlighted.
-	I then selected a folder to save the repository locally into and opened the repository when prompted.

### Setting up my IDE

To set up my development IDE so that I could start coding; I required Python.<br>
Python can be downloaded and easily installed from the [Python](https://www.python.org/downloads/) website. Select the version and operating system that you want to download python for click the installer file to download. I used 3.12.4. Once the file is downloaded, open the installer and follow the python installer wizard with the following changes to the default:
- Tick “Add python.exe to PATH” on the first page of the install wizard and click on custom installation  
- On optional features, ensure that they are all ticked and click next
- On advanced options, tick the option to install python for all users if desired, and tick “Precompile standard library” and click “Install”
When the wizard displays that the setup was successful, you can close it. You can confirm its installation on windows by typing CMD into the windows search bar to open the command prompt. Here type `python --version` and it will show the currently installed version. If this does not work, please see this [Python Beginners Guide](https://wiki.python.org/moin/BeginnersGuide) or [Python Documentation](https://docs.python.org/3/) for troubleshooting.<br>
I installed the Python by Microsoft VSCode extension in order to easily type and edit Python scripts for my project.

### Building a Virtual Environment
I did all of my work inside a virtual environment so that I could install and work with libraries and dependencies without worrying about the greater impact of them on my system. With the repository open in VSCode, I used the terminal to create a new python virtual environment by typing: `python -m venv venv`. To see if this has worked, a folder named venv should have appeared in your root directory. This virtual environment can be activated by typing `.\venv\Scripts\activate` into the terminal on windows or `source venv/bin/activate` on MacOS. This will show a green (venv) at the start of each terminal line indicating that you are within the virtual environment.<br>
To leave this virtual environment when you want to close the file later, you can type `deactivate` into the terminal. Please note you will need to activate the virtual environment each time you load up the files to work on to ensure that everything is running.

### Project Requirements
This project is built within the Django framework, so I installed the packages required for the project using pip; the python package manager.
```bash
pip3 install django
```
The full list of all libraries used can be found in my [requirements.txt](/requirements.txt) file. Copy and pasting this into your project and typing in the terminal `pip install -r requirements.txt` will install all dependencies used in this project simply and efficiently.

### Getting the Project up and Running
With my repository successfully cloned to my local IDE and being in my virtual environment, I set up the Django project following these steps:
- Install Django: ```pip3 install django```
- Check that I have the correct version of Django: ```djano-admin --version```
- Create the Django project in the root directory: ```django-admin startproject nunisi .```
- Check that the project folder has \_\_init\_\_.py, settings.py, urls.py, wsgi.py files.
- Create a .gitignore file and add files to it. These are listed [here](/README.md#security).
- Launch the app with: ```python manage.py runserver``` and open the url to show a success screen that Django has been successfully installed.
- Make the initial migrations to ensure all apps work with:
    - ```python manage.py showmigrations``` to show what has not been migrated yet
    - ```python manage.py makemigrations --dry-run``` for a dry run of the migrations
    - ```python manage.py makemigrations``` to queue up the migrations
    - ```python manage.py migrate --plan``` to show how the migrations will occur
    - ```python manage.py migrate``` to actually make the migrations

### Coding in Python and PEP8

Throughout this project, I kept strict adherence to the Python good practices for style; [PEP8](https://peps.python.org/pep-0008/). This included:
- Line lengths less than 80 characters long
- DOCSTRINGs on all functions and classes
- Naming conventions for functions, variables, and classes
- Comments on code functionality
- 2 empty lines beneath each block of code
- 1 empty line at the bottom of the file

The Python files were validated as shown [here](/TESTING.md#python-validation) in my TESTING.md file.

## Local Development
To install my project locally, you can follow my steps above in the [Development Environment](#development-environment) section, replacing file and folder names with the ones in my project.
You can also fork the GitHub repository to collaborate by once logged into GitHub by:
- Go to the repository for this project, [nunisi](https://github.com/amfairley/nunisi).
- Click the Fork button in the top right corner and create a new fork.

## Apps
Each section of functionality for the website were sequestered into their own apps in order to maximise the readability and reusablity of the code. The apps are:<br>
**Templates**: Though not technically an app, the base template of the app and Django AllAuth templates are stored here for reusability throughout the apps. The static folder holds the base CSS and JavaScript that are also reused across the app.<br>
**back_button**: The back button app holds the functionality for the back button that is used across the site. It holds the view that handles the redirection to the previous page or 404 page if the page is not found, the url for the back button, and the HTML template for the button to be included in other templates.<br>
**home**: The home app contains all the functionality for the homepage including the room availability search form that is shared site wide with a context processor and used in the site header and on the homepage. There are no models for the homepage and the only view and url renders the index.html page.<br>
**rooms**: The rooms app contains the functionality for the hotel rooms. It holds the models for the rooms and amenities, the views to display available rooms to the user and rooms/edit rooms/delete rooms to a superuser. It also houses the form for editing the rooms. <br>
**checkout**: The checkout app handles the checkout functionality. This includes populating the checkout form with the submitted values processing the payment, creating orders and trips, updating room instances, and sending the user a confirmation email. User details can be saved to their account if they choose. It holds the checkout form and the model for the order along with the webhandler to handle the logic for processing payment and order/trip creation and adding unavailable dates to the room instances. <br>
**trips**: The trips app handles the trip functionality across the site. It allows users to see their trips and request a cancellation. It also allows the site owner to see all the trips and cancel/uncancel them. It has templates for the user trips, cancel trip, cancel trip success, and superuser trips pages. It has the model for the Trip instances. In the view it has the logic for updating the room instances unavailability when trips are cancelled or uncancelled.
**reviews**: The reviews app handles the review functionality across the site. It has the template for the trip reviews (included in the user trips html page), a carousel of verified reviews (included in the hompage html) and the templates for the add/edit review forms. It has the model of the review along with the form for adding/editing the review instances. The views handle the adding/editing of the reviews including sending an email to alert the site owner, and the review deletion.
**user_profile**: The user profile app was named due to the pre-existing Django default apps of user and profile to avoid any complication with the code. It holds the code for the user profile data including the models for the UserProfile, the form for updating the user profile information, and a signal to create a user profile for users when the sign up or update the profile if they make changes. There are links on the user_profile.html that link to allauth functionality for changing/adding email addresses or changing the user password.


## Deployment

- A PostgreSQL database was created using the [CodeInstitute Database Creator](https://dbs.ci-dbs.net/)
- Heroku was used for deployement
    * Create new app ![new app button](/documentation/development/heroku_new_app.png)
    * Pick a name, select region and click create app. ![new app](/documentation/development/heroku_new_app_name.png)
    * Open settings tab ![settings tab](/documentation/development/heroku_settings_tab.png)
    * Add the PostgreSQL database to the config vars ![PostgreSQL config vars](/documentation/development/heorku_database_url.png)
- Install dj_database_url and psycopg2 for connection to an external database
```bash
pip3 install dj_database_url==0.5.0 psycopg2
```
- Update settings.py with: 
```python 
import dj_database_url
```
```python
DATABASES = {
    'default': dj_database_url.parse('your-database-url-here')
}
```
- To see that you are now connected to your new database you can use ```python manage.py showmigrations``` in the terminal and see all the migrations ready to be made.
- Then run the migrations using ```python manage.py migrate``` in the terminal.
- Load any data e.g. ```python manage.py loaddata amenities``` in the terminal.
- Set up a new superuser for this database using ```python manage.py createsuperuser```
- Add if/or statement to settings.py to use an external server if the database url is in the env.py file or use the local server if not
- Install gunicorn for the webserver with ```pip3 install gunicorn```
- Add a Procfile informing Heroku of how to access the webserver with ```web: gunicorn app_name.wsgi:application```
- Open up the heroku CLI with ```heroku login``` and follow the instructions to log in in browser
- Temporarily disable collect stattic with ```heroku config:set DISABLE_COLLECTSTATIC=1 --app_name``` to stop Heroku collecting static files when we deploy, as we have not linked them yet.
- Add host name of the Heroku app to allowed hosts in settings.py, e.g. ```ALLOWED_HOSTS = ['app-name.herokuapp.com', 'localhost']```
- In the deploy tab in Heroku, I linked up my GitHub repository by selecting github as the deployment method and selecting my respository. I enabled automatic deploys so that any changes I push to GitHub are automatically push to Heroku.  ![Heroku deployment method](/documentation/development/heroku_deployment_method.png)
- Back in config vars, I added the Django SECRET_KEY to allow the website to work.
- Use Amazon web services to create an S3 bucket to store the static files in
- Install boto3 and django-storages with ```pip3 install boto3``` and ```pip3 install django-storages``` in the terminal and add 'storages' to the installed apps in settings.py
- Add AWS settings to settings.py:
```python
if 'USE_AWS' in os.environ:
    AWS_STORAGE_BUCKET_NAME = 'nunisi-hotel-and-spa'
    AWS_S3_REGION_NAME = 'eu-north-1'
    AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
    AWS_S3_FILE_OVERWRITE = False
```
- Add the 2 secret keys and USE_AWS to Heroku config vars
- Remove the DISABLE_COLLECT_STATIC from Heroku config vars
- Set up storage locations in settings.py like:
```python
STORAGES = {
    # Media management
    "default": {
        "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
    },

    # CSS and JS
    "staticfiles": {
        "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
    },
}
```
- In the terminal run ```python manage.py collectstatic``` and click yes to overwrite files
- On AWS in the bucket, I added a media folder and manually uploaded all of my media files
- To set up emails, I went to my GMail account and ensured that I had 2 factor authentication set up
    * This will allow us to create an app password specific to our Django app to let it use our GMail account
    * Then in Google account I searched "app passwords"
    * Created one and copied it, adding it to Heroku config vars as EMAIL_HOST_PASS along with my email account as EMAIL_HOST_USER
    * I then updated the email settings in my settings.py file to:
```python
if 'DEVELOPMENT' in os.environ:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL')
else:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_USE_TLS = True
    EMAIL_PORT = 587
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASS')
    DEFAULT_FROM_EMAIL = os.getenv('EMAIL_HOST_USER')
```
All these steps resulted in the website being deployed successfully.
