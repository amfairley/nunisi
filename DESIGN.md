![Website logo](/linktologoimage.png)

---

# Design

See [README.md](/README.md) for information on project goals, user stories, security, future developments, technologies used, user feedback, credits, and acknowledgements.<br>
See [TESTING.md](/TESTING.md) for information on the test driven development of the website, manual and automated testing of the site, bugs encountered, and website analytics. <br>
See [DEV.md](/DEV.md) for an overview of the continuous integration and deployment process, how I set up my development environment, and deployment steps.

---

## Table of Contents
1. [Five Planes of UX](#five-planes-of-ux)
    1. [Strategy](#strategy)
        * [Viability and Feasibility](#viability-and-feasibility)
    2. [Scope](#scope)
        * [Back End](#back-end)
        * [Front End](#front-end)
    3. [Structure](#structure)
        * [Navigation Bar](#navigation-bar)
        * [base.html](#basehtml)
        * [index.html](#indexhtml)
        * [Allauth](#allauth)
        * [about-us.html](#about-ushtml)
        * [Booking](#booking)
        * [Checkout](#checkout)
        * [account.html](#accounthtml)
        * [Error Pages](#error-pages)
        * [Information Architecture](#information-architecture)

## Five Planes of UX
Here I outline the design process of the website, ensuring that I meet accessibility guidelines, follow the principles of UX design, and create a website that meets the purpose of being a fun and intuitive online community for reviewing and recommending children's toys through user interactions.

### Strategy
- **What value does the project provide?** This project is designed for a business to allow users to book rooms at their hotel. It provides value to the business by expanding their potential client base and tracking room availability, and it provides value to the users by allowing them to book rooms in an easy and secure way.
- **What are the business needs?** The business needs are to provide an intuitive, pleasant looking, and accessible website to entice more users to book rooms at their resort. They also require access to the database to check availability of rooms and a way to receive payment from users. The business also requires there to be good Search Engine Optimization (SEO) so that the website is easy to find.
- **Who is the target audience?** There are two target audiences for this web application. Firstly, the business, who expect a professional, working website that matches their needs. Secondly, any potential visitors to the resort, be it international travellers requiring one or two nights while travelling through the country, or domestic holidaymakers who are seeking a relaxing and restorative break.
- **What are the user requirements and expectations?** On top of expecting a responive website that functions properly and meets all current accessibility guidelines, they would expect to be able to search for an available room, book it securely, and create an account if they wish in order to track their bookings.

#### Viability and Feasibility
Followed is an analysis of the user stories and above user and business needs ranked from 1 (least important/viable) to 5 (most important/viable):
|   Task |   Importance | Viability/Feasibility |
| --------- | ------------- | ----------------- |
| Good SEO | 5 | 5 |
| Clear home screen conveying purpose | 4 | 5 |
| Easy and intuitive navigation | 5 | 5 |
| Immediate feedback to the user | 5 | 5 |
| Responsive | 4 | 4 |
| Accessible | 5 | 4 |
| Robust site and data security | 5 | 4 |
| Robust defensive programming | 5 | 4 |
| Login/Logout functionality | 5 | 5 |
| Full CRUD functionality of the user accounts for users | 5 | 5 |
| Search available rooms functionality | 5 | 4 |
| Sort available rooms functionality | 4 | 4 |
| Individual room pages showing further information | 5 | 5 |
| Information about the hotel and resort | 5 | 5 |
| FAQ section | 5 | 5 |
| Travel advice and location | 5 | 5 |
| Visible reviews | 2 | 3 |
| Ability to leave a review | 3 | 3 |
| Have contact information for the developer | 3 | 5 |
| Secure payment process | 5 | 5 |
| Have previous trips visible on user account pages | 5 | 5 |
| 404 error page | 5 | 5 |
| 403 error page | 4 | 4 |
| 500 error page | 5 | 4 |

Overall, most thing seem both feasible and important. The visible reviews option has been given low importance and feasibility pending research into how to integrate e.g. tripadvisor reviews into the website.

### Scope

#### Back-end
Multiple tables within a relational database are required for this project. These models are:
- **User**: This data will be provided through Django allauth. It will consist of an ID, email, and password.
- **Profile**: This data will will handle the account page information. It will consist of an ID, a foreign key to the user, a foreign key to trips that the user has booked, and a Boolean to show whether the user is signed up to a newsletter or promotional emails.
- **Trip**: This data will hold the information of the trips booked by users. It will have an ID, a foreign key to the room booked, a check-in date, a check-out date, and a total price.
- **Room**: This will be the information for each room. It will have an ID, a room name, a list of amenities, an integer number of beds, the number of people the room sleeps, a list of dates when the room is available, and the price per night.
- **Review**: This will hold the reviews left by visitors, it will have a primary ID, a foreign key to the allauth user information, a foreign key to the trip that the review is for, an integer rating between 1 and 5, and a review description.

#### Front-end
The website will utilise template inheritance that allows for less code to be written and quicker load times for a better user experience. Each section of the website will be created within separate Django apps, allowing for seamless integration of functions across the entire site.

**Apps and Templates**
There will be a root directory level folder with the site-wide templates. Included here will be:
- base.html that will have the meta information and general web page layout including footer.
- 404.html that will show the 404 page not found error when an unavailable page is accessed by the user.
- 403.html that will show the 403 access denied error if a user were to e.g. see the trip details of another user.
- 500.html that will show the 500 internal server error if there are server outages and the database cannot be reached.
- Django allauth templates that will house the allauth functionality pages (login/signup etc).
- An Includes folder which will have hold the toasts that appear to confirm user information and the navigation bar.

Followed are a series of planned apps and what templates and functionality they will contain:
- home:
    * The homepage html file; index.html
    * The about-us/information html file
- rooms:
    * The availability search page; search.html
    * The search results page; results.html
    * The individual rooms pages; room.html
    * Models for the room
- bag:
    * The shopping bag html file; bag.html
- checkout:
    * The checkout page; checkout.html
    * A checkout success page; checkout-success.html
    * Model for the purchased trip
- account:
    * The account page showing the account details and trips; account.html
    * Individual trip pages; trip.html
- reviews:
    * This will hold the data for the review model.
    * This will let the reviews be shown on the homepage.

### Structure

#### Navigation bar
 - The navigation bar will be used on every page of the website.
 - It will have a site logo that will also act as a link back to the homepage, this will help meet the requirement for the website to have a clear and obvious purpose by having the site branding on each page.
 - There will be a page link for the about-us page allowing us to meet the requirements for providing information about the hotel, an FAQ, and travel advice.
 - When logged out there will be options to log in or sign up. Whilst logged in there will be the option to log out. This meets the requirement for login/logout functionality.
 - When logged in there will be a link to the users profile. This meets the requirement for letting the users have full CRUD functionality over their profile.
 - On smaller screens the navigation links will be hidden in a burger menu, meeting the requirement for the website to be responsive.
 - There will be a basket which will show chosen, but not yet confirmed/purchased trips meeting some of the requirements for a secure payment process.
 - Overall, these sections in the navigation bar let us meet the requirement of having easy and intuitive navigation on the website.

#### base.html
 - The base.html will have all of the meta data, allowing for good SEO and meeting the good SEO requirement.
 - There will be a footer defined in the base template with contact details of the hotel and developer, meeting the requirement for having contact information for the developer.
#### index.html
 - This will act as the homepage.
 - There will be a large Hero Image and Hero Text welcoming the user to the website, meeting the requirement for a clear home screen conveying the purpose of the site.
 - There will be links, prompting the user to sign up / log in / book.
 - There will be reviews on the homepage in a carousel, meeting the requirement for visible reviews.
#### Allauth
 - Django allauth will be used for user authentication, meeting the requirements of robust site and data security.
 - The forms (login/signup/lost password etc) will have prompts for required fields or invalid user input, meeting the requirements for immediate feedback to user and robust defensive programming.
 - The allauth templates will all feature the header and footer and will help meet the requirement to clearly convey the purpose of each page.
 - The sign up form will have an extra check box to sign up to a newsletter.
#### about-us.html
 - This page will have all the information about the hotel and resort including history of the resort, services available, facilities on offer, how to get there information and an FAQ, meeting the requirements for information about the resort, an FAQ section, and travel advice and location.
#### Booking
 - There will be a search page, a search results page, and individual room pages meeting the requirement to search available rooms.
 - The search results page will have the option to filter the rooms based on amenities and sort them in order of price, numbers of beds etc, meeting the requirements for sorting and filtering available rooms.
 - The individual room pages will have more images and information on the rooms, meeting the requirement for further information on rooms.
#### Checkout
 - There will be a checkout.html and checkout-success.html page that helps meet the requirement of immediate feedback to the user.
 - The checkout payment will be processed with Stripe for security, meeting the requirements for robust site and data security and a secure payment process.
 - If the payment is made by a non-logged in user, a prompt will occur after payment to either log in or sign up and adding the trip to the user's account. This adds towards meeting the requirement to have previous trips visible on the account page.
#### account.html
 - This page will provide the user the options to change password / delete account / contact the hotel, meeting the requirement for full CRUD functionality of the user accounts for users.
 - The account page will also display previous trips, meeting the requirement to have previous trips visible on the user account pages.
 - Once trips have occurred, there will be an option to leave a review for the trip, this meets the requirement to be able to leave a review.
#### Error pages
 - The 403, 404, and 500 error pages will all have a display of the error and a short description along with a link back to the homepage, meeting the requirement for easy and intuitive navigation.

#### Information Architecture
 **Front-end**: Site map <br>
 Below is a proposed site map of the website showing links and redirections.
 ![Nunisi site map](/pathtositemap/map.png)

 **Back-end**: Entity-relationship-diagram (ERD)<br>
 Below is a proposed ERD for the tables to be modelled for the database that is relevant to the webite purpose and contains relationships between tables.
 ![Nunisi ERD](/documentation/database_erd.png.png)

