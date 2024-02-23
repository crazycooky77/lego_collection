# Online Lego Collection
This site is made for avid Lego collectors! You can keep track of your sets, their status, and where they are (like your attic, or spare room). You can Favourite sets, or add sets you don't own yet to build out a wish list. But the Lego page has a wish list, you say? Unfortunately you can't share that one! While sharing features are not yet implemented on this page, they will be soon, and you can then share your entire collection, and your wish list, with friends and family (or even strangers if you like)! Your Online Lego Collection also has a field to keep track of missing pieces in your sets, when needed, and you can sort and filter your collection to be able to easily access that information and more. This is your one-stop-shop to keep track of all your sets and what's happening with them.

<img src='static/images/readme/amiresponsive.webp' alt='Am I Responsive Image'>

1. [User Experience](#user-experience)
   1. [User Stores](#user-stories)
      1. [Visitor Goals](#visitor-goals)
         1. [First-Time Visitor Goals](#first-time-visitor-goals)
         2. [Returning Visitor Goals](#returning-visitor-goals-)
         3. [Frequent Visitor Goals](#frequent-visitor-goals-)
   2. [Design](#design)
      1. [Colour Palette](#colour-palette)
      2. [Typography](#typography)
      3. [Imagery](#imagery)
   3. [Site Planning](#site-planning)
      1. [Lucidchart](#lucidchart)
      2. [Wireframes](#wireframes)
2. [Features](#features)
   1. [To Be Implemented](#to-be-implemented)
   2. [Closed Enhancements](#closed-enhancements)
3. [Technologies](#technologies)
4. [Testing](#testing)
   1. [Manual Testing](#manual-testing)
   2. [Automated Testing](#automated-testing)
   3. [Validator Testing](#validator-testing)
      1. [WAVE](#wave)
      2. [Lighthouse](#lighthouse)
      3. [PEP8](#pep8)
   4. [Bugs](#bugs)
5. [Deployment](#deployment)
   1. [Heroku](#heroku)
   2. [Droplet](#droplet)
6. [Credits](#credits)

## User Experience

### Visitor Goals

#### First-Time Visitor Goals
- As a first-time visitor to the site, I can create an account and a Lego collection to keep track of my sets.
- As a first-time visitor to the site, I can view public Lego collections, and Lego collections shared with me.*

_*Once Sharing features are enabled_

#### Returning Visitor Goals 
- As a returning visitor to the site, I can log into my account to view and edit my Lego collection.
- As a returning visitor to the site, I can manage my account, to ensure passwords, usernames, and email addresses are kept up-to-date and secure.

#### Frequent Visitor Goals 
- As a frequent visitor to the site, I can manage my Lego collection, including the build status and location for all my sets.
- As a frequent visitor to the site, I can create new Lego sets in the database, so I and others can add them to collections.
- As a frequent visitor, I can delete my Lego collection, and my account.

### User Stories
All implemented, detailed EPICs and related user stories are available in [project Issues](https://github.com/crazycooky77/ci_project4/issues?q=is%3Aissue+is%3Aclosed+-label%3Abug+-label%3Adocumentation+-label%3Awont-have+-label%3Awontfix+-label%3Aenhancement).

### Design

#### Colour Palette
<img src='static/images/readme/colourmind.webp' alt='Colourmind image'>

#### Typography
2 different Google Fonts were used for the [page title](https://fonts.google.com/specimen/Londrina+Outline?query=londrina) and [website text](https://fonts.google.com/specimen/Londrina+Solid?query=londrina). They are the same font in different styles for improved design.

#### Imagery
AI-generated images were used throughout. [Stable Diffusion](https://github.com/AUTOMATIC1111/stable-diffusion-webui) and [ComfyUI](https://stable-diffusion-art.com/how-to-install-comfyui/) were used with the [Dreamshaper 8](https://civitai.com/models/4384/dreamshaper) model.

### Site Planning

#### Lucidchart
Lucidchart was used to plan out the database models. An additional "Build Status" was later added ("Extra").

<img src='static/images/readme/lucid.webp' alt='Lucidchart image'>

#### Wireframes
Wireframes were used to plan out the pages for the site.

##### Homepage
Logged in:
<img src='static/images/readme/home-logged-in.webp' alt='Homepage wireframe (logged in)'>

Logged out:
<img src='static/images/readme/home-logged-out.webp' alt='Homepage wireframe (logged out)'>

#### Collections
Main page with collection - slight adjustments to buttons were made for better styling and added pagination:
<img src='static/images/readme/col.webp' alt='Collection wireframe'>

Main page without collections:
<img src='static/images/readme/col-no-col.webp' alt='Collection page without collections wireframe'>

Add Sets - this page was split into 2 in the end. 1 page for the "Global Set Details" ("Create Set" in the final page version), and 1 page for the "Personal Set Details" ("Add Set"):
<img src='static/images/readme/col-add-set.webp' alt='Add/Create set wireframe'>

Additionally, a new view was added but not planned in wireframes for existing collections without any sets. No sort/filter buttons are shown, but instead a message advising the user to add or create a set.

#### Profile
Logged in:
<img src='static/images/readme/profile-logged-in.webp' alt='Profile logged in wireframe'>

Logged out:
<img src='static/images/readme/profile-logged-out.webp' alt='Profile logged out wireframe'>

#### Shared
Sharing features are not yet implemented. However wireframes were created to plan out the features. 

Logged in with selected collection:
<img src='static/images/readme/shared-logged-in-selected-col.webp' alt='Shared logged in wireframe'>

Logged in without a selected collection (dropdown list for all collections the user was given access to):
<img src='static/images/readme/shared-logged-in-unselected-col.webp' alt='Shared logged in without selected collection wireframe'>

Logged out (public collection link):
<img src='static/images/readme/shared-logged-out.webp' alt='Shared logged out wireframe'>

## Features
All features have been planned and outlined in the [Kanban board](https://github.com/users/crazycooky77/projects/1) for the project using Issues. The implemented features are available [here](https://github.com/crazycooky77/ci_project4/issues?q=is%3Aissue+is%3Aclosed+-label%3Abug+-label%3Awont-have+-label%3Awontfix+-label%3Adocumentation).

### To Be Implemented
Features not yet implemented are available in the [project's Kanban board](https://github.com/users/crazycooky77/projects/1) in the To Do and In Progress columns, as well as [these EPICs](https://github.com/crazycooky77/ci_project4/issues?q=is%3Aopen+is%3Aissue+label%3AEPIC).

### Closed Enhancements
Closed enhancements can be found [here](https://github.com/crazycooky77/ci_project4/issues?q=is%3Aissue+label%3Aenhancement+is%3Aclosed). If an enhancement is labelled as "wont-have", it was not and will not be implemented.

## Technologies
- [Lucidchart](https://www.lucidchart.com/pages) to create the entity relationship diagram
- [Balsamiq](https://balsamiq.com/wireframes/) to plan out the pages using wireframes
- [Pycharm](https://www.jetbrains.com/pycharm/) IDE linked to GitHub to edit the project files
- [GitPod](https://gitpod.io/) when utilising Tutor Support
- [GitHub](https://github.com/) to store the code and for version-control
- [GitHub Desktop](https://desktop.github.com/) to be able to commit changes to the code without having to use the web-based tool
- [Heroku](https://heroku.com/) to deploy the app and have it available for use online
- [Python](https://www.python.org/) for project functionality
  - [Cloudinary](https://cloudinary.com/documentation/django_integration) for image upload and management
  - [Coverage](https://coverage.readthedocs.io/en/7.4.1/) to check test coverage for the project
  - [dj-database-url](https://pypi.org/project/dj-database-url/) for easier database configuration
  - [django-allauth](https://docs.allauth.org/en/latest/) for user creation, authentication, and management
  - [Django-Select2](https://django-select2.readthedocs.io/en/latest/) to enable database searching within a dropdown
  - [Gunicorn](https://gunicorn.org/) to enable web services
  - [Pillow](https://pypi.org/project/pillow/) for image processing
  - [Whitenoise](https://whitenoise.readthedocs.io/en/latest/) for static files
- [JavaScript](https://www.javascript.com/) for site functions
- [HTML](https://html.spec.whatwg.org/) for the templates for each of the pages for the site
- [CSS](https://www.w3.org/Style/CSS/Overview.en.html) for page styling
- [Django](https://www.djangoproject.com/) was used as the Python framework for the project
- [PostgreSQL](https://www.postgresql.org/) as the database for local development
- [ElephantSQL](https://www.elephantsql.com/) as the database for the live web app
- [Favicon](https://favicon.io/) to generate the page's Favicon
- [Flexbox](https://css-tricks.com/snippets/css/a-guide-to-flexbox/) for CSS styling
- [Unicorn Revealer](https://chromewebstore.google.com/detail/unicorn-revealer/lmlkphhdlngaicolpmaakfmhplagoaln?hl=en-GB) for CSS debugging
- [Wave](https://wave.webaim.org/extension/) for accessibility checks

## Testing

### Manual Testing
All manual testing in the below table was done using Microsoft Edge, Chrome, and Safari browsers, on MacOS, Windows 11, AndroidOS, and iOS.

| Function                                    |                                                                                                                                                                                                                                   Expectation                                                                                                                                                                                                                                    | MacOS Safari | iOS Safari | iPadOS Chrome | Windows 11 Edge | AndroidOS Chrome |
|---------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:-------------|:-----------|:--------------|:----------------|:-----------------|
| Homepage view (logged out)                  |                                                                                                                                                                                       When viewing the homepage while logged out, the user should be asked to log in or create an account                                                                                                                                                                                        | &check;      | &check;    | &check;       | &check;         | &check;          |
| Collections view (logged out)               |                                                                                                                                                                                   When viewing the collections page while logged out, the user should be asked to log in or create an account                                                                                                                                                                                    | &check;      | &check;    | &check;       | &check;         | &check;          |
| Create Collection (logged out)              |                                                                                                                                                                                      When logged out, the Create Collection page will show a message asking the user to sign up or log in.                                                                                                                                                                                       | &check;      | &check;    | &check;       | &check;         | &check;          |
| Edit Collection (logged out)                |                                                                                                                                                                                       When logged out, the Edit Collection page will show a message asking the user to sign up or log in.                                                                                                                                                                                        | &check;      | &check;    | &check;       | &check;         | &check;          |
| Create New Set (logged out)                 |                                                                                                                                                                                          When logged out, the Create Set page will show a message asking the user to sign up or log in.                                                                                                                                                                                          | &check;      | &check;    | &check;       | &check;         | &check;          |
| Add Set (logged out)                        |                                                                                                                                                                                           When logged out, the Add Set page will show a message asking the user to sign up or log in.                                                                                                                                                                                            | &check;      | &check;    | &check;       | &check;         | &check;          |
| Profile view (logged out)                   |                                                                                                                                                                                     When viewing the profile page while logged out, the user should be asked to log in or create an account                                                                                                                                                                                      | &check;      | &check;    | &check;       | &check;         | &check;          |
| Shared view (logged out)                    |                                                                                                                                                                         When viewing the Shared page while logged out, a message should be displayed advising that the sharing features are coming soon                                                                                                                                                                          | &check;      | &check;    | &check;       | &check;         | &check;          |
| Create Account (logged out)                 |                                                   The Create Account page, when logged out, should display sign-in and forgot password links, as well as the required fields for creating an account and the Signup button.<br><br>When entering information that doesn't cause errors, the account should be created in the database, and the user should automatically be logged in and redirected to their Collections page                                                   | &check;      | &check;    | &check;       | &check;         | &check;          |
| Create Account Errors                       |                                                                                                                                     When creating an account, if the user enters a username or email address that is already in the database, or a password that doesn't meet the minimum requirements, an error message should be displayed                                                                                                                                     | &check;      | &check;    | &check;       | &check;         | &check;          |
| Forgot Login/Password (logged out)          |                                                                                                                                                                    Reset password links should redirect to the password reset page and allow the user to send a forgot password email to their email address                                                                                                                                                                     | &check;      | &check;    | &check;       | &check;         | &check;          |
| Password Reset Email                        |                                                                                When the user clicks the link in the email to reset their password, they should be directed to a page to change it.<br><br>If the password meets the minimum requirements, the password should be successfully changed for the account, the user automatically logged in, and redirected to their Collections page                                                                                | &check;      | &check;    | &check;       | &check;         | &check;          |
| Password Reset Email Errors                 |                                         When the user clicks the link in the email to reset their password, they should be directed to a page to change it.<br><br>If the password they enter does not meet the minimum requirements,they should receive an error.<br><br>If the user uses a password reset link that is invalid (expired/already used), they should also receive an error and be directed to request a new reset email                                          | &check;      | &check;    | &check;       | &check;         | &check;          |
| Log In (logged out)                         |                                                                                                                                                                              When a user logs into their account with the correct credentials, they should be redirected to their Collections page.                                                                                                                                                                              | &check;      | &check;    | &check;       | &check;         | &check;          |
| Log In Errors                               |                                                                                                                                                                                       If using incorrect credentials when trying to log in, error messages should be displayed accordingly                                                                                                                                                                                       | &check;      | &check;    | &check;       | &check;         | &check;          |
| Create Account (logged in)                  |                                                                                                                                                                            The Create Account page should automatically redirect to the Collections page if a user tries to access it while logged in                                                                                                                                                                            | &check;      | &check;    | &check;       | &check;         | &check;          |
| Forgot Login/Password (logged in)           |                                                                                                                                                                The reset password page should provide a message informing the user they are already logged in, and referring to change password and profile pages                                                                                                                                                                | &check;      | &check;    | &check;       | &check;         | &check;          |
| Homepage view (logged in)                   |                                                                                                                                                                                               A message should be displayed to the user, referring them to their Collections link                                                                                                                                                                                                | &check;      | &check;    | &check;       | &check;         | &check;          |
| Collections view (logged in, no collection) |                                                                                                                                                                                                            A button to Create Collection should be shown to the user                                                                                                                                                                                                             | &check;      | &check;    | &check;       | &check;         | &check;          |
| Collections view (logged in, no sets)       |                                                                                                                                                                               Buttons should be shown to the user to allow them to Add Set, Create New Set, Edit Collection, or Delete Collection                                                                                                                                                                                | &check;      | &check;    | &check;       | &check;         | &check;          |
| Collections view (logged in, with sets)     |                                                            Buttons should be available for the user to sort, reverse sort and filter their collection, as well as Add Set, Create New Set, Edit Collection, or Delete Collection.<br><br>Users can, of course, also view all the information for their sets on this page (image, number, name, pieces, build status, set location, missing pieces, favourite status)                                                             | &check;      | &check;    | &check;       | &check;         | &check;          |
| Create Collection (with custom picture)     |                                                                                                                                                                              Users can create a collection and upload their own picture when doing so, which will then show on the Collections page                                                                                                                                                                              | &check;      | &check;    | &check;       | &check;         | &check;          |
| Create Collection (without picture)         |                                                                                                                                                      Users can create a collection without uploading a custom picture, and their collection name will then show on the Collections page with the default collection picture                                                                                                                                                      | &check;      | &check;    | &check;       | &check;         | &check;          |
| Create Collection Errors                    |                                                                                                                                                                                      If a user tries to create a collection without a name, they will receive a message that it is required                                                                                                                                                                                      | &check;      | &check;    | &check;       | &check;         | &check;          |
| Create New Set (without picture)            |                                                                                                                   Users can create a new set, which will add it to the database with a set number and name, and optionally set picture, number of pieces (in the set) and link to the Lego site. When not adding a picture, a default set image will be added.                                                                                                                   | &check;      | &check;    | &check;       | &check;         | &check;          |
| Create New Set (with custom picture)        |                                                                                            Users can create a new set, which will add it to the database with a set number and name, and optionally set picture, number of pieces (in the set) and link to the Lego site. When creating a set with an uploaded picture, that picture will be available for that set in the database.                                                                                             | &check;      | &check;    | &check;       | &check;         | &check;          |
| Create New Set Errors                       |                                                                                                                                                  If a user tries to create a set using a set number already in the database, they will receive an error. They will also receive an error if no set number and name are provided                                                                                                                                                  | &check;      | &check;    | &check;       | &check;         | &check;          |
| Add Set (logged in)                         |                                                                                                                                               Users can search for sets in the database, add a build status (required), as well as (optional) set location, favourited status, and missing pieces, and add it to their collection                                                                                                                                                | &check;      | &check;    | &check;       | &check;         | &check;          |
| Add Set Errors                              |                                                                                                                                                                           If a Build Status is not provided and the user tries to save the set to their collection, they will receive an error message                                                                                                                                                                           | &check;      | &check;    | &check;       | &check;         | &check;          |
| Sorting                                     |                                                                   Sorting options should be available for Set Number, Set Name, # Pieces, Build Status, Set Location, Missing Pieces, and Favourite.<br><br>Clicking the applicable option will sort the sets in the list accordingly.<br><br>Clicking "Reverse Sort" will reverse the set list, and "Reset Sort" will reload the page without special sorting                                                                   | &check;      | &check;    | &check;       | &check;         | &check;          |
| Filtering                                   |                                                                            Filtering options should be available for # Pieces, Build Status, Set Location, Missing Pieces, and Favourite.<br><br>Clicking the applicable option will enable the Filter Details to be selected, and the sets to be filtered accordingly.<br><br>Clicking "Reset Filter" will reload the page without special filtering                                                                            | &check;      | &check;    | &check;       | &check;         | &check;          |
| Column Selection (small screens only)       |                                                                        On small screens (typically phones), only 4 columns can be shown at a time. An extra dropdown should be shown for users to change which columns they are viewing, from the default.<br><br>When users remove and add columns using the checkboxes in this dropdown, the visible columns should be updated accordingly in the table                                                                        | N/A          | &check;    | N/A           | N/A             | &check;          |
| Edit Collection (logged in)                 | Users can change their collection name and picture, and their set details (build status, set location, missing pieces, favourite status).<br><br>They can also delete sets in bulk from their collection and have buttons available to Save or Discard the changes made.<br><br>Save Changes will update all the relevant data in the database.<br><br>Discard Changes will redirect the user back to Collections. Add/Create New Set buttons are available on this page as well | &check;      | &check;    | &check;       | &check;         | &check;          |
| Edit Collection Errors                      |                                                                                                                                                                             If the user tries to Save Changes while the collection name or any set build status is empty, they will receive an error                                                                                                                                                                             | &check;      | &check;    | &check;       | &check;         | &check;          |
| Delete Collection                           |                                                                                                                                               Users can delete their collection using the button on their Collections page. Once they confirm in the pop-up that they want to proceed, the collection is deleted from the database                                                                                                                                               | &check;      | &check;    | &check;       | &check;         | &check;          |
| Profile view (logged in)                    |                                                                                                                                                The user should be able to see their profile details (username, email, privacy, set details), change their profile (username, email, privacy, password), and delete their account                                                                                                                                                 | &check;      | &check;    | &check;       | &check;         | &check;          |
| Change Username                             |                                                                                                                                                           When entering a new username on the Profile page and pressing the Save button, the user's username should be updated in the database, if it is not yet taken                                                                                                                                                           | &check;      | &check;    | &check;       | &check;         | &check;          |
| Change Username Errors                      |                                                                                                                                                      When entering a new username on the Profile page and pressing the Save button, the user should receive an error message if the username already exists in the database                                                                                                                                                      | &check;      | &check;    | &check;       | &check;         | &check;          |
| Change Email                                |                                                                                                                                         When entering a new email address on the Profile page and pressing the Save button, the user's email should be added to their account in the database, if it is not yet used in another account                                                                                                                                          | &check;      | &check;    | &check;       | &check;         | &check;          |
| Change Email Errors                         |                                                                                                                                                         When entering an email address that is already associated with an account, and pressing the Save button, the user should receive an error message to that effect                                                                                                                                                         | &check;      | &check;    | &check;       | &check;         | &check;          |
| Update account Privacy                      |                                                                                                                                                                     Users can choose a different Privacy setting for their account in their Profile, and when they Save it, it should update in the database                                                                                                                                                                     | &check;      | &check;    | &check;       | &check;         | &check;          |
| Change Password                             |                                                                                                            Users can change their password by entering their current password, and a new password twice, that meets the minimum requirements.<br><br>An error will appear if the new password does not meet those requirements, or the current password is incorrect                                                                                                             | &check;      | &check;    | &check;       | &check;         | &check;          |
| Manage Emails                               |                                                                                                                                                                          Users can re-send verification emails and remove addresses from their account, when applicable, as well as add email addresses                                                                                                                                                                          | &check;      | &check;    | &check;       | &check;         | &check;          |
| Email Verification/Removal                  |                                                                     When clicking a valid verification link for an email, the user should be directed to the Profile page, and the email should be confirmed. Other addresses in the account should be automatically removed.<br><br>When removing emails, an error should appear if the user attempts to remove the verified or only email in the account.                                                                      | &check;      | &check;    | &check;       | &check;         | &check;          |
| Email Verification/Removal Errors           |                                                                                                                          If clicking an invalid/expired email verification link, they should receive an error to that effect and be advised to request a new one.<br><br>If the user tries to remove a second unverified email, that should be removed.                                                                                                                          | &check;      | &check;    | &check;       | &check;         | &check;          |
| Delete Account                              |                                                                                                            On the Profile page, users can delete their account by checking the box, clicking the Delete Account button, and confirming deletion in the pop-up menu. After doing so, the account is deleted from the database and a confirmation is shown to the user                                                                                                             | &check;      | &check;    | &check;       | &check;         | &check;          |
| Delete Account Errors                       |                                                                                                                                                                                   If the user tries to delete their account without ticking the required checkbox, they will receive an error                                                                                                                                                                                    | &check;      | &check;    | &check;       | &check;         | &check;          |
| Shared view (logged in)                     |                                                                                                                                                                          When viewing the Shared page while logged in, a message should be displayed advising that the sharing features are coming soon                                                                                                                                                                          | &check;      | &check;    | &check;       | &check;         | &check;          |
| Log In (logged in)                          |                                                                                                                                                                         When a user accesses the login page while already logged in, they should be automatically redirected to their Collections page.                                                                                                                                                                          | &check;      | &check;    | &check;       | &check;         | &check;          |
| Log Out                                     |                                                                                                                                                                                                     When a user logs out, they are logged out and redirected to the homepage                                                                                                                                                                                                     | &check;      | &check;    | &check;       | &check;         | &check;          |

### Automated Testing
115 automated tests were created to ensure forms and views perform as intended. These tests provide 99% coverage for the project and all tests pass.

<img src='static/images/readme/coverage-run.webp' alt='Coverage test run'>
<img src='static/images/readme/coverage-report.webp' alt='Coverage report'>

### Validator Testing

#### HTML
All pages were put through the [W3 HTML Validator](https://validator.w3.org/#validate_by_input) and all issues identified were resolved, where possible. There is 1 issue below that could not be resolved.

<img src='static/images/readme/validator-w3.webp' alt='W3 Validator Results'>

The **Add Set** page has an error, however this is from django-select2:

`Error: A select element with a required attribute, and without a multiple attribute, and without a size attribute whose value is greater than 1, must have a child option element.`

#### CSS
CSS code was put through [W3C](https://jigsaw.w3.org/css-validator/#validate_by_input) and no errors are found.

<img src='static/images/readme/validator-w3c.webp' alt='W3C Validator Results'>

#### JSHint
[JSHint](https://jshint.com/) was used to validate the JavaScript used. There are no legitimate errors found.

- The validator twice shows the error "The body of a for in should be wrapped in an if statement to filter unwanted properties from the prototype."
  - The lines in question are, however, wrapped in if statements
- "$" is mentioned as an undefined variable several times, however these are from JQuery.
- 3 unused variables mentioned are used in templates

<img src='static/images/readme/validator-jshint.webp' alt='JSHint Validator Results'>

#### PEP8
Some spacing issues (lines too long) were identified by [PEP8](https://pep8ci.herokuapp.com/), but these were all resolved except for settings.py, where one of the Django password validator names is too long.

<img src='static/images/readme/validator-pep8.webp' alt='PEP8 Validator Results'>

#### WAVE
All pages were checked with WAVE. There are some Alerts, however nothing unexpected. All errors were resolved.

<img src='static/images/readme/validator-wave.webp' alt='Wave Validator Results'>

#### Lighthouse
Lighthouse was run on all pages for the site and issues identified were resolved, where possible.
- Images were all converted from png to webp
- Missing meta header details were added
- JavaScript console errors resolved

Cumulative Layout Shifts caused a lower score in Performance for the pages listed below. This was deemed acceptable, to enable better responsiveness and dynamic resizing.
- Create Collection
- Create Set
- Profile page
- Change password
- Change email

Accessibility issues were noted on some pages, due to automatically rendered Django forms:
- Add Set
  - ARIA input fields without accessible names (from Django Select2)
- Collections page with sets
  - Missing labels noted, but labels are present (though hidden). Text is still provided for these fields
- Edit Collection
  - Form/select/input fields are missing labels, from Django forms
- Profile
  - Form/select/input fields are missing labels, from Django forms

Best Practice and SEO issues:
- Collections page with sets
  - User-entered images are provided with low resolution and incorrect aspect ratios (this is a conscious choice to keep the table layout styled accordingly)
  - Hamburger links are not crawlable, however they are formatted as normal links
- Edit Collection
  - User-entered images are provided with low resolution and incorrect aspect ratios (this is a conscious choice to keep the table layout styled accordingly)


Homepage
<img src='static/images/readme/lh-home.webp' alt='Lighthouse scores for Hhomepage'>

Collections page without collections
<img src='static/images/readme/lh-col-no-col.webp' alt='Lighthouse scores for Collection page without Collection'>

Create Collection
<img src='static/images/readme/lh-create-col.webp' alt='Lighthouse scores for Create Collection page'>

Collections page with collection but no sets
<img src='static/images/readme/lh-col-no-sets.webp' alt='Lighthouse scores for Collection page without Sets'>

Create Set
<img src='static/images/readme/lh-create-set.webp' alt='Lighthouse scores for Create Set page'>

Add Set
<img src='static/images/readme/lh-add-set.webp' alt='Lighthouse scores for Add Set page'>

Collections page with sets
<img src='static/images/readme/lh-col-w-sets.webp' alt='Lighthouse scores for Collection page with Sets'>

Edit Collection
<img src='static/images/readme/lh-edit-col.webp' alt='Lighthouse scores for Edit Collection page'>

Profile page
<img src='static/images/readme/lh-profile.webp' alt='Lighthouse scores for Profile page'>

Change password
<img src='static/images/readme/lh-change-pw.webp' alt='Lighthouse scores for Change Password page'>

Change email
<img src='static/images/readme/lh-change-email.webp' alt='Lighthouse scores for Change Email page'>

Shared page
<img src='static/images/readme/lh-shared.webp' alt='Lighthouse scores for Shared page'>


### Bugs
Known bugs are all listed in these [project's Issues](https://github.com/crazycooky77/ci_project4/issues?q=is%3Aopen+is%3Aissue+label%3Abug) with the label "bug".

Fixed bugs can also be found in the [project's Issues here](https://github.com/crazycooky77/ci_project4/issues?q=is%3Aissue+label%3Abug+is%3Aclosed).

## Deployment
The site was deployed on both Heroku and using a [Digital Ocean](https://www.digitalocean.com/) Droplet. This was to keep the site live after the project submission, and due to networking issues caused by Heroku (see [this bug](https://github.com/crazycooky77/ci_project4/issues/44) for additional details).

### Heroku
For Heroku, the following steps were used for deployment:
1. Cloned the basic repository from [Code Institute](https://github.com/Code-Institute-Org/ci-full-template)
   1. Code > Open with GitHub Desktop
2. Created new repository in [own GitHub](https://github.com/crazycooky77/ci_project4) for the cloned repository
3. Created new app on [Heroku](https://dashboard.heroku.com/apps)
   1. New > Create new app
   2. Provide app name and select region > Create app
4. Linked Heroku to cloned GitHub repository
   1. Click GitHub in the Deployment method section
   2. Log into GitHub, provide access to Heroku, and type in the repository name
   3. Search
   4. Connect
5. Enabled automatic deploys
   1. Tick the box for Automatic deploys in the corresponding section
6. Added python buildpack in the Settings > Buildpacks section
7. Added necessary Config Vars

### Droplet
To deploy the project using a Digital Ocean Droplet, these steps were followed:
1. In your settings.py in GitHub for ALLOWED_HOSTS and CSRF_TRUSTED_ORIGINS:
   1. Ensure "localhost" and "https\://localhost" are added
   2. Add environment variables for your DROPLET_IP and your public domain name (if applicable)
2. Create Droplet in Digital Ocean project
   1. Select the nearest Datacenter and preferred OS
   2. Leave Droplet Type as Basic (Shared CPU)
   3. Select Regular > $4/mo CPU options (choose a more expensive plan if desired)
   4. Select the Authentication Method
   5. Enter the name for your Droplet (or use the default one provided)
   6. Create Droplet
   7. Click "Enable now" for Reserved IP within the Droplet
   8. Click "Assign Reserved IP"
      1. If you have a public domain name you want to use, ensure you add your reserved Droplet IP to your URL forwarding
   9. Within Networking > Firewalls, "Create Firewall"
      1. Enter a name for your firewall
      2. New rule under SSH
         1. HTTP
      3. New rule under SSH
         1. HTTPS
      4. Search for your Droplet name under Apply to Droplets
      5. "Create Firewall"
3. Open the Droplet Console and clone your GitHub repository with the Django project
   1. In the GitHub repository, click Code and copy the HTTPS link
   2. In the Droplet console: ```git clone <HTTPS_LINK>```
4. Update and install the necessary packages via the console
   1. ```sudo apt-get update```
   2. ```sudo apt-get dist-upgrade```
   3. ```sudo reboot```
   4. ```apt install python3-pip python3.11-venv nginx``` (replace with your python version as needed)
   5. ```sudo snap install core; sudo snap refresh core```
   6. ```sudo snap install --classic certbot```
   7. ```cd <CLONED_GITHUB_PROJECT_FOLDER>```
   8. If you have/need a .env file, you can copy it via your local machine's console using:
      1. ```scp LOCAL_FOLDER/.env DROPLET_USER@DROPLET_IP:/root/DROPLET_DIRECTORY```
      2. Remember to add your environment variables for your Droplet IP and public domain name (if applicable)
   9. ```python3 -m venv .venv```
   10. ```source .venv/bin/activate```
   11. ```python3 -m pip install -r requirements.txt```
   12. ```deactivate```
5. Some files on the Droplet now need to be edited, and services enabled and started, so that your site will constantly run without having to manually runserver
   1. In your Droplet's console: ```vi /etc/systemd/system/gunicorn.socket```
   2. ```i``` (for "insert")
   3. Paste:
    ```
    [Unit]
    Description=gunicorn socket
    
    [Socket]
    ListenStream=/run/gunicorn.sock
    
    [Install]
    WantedBy=sockets.target
    ```
   4. Press the Escape key
   5. Type: ```:wq``` and press Enter ("write quit")
   6. ```vi /etc/systemd/system/gunicorn.service```
   7. ```i```
   8. Paste:
   ```
    [Unit]
    Description=gunicorn daemon
    Requires=gunicorn.socket
    After=network.target
    
    [Service]
    User=root
    Group=www-data
    WorkingDirectory=/root/<GITHUB_PROJECT_FOLDER>
    EnvironmentFile=/root/<GITHUB_PROJECT_FOLDER>/.env
    ExecStart=/root/<GITHUB_PROJECT_FOLDER>/.venv/bin/gunicorn \
              --access-logfile - \
              --workers 1 \
              --timeout 120 \
              --bind unix:/run/gunicorn.sock \
              <DJANGO_PROJECT_NAME>.wsgi:application
    
    [Install]
    WantedBy=multi-user.target
    ```
   9. Escape key
   10. ```:wq``` and Enter
   11. ```vi /etc/nginx/sites-available/<GITHUB_PROJECT_FOLDER>```
   12. ```i```
   13. Paste:
   ```
    server {
        listen 80;
        server_name <PUBLIC_DOMAIN_NAME>;

        location = /favicon.ico { access_log off; log_not_found off; }
        location /<STATIC_ROOT_FOLDER_FROM_SETTINGS_PY>/ {
            root /root/<GITHUB_PROJECT_FOLDER>>;
        }

        location / {
            include proxy_params;
            proxy_pass http://unix:/run/gunicorn.sock;
        }
    }
    ```
   14. Escape key
   15. ```:wq``` and Enter
   16. ```systemctl enable gunicorn.socket```
   17. ```systemctl enable gunicorn.service```
   18. ```systemctl start gunicorn.service```
   19. ```systemctl start gunicorn.socket```
   20. ```vi /etc/nginx/nginx.conf```
   21. Use your arrow key to move your text cursor to the empty line above "sendfile on;"
   22. ```o```
   23. ```client_max_body_size 10M;``` (change 10M to a larger number if you want to allow larger file sizes)
   24. Escape key
   25. ```:wq``` and Enter
   26. ```sudo ln -s /etc/nginx/sites-available/<GITHUB_FOLDER> /etc/nginx/sites-enabled```
   27. ```nginx -t```
       1. You want to see a "test is successful" here to ensure the previous steps were correctly followed and without typos
6. Adjust settings as below to enable encryption on your webpage via letsencrypt. This only works if you own the domain yourself and is automatically renewed every 90 days.
   1. ```sudo ln -s /snap/bin/certbot /usr/bin/certbot```
   2. ```certbot --nginx -d <YOUR_PUBLIC_DOMAIN_NAME>```
      1. Enter an email address, as required by the console
      2. ```Y``` to agree to terms of service
      3. ```N``` to decline sharing your email address
   3. ```sudo systemctl restart nginx```
7. After making changes in GitHub, you will need to ```git pull``` in the Droplet console and ```systemctl restart gunicorn.service```

## Credits
The base template was cloned from the [Code Institute GitHub repository](https://github.com/Code-Institute-Org/ci-full-template). Various other resources were used for different features. They are all listed below, categorised accordingly.

Special thanks to [my husband](https://twitter.com/fbuechsel) who helped with troubleshooting and figuring out the Droplet setup, and [my mentor](https://github.com/CluelessBiker) for her various resources and constant reminders to document **everything**. Also thank you to Tutor Support for helping with my complicated questions, even if the topic was out-of-scope.

#### CustomUser Documentation
- [Django authentication](https://docs.djangoproject.com/en/5.0/topics/auth/default/)
- [CustomUser model usage](https://docs.djangoproject.com/en/3.2/topics/auth/customizing/#substituting-a-custom-user-model)
- [CustomUser user management](https://reintech.io/blog/creating-a-custom-user-management-system-in-django)
- [Choices fields in models](https://docs.djangoproject.com/en/3.1/ref/models/fields/#field-choices-enum-subclassing)
- [Case-insensitive usernames](https://stackoverflow.com/questions/13190758/django-case-insensitive-matching-of-username-from-auth-user)

#### CSS
- [Rainbow gradient](https://stackoverflow.com/questions/40557461/rainbow-gradient-on-text-in-css)

#### Custom Form Messages
- [Custom invalid login messages](https://stackoverflow.com/questions/47923952/python-django-how-to-display-error-messages-on-invalid-login)
- [Custom form errors](https://stackoverflow.com/questions/24273839/django-allauth-custom-login-does-not-show-errors)

#### Account Management
- [Django introduction](https://docs.djangoproject.com/en/4.0/intro/tutorial03/)
- [Custom login view](https://stackoverflow.com/questions/75401759/how-to-set-up-login-view-in-python-django)
- [Remove intermediate logout page](https://stackoverflow.com/questions/18134807/how-to-disable-intermediate-signout-page-in-django-allauth)
- [Allauth account templates (to assist in template customisation)](https://github.com/pennersr/django-allauth/tree/main/allauth/templates/account)
- [Updating user profiles](https://dev.to/earthcomfy/django-update-user-profile-33ho)
- [User-led account deletion](https://stackoverflow.com/questions/38047408/how-to-allow-user-to-delete-account-in-django-allauth)
- [Fixing stray django-added tags](https://stackoverflow.com/questions/63455725/remove-unwanted-th-td-and-tr-tags-from-django-generated-form)

#### Collection Sort, Filter, Edit
- [Assign values to objects for inserting into database (collection owner from collection model for lego_collection model)](https://forum.djangoproject.com/t/automatically-get-user-id-to-assignate-to-form-when-submitting/5333/7)
- [Javascript redirect bugfix for sorting and filtering](https://stackoverflow.com/questions/8898998/window-location-replace-not-working-to-redirect-browser)
- [Edit multiple objects at once (for sets in collections)](https://collingrady.wordpress.com/2008/02/18/editing-multiple-objects-in-django-with-newforms/)
- [Cascading dropdowns for filter](https://www.w3schools.com/howto/howto_js_cascading_dropdown.asp)
- [Pagination](https://docs.djangoproject.com/en/5.0/topics/pagination/)

#### Collection Mobile View
- [HTML select option checkboxes](https://stackoverflow.com/questions/17714705/how-to-use-checkbox-inside-select-option)
- [Display column based on checkboxes](https://stackoverflow.com/questions/60344393/how-to-display-hide-columns-when-checkboxes-are-checked)
- [Hide columns based on checkboxes](https://www.sitepoint.com/community/t/hide-table-column-whose-checkbox-is-not-checked-on-page-load/242783)

#### Droplet Setup
- [Update Kernel](https://docs.digitalocean.com/products/droplets/how-to/kernel/upgrade/)
- [Installing requirements](https://stackoverflow.com/questions/75602063/pip-install-r-requirements-txt-is-failing-this-environment-is-externally-mana)
- [Setup instructions](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-22-04)
- [Error fix for file upload](https://www.cyberciti.biz/faq/linux-unix-bsd-nginx-413-request-entity-too-large/)
- [Encrypting pages](https://www.digitalocean.com/community/tutorials/how-to-secure-nginx-with-let-s-encrypt-on-ubuntu-22-04)