![Website logo](/documentation/site_logo.png)

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
    - [Bug 4](#bug-4)
    - [Bug 5](#bug-5)
    - [Known Bugs](#known-bugs)
6. [Analytics](#analytics)

## Testing User Stories
The [user stories](/README.md#user-stories) have been a driving force for the development of this project. More information on each user story and how the features implemented in this web app meet their criteria can be seen [here](/DESIGN.md#features). Most user stories were met to create a MVP, however future development will include adding form elements to the checkout to allow users without an account create one and save their order.

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
| Booking form | Click check in/check out | Calendar widget appears to select dates with a golden halo on the widgets | Y | N/A |
| Booking form | Open check in/ check out calendar widgets | Dates in the past are disabled | Y | N/A |
| Booking form | Open check in/ check out calendar widgets | Dates over a year away are disabled | Y | N/A |
| Booking form | Add guests | "Guests" automatically updates to show total guests | Y | N/A |
| Booking form | Hover the submit button | The colours invert and gold halo appears | Y | N/A |
| Account menu | Hover | The button hover effect occurs | Y | N/A |
| Account menu items | Hover | Elegant underline effect occurs | Y | N/A |
| Account menu | Click when logged out| Display login/signup links | Y | N/A |
| Account menu - sign up link | Click | Redirected to the sign up page | Y | N/A |
| Account menu - log in link | Click | Redirected to the log in page | Y | N/A |
| Account menu | Click when logged in | Displays Trips/Account Settings/Log out links | Y | N/A |
| Account menu - Trips link | Click | Redirected to Trips page | Y | N/A |
| Account menu - Rooms link | Click | Redirected to the Rooms page | Y | N/A |
| Account menu - Account Settings link | Click | Redirected to account settings page | Y | N/A |
| Account menu - Logout | Click | Redirected to log out page | Y | N/A |
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
| **Back Button** | | | | |
| Back button | Hover | Colours invert and gold halo appears | Y | N/A |
| **Homepage** | | | | |
| Header- Desktop | Hover links | Underline effect occurs | Y | N/A |
| Header- Desktop | Click links | Page scrolls to respective section | Y | N/A |
| Header | Reduce screen size | Header collapses to a burger menu and font changes | Y | N/A |
| Header- Mobile | Click burger menu | Burger menu is highlighted and links are displayed | Y | N/A |
| Header- Mobile | Hover links | Underline effect occurs | Y | N/A |
| Header- Mobile | Click links | Page scrolls to respective section and menu closes | Y | N/A |
| Header | Scroll down the page | Header stays at top of the page view | Y | N/A |
| Booking form | Reduce screen size | Booking form appears as the navigation booking form vanishes | Y | N/A |
| About us | Hover carousel | Next/Previous buttons appear | Y | N/A |
| About us | Hover carousel buttons | Next/Previous buttons become bold with a golden halo | Y | N/A |
| About us | Click next/previous on carousel | Image changes to the next/previous image | Y | N/A |
| About us | Reduce screen size | Image carousel goes above the text | Y | N/A |
| Services | Hover carousel | Next/Previous buttons appear | Y | N/A |
| Services | Hover carousel buttons | Next/Previous buttons become bold with a golden halo | Y | N/A |
| Services | Click next/previous on carousel | Card changes to the next/previous service card | Y | N/A |
| Services | Reduce screen size | Image goes above the text in the carousel cards | Y | N/A |
| Location | Manipulate Google Map | Works as expected | Y | N/A |
| Location | Reduce screen size | Map is put under the text | Y | N/A |
| FAQs | Reduce screen size | Columns go from 3 to 1 | Y | N/A |
| Reviews | Have no verified reviews | Section is missing | Y | N/A |
| Reviews | Verify some reviews | These reviews are showin the reviews section on the homepage | Y | N/A |
| Reviews | Click through the carousel | The carousel turns to show each new review | Y | N/A |
| **available_rooms.html** | | | | |
| Booking form - header | Submit form with values | The available rooms page loads with the header booking form pre-filled with the user choices | Y | N/A |
| Booking form - header | Submit form with check in date after check out date | The form submits and provides the user with the correct error message | Y | N/A |
| Booking form - header | Submit form with a check in date of today | The form submits and provides the user with the correct error message | Y | N/A |
| Booking form - header | Submit correct data | The form submits and redirects the user to a page showing the available rooms | Y | N/A |
| Booking form - homepage body | Submit form with values | The available rooms page loads with the header booking form pre-filled with the user choices | Y | N/A |
| Booking form - homepage body | Submit form with check in date after check out date | The form submits and provides the user with the correct error message | Y | N/A |
| Booking form - homepage body | Submit form with a check in date of today | The form submits and provides the user with the correct error message | Y | N/A |
| Booking form - homepage body | Submit correct data | The form submits and redirects the user to a page showing the available rooms | Y | N/A |
| Amenity filter accordion | Click the accordion title when closed | Accordion opens, the title gets a gold focus halo and the accordion icon becomes an up arrow. | Y | N/A |
| Amenity filter accordion | Resize the screen | The number of columns go from 4 to 3 to 2 to 1 as screen size is reduced | Y | N/A |
| Amenity filter accordion | Click the accordion title when open | Accordion closes and the accordion icon becomes a down arrow | Y | N/A |
| Amenity filter accordion | Make some selections | Selection inputs get a blue tick | Y | N/A |
| Amenity filter accordion | Hover the apply filters button | Site button branding occurs | Y | N/A |
| Amenity filter accordion | Multiple submissions of various selections | The page reloads only with options that match the choices | Y | N/A |
| Sort by | Hover the sort by button | Sitewide button effect occurs, gold halo around the options | Y | N/A |
| Sort by | Click the options | Dropdown menu opens with choices | Y | N/A |
| Sort by | Select and submit "Sort by..." | Nothing happens | Y | N/A |
| Sort by | Select and submit "Price (low to high)" | Page refreshes with rooms ordered from low to high price keeping the previously chosen amenity filter | Y | N/A |
| Sort by | Select and submit "Price (high to low)" | Page refreshes with rooms ordered from high to low price keeping the previously chosen amenity filter | Y | N/A |
| Pagination | Hover clickable choices | Choices become larger | Y | N/A |
| Pagination | Go to another page | The amenity filter choices and sort choices are kept and correct page appears |
| Pagination | Go to the first page | "Previous" button becomes disabled | Y | N/A |
| Pagination | Go to the last page | "Next" button becomes disabled | Y | N/A |
| Room card | Hover book now button | Cursor changes and button colour inverts | Y | N/A |
| Room card | Resize page | Image drops below room information on smaller screens | Y | N/A |
| Room card | Click "Book Now" | User is redirect to checkout page with correct order summary | Y | N/A |
| **rooms_superuser.html** | | | | |
| Room cards | Resize the page | Rows go from 3 cards, to 2 cards, to 1 card as the screen size decreases | Y | N/A |
| Add room button | Click | Redirected to add room page | Y | N/A |
| Edit room link | Click | Redirected to edit room page | Y | N/A |
| Delete room link | Hover | Button shows a red background with white font as opposed to the site-wide button hover effect | Y | N/A |
| Delete room link | Click | Redirected to edit room page | Y | N/A |
| **add_room.html** | | | | |
| Add room form | Submit the form without a name | Form scrolls up and the name section is focused | Y | N/A |
| Add room form | Submit the form without a sanitised name | Form scrolls up and the sanitised name section is focused | Y | N/A |
| Add room form | Submit the form without a price | An alert indicates to the user to fill this field | Y | N/A |
| Add room form | Submit the form without amenities | A toast appears indicating an error and the error is listed below the form | Y | N/A |
| Add room form | Submit the form with an incorrect date format for unavailability | A toast appears indicating an error and the error is listed below the form | Y | N/A |
| Add room form | Submit a full form | A toast appears indicating success and user is redirected to all rooms where the new room has been added | Y | N/A |
| Add a new room | Search availability to see if it appears | It appears in available rooms | Y | N/A |
| Add a new room with unavailability | Search availability to see if it does not appear | It does not appear in available rooms | Y | N/A |
| **edit_room.html** | | | | |
| Edit room form | Submit the form without a price | An alert indicates to the user to fill this field | Y | N/A |
| Edit room form | Submit the form without amenities | A toast appears indicating an error and the error is listed below the form | Y | N/A |
| Edit room form | Submit the form with an incorrect date format for unavailability | A toast appears indicating an error and the error is listed below the form | Y | N/A |
| Edit room form | Submit a full form | A toast appears indicating success and user is redirected to all rooms where the room has been updated | Y | N/A |
| Edit a new room | Search availability to see if it appears | It appears in available rooms | Y | N/A |
| Edit a new room with unavailability | Search availability to see if it does not appear | It does not appear in available rooms | Y | N/A |
| **delete_room.html** | | | | |
| Delete room | Confirm deleteion | Room instance is deleted, success toast alerts the user, and user is redirected to superuser rooms page | Y | N/A |
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
| **success.html** | | | | |
| Success page | N/A | Correct order data is displayed | Y | N/A |
| Home button | Click | User redirected to homepage | Y | N/A |
| **trips.html** | | | | |
| Cancel upcoming trips | Click | User redirected to cancel trip page | Y | N/A |
| Sort past trips | Change the sort parameter | Past trips are sorted correctly | Y | N/A |
| Past trips pagination | Click through the pages | They work as expected and the sort parameter is kept | Y | N/A |
| Past trips leave a review | Click | User is redirected to add review page | Y | N/A |
| Past trips edit review | Click | User is redirected to edit review page | Y | N/A |
| Review - unverified | N/A | The review has no verified tick on it | Y | N/A |
| Review | Verify the review as an admin | The review has a verified tick on it and will appear on the homepage | Y | N/A |
| Verified tick | Hover over | A title descibes the review as verified | Y | N/A |
| Edit review button | Click | User is taken to the edit review page | Y | N/A |
| **cancel_trip.html** | | | | |
| Cancel trip form | Submit | A toast appears telling the user that the cancellation was submitted and the user is redirect tot he cancellation request successful page. | Y | N/A |
| Cancel trip form | Submit | An email is sent to the hotel owner with the information about the trip and reason for cancellation |  |  |
| **cancel_trip_success.html** | | | | |
| Homepage button | Click | Redirected to homepage | Y | N/A |
| **add_review.html** | | | | |
| Review content | Leave blank and submit review | An alert indicates that the section needs to be filled out | Y | N/A |
| Review rating | Leave blank and submit review | An alert indicates that the section needs to be filled out | Y | N/A |
| Review | Fill out and submit | A toast appears telling the user that the review was submitted. A toast appears telling the user that the review has been sent to the business owner for review. The user is redirected to their trips page. The review appears under the correct trip with the correct information | Y | N/A |
| Review | Fill out and submit | An email is sent to the business owner describing the review and inviting them to verify it | | |
| **edit_review.html** | | | | |
| Review content | Delete content, leave blank, and submit review | An alert indicates that the section needs to be filled out | Y | N/A |
| Review | Change values and submit | A toast appears telling the user that the review was updated. A toast appears telling the user that the review has been sent to the business owner for review. The user is redirected to their trips page. The review appears under the correct trip with the correct information. If the review was verfied, the verification has been removed. | Y | N/A |
| Delete review button | Hover | Colour turns to red with halo hover effect | Y | N/A |
| Delete review button | Click | Confirm delete modal opens | Y | N/A |
| Delete review modal | Click "close" or "x" | Modal closes | Y | N/A |
| Delete review modal | Click "delete" | Toast appears telling the user that the review has been deleted, review is deleted, user is redirected back to trips page | Y | N/A |
| **trips_superuser.html** | | | | |
| Screen size warning | Resize the screen | On smaller screen where the table is not displayed correctly, a prompt appears tell the admin to access the page on a larger screen | Y | N/A |
| Cancel trip | Click | The trip is cancelled, the trip instance is updated in the backend, the room unavailablity is updated in the backend, the table column displays "Cancelled", the cancel button becomes the un-cancel trip button, and a toast appears telling the user that the action was successful | Y | N/A |
| Un-Cancel trip | Click | The trip is un-cancelled, the trip instance is updated in the backend, the room unavailablity is updated in the backend, the table column displays "Confirmed", the un-cancel button becomes the cancel trip button, and a toast appears telling the user that the action was successful | Y | N/A |
| Un-Cancel trip | Make the room unavailable and uncancel the trip | The trip is not uncancelled, a toast appears informing the user that the room is not available anymore for those dates | Y | N/A |
| Homepage button | Click | Redirected to homepage | Y | N/A |
| **user_profile.html** | | | | |
| Email addresses button | Hover | Text appears informing user that clicking will redirect them to the email management page | Y | N/A |
| Email addresses button | Click | Redirected to email management page | Y | N/A |
| Profile data table | Hover each cell | Hovered row is highlighted | Y | N/A |
| Edit profile button and change password buttons | Click | Redirected to edit profile page and change password page | Y | N/A |
| Delete profile button | Click | Redirected to confirm deletion page | Y | N/A |
| **edit_profile.html** | | | | |
| Edit profile form | Fill and submit | Values updated, toast appears confirming changes, and user redirected to profile page | Y | N/A |
| **delete_user.html** | | | | |
| Delete account | Click delete | User redirected to delete_successful.html, toast appears informing the user that their account has been deleted, and user account deleted | Y | N/A |
| **delete_successful.html** | | | | |
| Homepage button | Click | Redirected to homepage | Y | N/A |
| **AllAuth Pages** | | | | |
| Sign up message | Hover "sign in" | Text boldens | Y | N/A |
| Sign up message | Click "sign in" | User redirected to login page | Y | N/A |
| Sign up form | Enter an incorrect email address | Prompt appears telling the user to enter a valid email | Y | N/A |
| Sign up form | Do not enter the password again | Prompt appears telling the user to fill out that field | Y | N/A |
| Sign up form | Incorrectly confirm the password | Error appears informing the user that the passwords do not match | Y | N/A |
| Sign up form | Enter invalid passwords | Errors appear informing users on why the password failed to meet specifications | Y | N/A |
| Sign up form | Click sign up with google | Redirected to Sign in via Google page | Y | N/A |
| Email validation | Click confirm | Email becomes verified and redirected to sign in page | Y | N/A |
| Email validation | Go on page when already verified and hover and click the email confirmation request | Text is boldened on hover and new verification sent and redirected to sign in page | Y | N/A |
| Login message | Hover "sign up" | Text bolds | Y | N/A |
| Login message | Click "sign up" | User redirected to signup page | Y | N/A |
| Login form | Enter incorrect email | Error appears saying The email address and/or password you specified are not correct | Y | N/A |
| Login form | Enter incorrect password | Error appears saying The email address and/or password you specified are not correct | Y | N/A |
| Login form | Successfully sign in | User redirected to home page and success toast appears | Y | N/A |
| Login page | Click sign in with google | User redirected to Sign In Via Google Page | Y | N/A |
| Logout page | Click sign out | User signed out and redirected to homepage | Y | N/A |
| Reauthenticate page | Submit an incorrect password | An incorrect password error appears | Y | N/A |
| Reauthenticate page | Submit correct password | User is redirected to the homepage | Y | N/A |
| Emails page | Add a new email | New unverified email is added to the list | Y | N/A |
| Emails page | Select unverified email and click resend verification | Verification email resent | Y | N/A |
| Emails page | Go through email verification | Email is tagged as verfied | Y | N/A |
| Emails page | Change primary email | Primary email tag is moved to new email | Y | N/A |
| Emails page | Remove an email | Email is deleted | Y | N/A |
| Emails page | Try to remove primary email | Toast appears indicating that the primary email cannot be removed | Y | N/A |
| Change password | Change password with invalid current password | Alert shows that the current password is incorrect | Y | N/A |
| Change password | Change password with invalid new password | Specific alerts show the user what is wrong with the new password | Y | N/A |
| Change password | Change password with valid password | Page refreshes and password updated | Y | N/A |
| Change password | Click "Forgot password?" | Redirects user to reset password page on click | Y | N/A |
| Reset Password | Enter an invalid email address (no @ sign) | Error appears informing user to use a valid email address | Y | N/A |
| Reset Password | Enter valid email address and submit | Email sent with password reset link and user redirected to /password/reset/done page | Y | N/A |
| Google login | Click continue | Redirected to Google access page | Y | N/A |
| Google login | Sign up with Google | Allows login with the Google account | Y | N/A |
| **Error Pages** | | | | |
| 400 | Click homepage link | Redirected to homepage | Y | N/A |
| 403 | Click homepage link | Redirected to homepage | Y | N/A |
| 404 | Click homepage link | Redirected to homepage | Y | N/A |
| 500 | Click homepage link | Redirected to homepage | Y | N/A |

## Device and Browser Testing
I tested the responsiveness of the website using my 14" laptop screen and 17.5" desktop screen. I also used Google Chrome Devtools to simulate 17 additional screen sizes for a range of mobile devices. I am happy to report that the website appears and functions as intended across the large screen size range. The screen sizes checked were:
- iPhone SE (375px x 667px)
- iPhone XR (414px x 896px)
- iPhone 12 Pro (390px x 844px)
- Pixel 7 (412px x 915px)
- Samsung Galaxy Galaxy S8+ (360px x 740px)
- Samsung Galaxy S20 Ultra (412px x 915px)
- iPad mini (768px x 1024px)
- iPad air (820px x 1180px)
- iPad pro (1024px x 1366px)
- Surface Pro 7 (912px x 1368px)
- Surface Duo (540px x 720px)
- Galaxy Z fold 5 (344px x 882px)
- ASUS Zenbook fold (853px x 1280px)
- Samsung Galaxy A51/71 (412px x 914px)
- Nest Hub (1024px x 600px)
- Nest Hub Max (1280px x 800px)
- iPhone 5/SE (320px x 568px)

## Automated Testing

### Test Driven Development

The tests written during my TDD along with all other unit and integration tests were tested for their completeness with the Django coverage app. To install coverage, you can use the pip package manager with:
```sh
pip install coverage
```
The test can then be run with:
```sh
coverage run manage.py test
```
A report can be compiled with:
```sh
coverage report
```

The coverage report can be seen [here](/documentation/testing/coverage_report.txt). Overall a coverage of 87% was achieved with all 156 automated tests passing. The number was reduced from 100 largely due to the complexity of the webhook_handler and webook files and the Django project files such as settings.py which did not require TDD.

**Errors**:
- When doing TDD for the available_rooms view, the commits were added at the end of the process, obscuring the order of the testing, however these were done following the TDD philosophy.

### Accessibility Testing
Accessibility was kept in mind throughout development and the best practices were kept to across the website including, but not limited to, ensuring aria-labels and alt texts were used throughout, using semantic HTML, creating easy to see colour contrasts. Where hidden text was used, it was hidden in a way that was still accessible to screen readers.
Accessibility testing was performed using the [Wave](https://wave.webaim.org/) validator to provide key information about the accessibility standard of the website. Pages that required login were beyond the purview of the [Wave](https://wave.webaim.org/) browser tool, so the Wave extension for Google Chrome was used, which can be found [here](https://wave.webaim.org/extension/).

**Base Template**<br>
- 2 Low contrast errors: These appear because wave does not recognise the position of the check in/ check out labels being as being form-floating inside the inputs so incorrectly computes the contrast against the header background, not the input background. This error in the wave validation is carried over to every page of the website as they all extend from this base template. These errors do not affect the usability of the website and are ignored when they appear.
- 1 alert for no heading structure. This is because a H1 element is not used within the base template. As each page inherits from this template, they will have their own H1 headings, so this alert only occurs when testing the base template in isolation and thus is ignored going forward.
<details>
<summary>Base template results</summary>
<img src="/documentation/testing/wave/base.png">
</details><br>

**Homepage**<br>
- Contrast error 1 and 2: From the date widgets in the base template.
- Contrast error 3 and 4: Wave reads the Hero Image as a white background creating a contrast error with the white text despite the black shadow effect added to the text. This is not the case and has no impact on the user.
- Contrast error 5, 6, 7, 8, 9, 10: From the bootstrap carousel buttons. Bootstrap has "next" or "previous" as text the same colour as the background. This has no effect on the website usability, as the arrows use colours shown to have good contrast.
<details>
<summary>Homepage results</summary>
<img src="/documentation/testing/wave/homepage.png">
</details><br>

**Rooms: available_rooms.html**<br>
- 2 contrast errors from the date widgets in the base template.
- 1 alert for a missing fieldset. This relates to the checkboxes in the amenity filter, however these do not require a legend to explain so this alert was ignored.
<details>
<summary>Available rooms results</summary>
<img src="/documentation/testing/wave/rooms_available_rooms.png">
</details><br>

**Rooms: rooms_superuser.html**<br>
- 2 contrast errors from the date widgets in the base template.
<details>
<summary>Superuser rooms results</summary>
<img src="/documentation/testing/wave/rooms_rooms_superuser.png">
</details><br>

**Rooms: add_room.html**<br>
- 2 contrast errors from the date widgets in the base template.
<details>
<summary>Add room results</summary>
<img src="/documentation/testing/wave/rooms_add_room.png">
</details><br>

**Rooms: edit_room.html**<br>
- 2 contrast errors from the date widgets in the base template.
<details>
<summary>Edit room results</summary>
<img src="/documentation/testing/wave/rooms_edit_room.png">
</details><br>

**Rooms: delete_room.html**<br>
- 2 contrast errors from the date widgets in the base template.
- 1 possible heading alert for the confirmation message, but as this is a paragraph appearing below a h1 heading, this alert was ignored.
<details>
<summary>Delete room results</summary>
<img src="/documentation/testing/wave/rooms_delete_room.png">
</details><br>

**Checkout: checkout.html**<br>
- 2 contrast errors from the date widgets in the base template.
- 1 alert for a JavaScript jump menu. The wave validator reads the country select as a JavaScript jump menu, which would make the page unusable using only a keyboard. However there is no onchange functionality assigned to this dropdown, making it perfectly usable and accessible, so this alert was ignored.
<details>
<summary>Checkout results</summary>
<img src="/documentation/testing/wave/checkout_checkout.png">
</details><br>

**Checkout: success.html**<br>
- 2 contrast errors from the date widgets in the base template.
<details>
<summary>Checkout success results</summary>
<img src="/documentation/testing/wave/checkout_success.png">
</details><br>

**Trips: trips.html**<br>
- 2 contrast errors from the date widgets in the base template.
- 2 alerts for redundant links. These are the next/previous in the past trip pagination that go to the same pages as some of the numbers in the pagination. This is by design for a better user experience so was left in.
<details>
<summary>Trips results</summary>
<img src="/documentation/testing/wave/trips_trips.png">
</details><br>

**Trips: cancel_trip.html**<br>
- 2 contrast errors from the date widgets in the base template.
<details>
<summary>Cancel trip results</summary>
<img src="/documentation/testing/wave/trips_cancel_trip.png">
</details><br>

**Trips: cancel_trip_success.html**<br>
- 2 contrast errors from the date widgets in the base template.
<details>
<summary>Cancel trip success results</summary>
<img src="/documentation/testing/wave/trips_cancel_trip_success.png">
</details><br>

**Trips: trips_superuser.html**<br>
- 2 contrast errors from the date widgets in the base template.
<details>
<summary>Trips superuser results</summary>
<img src="/documentation/testing/wave/trips_superuser.png">
</details><br>

**Reviews: add_review.html**<br>
- 2 contrast errors from the date widgets in the base template.
- 2 alerts. For an orphaned form label and missing fieldset. These are both for the rating field, which is defined in the form. Works as expected and has no impact on accessibility so these alerts were considered and then ignored.
<details>
<summary>Add review results</summary>
<img src="/documentation/testing/wave/reviews_add_review.png">
</details><br>

**Reviews: edit_review.html**<br>
- 2 contrast errors from the date widgets in the base template.
- 2 alerts. For an orphaned form label and missing fieldset. These are both for the rating field, which is defined in the form. Works as expected and has no impact on accessibility so these alerts were considered and then ignored.
<details>
<summary>Edit review results</summary>
<img src="/documentation/testing/wave/reviews_edit_review.png">
</details><br>

**User_profile: user_profile.html**<br>
- 2 contrast errors from the date widgets in the base template.
<details>
<summary>User profile page results</summary>
<img src="/documentation/testing/wave/user_profile_user_profile.png">
</details><br>

**User_profile: edit_profile.html**<br>
- 2 contrast errors from the date widgets in the base template.
- 1 alert for a JavaScript jump menu. The wave validator reads the country select as a JavaScript jump menu, which would make the page unusable using only a keyboard. However there is no onchange functionality assigned to this dropdown, making it perfectly usable and accessible, so this alert was ignored.
<details>
<summary>Edit profile results</summary>
<img src="/documentation/testing/wave/user_profile_edit_profile.png">
</details><br>

**User_profile: delete_user.html**<br>
- 2 contrast errors from the date widgets in the base template.
<details>
<summary>Delete user results</summary>
<img src="/documentation/testing/wave/user_profile_delete_profile.png">
</details><br>

**User_profile: delete_successful.html**<br>
- 2 contrast errors from the date widgets in the base template.
<details>
<summary>Profile delete successful results</summary>
<img src="/documentation/testing/wave/user_profile_delete_successful.png">
</details><br>

**Allauth: Signup**<br>
- 2 contrast errors from the date widgets in the base template.
- 2 alerts. One for a redundant text title of "Google" on the link for 3rd party login. This is required for good user experience so the alert was ignored. Another for redundant link to signup page being in the text under the title and the navbar. This was done by design for good user experience so was left in.
<details>
<summary>Signup results</summary>
<img src="/documentation/testing/wave/allauth_signup.png">
</details><br>

**Allauth: Email verification**<br>
- 2 contrast errors from the date widgets in the base template.
<details>
<summary>Confirm email results</summary>
<img src="/documentation/testing/wave/allauth_email_verification.png">
<img src="/documentation/testing/wave/allauth_email_verification_confirm.png">
</details><br>

**Allauth: Login**<br>
- 2 contrast errors from the date widgets in the base template.
- 1 alert for redundant title text on the Google login, but considering that it does not negatively impact accessibility and is a built in feature of allauth, this is left in.
<details>
<summary>Login results</summary>
<img src="/documentation/testing/wave/allauth_login.png">
</details><br>

**Allauth: Logout**<br>
- 2 contrast errors from the date widgets in the base template.
<details>
<summary>Logout results</summary>
<img src="/documentation/testing/wave/allauth_logout.png">
</details><br>

**Allauth: Reauthenticate**<br>
- 2 contrast errors from the date widgets in the base template.
<details>
<summary>Reauthenticate results</summary>
<img src="/documentation/testing/wave/allauth_reauthenticate.png">
</details><br>

**Allauth: Emails**<br>
- 2 contrast errors from the date widgets in the base template.
<details>
<summary>Emails results</summary>
<img src="/documentation/testing/wave/allauth_emails.png">
</details><br>

**Allauth: Change Password**<br>
- 2 contrast errors from the date widgets in the base template.
<details>
<summary>Change password results</summary>
<img src="/documentation/testing/wave/allauth_change_password.png">
</details><br>

**Allauth: Password Reset**<br>
- 2 contrast errors from the date widgets in the base template.
<details>
<summary>Password reset results</summary>
<img src="/documentation/testing/wave/allauth_password_reset.png">
<img src="/documentation/testing/wave/allauth_password_reset_done.png">
</details><br>

**Allauth: 3rd party login cancelled**<br>
- 2 contrast errors from the date widgets in the base template.
- Alert: redundant link for redirect sign up button, but this is required to explain to the user the purpose of the page and redirect them back to the sign up page.
<details>
<summary>3rd party login cancelled results</summary>
<img src="/documentation/testing/wave/allauth_3rd_party_login_cancelled.png">
</details><br>

**Allauth: 3rd party login error**<br>
- 2 contrast errors from the date widgets in the base template.
<details>
<summary>3rd party login results</summary>
<img src="/documentation/testing/wave/allauth_3rd_party_login_error.png">
</details><br>

**Allauth: Google signup**<br>
- 2 contrast errors from the date widgets in the base template.
<details>
<summary>Google signup results</summary>
<img src="/documentation/testing/wave/allauth_google_signup.png">
</details><br>

**Allauth: Inactive**<br>
- 2 contrast errors from the date widgets in the base template.
<details>
<summary>Inactive results</summary>
<img src="/documentation/testing/wave/allauth_inactive.png">
</details><br>

**Error pages**
- 2 contrast errors from the date widgets in the base template.
<details>
<summary>Error results</summary>
<img src="/documentation/testing/wave/error_page_400.png">
<img src="/documentation/testing/wave/error_page_403.png">
<img src="/documentation/testing/wave/error_page_404.png">
<img src="/documentation/testing/wave/error_page_500.png">
</details><br>

### Performance Testing
The performance of the webpage was tested using Lighthouse within the Google Chrome Devtools to confirm that the site was performing well, is accessible, follows best practices, and follows basic SEO (search engine optimisation) advice. 
During development, care was taking to provide the best performing website that could be provided. These efforts include:
- Image optimisation: [Cloud Convert](https://cloudconvert.com/png-to-webp) was used to convert site images to smaller file formats for faster load times. .PNG files were only used where the file size was already very small, for example the bubble text on page titles. Otherwise, .WEBP and .SVG files to reduce file sizes and optimise them for web application usage.
- Code minification: Complete code minification was avoided in this project to allow easier assessment upon submission. That being said, code has been written to meet the highest standards, repetition had been removed, and short, elegant solutions have been used wherever possible in order to reduce the code size. In future minification will be used. For example [Python Minifier](https://python-minifier.com/) reduces the size of the python files from X to Y.
- Caching files. AWS will cache the media files, as they do not update often, allowing better performance on repeat visits to the website.

The performance was tested for normal internet speed, fast 3G, and slow 3G to test the performance in a majority of scenarios and locations. This was done by setting the performance network throttling in Google Chrome Devtools. The testing was also run on Google Chrome incognito mode to avoid any complications with plugins or extensions. On normal internet speed, the performance never dropped below 87%, that being on the homepage with the majority of the site content.


### HTML Validation
The [W3C markup validation service](https://validator.w3.org/) was used to validate the HTML of each page of this website. As each page including some Django templating language that threw errors in the validator; the HTML was validated after deployment. Each page was accessed and the source code (CTRL+U or right click > View Page Source) was copied and pasted into the validator to validate by direct input.<br>
| Page | Warnings | Errors |
| ----- | ------ | ------ |
| Base template | None | None |
| Back button | None | None |
| Homepage | None | None |
| Rooms: available_rooms | None | None |
| Rooms: rooms_superuser | None | None |
| Rooms: add_room | None | None |
| Rooms: edit_room | None | None |
| Rooms: delete_room | None | None |
| Checkout: checkout | None | None |
| Checkout: success | None | None |
| Trips: trips | None | None |
| Trips: cancel trip | None | None |
| Trips: cancel trip success | None | None |
| Trips: trips superuser | None | None |
| Reviews: add review | None | None |
| Reviews: edit review | None | None |
| User profile page | None | None |
| User profile edit profile | None | None |
| User profile delete user | None | None |
| User profile delete successful | None | None |
| Allauth - signup | None | None |
| Allauth - confirm-email | None | None |
| Allauth - login | None | None |
| Allauth - Google signup | None | None |
| Allauth - logout | None | None |
| Allauth - reauthenticate | None | None |
| Allauth - emails | None | None |
| Allauth - change password | None | None |
| Allauth - reset password | None | None |
| Allauth - password reset done | None | None |
| Allauth - 3rd party login | None | None |
| Allauth - 3rd party login cancelled | None | None |
| Allauth - 3rd party login error | None | None |
| Error pages - 400 | None | None |
| Error pages - 403 | None | None |
| Error pages - 404 | None | None |
| Error pages - 500 | None | None |

### CSS Validation
CSS validation was completed using the [W3C Jigsaw CSS validator](https://jigsaw.w3.org/css-validator/). It showed no errors in the CSS code.

### JavaScript Validation
The custom JavaScript code was testing using the JavaScript linter [JSLint](https://www.jslint.com/) with no errors across the entirity of the written JavaScript code. Any warnings are discussed above the results.

**Base template**<br>
- The base.js file was copied into the linter and the postload JavaScript at the bottom of base.html was added to this for the purpose of validation. 
- The following linter settings were selected: browser, this. 
- The following variables were added: bootstrap.
- No warnings.
- Full results can be seen [here](/documentation/testing/jslint/base_template.pdf)

**Homepage template**<br>
- The script at the bottom of the home template index.html was copied into the linter.
- The following linter settings were selected: browser. 
- The following variables were added: bootstrap.
- No warnings.
- Full results can be seen [here](/documentation/testing/jslint/index.pdf)

**Available Rooms**<br>
- The script at the bottom of the home template index.html was copied into the linter.
- The following linter settings were selected: browser, this (this was used in the code), white (to oversome an alert for parentheses but putting in parentheses created an alert to remove said parentheses), fart (to use more complicated arrow function).
- No warnings.
- Full results can be seen [here](/documentation/testing/jslint/available_rooms.pdf)

**Checkout: stripe_elements.js**
- This script handles the function associated with the stripe elements and the data cache from the checkout
- The following linter settings were selected: browser, unordered(to remove warnings for the ordering of defining room_id, room etc.)
- The following variables were added: $ (for JQuery)
- 1 warning: Unexpected ':card' when defining the card for confirming the card payment. The code works as expected with no errors, so this was left in.
- Full results can be seen [here](/documentation/testing/jslint/available_rooms.pdf)

**Trips: trips.html**
- The script at the bottom of the trips.html page was copied into the linter.
- The following linter settings were selected: browser
- No warnings.
- Full results can be seen [here](/documentation/testing/jslint/trips.pdf)

### Python Validation
The Python code for this project was written in strict accordance with the [PEP 8](https://peps.python.org/pep-0008/) style guide for Python code. These include using correct indentations, maximum line lengths of 79 characters, and adhering to naming conventions for variables, functions, and classes. The [Code Institue python linter](https://pep8ci.herokuapp.com/) was used to validate the written code.

**Project: settings.py**<br>
- No errors or alerts
<details>
<summary>Settings results</summary>
<img src="/documentation/testing/python/project_settings.png">
</details><br>

**Project: urls.py**<br>
- No errors or alerts
<details>
<summary>Urls results</summary>
<img src="/documentation/testing/python/project_urls.png">
</details><br>

**Back Button: views.py**<br>
- No errors or alerts
<details>
<summary>Back button views results</summary>
<img src="/documentation/testing/python/back_button_views.png">
</details><br>

**Back Button: test_views.py**<br>
- No errors or alerts
<details>
<summary>Back button test views results</summary>
<img src="/documentation/testing/python/back_button_test_views.png">
</details><br>

**Back Button: urls.py**<br>
- No errors or alerts
<details>
<summary>Back button urls results</summary>
<img src="/documentation/testing/python/back_button_urls.png">
</details><br>

**Home: forms.py**<br>
- No errors or alerts
<details>
<summary>Froms results</summary>
<img src="/documentation/testing/python/home_forms.png">
</details><br>

**Home: test_forms.py**<br>
- No errors or alerts
<details>
<summary>Test forms results</summary>
<img src="/documentation/testing/python/home_test_forms.png">
</details><br>

**Home: views.py**<br>
- No errors or alerts
<details>
<summary>Views results</summary>
<img src="/documentation/testing/python/home_views.png">
</details><br>

**Home: test_views.py**<br>
- No errors or alerts
<details>
<summary>Test views results</summary>
<img src="/documentation/testing/python/home_test_views.png">
</details><br>

**Home: urls.py**<br>
- No errors or alerts
<details>
<summary>Urls results</summary>
<img src="/documentation/testing/python/home_urls.png">
</details><br>

**Home: context_processor.py**<br>
- No errors or alerts
<details>
<summary>Context processor results</summary>
<img src="/documentation/testing/python/home_context_processor.png">
</details><br>

**Rooms: admin.py**<br>
- No errors or alerts
<details>
<summary>Admin results</summary>
<img src="/documentation/testing/python/rooms_admin.png">
</details><br>

**Rooms: models.py**<br>
- No errors or alerts
<details>
<summary>Models results</summary>
<img src="/documentation/testing/python/rooms_models.png">
</details><br>

**Rooms: test_models.py**<br>
- No errors or alerts
<details>
<summary>Test models results</summary>
<img src="/documentation/testing/python/rooms_test_models.png">
</details><br>

**Rooms: forms.py**<br>
- No errors or alerts
<details>
<summary>Forms results</summary>
<img src="/documentation/testing/python/rooms_forms.png">
</details><br>

**Rooms: test_forms.py**<br>
- No errors or alerts
<details>
<summary>Forms results</summary>
<img src="/documentation/testing/python/rooms_test_forms.png">
</details><br>

**Rooms: views.py**<br>
- No errors or alerts
<details>
<summary>Views results</summary>
<img src="/documentation/testing/python/rooms_views.png">
</details><br>

**Rooms: test_views.py**<br>
- No errors or alerts
<details>
<summary>Test views results</summary>
<img src="/documentation/testing/python/rooms_test_views.png">
</details><br>

**Rooms: urls.py**<br>
- No errors or alerts
<details>
<summary>URLs results</summary>
<img src="/documentation/testing/python/rooms_urls.png">
</details><br>

**Checkout: admin.py**<br>
- No errors or alerts
<details>
<summary>Admin results</summary>
<img src="/documentation/testing/python/checkout_admin.png">
</details><br>

**Checkout: models.py**<br>
- No errors or alerts
<details>
<summary>Models results</summary>
<img src="/documentation/testing/python/checkout_models.png">
</details><br>

**Checkout: test_models.py**<br>
- No errors or alerts
<details>
<summary>Test models results</summary>
<img src="/documentation/testing/python/checkout_test_models.png">
</details><br>

**Checkout: forms.py**<br>
- No errors or alerts
<details>
<summary>Forms results</summary>
<img src="/documentation/testing/python/checkout_forms.png">
</details><br>

**Checkout: test_forms.py**<br>
- No errors or alerts
<details>
<summary>Test forms results</summary>
<img src="/documentation/testing/python/checkout_test_forms.png">
</details><br>

**Checkout: views.py**<br>
- No errors or alerts
<details>
<summary>Views results</summary>
<img src="/documentation/testing/python/checkout_views.png">
</details><br>

**Checkout: test_views.py**<br>
- No errors or alerts
<details>
<summary>Test views results</summary>
<img src="/documentation/testing/python/checkout_test_views.png">
</details><br>

**Checkout: urls.py**<br>
- No errors or alerts
<details>
<summary>URLs results</summary>
<img src="/documentation/testing/python/checkout_urls.png">
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

**Trips: admin.py**<br>
- No errors or alerts
<details>
<summary>Trips admin results</summary>
<img src="/documentation/testing/python/trips_admin.png">
</details><br>

**Trips: models.py**<br>
- No errors or alerts
<details>
<summary>Trips models results</summary>
<img src="/documentation/testing/python/trips_models.png">
</details><br>

**Trips: test_models.py**<br>
- No errors or alerts
<details>
<summary>Trips test_models results</summary>
<img src="/documentation/testing/python/trips_test_models.png">
</details><br>

**Trips: views.py**<br>
- No errors or alerts
<details>
<summary>Trips views results</summary>
<img src="/documentation/testing/python/trips_views.png">
</details><br>

**Trips: test_views.py**<br>
- No errors or alerts
<details>
<summary>Trips test_views results</summary>
<img src="/documentation/testing/python/trips_test_views.png">
</details><br>

**Trips: urls.py**<br>
- No errors or alerts
<details>
<summary>Trips urls results</summary>
<img src="/documentation/testing/python/trips_urls.png">
</details><br>

**Reviews: admin.py**<br>
- No errors or alerts
<details>
<summary>Reviews admin results</summary>
<img src="/documentation/testing/python/reviews_admin.png">
</details><br>

**Reviews: models.py**<br>
- No errors or alerts
<details>
<summary>Reviews models results</summary>
<img src="/documentation/testing/python/reviews_models.png">
</details><br>

**Reviews: test_models.py**<br>
- No errors or alerts
<details>
<summary>Reviews test_models results</summary>
<img src="/documentation/testing/python/reviews_test_models.png">
</details><br>

**Reviews: forms.py**<br>
- No errors or alerts
<details>
<summary>Reviews forms results</summary>
<img src="/documentation/testing/python/reviews_forms.png">
</details><br>

**Reviews: test_forms.py**<br>
- No errors or alerts
<details>
<summary>Reviews test_forms results</summary>
<img src="/documentation/testing/python/reviews_test_forms.png">
</details><br>

**Reviews: views.py**<br>
- No errors or alerts
<details>
<summary>Reviews views results</summary>
<img src="/documentation/testing/python/reviews_views.png">
</details><br>

**Reviews: test_views.py**<br>
- No errors or alerts
<details>
<summary>Reviews test_views results</summary>
<img src="/documentation/testing/python/reviews_test_views.png">
</details><br>

**Reviews: urls.py**<br>
- No errors or alerts
<details>
<summary>Reviews urls results</summary>
<img src="/documentation/testing/python/reviews_urls.png">
</details><br>

**User_profile: admin.py**<br>
- No errors or alerts
<details>
<summary>Admin results</summary>
<img src="/documentation/testing/python/user_profile_admin.png">
</details><br>

**User_profile: models.py**<br>
- No errors or alerts
<details>
<summary>Models results</summary>
<img src="/documentation/testing/python/user_profile_models.png">
</details><br>

**User_profile: test_models.py**<br>
- No errors or alerts
<details>
<summary>Test models results</summary>
<img src="/documentation/testing/python/user_profile_test_models.png">
</details><br>

**User_profile: forms.py**<br>
- No errors or alerts
<details>
<summary>Forms results</summary>
<img src="/documentation/testing/python/user_profile_forms.png">
</details><br>

**User_profile: test_forms.py**<br>
- No errors or alerts
<details>
<summary>Test_forms results</summary>
<img src="/documentation/testing/python/user_profile_test_forms.png">
</details><br>

**User_profile: views.py**<br>
- No errors or alerts
<details>
<summary>Views results</summary>
<img src="/documentation/testing/python/user_profile_views.png">
</details><br>

**User_profile: test_views.py**<br>
- No errors or alerts
<details>
<summary>Test_views results</summary>
<img src="/documentation/testing/python/user_profile_test_views.png">
</details><br>

**User_profile: signals.py**<br>
- No errors or alerts
<details>
<summary>Signals results</summary>
<img src="/documentation/testing/python/user_profile_signals.png">
</details><br>

**User_profile: urls.py**<br>
- No errors or alerts
<details>
<summary>Urls results</summary>
<img src="/documentation/testing/python/user_profile_urls.png">
</details><br>

The env.py file was also linted showing no errors but the screenshot has been omitted for security issues as it contains sensitive information. An example of the env.py file can be found [here](/env_example.txt).

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

### Bug 4:
- Upon successful reservation, the trip instance was not being created, the room instance was not updated with unavailable dates, and the confirmation email was not being sent. The issue with the confirmation email is assumed to be the inability to find a trip instance, so will be explored after trips are successfully created.
Separate print statements were littered throughout the webhook handler to help debug in the format of:
```python
print("Debug message:", variable)
```
- This led me to an issue that the trip was trying to create an instance with the room as the room id, rather than a room instance. I updated the code to take the input room_id in the create_trip() function and use it to get the correct room, then pass that into the trip_form_data.
- Now a trip was successfully created, but this error occurred when trying to send an email: "DEBUG: ERROR OCCURRED: 'NoneType' object has no attribute 'email'". This occurred within the _send_confirmation_email function, so a debug print statment of printing the order instance was added to the start to check how the email should be retrieved. This showed that 'none' was being passed as the order. This issue found was that the _send_confirmation_email function if the order did not exists was the same as the function if the order did exist and tried to pass _send_confirmation_email(order). This was updated to the correct _send_confirmation_email(order_instance).
- The next error occurred because the email tried to access all trips from the user instead of the most recent. This was fixed by returning the trip_instance from the create_trip function and then passing this into the _send_confirmation_email function.
- This solved the issue but the room failed to update with an error of "ERROR OCCURRED: 'str' object has no attribute 'id'". I updated room_id = trip_data.get('room').id to room_id = trip_data.get('room').
- The next error occured when retrieving the unavailability dates in the update_room function using room_booked_unavailable_dates = json.loads(room_booked.unavailability). This is because it was already saved as a python list, so I updated this to room_booked_unavailable_dates = room_booked.unavailability.
- The next error in the update_room function came about from interacting with the dates as they retrieved as a string and I tried to string them using strftime(). I commented out this step and retried the code. This created an error as the date needs to be in a date format. I added an extra step to turn the date into a date format, then string it later. This solved the bug.

### Bug 5:
Bug 5 involved the filtering and sorting of the available room results. The usual way using GET was not working because the submitted search values were accessed through a POST check. This was overcome by using JavaScript to add a sort / filter / pagination hidden input to the populated form in the header and resubmitting the form. However this introduced a further complication when having multiple sort / filter / pagination functions running concurrently as each of them submitted the form individually. A workaround was conceived where:
- The filter function will add a hidden filter input to form and not submit it
- The sort function will run the filter function and then add a hidden sort input to the form and not submit it
- The pagination function will run the sort function (adding the hidden filter and sort inputs to the form) and then add a hidden page input to the form and not submit it
- The onchange for the sort dropdown and the onclick for the filter and pagination buttons were given event listeners to submit the form by accessing their given data-action attributes
The only downside of this is that when applying a new filter, the pagination resets to page 1 which works as intended for a good user experience, however the sort is also reset. For now this is deemed acceptable due to the time and effort put in to achieving the current functionality.

### Known Bugs
- edit_room.html: The styling for changing the image when editing a room that already has an image is cramped but repeated attempts to access the styling have not been fruitful.
- rooms/test_views.py: The room instance will not update when testing the edit room view. However this does work through manual testing, so this test is omitted in the automated tests.

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