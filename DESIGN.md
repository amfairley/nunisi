![Website logo](/linktologoimage.png)

---

# Design

See [README.md](/README.md) for information on project goals, user stories, security, future developments, technologies used, user feedback, credits, and acknowledgements. <br>
See [TESTING.md](/TESTING.md) for information on the test driven development of the website, manual and automated testing of the site, bugs encountered, and website analytics. <br>
See [DEV.md](/DEV.md) for an overview of the continuous integration and deployment process, how I set up my development environment, and deployment steps.

---

## Table Of Contents
1. [Five Planes of UX](#five-planes-of-ux)
    - [Strategy](#strategy)
        * [Viability and Feasibility](#viability-and-feasibility)
    - [Scope](#scope)
        * [Back-end](#back-end)
        * [Front-end](#front-end)
    - [Structure](#structure)
        * [base.html](#basehtml)
        * [index.html](#indexhtml)
    - [Skeleton](#skeleton)
        * [wireframes](#wireframes)
    - [Surface](#surface)
        * [Colour Scheme](#colour-scheme)
        * [Typography](#typography)
        * [Images](#images)
2. [Features](#features)



## Five Planes of UX
Outlined here is the design process for this webapp. Building up the webapp using the 5 planes of UX design allows seemless transition from a business idea through to the finished polished product whilst maintaining the criteria for the site are kept, accessibility guidelines are met, and that the final product is fit for purpose.

### Strategy

- **What value does the project provide?** From the business perspective; this project provides a website to display and rent out their rooms to potential guests. It allows the business owner to track trends in booking, see feedback from guests, and edit/update information about their rooms. From a customer perspective it provides a website where they can securely and safely book a room for their visit, find out more about the hotel and resort, and track previous trips that they have taken.
- **What are the business needs?** The business needs are to provide an intuitive, pleasant looking, and accessible website to entice more users to book rooms at their resort. They business also requires agency over the information they give out, being able to update specifications to rooms to reflect renovations. With enough use, the website will be able to provide information about trends in trips (time of year/amount of guests) and feedback in the form of reviews so that the business can continue to grow and match public demand.
- **Who is the target audience?** The target audience will primarily be potential travellers. This will be split into sub sections of international travellers to Georgia who are looking for more of a nature focussed holiday that a city break, and domestic travellers seeking a break from city life. The business owners are another target audience, as they will need to have faith that the website will provide all the functionality that they need and that the website meets their standards for how they wish to portray the hotel. 
- **What are the user requirements and expectations?** The users can make their own profile in order to save their personal details and track previous trips. They also expect to be able to Create, Read, Update, and Delete their own profile, personal data, and reviews whenever they want. It is expected that they can search for available rooms to rent and to safely and securely pay for the rooms.

#### Viability And Feasibility
Followed is an analysis of the user stories and above user and business needs ranked from 1 (least important/viable) to 5 (most important/viable):
|   Task |   Importance | Viability/Feasibility |
| --------- | ------------- | ----------------- |
| Clear home screen showing the purpose of the website | 5 | 5 |
| Intuitive website design | 5 | 5 |
| Resort information | 4 | 5 |
| Information on services offered | 4 | 5 |
| How to get to the resort | 4 | 5 |
| Hotel FAQs | 4 | 5 |
| Show reviews of the hotel | 3 | 3 |
| Clear error pages | 5 | 5 |
| Contact information for the hotel | 5 | 5 |
| Contact information for the developer | 2 | 5 |
| Safe and secure user authentication | 5 | 4 |
| Allow signup/login using email instead of username | 3 | 5 |
| Allow users to delete their account | 5 | 4 |
| Allow users to sign up to a newsletter | 3 | 5 |
| Allow users to leave a review | 5 | 4 |
| Simple search for available rooms | 5 | 4 |
| Filter/sort room search results | 4 | 3 |
| See room information | 5 | 5 |
| Allow users to view previous trips | 4 | 4 |
| Allow users to book through the website | 5 | 3 |

Overall, most of the targets meets a ranking of at least 4 in either importance or viability. Extra effort will be given to those with higher importance but lower viability (due to currently not knowing how to implement the features required) and those with low importance and higher viability will be included due to their ease of inclusion.<br>
Showing reviews of the hotel has been rated a 3/3, as this will depend on the availability of reviews on websites such as TripAdvisor and whether they can be accessed via API if you are not the resort owner. Should this prove not possible, showing reviews will be added to "future development" once reviews have been received through this website, giving a resource of reviews to display. <br>
The "safe and secure user authentication" will be achieved by using Django AllAuth, this will also meet the user story requirements for signing in via social media, email validation, easy login/logout, password updating, and password recovery.
Stripe will be used for payment and booking, meeting the further user stories of seeing an order confirmation and saving their details for future.

### Scope
#### Back-end
Multiple tables in a relational database will be required to meet all of the targets for this project. These models will be:
- **User**: A Django model that will be updated using Django AllAuth and consisting of a number of fields that will not be queried or used in the project. The fields of note will be: ID, email, password, is_superuser (for admin privileges on the site).
- **Profile**: This will handle the user profile data. The fields will be: ID, User (foreign key; one to one), newsletter (True if signed up to a newsletter), and the information fields required for stripe such as first and last names, address information and contact details etc.
- **Room**: This will hold all the information about the specific rooms. The fields will be: ID, name, sanitised_name (for display on the website), amenities (a JSON list of amenity IDs), description, image, price, unavailability (a JSON list of book dates).
- **Amenities**: This will have the amenity information for rooms such as air conditioning, balcony, bed size etc. The fields will be: ID, name, sanitised_name (for display on the website), icon (a string of the html for a fontawesome icon).
- **Trip**: This will hold the information of a trip that has been booked. It will have: ID, Profile (foreign key, many to one), Room (foreign key, one to one), start_date, end_date, cancelled (boolean field with defautl to False).
- **Review**: This will have the information for a review of a trip. The fields will be: ID, Trip (foreign key, one to one), clean_rating (rating cleanliness 1-5), food_rating (rating the food 1-5), service_rating (rating the service received 1-5), staff_rating (rating the staff attitude/helpfulness etc 1-5), overall_rating (1-5), review_content (text). 

#### Front-end
The website will be built using Django, allowing for template inheritance and partitions functionality into different apps, resulting in less duplicate code written and quicker load times for the user.

**Templates**
- **base.html**: This will be the base template that the others call from to ensure a cohesive structure across the website. Present here will be:
    - All the header meta information
    - Links to styling and JavaScript scripts
    - The header with the site logo, a booking form, and account navigation links
    - The footer with the hotel social media links, hotel contact information, the site logo, and developer contact information
- **index.html**: This will act as the website homepage. It will have:
    - Navigation links for the different sections on the page
    - A large hero image and text welcoming the user to the website
    - A booking form
    - Resort information and images
    - Service information and images
    - Location information with a google maps widget
    - Hotel FAQs
    - A carousel of reviews if available

### Structure

#### base.html
- As the base template, this will have the site-wide navigation bar and footer
- The navigation bar will meet the requirement for intuitive and responsive navigation, consisting of a site logo, booking form on large screens, and account links. When logged out the links will be to Sign Up / Login. When logged in the links will be to Trips / Account Settings / Logout. When logged in as a Super User the links will be to Rooms / Trips / Account Settings / Logout.
- The footer will meet the requirement for the hotel and developer contact information and will consist of the hotel social media links, contact information for the hotel and developer, and site logo.

#### index.html
- The homepage will display all information about the user, allowing it to be find and look through.
- A home page navigation bar with each homepage section on it meets the requirment for intuitive and responsive navigation.
- The large hero image and text meets the requirement for a clear homescreen showing the website purpose.
- When logged out there will be buttons on the hero image urging the user to sign up or login.
- On smaller than desktop screens (when the booking form disappears from the navigation bar) there will be a booking button on the hero image which takes the user down to the booking form section.
- The section after the hero image will be the booking form on mobile screens, this meets the requirement for users being able to search for available rooms.
- The next section will be a resort info section, meeting the requirement for more information about the hotel. It will consist of a carousel of hotel images, a section title, and a description about the history and key facts of the hotel.
- The next section will be a services section, meeting the requirement for displaying what services are on offer. This will be a carousel of cards, each card will describe the service, cost, how to book, and an image.
- The next section will be the location section, meeting the requirement of showing how to get to the hotel. This will consist of a section title and travel advice and a google maps widget of the hotel location.
- The next section will be the FAQ section. This meets the requirement for providing FAQs. This will have a section title and an unordered list of questions and answers. This will take up 3 columns on desktop, 2 on tablet, and 1 on mobile devices.
- The last section will be a carousel of reviews if reviews are available. This meets the requirement for showing user reviews. They will give a general name e.g. First_name from country, the review content, and a star rating.

### Skeleton

#### Wireframes
[Balsamiq Wireframes](https://balsamiq.com/) was used to create wireframe templates for this webapp.

### Surface

#### Colour Scheme
The colour scheme started as an idea for gold and green to portray the natural aspects of the resort and nature, whilst also conveying sophistication and prestige.

![Colour Scheme](/linktoimage.png)

| Green #3A6B35 | Gold #E3B448 | Medium Spring Bud #CBD18F |
| ----- | ----- | ----- |

**Other colours used:**
- Colour 1: 

#### Typography

I wanted the typefaces used in this project to reflect the prestige of the hotel and resort as well as highlighting that it is family run.

**[Jost Regular](https://fonts.google.com/specimen/Jost?query=jost)**<br>
![Jost Regular](/documentation/typography_jost.png)
This is my selection for headings across the website. Inspired by the 1920’s German sans-serif; Jost is an elegant and legible font that portrays history and excellence. This makes it a great choice for headings and titles across the website. As a sans-serif font, the backup fonts were Arial, Helvetica, and sans-serif.

**[Caveat Regular](https://fonts.google.com/specimen/Caveat?query=caveat)**<br>
![Caveat Regular](/documentation/typography_caveat.png)
This is my selection for small notes across the website. Caveat is an elegant handwriting font that makes text seem personal and handwritten by giving the letters variations dependent on their placing in a word. This makes it excellent for use for small annotations on the website that give the site a feeling of being family run and personable. As a handwriting font, the backup fonts used were Brush Script MT and cursive.

**[Roboto](https://fonts.google.com/specimen/Roboto?query=roboto)**<br>
![Roboto](/documentation/typography_roboto.png)
This is my selection for block text across the website. Roboto is the most popular google font with high legibility and nice curves. It is used for the bulk text of the website to be easy on user's eyes and not cause strain when reading longer reviews. As a sans serif font, the backup fonts were Arial, Helvetica, and sans-serif.

#### Images
- The site logo was created using [Logo Design AI](https://logodesign.ai/) to create a simple and usable logo throughout the website.
- - The icons used across the site were from [Font Awesome](https://fontawesome.com/).

## Features

| **Feature Name** |
| ----- |
| **Page:** |
| <details><summary>Feature Image</summary><img src=""></details> |
| **Details:** |
| **User Stories Covered:** |
