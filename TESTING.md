![Website logo](/linktologoimage.png)

---

# Testing
Manual testing (often called user testing) is where the site is manually tested from the point of view of the user by actions such as clicking buttons, filling out forms, and testing that all the behind the scenes logic creates the intended user experience. Automated testing involves using scripts and a testing frameworks to test functionality automatically. Automated testing can be quick, thorough, and allow the developer to pick up errors early on but relies on the developer asking the right questions and does not test for user experience. For this project, I heavily tested both with automated testing and manual testing.<br>

I have taken a Test Driven Development (TDD) approach when implementing python functionality in the Django framework through unit and integration testing. This is characterised by a three stage cycle. Stage 1 (Red): Where a simple test is written that will fail, as the functional code has not yet been written. This can be seen in the git commits used for version control with the tag of "test: [TDD Red]". Stage 2 (Green): Involves writing simple code that passes this test. This can be seen in the git commits with the tag "test: [TDD Green]. Stage 3 (Refactor): When the test passes 100%, the code is refactored to either reduce size or make it more succinct whilst still passing the test. After stage 3 is complete, stage 1 is undergone again for the next step of functionality. In this way, I have ensured that the functionality of my code works as expected from the start and that any issues I encounter are fixed more easily, as with the saying about TDD: "I know my code worked 30 seconds ago."<br>

When new functionality is implemented, unit tests local to the specific app or function are run first. When the function is proved to run without error, all written automated tests are run as an integration test to ensure that there has not been an impact on other functionality. This type of regression testing allows bugs to be caught when code interacts in a way that was not intended and ensures that the web app will work as expected as a whole. A similar process is taken when manual testing; the feature is tested as it is introduced and then all the features are tested when the web page is complete and when extra features are added in the future.<br>

To ensure that the website is fully tested, the Django coverage app is used to produce reports and highlight areas that are not tested to their fullest. This simple tool allowed me to ensure that the webapp was tested in its totality.

See [README.md](/README.md) for information on project goals, user stories, security, future developments, technologies used, user feedback, credits, and acknowledgements. <br>
See [DESIGN.md](/DESIGN.md) for information on the five planes of UX design, site map, database schema, and features. <br>
See [DEV.md](/DEV.md) for an overview of the continuous integration and deployment process, how I set up my development environment, and deployment steps.

---

## Table Of Contents

1. [Testing User Stories](#testing-user-stories)
2. [Manual Testing](#manual-testing)
3. [Device and Browser Testing](#device-and-browser-testing)
4. [Automated Testing](#automated-testing)
    - [Test Driven Development](#test-driven-development)
    - [Accessibility Testing](#accessibility-testing)
    - [Performance Testing](#performance-testing)
    - [HTML Validation](#html-validation)
    - [CSS Validation](#css-validation)
    - [JavaScript Validation](#javascript-validation)
    - [Python Validation](#python-validation)
5. [Bugs](#bugs)
    - [Bug 1](#bug-1)
    - [Bug 2](#bug-2)
    - [Bug 3](#bug-3)
    - [Known Bugs](#known-bugs)
6. [Analytics](#analytics)

## Testing User Stories
The [user stories](/README.md#user-stories) have been a driving force for the development of this project. More information on each user story and how the features implemented in this web app meet their criteria can be seen [here](/DESIGN.md#features). All user story criteria were met, creating a website that the target audience of the hotel owners and travellers will find usable, intuitive, and fit for purpose.

## Manual Testing

| Feature | Action | Expected results | Passed | Comments |
| ----- | ----- | ----- | ----- | ----- |
| **base.html** | | | | |
| Site logo - header | Click | Redirected to the hompage | Y | N/A |
| Site logo - footer | Click | Redirected to the hompage | Y | N/A |
| Booking form | Submit with empty fields | Prompt to enter a check in date | Y | N/A |
| Booking form | Submit with only check in date | Prompt to enter a check out date | Y | N/A |
| Booking form | Submit with dates and no guests | Prompt to add guests | N | [Bug 1](#bug-1) highlighted and fixed |
| Booking form | Submit with dates and no guests | Prompt to add guests | Y | N/A |
| Booking form | Click check in/check out | Calendar widget appears to select dates | Y | N/A |
| Booking form | Open check in/ check out calendar widgets | Dates in the past are disabled | Y | N/A |
| Booking form | Open check in/ check out calendar widgets | Dates over a year away are disabled | Y | N/A |
| Booking form | Add guests | "Guests" automatically updates to show total guests | Y | N/A |
| Booking form | Hover the submit button | The colours invert | Y | N/A |
| Booking form | Submit form with check in date after check out date | The form submits and provides the user with an error | Y | N/A |
| Booking form | Submit correct data | The form submits and redirects the user to a page showing the available rooms | Y | N/A |
| Account menu | Hover | The border becomes bolder and larger | Y | N/A |
| Account menu | Click when logged out| Display login/signup links | Y | N/A |
| Account menu - sign up link | Click | Redirected to the sign up page | Y | N/A |
| Account menu - log in link | Click | Redirected to the log in page | Y | N/A |
| Account menu | Click when logged in | Displays Trips/Account Settings/Log out links | Y | N/A |
| Account menu - Trips link | Click | Redirected to Trips page | Y | N/A |
| Account menu - Rooms link | Click | Redirected to the Rooms page | Y | N/A |
| Account menu - Account Settings link | Click | Redirected to account settings page | Y | N/A |
| Account menu - Logout | Redirected to log out page | Y | N/A |
| Account menu | Click when logged in as Admin | See an extra link for Rooms | Y | N/A |
| Account menu | Click Trips when logged in as Admin | Redirected to trips super user page | Y | N/A |
| Account meny | Click Rooms when logged in as Admin | Redirected to rooms super user page | Y | N/A |
| Hotel Facebook icon | Hover | Icon turns to Facebook brand colours | Y | N/A |
| Hotel Facebook icon | Click | Opens the Facebook homepage in a new tab | Y | N/A |
| Hotel Instagram icon | Hover | Icon turns to Instagram brand colours | Y | N/A |
| Hotel Instagram icon | Click | Opens the Instagram homepage in a new tab | Y | N/A |
| Hotel email address | Hover | Text becomes bold | Y | N/A |
| Hotel email address | Click | Opens a new email draft to the hotel email address | Y | N/A |
| Developer GitHub link | Hover | Icon turns to GitHub brand colours | Y | N/A |
| Developer GitHub link | Click | The developer's github profile is opened in a new tab | Y | N/A |
| Responsivity | Reduce screen size to below 992px | Booking form disappears | Y | N/A |
| Responsivity | Reduce screen size to below 992px | Footer logo disappears | Y | N/A |
| **AllAuth Pages** | | | | |
| Sign up form | Enter an incorrect email address | Prompt appears telling the user to enter a valid email | Y | N/A |
| Sign up form | Do not enter the password again | Prompt appears telling the user to fill out that field | Y | N/A |
| Sign up form | Incorrectly confirm the password | Error appears informing the user that the passwords do not match | Y | N/A |
| Sign up form | Enter invalid passwords | Errors appear informing users on why the password failed to meet specifications | Y | N/A |
| Sign up form | Hover submit button | Button colours invert | Y | N/A |
| Sign up form | Click sign up with google | Redirected to Sign in via Google page | Y | N/A |
| Sign in form | Enter incorrect email | Error appears saying The email address and/or password you specified are not correct | Y | N/A |
| Sign in form | Enter incorrect password | Error appears saying The email address and/or password you specified are not correct | Y | N/A |
| Sign in form | Hover submit button | Colours invert | Y | N/A |
| Sign in form | Successfully sign in | User redirected to home page | Y | N/A |
| Sign in page | Click sign in with google | User redirected to Sign In Via Google Page | Y | N/A |
| Log out page | Hover the sign out button | Button colours invert | Y | N/A |
| Log out page | Click the sign out button | User signed out and redirected to the home screen | Y | N/A |
| Reauthenticate page | Hover the confirm button | Button colours are inverted | Y | N/A |
| Reauthenticate page | Submit an incorrect password | An incorrect password error appears | Y | N/A |
| Reauthenticate page | Submit correct password | User is redirected to the homepage | Y | N/A |
| Emails page | Hover buttons | Button colours invert | Y | N/A |
| Emails page | Add a new email | New unverified email is added to the list | Y | N/A |
| Emails page | Select unverified email and click resend verification | Verification email resent | Y | N/A |
| Emails page | GO through email verification | Email is tagged as verfied | Y | N/A |
| Emails page | Change primary email | Primary email tag is moved to new email | Y | N/A |
| Emails page | Remove an email | Email is deleted | Y | N/A |
| Email validation | Hover confirm button | Button colours invert | Y | N/A |
| Email validation | Click confirm | Email becomes verified and redirected to sign in page | Y | N/A |
| Email validation | Go on page when already verified and hover and click the email confirmation request | Text is boldened on hover and new verification sent and redirected to sign in page | Y | N/A |
| Change password | Change password with invalid current password | Alert shows that the current password is incorrect | Y | N/A |
| Change password | Change password with invalid new password | Specific alerts show the user what is wrong with the new password | Y | N/A |
| Change password | Change password with valid password | Page refreshes and password updated | Y | N/A |
| Change password | Click "Forgot password?" | Text bolds on hover and redirects user to reset password page on click | Y | N/A |
| Reset Password | Enter an invalid email address (no @ sign) | Error appears informing user to use a valid email address | Y | N/A |
| Reset Password | Hover reset password button | Button colours invert | Y | N/A |
| Reset Password | Enter valid email address and submit | Email sent with password reset link and user redirected to /password/reset/done page | Y | N/A |
| Google login | Hover continue button | Button colours invert | Y | N/A |
| Google login | Click continue | Redirected to Google access page | Y | N/A |
| Google login | Sign up with Google | Allows login with the Google account | Y | N/A |
| **Homepage** | | | | |
| Header | Hover links | Link background darkens | Y | N/A |
| Header | Click links | Page scrolls to respective section | Y | N/A |
| Header | Reduce screen size | Header collapses to a burger menu | Y | N/A |
| Header | Click the links in the burger menu | Page scrolls to section and burger menu closes | Y | N/A |
| Header | Scroll down the page | Header stays at top of the page view | Y | N/A |
| Booking form | Reduce screen size | Booking form appears as the navigation booking for vanishes | Y | N/A |
| About us | Click next/previous on carousel | Image changes to the next/previous image | Y | N/A |
| Services | Click next/previous on carousel | Card changes to the next/previous service card | Y | N/A |
| Location | Manipulate Google Map | Works as expected | Y | N/A |
| Location | Reduce screen size | Map is put under the text | Y | N/A |
| FAQs | Reduce screen size | Columns go from 3 to 1 | Y | N/A |
| **available_rooms.html** | | | | |
| Page loading | Submit an availability search | The page loads with the search form prefilled with the user submitted values | Y | N/A |
| Page loading | Submit an invalid availability search | The page loads a message informing the user of the errors in the form | Y | N/A |
| Page loading | Submit a valid form that matches no criteria | The page loads with a message informing the user that there are no matches to their search | Y | N/A |
| Page loading | Submit a valid search form | The page loads and displays available rooms | Y | N/A |
| Room card | Hover book now button | Cursor changes and button colour inverts | Y | N/A |
| Room card | Resize page | Image drops below room information on smaller screens | Y | N/A |
| **rooms_superuser.html** | | | | |
| Add room button | Hover | Button colours invert | Y | N/A |
| Add room button | Click | Redirected to add room page | Y | N/A |
| Edit room link | Hover | Text bolds | Y | N/A |
| Edit room link | Click | Redirected to edit room page | Y | N/A |
| Delete room link | Hover | Text bolds | Y | N/A |
| Delete room link | Click | Redirected to edit room page | Y | N/A |
| Rooms page | Resize page | Rooms are displayed in a row of 3 on large screens, 2 on medium, and 1 on small | Y | N/A |
| **add_room.html** | | | | |
| Add room button | Hover | Button colours invert | Y | N/A |
| Add room button | Click | Room created and redirected to superuser room page | Y | N/A |
| Add room form | Complete form and submit | Room created and redirected to superuser room page | Y | N/A |
| **edit_room.html** | | | | |
| Edit room button | Hover | Button colours invert | Y | N/A |
| Edit room button | Click | Room updated and redirected to superuser room page | Y | N/A |
| Edit room form | Complete form and submit | Room updated with new values and redirected to superuser room page | Y | N/A |
| **delete_room.html** | | | | |
| Delete room button | Hover | Button colours invert | Y | N/A |
| Delete room button | Click | Room instance is deleted and redirected to superuser rooms page | Y | N/A |
| **checkout.html** | | | | |
| Load page | N/A | Form is pre-filled with profile data | Y | N/A |
| Load page | N/A | Correct trip details appear on the page | Y | N/A |
| Checkout form | Leave name input empty | Alert appears informing user to provide name | Y | N/A |
| Checkout form | Leave email input empty | Alert appears informing user to provide email | Y | N/A |
| Checkout form | Leave phone number input empty | Alert appears informing user to provide phone number | Y | N/A |
| Checkout form | Leave street address 1 input empty | Alert appears informing user to provide street address | Y | N/A |
| Checkout form | Leave town or city input empty | Alert appears informing user to provide town or city | Y | N/A |
| Checkout form | Leave country input empty | Alert appears informing user to provide country | Y | N/A |
| Checkout form | Provide incorrect credit card information | Alerts appear informing user to credit card errors | Y | N/A |
| Checkout form | Provide correct data and submit | The form is submitted, order created, trip created, and confirmation email sent | | |
| Checkout form | Hover Pay Now button | Button colour inverts | Y | N/A |







## Device and Browser Testing
I tested the responsiveness of the website using Google Chrome Devtools to simulate 17 screen sizes; ranging from large desktops to the iPhone 5/SE and am happy to report that the website appears and functions as intended across the large screen size range. Additionally the website was tested on the Google Chrome, Mozzila Firefox, Microsoft Edge, and Brave browsers and no issues were encountered. I also tested the website on my 17.5" Laptop, 14" Laptop, and smart phone, noticing that it worked well in each case.

## Automated Testing

### Test Driven Development

The tests written during my TDD along with all other unit and integration tests were tested for their completeness with the Django coverage app. To install coverage, you can use the pip package manager with:
```sh
pip install coverage
```
The test can then be run with:
```sh
coverage run --source-project_name manage.py test
```
A report can be compiled with:
```sh
coverage report
```

Here is the the coverage report of my Django testing:
![Coverage Report](/linktoreport)

Discussion of report:

**Errors**:
- When doing TDD for the available_rooms view, the commits were added at the end of the process, obscuring the order of the testing, however these were done following the TDD philosophy.

### Accessibility Testing
Accessibility was kept in mind throughout development and the best practices were kept to across the website including, but not limited to, ensuring aria-labels and alt texts were used throughout, using semantic HTML, creating easy to see colour contrasts. Where hidden text was used, it was hidden in a way that was still accessible to screen readers.
Accessibility testing was performed using the [Wave](https://wave.webaim.org/) validator to provide key information about the accessibility standard of the website. Pages that required login were beyond the purview of the [Wave](https://wave.webaim.org/) browser tool, so the Wave extension for Google Chrome was used, which can be found [here](https://wave.webaim.org/extension/).

**Allauth: Login**<br>
- Alert: Redundant text title of "Google" on the link for 3rd party login. This is required for good user experience so the alert was ignored.
<details>
<summary>Login results</summary>
<img src="/documentation/testing/wave/allauth_login.png">
</details><br>

**Allauth: Logout**<br>
- No errors or alerts
<details>
<summary>Logout results</summary>
<img src="/documentation/testing/wave/allauth_logout.png">
</details><br>

**Allauth: Inactive**<br>
- No errors or alerts
<details>
<summary>Inactive results</summary>
<img src="/documentation/testing/wave/allauth_inactive.png">
</details><br>

**Allauth: Signup**<br>
- Alert: Redundant link for "sign up" but it is required below the title to redirect the user if they already have an account as well as in the navigation bar so was ignored.
- Alert: Redundant text title of "Google" on the link for 3rd party login. This is required for good user experience so the alert was ignored.
<details>
<summary>Signup results</summary>
<img src="/documentation/testing/wave/allauth_signup.png">
</details><br>

**Allauth: Reauthenticate**<br>
- No errors or alerts
<details>
<summary>Reauthenticate results</summary>
<img src="/documentation/testing/wave/allauth_reauthenticate.png">
</details><br>

**Allauth: Emails**<br>
- No errors or alerts
<details>
<summary>Emails results</summary>
<img src="/documentation/testing/wave/allauth_emails.png">
</details><br>

**Allauth: Confirm Email**<br>
- No errors or alerts
<details>
<summary>Confirm email results</summary>
<img src="/documentation/testing/wave/allauth_confirm_email.png">
</details><br>

**Allauth: Change Password**<br>
- No errors or alerts
<details>
<summary>Change password results</summary>
<img src="/documentation/testing/wave/allauth_change_password.png">
</details><br>

**Allauth: Password Reset**<br>
- No errors or alerts
<details>
<summary>Password reset results</summary>
<img src="/documentation/testing/wave/allauth_password_reset.png">
</details><br>

**Allauth: Password Reset Done**<br>
- No errors or alerts
<details>
<summary>Password reset done results</summary>
<img src="/documentation/testing/wave/allauth_password_reset_done.png">
</details><br>

**Allauth: 3rd party login cancelled**<br>
- Alert: redundant link for redirect sign up button, but this is required to explain to the user the purpose of the page and redirect them back to the sign up page.
<details>
<summary>3rd party login cancelled results</summary>
<img src="/documentation/testing/wave/allauth_3rd_party_login_cancelled.png">
</details><br>

**Allauth: 3rd party login error**<br>
- No errors or alerts
<details>
<summary>3rd party login results</summary>
<img src="/documentation/testing/wave/allauth_3rd_party_login_error.png">
</details><br>


**Allauth: Google signup**<br>
- No errors or alerts
<details>
<summary>Google signup results</summary>
<img src="/documentation/testing/wave/allauth_google_signup.png">
</details><br>


**Homepage**<br>
- Contrast error 1: Wave mistakenly takes the booking form check in label as the same colour as the background. This is not the case so has no impact on the user.
- Contrast error 2: Wave mistakenly takes the booking form check out label as the same colour as the background. This is not the case so has no impact on the user.
- Contrast error 3 and 4: Wave puts the Hero Image as a white background creating a contrast error with the white text. This is not the case and has no impact on the user.
- Contrast error 5 and 6: Similar to 3 and 4 but with the next/previous arrows on the about us carousel.
- Contrast error 7 and 8: Same as 5 and 6 but for the services carousel.
<details>
<summary>Homepage results</summary>
<img src="/documentation/testing/wave/homepage.png">
</details><br>


**Rooms: available_rooms.html**<br>
- 2 contrast errors where wave mistakes the font colour and background colour in the check in/out inputs in the navigation bar booking form, present on every page. This is not the case and has no impact on the user.
<details>
<summary>Available rooms results</summary>
<img src="/documentation/testing/wave/rooms_available_rooms.png">
</details><br>


**Rooms: rooms_superuser.html**<br>
- 2 contrast errors where wave mistakes the font colour and background colour in the check in/out inputs in the navigation bar booking form, present on every page. This is not the case and has no impact on the user.
<details>
<summary>Superuser rooms results</summary>
<img src="/documentation/testing/wave/rooms_rooms_superuser.png">
</details><br>


**Rooms: add_room.html**<br>
- 2 contrast errors where wave mistakes the font colour and background colour in the check in/out inputs in the navigation bar booking form, present on every page. This is not the case and has no impact on the user.
<details>
<summary>Add room results</summary>
<img src="/documentation/testing/wave/rooms_add_room.png">
</details><br>

**Rooms: edit_room.html**<br>
- 2 contrast errors where wave mistakes the font colour and background colour in the check in/out inputs in the navigation bar booking form, present on every page. This is not the case and has no impact on the user.
<details>
<summary>Edit room results</summary>
<img src="/documentation/testing/wave/rooms_edit_room.png">
</details><br>

**Rooms: delete_room.html**<br>
- 2 contrast errors where wave mistakes the font colour and background colour in the check in/out inputs in the navigation bar booking form, present on every page. This is not the case and has no impact on the user.
<details>
<summary>Delete room results</summary>
<img src="/documentation/testing/wave/rooms_delete_room.png">
</details><br>


**Checkout: checkout.html**<br>
- 2 contrast errors where wave mistakes the font colour and background colour in the check in/out inputs in the navigation bar booking form, present on every page. This is not the case and has no impact on the user.
<details>
<summary>Checkout results</summary>
<img src="/documentation/testing/wave/checkout_checkout.png">
</details><br>


****<br>
- No errors or alerts
<details>
<summary> results</summary>
<img src="/documentation/testing/wave">
</details><br>


****<br>
- No errors or alerts
<details>
<summary> results</summary>
<img src="/documentation/testing/wave">
</details><br>


****<br>
- No errors or alerts
<details>
<summary> results</summary>
<img src="/documentation/testing/wave">
</details><br>


****<br>
- No errors or alerts
<details>
<summary> results</summary>
<img src="/documentation/testing/wave">
</details><br>




### Performance Testing
The performance of the webpage was tested using Lighthouse within the Google Chrome Devtools to confirm that the site was performing well, is accessible, follows best practices, and follows basic SEO (search engine optimisation) advice. 
During development, care was taking to provide the best performing website that could be provided. These efforts include:
- Image optimisation: [Cloud Convert](https://cloudconvert.com/png-to-webp) was used to convert site images to smaller file formats for faster load times. .PNG files were only used where the file size was already very small, for example the bubble text on page titles. Otherwise, .WEBP and .SVG files to reduce file sizes and optimise them for web application usage.
- Code minification: Complete code minification was avoided in this project to allow easier assessment upon submission. That being said, code has been written to meet the highest standards, repetition had been removed, and short, elegant solutions have been used wherever possible in order to reduce the code size. In future minification will be used. For example [Python Minifier](https://python-minifier.com/) reduces the size of the python files from X to Y.


The performance was tested for normal internet speed, fast 3G, and slow 3G to test the performance in a majority of scenarios and locations. This was done by setting the performance network throttling in Google Chrome Devtools. The testing was also run on Google Chrome incognito mode to avoid any complications with plugins or extensions.

**Results**: The resulting screenshots are provided in [PERFORMANCE.md](/PERFORMANCE.md) but the results are discussed here.
- Errors and low value discussion

### HTML Validation
The [W3C markup validation service](https://validator.w3.org/) was used to validate the HTML of each page of this website. As each page including some Django templating language that threw errors in the validator; the HTML was validated after deployment. Each page was accessed and the source code (CTRL+U or right click > View Page Source) was copied and pasted into the validator to validate by direct input.<br>
| Page | Warnings | Errors |
| ----- | ------ | ------ |
| Allauth - login | None | None |
| Allauth - logout | None | None |
| Allauth - inactive | None | None |
| Allauth - signup | None | None |
| Allauth - reauthenticate | None | None |
| Allauth - emails | None | None |
| Allauth - confirm-email | None | None |
| Allauth - change password | None | None |
| Allauth - reset password | None | None |
| Allauth - password reset done | None | None |
| Allauth - 3rd party login cancelled | None | None |
| Allauth - 3rd party login error | None | None |
| Allauth - Google signup | None | None |
| Homepage | None | None |
| Available Rooms | None | None |
| All rooms - superuser | None | None |
| Add room | None | None |
| Edit room | None | None |
| Delete room | None | None |
| Checkout page | None | None |
| Checkout success page | None | None |

**Warnings**:
- 

**Errors**
- Explain errors here, but there should be none.


### CSS Validation
CSS validation was completed using the [W3C Jigsaw CSS validator](https://jigsaw.w3.org/css-validator/). It showed no errors in the CSS code. Explain any warnings.
<details>
    <summary>CSS validation results</summary>
    <img src="/documentation/testing/css_validation.png">
</details>

### JavaScript Validation
The custom JavaScript code was testing using the JavaScript linter [JSLint](https://www.jslint.com/). The settings were set for browser, so that the linter recognised the "document" variable. The code passed through with no errors.
<details>
    <summary>JavaScript validation results</summary>
    <img src="/documentation/testing/js_validation.png">
</details>

### Python Validation
The Python code for this project was written in strict accordance with the [PEP 8](https://peps.python.org/pep-0008/) style guide for Python code. These include using correct indentations, maximum line lengths of 79 characters, and adhering to naming conventions for variables, functions, and classes. The [Code Institue python linter](https://pep8ci.herokuapp.com/) was used to validate the written code. 

**Home: context_processor.py**<br>
- No errors or alerts
<details>
<summary>Context processor results</summary>
<img src="/documentation/testing/python/home_context_processor.png">
</details><br>

**Home: forms.py**<br>
- No errors or alerts
<details>
<summary>Froms results</summary>
<img src="/documentation/testing/python/home_forms.png">
</details><br>

**Home: views.py**<br>
- No errors or alerts
<details>
<summary>Views results</summary>
<img src="/documentation/testing/python/home_views.png">
</details><br>

**Home: urls.py**<br>
- No errors or alerts
<details>
<summary>Urls results</summary>
<img src="/documentation/testing/python/home_urls.png">
</details><br>

**Home: test_forms.py**<br>
- No errors or alerts
<details>
<summary>Test forms results</summary>
<img src="/documentation/testing/python/home_test_forms.png">
</details><br>

**Home: test_views.py**<br>
- No errors or alerts
<details>
<summary>Test views results</summary>
<img src="/documentation/testing/python/home_test_views.png">
</details><br>

**Rooms: admin.py**<br>
- No errors or alerts
<details>
<summary>Admin results</summary>
<img src="/documentation/testing/python/rooms_admin.png">
</details><br>

**Rooms: forms.py**<br>
- No errors or alerts
<details>
<summary>Forms results</summary>
<img src="/documentation/testing/python/rooms_forms.png">
</details><br>

**Rooms: models.py**<br>
- No errors or alerts
<details>
<summary>Models results</summary>
<img src="/documentation/testing/python/rooms_models.png">
</details><br>

**Rooms: views.py**<br>
- No errors or alerts
<details>
<summary>Views results</summary>
<img src="/documentation/testing/python/rooms_views.png">
</details><br>

**Rooms: urls.py**<br>
- No errors or alerts
<details>
<summary>URLs results</summary>
<img src="/documentation/testing/python/rooms_urls.png">
</details><br>

**Rooms: test_models.py**<br>
- No errors or alerts
<details>
<summary>Test models results</summary>
<img src="/documentation/testing/python/rooms_test_models.png">
</details><br>

**Rooms: test_views.py**<br>
- No errors or alerts
<details>
<summary>Test views results</summary>
<img src="/documentation/testing/python/rooms_test_views.png">
</details><br>

**Checkout: admin.py**<br>
- No errors or alerts
<details>
<summary>Admin results</summary>
<img src="/documentation/testing/python/checkout_admin.png">
</details><br>

**Checkout: forms.py**<br>
- No errors or alerts
<details>
<summary>Forms results</summary>
<img src="/documentation/testing/python/checkout_forms.png">
</details><br>

**Checkout: models.py**<br>
- No errors or alerts
<details>
<summary>Models results</summary>
<img src="/documentation/testing/python/checkout_models.png">
</details><br>

**Checkout: views.py**<br>
- No errors or alerts
<details>
<summary>Views results</summary>
<img src="/documentation/testing/python/checkout_views.png">
</details><br>

**Checkout: urls.py**<br>
- No errors or alerts
<details>
<summary>URLs results</summary>
<img src="/documentation/testing/python/checkout_urls.png">
</details><br>


**Checkout: test_forms.py**<br>
- No errors or alerts
<details>
<summary>Test forms results</summary>
<img src="/documentation/testing/python/checkout_test_forms.png">
</details><br>


**Checkout: test_models.py**<br>
- No errors or alerts
<details>
<summary>Test models results</summary>
<img src="/documentation/testing/python/checkout_test_models.png">
</details><br>


**Checkout: test_views.py**<br>
- No errors or alerts
<details>
<summary>Test views results</summary>
<img src="/documentation/testing/python/checkout_test_views.png">
</details><br>

**Checkout: webhooks.py**<br>
- No errors or alerts
<details>
<summary>Web hooks results</summary>
<img src="/documentation/testing/python/checkout_webhooks.png">
</details><br>

**Checkout: webhook_handler.py**<br>
- No errors or alerts
<details>
<summary>Webhook handler results</summary>
<img src="/documentation/testing/python/checkout_webhook_handler.png">
</details><br>



**Home: **<br>
- No errors or alerts
<details>
<summary>results</summary>
<img src="/documentation/testing/python">
</details><br>



**Home: **<br>
- No errors or alerts
<details>
<summary>results</summary>
<img src="/documentation/testing/python">
</details><br>



**Home: **<br>
- No errors or alerts
<details>
<summary>results</summary>
<img src="/documentation/testing/python">
</details><br>









The env.py file was also linted showing no errors but the screenshot has been omitted for security issues as it contains sensitive information.
<details>
    <summary>File 1 results</summary>
    <img src="/documentation/testing/python_init.png">
</details>

## Bugs

### Bug 1:
This bug occurred when creating the booking form. Initially the choice of guests was put inside a dropdown menu, making a sleek design. However upon submission of the form with invalid guest numbers; the following error happened:<br>
![Bug 1](/documentation/bugs/bug_1_not_focussable_error.png)<br>
The reason behind this is that since the number of e.g. adults was in a hidden dropdown when the form is submitted, the error cannot display correctly and the functionality cannot work. Multiple JavaScript functions were written to either display the error in the dropdown menu when the number is first entered (similar to the total guest update function) or to focus and open the dropdown menu when the form is submitted so that the input is not hidden. However, these did not fix the issue in a satisafactory way, so the decision was taken to have the inputs outside of a dropdown menu, removing this major bug.

### Bug 2:
On the homepage, the addition of the homepage header overlapped the account menu dropdown: <br>
![Bug 2](/documentation/bugs/bug_2_header_overlap.png) <br>
This was fixed by adding a CSS rule to the dropdown menu making the z-index 9999.

### Bug 3:
On the homepage, as there are two instances of the booking form (navigation bar on larger screens and body on smaller screens) there were duplicate ids for the field labels and inputs. This was rectified by creating prefixes to the form instances in the context processor for the form resulting in prefixed ids:
```python
def booking_form(request):
    '''Add the booking form to the context'''
    return {
        'booking_form_mobile': BookingForm(prefix="mobile"),
        'booking_form_desktop': BookingForm(prefix="desktop"),
    }
```

### Known Bugs

## Analytics

[Google Analytics](https://marketingplatform.google.com/about/analytics/) has been used to provide real time analytics about how users use my webpage. This includes how many page views, how many users scroll to the bottom of the page, indicating that content hinting is working, and how many users sign up. The data received from this will be used to inform the future updates to the webpage. This required the following code to be added to the base.html template at the bottom of the head element as directed:
```HTML
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-P76K2YLKVH"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      
      gtag('config', 'G-P76K2YLKVH', { 'anonymize_ip': true });
    </script> 
```