# Online Lego Collection
_introduction_

<img src='assets/images/am-i-responsive.webp' alt='Am I Responsive Image'>

1. [User Experience](#user-experience)
2. [Features](#features)
3. [Technologies](#technologies)
4. [Testing](#testing)
5. [Deployment](#deployment)
6. [Credits](#credits)
7. [Media](#media)

## User Experience
_First time, returning, frequent visitor goals_

### User Stories
All implemented, detailed EPICs and related user stories are available in [project Issues](https://github.com/crazycooky77/ci_project4/issues?q=is%3Aissue+is%3Aclosed+-label%3Abug+-label%3Adocumentation+-label%3Awont-have+-label%3Awontfix+-label%3Aenhancement).

_insert image_

### Design

#### Colour Palette
<img src='static/images/readme/colourmind.webp' alt='Colourmind image'>

#### Typography
2 different Google Fonts were used for the [page title](https://fonts.google.com/specimen/Londrina+Outline?query=londrina) and [website text](https://fonts.google.com/specimen/Londrina+Solid?query=londrina). They are the same font in different styles for improved design.

#### Imagery
AI-generated images were used throughout. [Stable Diffusion](https://github.com/AUTOMATIC1111/stable-diffusion-webui) and [ComfyUI](https://stable-diffusion-art.com/how-to-install-comfyui/) were used with the [Dreamshaper 8](https://civitai.com/models/4384/dreamshaper) model.

### Site Planning

#### Lucidchart
Lucidchart was used to plan out the database models.

<img src='static/images/readme/lucid.webp' alt='Lucidchart image'>

#### Wireframes
Wireframes were used to plan out the pages for the site.

##### Homepage
Logged in:
<img src='static/images/readme/home-logged-in.webp' alt='Homepage wireframe (logged in)'>

Logged out:
<img src='static/images/readme/home-logged-out.webp' alt='Homepage wireframe (logged out)'>

#### Collections
Main page with collection - slight adjustments to buttons were made for better styling:
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

_image_

### To Be Implemented
Features not yet implemented are available in the [project's Kanban board](https://github.com/users/crazycooky77/projects/1) in the To Do and In Progress columns.

_insert image_

### Closed Enhancements
Closed enhancements can be found [here](https://github.com/crazycooky77/ci_project4/issues?q=is%3Aissue+label%3Aenhancement+is%3Aclosed). If an enhancement is labelled as "wont-have", it was not and will not be implemented.

_insert image_

## Technologies
- [Lucidchart](https://www.lucidchart.com/pages) to create the entity relationship diagram
- [Balsamiq](https://balsamiq.com/wireframes/) to plan out the pages using wireframes
- [Pycharm](https://www.jetbrains.com/pycharm/) IDE linked to GitHub to edit the project files
- [GitHub](https://github.com/) to store the code and for version-control
- [GitHub Desktop](https://desktop.github.com/) to be able to commit changes to the code without having to use the web-based tool
- [Heroku](https://heroku.com/) to deploy the app and have it available for use online
- [Python](https://www.python.org/) for project functionality
  - [Cloudinary](https://cloudinary.com/documentation/django_integration) for image upload and management
  - [Coverage](https://coverage.readthedocs.io/en/7.4.1/) ???
  - [dj-database-url](https://pypi.org/project/dj-database-url/) for easier database configuration
  - [django-allauth](https://docs.allauth.org/en/latest/) for user creation, authentication, and management
  - [Django-Select2](https://django-select2.readthedocs.io/en/latest/) to enable database searching within a dropdown
  - [Gunicorn](https://gunicorn.org/) ???
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

### Automated Testing

### Validator Testing
_https://validator.w3.org/#validate_by_input_

_https://jigsaw.w3.org/css-validator/#validate_by_input_

_https://jshint.com/_

_https://pep8ci.herokuapp.com/_

_http://eightshapes.com/_

_Lighthouse, WAVE, Responsiveness (screen pixel width), different browsers and devices_

Lighthouse:
images to webp
missing meta details
javascript console errors
set cloudinary images to use a secure URL

Cumulative Layout Shifts causing dip in Performance score for create-col and create-set
Minor dip in Accessibility for add-set due to ARIA Input fields not having accessible names, however from django select2 field

col-w-sets has Accessibility dip for supposedly missing labels. Labels are present, but hidden, and text is still provided;
user-entered images provided with incorrect aspect ratio
hamburger links not crawlable

edit-col Accessibility issues due to form/select/input missing labels from django forms
user-entered images provided with incorrect aspect ratio

profile performance dip due to cumulative layout shifts
Accessibility issues due to form/select/input missing labels from django forms

change-pw performance dip due to cumulative layout shifts

change-email performance dip due to cumulative layout shifts


#### PEP8
<img src='assets/images/pep8.webp' alt='PEP8 result'>

### Bugs
Known bugs are all listed in the [project's Issues](https://github.com/crazycooky77/ci_project4/issues?q=is%3Aopen+is%3Aissue+label%3Abug) with the label "bug". The current list can also be viewed below.

_Insert image_

[Fixed bugs] can also be found in the [project's Issues](https://github.com/crazycooky77/ci_project4/issues?q=is%3Aissue+label%3Abug+is%3Aclosed).

_Insert image_

## Deployment
The site was deployed via the following steps:
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

## Credits
The base template was cloned from the [Code Institute GitHub repository](https://github.com/Code-Institute-Org/ci-full-template). Various other resources were used for different features. They are all listed below, categorised accordingly.

#### CustomUser Documentation
- [Django authentication](https://docs.djangoproject.com/en/5.0/topics/auth/default/)
- [CustomUser model usage](https://docs.djangoproject.com/en/3.2/topics/auth/customizing/#substituting-a-custom-user-model)
- [CustomUser user management](https://reintech.io/blog/creating-a-custom-user-management-system-in-django)
- [Choices fields in models](https://docs.djangoproject.com/en/3.1/ref/models/fields/#field-choices-enum-subclassing)

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

#### Collection Sort, Filter, Edit
- [Assign values to objects for inserting into database (collection owner from collection model for lego_collection model)](https://forum.djangoproject.com/t/automatically-get-user-id-to-assignate-to-form-when-submitting/5333/7)
- [Javascript redirect bugfix for sorting and filtering](https://stackoverflow.com/questions/8898998/window-location-replace-not-working-to-redirect-browser)
- [Edit multiple objects at once (for sets in collections)](https://collingrady.wordpress.com/2008/02/18/editing-multiple-objects-in-django-with-newforms/)
- [Cascading dropdowns for filter](https://www.w3schools.com/howto/howto_js_cascading_dropdown.asp)

#### Collection Mobile View
- [HTML select option checkboxes](https://stackoverflow.com/questions/17714705/how-to-use-checkbox-inside-select-option)
- [Display column based on checkboxes](https://stackoverflow.com/questions/60344393/how-to-display-hide-columns-when-checkboxes-are-checked)
- [Hide columns based on checkboxes](https://www.sitepoint.com/community/t/hide-table-column-whose-checkbox-is-not-checked-on-page-load/242783)
