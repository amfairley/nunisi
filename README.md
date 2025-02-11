![Website logo](/documentation/site_logo.png)

---

# Nunisi Hotel and Spa

*A hotel management system for a forest retreat hotel*

This full stack hotel management system is built for use of taking bookings and payment for a forest retreat hotel in the region of Nunisi in Georgia. The business audience is the hotel owners and the target audience for the site are travellers who are seeking a relaxing getaway, either travelling domestically or internationally. The website was created using custom code written in HTML, CSS, Python, and JavaScript , utilising the full stack framework Django. It is hosted on Heroku with static files hosted by Amazon Web Services (AWS), has a connected PostgreSQL relational database and provides the users full CRUD functionality. It provides users with the ability to create and log into a user profile in order to track their previous and upcoming trips and leave reviews. This allows for easier administration by users in the lead up to their trip and a way of verifying reviews so that the business owner can know that recieved reviews are genuine.

The live site can be viewed [here](https://nunisi-hotel-and-spa-39411ddf3dfa.herokuapp.com/)

See [DESIGN.md](/DESIGN.md) for information on the five planes of UX design, site map, database schema, and features. <br>
See [TESTING.md](/TESTING.md) for information on the test driven development of the website, manual and automated testing of the site, bugs encountered, and website analytics. <br>
See [DEV.md](/DEV.md) for an overview of the continuous integration and deployment process, how I set up my development environment, and deployment steps.

---

## Table of Contents
1. [Project Goals](#project-goals)
    1. [User Goals](#user-goals)
    2. [Site Owner Goals](#site-owner-goals)
    3. [Developer Goals](#developer-goals)
2. [User Stories](#user-stories)
3. [Security](#security)
    1. [Defensive Programming](#defensive-programming)
    2. [Form Validation](#form-validation)
4. [Future Development](#future-development)
5. [Technologies Used](#technologies-used)
    1. [Languages](#languages)
    2. [Frameworks](#frameworks)
    3. [Libraries and Packages](#libraries-and-packages)
    4. [Tools](#tools)
6. [User Feedback](#user-feedback)
7. [Credits](#credits)
    1. [Images](#images)
8. [Acknowledgements](#acknowledgements)



## Project Goals

### User Goals
- A website that is easy to navigate.
- A website that will display well on different devices.
- Positive and immediate feedback from the site such as on hover or on click JavaScript animations to ensure a good user experience.
- Contact information of the developer.
- Able to create an account to log in and out.
- Able to opt in/out to promotional emails.
- Full CRUD (Create Read Update Delete) functionality on my user account.
- Ability to book a room.
- Partial CRUD functionality for the user to create and read their Trip, request cancellation and edit/remove a review on a previous trip. With full update capability for admins via the admin portal and cancel/uncancel capability for the admins via the webapp.
- Ability to leave a review.
- Full CRUD functionality on my review.
- Security in place to stop others accessing my account and trip.
- A secure payment method to pay for the trip.
- Ability to search for available rooms within a given timeframe.
- Ability to restrict or order available rooms based on amenities offered.
- Have my data and information stored securely.

### Site Owner Goals
- Provide the user with room options with correct details and availability.
- Able to track when rooms are not available.
- Able to take payment from the users.
- Able to receive reviews from the users.
- Provide a website that is safe for users to sign up to and that their data is handled securely.

### Developer Goals
- A well designed website that catches the attention of the users.
- A responsive website where the functionality is not impacted by screen size.
- Easy navigation that is intuitive and responsive.
- A website designed with accessibility in mind.
- A back end that will handle user details, room details, and trip details.
- A finished product that will proudly be displayed within the developer's portfolio.

## User Stories

| User Story ID | As A/An | I Want To Be Able To... | So That I Can... |
|-----|------|-----|-----|
|<td colspan="4">**Viewing and Navigation**</td>|
| 1 | First Time Visitor | Tell the purpose of the website immediately | Decide whether I want to use the website |
| 2 | First Time Visitor | Navigate the website easily and intuitively | I can find the content that I need |
| 3 | First Time Visitor | Find out more about the hotel and resort | I can decide whether I would like to visit |
| 4 | First Time Visitor | See various services and facilities that the resort offers | Plan my stay there |
| 5 | First Time Visitor | See some FAQs | Be well informed |
| 6 | First Time Visitor | See the location of the resort | Plan my trip accordingly |
| 7 | First Time Visitor | See reviews of guests who have stayed at the resort | Make a well informed decision about travelling |
| 8 | First Time Visitor | Know that my interactions on the website have worked | Be sure that the website is resposinsive |
| 9 | First Time Visitor | Be informed if I land on a non-existant or restricted page | Be sure of what happened and be redirected back to the homepage |
| 10 | First Time Visitor | Contact the developer | Collaborate on a similar project for my business |
|<td colspan="4">**Registration and User Accounts**</td>|
| 11 | Site User | Have the site content to be safe and secure | Know that I am not open to any malicious activities |
| 12 | Site User | Easily register for an account | Track my previous purchases |
| 13 | Site User | Create an account under my email, rather than create a username | Login quicker in future and not forget my login details |
| 14 | Site User | Sign up with my various social media or other accounts | Sign up and log in quicker and easier |
| 15 | Site User | Receive an email confirmation after registering | Verify that my account registration was successful |
| 16 | Site User | Easily login or logout | Keep my data is secure when I use a shared device |
| 17 | Site User | Update my password | Keep my account secure over time |
| 18 | Site User | Reset my password if I forget it | Continue to access my account |
| 19 | Site User | Delete my account if I wish | Retain agency over my information |
| 20 | Site User | Sign up to a newsletter | Receive updates and offers for my future trips |
| 21 | Site User | Leave a review | Let others know of my experience |
|<td colspan="4">**Sorting and Searching**</td>|
| 22 | Potential Guest | Search for room availability based on how many people will be going and when | See choices that suit my needs |
| 23 | Potential Guest | Filter and sort the available rooms | Find the best room for me |
| 24 | Potential Guest | Find out more information about the rooms | Be sure I am making the correct choice |
| 25 | Potential Guest | See and sort my previous trips | Keep track of them for my records |
|<td colspan="4">**Purchasing and Checkout**</td>|
| 26 | Guest | Book the room through the website | I can book easily and by convenience |
| 27 | Guest | Easily select dates and number of guests | Ensure I do not book for the correct amount of people on the correct dates |
| 28 | Guest | Easily enter my payment information | Check out quickly and with no hassles |
| 29 | Guest | Feel my personal and payment information is safe and secure | Confidently provide the needed information to make a purchase. |
| 30 | Guest | View an order confirmation after checkout | Verify that I haven't made any mistakes |
| 31 | Guest | Receive an email confirmation after checking out | Keep the confirmation of what I've purchased for my records |
| 32 | Guest | Be prompted to make an account/login to save this trip to "my trips" if I have booked a trip whilst logged out | To maintain a record of my trips |
|<td colspan="4">**Admin and Store Management**</td>|
| 33 | Business Owner | Sure that the room availability is updated correctly with each booking and cancellation | Avoid scheduling conflicts |
| 34 | Business Owner | Have the payment system easy and secure | Have the rooms paid for |
| 35 | Business Owner | See information on user accounts | Adjust my business needs to demand |
| 36 | Business Owner | Add, update, and delete rooms on the database | Keep the information on the website current and correct |
| 37 | Business Owner | See reviews for user trips | Improve as a business |

## Security

**.gitignore**<br>
One of the security steps taken was to put all sensitive and irrelevant information in the .gitignore file so as to not upload them to the public online repository. Those added to this file were:
| Inclusion in .gitignore | Reasoning |
|-----|-----|
| *.sqlite3 | Prevent SQLite database files being tracked by GitHub, as it contains local data that is either not relevant to the development or potentially sensitive. |
| \_\_pycache__ | Contains files generated by the python interpreter which are recreated as needed, so is removed from the version control in order to decrease the size and clutter of the repository. |
| venv | It has the virtual environment information including paths and configurations that won't work for other developers or environments. So it was added to .gitignore to reduce redundancy and clutter in the repository. |
| env.py | To hide sensitive information such as… |
|.coverage| The coverage reports for the testing will not require hosting on the repository. Instead, final coverage reports will be added to the [TESTING.md](/TESTING.md) file|
| htmlcov/ | This folder houses the html coverage reports which do not require hosting on the repository. |

**Meta Data**<br>
Some of the meta data included in the head element of the base template and reproduced across every page of the site add extra security to the webapp. 
```html
<meta http-equiv="X-UA-Compatible" content="ie=edge">
```
This makes internet explorer avoid compatability issues with older versions of itself that may themselves have security vulnerabilities.
```html
<meta charset="utf-8">
```
UTF-8 encoding prevents character encoding mismatches that could result in vulnerabilities with cross-site scripting or malicious user input.

**Django Allauth**<br>
AllAuth is an open source Django package that I used to handle user authentication on the website. It is open source, so it is backed by millions of developers who keep it up to date and secure, providing a key part in the security of this website and data-security of the users who will create user accounts with us. The client ID and secret keys for the social sign-ins are kept in the secure admin dashboard.

**crsf tokens**<br>
These are present in all forms on the website, preventing from Cross-site Request Forgery attacks, confirming that the form is submitted by a real user, not a malicious third party.

**Password Security**<br>
Django AllAuth uses the password hashing algorithm PBKDF2 to hash passwords before storing them, allowing them to be stored securely and for the possibility for multiple users to have the same password without impacting site security.

**Email Validation**<br>
As a part of Django-allauth, email validation is required to prevent fake accounts, verify ownership of the email address, and to reduce phishing risks.

**External links**<br>
All external links open in a new tab and have rel="noopener" to prevent the opened page from accessing the pages on this website, increasing security.

**Access required**<br>
On certain pages, the view only loads the page if the user is a superuser or is logged in depending on the requiremnet.

**env.py**<br>
All sensitive values such as passcodes and secret keys were kept in an env.py file and added to the .gitignore in order to prevent them being posted online. An example of the setup of my env.py can be found [here](/env_example.txt) to help set up yours.

### Defensive Programming

**Password confirmation**<br>
The signup form requires a confirmation of the password to prevent the user from making a typo.

**Email login**<br>
The site login requires the user's email address, since it is harder to recall a username. Since the website does not include any user to user interactions, usernames were deemed an unnecessary complication for users.

**Logout page**<br>
When logging out the user is redirected to a page to confirm log out, preventing the user from logging out accidentally.

**Forms**<br>
Forms throughout the site are defined with required fields when necessary. These prevent the user from submitting an incomplete form and provide a pop up alerting the user as to why the form wasn't submitted.

**Delete room/user**<br>
The delete room/user functionality redirects the user to a confirmation page to remove the chance of accidentally deleting a room or account.

**Delete review modal**<br>
The delete review modal pops up to make the user confirm a deletion, preventing them from accidentally deleting thier review with one mouse click.

### Form validation
Form validation is handled throughout the website. When needing more than the built in validation tools, these are included in the forms when a model is accessed or in the view for accessing the database (e.g. searching for available rooms). A good example of this is in the review forms.py file, where there are defined cleaning steps to ensure that the content is a certain length, all sections are present and that the trip being reviewed is in the past.

## Future Development
- Footer
    * Facebook and Instagram links will be updated with the real profiles when the website is ready to go live.
- Allauth updates
    * redirect user to profile page after updating password
- index.html
    * better carousel transitions
- rooms_superuser.html
    * Add carousel for multiple room images
- trips_superuser.html
    * Add column filtering
- user_profile
    * An admin only page allowing them to send an email to everyone signed up to the newsletter
    * An admin only page to show trends in booking and graphical representations of booking trends over the year

## Technologies Used

### Languages
- [HTML](https://en.wikipedia.org/wiki/HTML)
    - Markup language used for website structure.
- [CSS](https://en.wikipedia.org/wiki/CSS)
    - Used for styling the elements on the webpage.
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
    - Used for dynamic functionality on the website.
- [Python](https://www.python.org/)
    - Used for server side scripting and backend development.
- [SQL](https://en.wikipedia.org/wiki/SQL)
    - Used for maintenance and querying of database throughout to confirm correct functionality.

### Frameworks
- [Django](https://www.djangoproject.com/)
    - Django is a full server-side framework used to build this web app. It is written in python and provides batteries and low-level automation that makes it easier to build a better web app with less code.

### Libraries and Packages
- [Pip](https://pypi.org/project/pip/)
    - The package installer for python used to install packages and libraries.
- [Django Allauth](https://django-allauth.readthedocs.io/en/latest/)
    - Used for user authentication along with registration and account management.
- [Stripe](https://stripe.com/gb)
    - Used for processing and handling payments securely
- [Pillow](https://pypi.org/project/pillow/)
    - Adds image processing to the python interpretor
- [Django countries](https://pypi.org/project/django-countries/)
    - Used to submit country codes to stripe
- [Bootstrap 5](https://getbootstrap.com/docs/5.0/getting-started/introduction/)
    - Used for some styling and site functionality
- [JQuery](https://jquery.com/)
    - Used for some JavaScript code
- [DateTime](https://docs.python.org/3/library/datetime.html)
    - Used for providing date data
- [dj-database-url](https://pypi.org/project/dj-database-url/)
    - For connecting to an external database
- [psycopg2](https://pypi.org/project/psycopg2/)
    - For connecting to an external database
- [gunicorn](https://gunicorn.org/)
    - For the webserver
- [django-storages](https://django-storages.readthedocs.io/en/latest/)
    - Provides support for storage backend
- [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
    - To create a pythonic link between the django application and the S3 bucket

### Tools
- [Visual Studio Code](https://code.visualstudio.com/)
    - This is my IDE of choice for writing my HTML, CSS, JavaScript, and Python code for this project
- [Git](https://git-scm.com/)
	- Used for version control.
- [GitHub](https://github.com/)
	- Used to store the code in a repository
- [Heroku](https://dashboard.heroku.com/login)
    - For deploying the live website
- [Amazon Web Servives (AWS)](https://aws.amazon.com/)
    - For hosting the static files
- [Gmail](/https://gmail.com/)
    - For sending emails
- [Google Developer Tools](https://console.cloud.google.com/apis/dashboard)
    - Used to implement google login and verification
- [Google Fonts](https://fonts.google.com/)
    - Used to get different typefaces and fonts for the project
- [Google Maps](https://www.google.com/maps/)
    - Used for the interactive location map
- [Favicon](https://favicon.io/)
    - Used for creating an icon in the browser tab
- [FontAwesome](https://fontawesome.com/)
    - Used for icons throughout
- [Balsamiq Wireframes](https://balsamiq.com/)
    - Used for creating wireframes for the project
- [Logo Design AI](https://logodesign.ai/)
    - Used for creating the site logo
- [BGJar](https://bgjar.com/)
    - Used for creating the website background
- [Pexels](https://www.pexels.com/)
    - Used for stock images across the website
- [Coolers](https://coolors.co/)
    - Used to visualise the colour palette
- [CloudConvert](https://cloudconvert.com/)
    - Used for compressing images to .webp format for better performance
- [W3C HTML Validator](https://validator.w3.org/)
    - For validating the HTML on each page
- [Jigsaw CSS Validator](https://jigsaw.w3.org/css-validator/)
    - For validating all CSS files
- [JSLint](https://www.jslint.com/)
    - For validating all JavaScript scripts
- [CodeInstitute Pep8 Validator](https://pep8ci.herokuapp.com/)
    - For validating python code


## User Feedback
The website was reviewed by friends and family during development. This allowed me to ensure that the highest standards were continuously met by providing feedback on this that did not work well or that were missing. These can be seen during the commits at around halfway through the development, where changes to previously completed apps and issues were revisited the key changes made due to the feedback were:
- Moving trips to its own app for clearer code management
- Adding "back" buttons to pages that needed them for a better user experience
- Allowing the hotel owner to cancel trips using a user interface instead of the admin page
- Adding pagination to available room results and past trips
- Add sorting and filtering to available rooms
- Add sorting to past trips
- Add CRUD for reviews

Additionally, this provided feedback from different screen sizes that I had tested and other browsers that I did not have access to (Safari and Opera). There were no complaints with the working of the website.

## Credits
[Cloud With Django](https://www.youtube.com/watch?v=JQVQcNN0cXE) for correct syntax and setup for linking AWS static files to a deployed django project.

### Images
- All images of the hotel and surrounding areas were used with permission from the hotel owners
- Homepage massage image: [Andrea Piacquadio](https://www.pexels.com/photo/topless-woman-lying-on-bed-getting-massage-3757952/)
- Homepage cave hike image: [Roberto Lee Cortes](https://www.pexels.com/photo/trees-behind-cave-entrance-17652141/)
- Homepage forest river: [Manuela Alder](https://www.pexels.com/photo/body-of-water-across-forest-949194/)
- Homepage location map image: [Waldir Felix Chirinos](https://www.istockphoto.com/photo/georgia-imereti-region-map-administrative-divisions-of-georgia-3d-isometric-map-gm2175464797-595023374)

## Acknowledgements
- The remaining members of my Code Institute learning cohort for their support and comradery
- My friends and relatives who provided keen insights and constructive criticism during development
- My wife who did her very best impression of a rubber duck to help debug the more complex code