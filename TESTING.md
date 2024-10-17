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
    - [Known Bugs](#known-bugs)
6. [Analytics](#analytics)

## Testing User Stories
The [user stories](/README.md#user-stories) have been a driving force for the development of this project. More information on each user story and how the features implemented in this web app meet their criteria can be seen [here](/DESIGN.md#features). All user story criteria were met, creating a website that the target audience of the hotel owners and travellers will find usable, intuitive, and fit for purpose.

## Manual Testing

| Feature | Action | Expected results | Passed | Comments |
| ----- | ----- | ----- | ----- | ----- |
| **base.html** | | | | |
| | | | | |

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

### Accessibility Testing
Accessibility was kept in mind throughout development and the best practices were kept to across the website including, but not limited to, ensuring aria-labels and alt texts were used throughout, using semantic HTML, creating easy to see colour contrasts. Where hidden text was used, it was hidden in a way that was still accessible to screen readers.
Accessibility testing was performed using the [Wave](https://wave.webaim.org/) validator to provide key information about the accessibility standard of the website. Pages that required login were beyond the purview of the [Wave](https://wave.webaim.org/) browser tool, so the Wave extension for Google Chrome was used, which can be found [here](https://wave.webaim.org/extension/).

**Page**<br>
- Error explanations
<details>
<summary>Home results</summary>
<img src="/documentation/testing/wave_home.png">
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
**Warnings**:
- Explain warnings here

**Errors**
- Explain errors here, but there should be none.

<br>
Screenshots of the validation results are shown here:

<details>
    <summary>Page</summary>
    <img src="/documentation/testing/html_home.png">
</details>

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

Explanation of errors:

The env.py file was also linted showing no errors but the screenshot has been omitted for security issues as it contains sensitive information.
<details>
    <summary>File 1 results</summary>
    <img src="/documentation/testing/python_init.png">
</details>

## Bugs

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