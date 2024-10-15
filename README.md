![Website logo](/linktologoimage.png)

---

# Nunisi Hotel and Spa

*A hotel management system for a forest retreat hotel*

This full stack hotel management system is built for use of taking bookings and payment for a forest retreat hotel in the region of Nunisi in Georgia. The business audience is the hotel owners and the target audience for the site are travellers who are seeking a relaxing getaway, either travelling domestically or internationally. The website was created using custom code written in HTML, CSS, Python, and JavaScript , utilising the full stack framework Django. It is hosted on Heroku with a connected PostgreSQL relational database and provides the users full CRUD functionality.


![A mock-up image of the website](/linktomockupimage.png)

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
    2. [Future Security Implementations](#future-security-implementations)
4. [Future Development](#future-development)
5. [Technologies Used](#technologies-used)
    1. [Languages](#languages)
    2. [Frameworks](#frameworks)
    3. [Libraries and Packages](#libraries-and-packages)
    4. [Tools](#tools)
6. [User Feedback](#user-feedback)
7. [Credits](#credits)
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
- Full CRUD functionality on my planned trip.
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
- A back end that will handle user details, toy details, and review details.
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

**Django Allauth**<br>
AllAuth is an open source Django package that I used to handle user authentication on the website. It is open source, so it is backed by millions of developers who keep it up to date and secure, providing a key part in the security of this website and data-security of the users who will create user accounts with us. The client ID and secret keys for the social sign-ins are kept in the secure admin dashboard.

**Password Security**<br>
Django AllAuth uses the password hashing algorithm PBKDF2 to hash passwords before storing them, allowing them to be stored securely and for the possibility for multiple users to have the same password without impacting site security.

**Email Validation**<br>
As a part of Django-allauth, email validation is required to prevent fake accounts, verify ownership of the email address, and to reduce phishing risks.

### Defensive Programming

**Password confirmation**<br>
The signup form requires a confirmation of the password to prevent the user from making a typo.

### Future Security Implementations

## Future Development

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

### Tools
- [Visual Studio Code](https://code.visualstudio.com/)
    - This is my IDE of choice for writing my HTML, CSS, JavaScript, and Python code for this project
- [Git](https://git-scm.com/)
	- Used for version control.
- [GitHub](https://github.com/)
	- Used to store the code in a repository.
- [Google Developer Tools](https://console.cloud.google.com/apis/dashboard)
    - Used to implement google login and verification

## User Feedback

## Credits

## Acknowledgements
