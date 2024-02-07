
![Website](README_docs/photos/SC-PP4-home.jpg)

# VAN BUILDS 101


## [Live Site](https://vanbuilds-758ccba3a303.herokuapp.com/)


## [Repository](https://github.com/lukecdev/VanBuilds101)

### Intro

- Van Builds 101 is a blog focused on diy campervans. Offering advice and insit into building your own campervan and what is the best materials to use. There is also a section to show photos of campervans to help other users get inspiration for their own builds. 

## Table of contents

 1. Project Planning 
 2. UX
 3. CRUD
 4. Testing
 5. Bugs
 6. Deployment
 7. Credits
 8. Acknowledgments

# Project Planning

## Database 

#### Post Model

| id | Field |
|--|--|
| title |CharField|
| slug |SlugField|
| author |CharField|
| excerpt |TextField|
| created on |DateTimeField|
| content |textField|
| featured_image |CloudinaryField|
| status |IntegerField|
| likes |ManyToManyField|

#### Comment Model

| id | Field |
|--|--|
| post |ForeignKey|
| name |CharField|
| email |Emailfield|
| body |TextField|
| created on |DateTimeField|
| approved |BooleanField|

#### Image Model

| id | Field |
|--|--|
| title |CharField|
| slug |SlugField|
| excerpt |TextField|
| gallery_image |CloudinaryField|
| author |ForeignKey|
| approved |BooleanField|

# UX Design

### Site Goal
The goal of the site is to create a platform for online communication. To create an engaging experience to provide a userful edication for the Vanlife community. 

## WireFrame
![Wireframe](README_docs/wireframes/van-blog-sc-2.png)

## Design
The design philosophy for this site is a easy to navigate and read site. As this site will be hosting articles that provides information, I want to make getting to the particular blog and reading it a minimal effort.

## Agile Methodology
- The principles of agile methodology were implemented during the project. By assigning user stories to issues and utilizing the GitHub Kanban board, the necessary project goals could be easliy prioritized. Labels were used to fine tune the priority of each user story.

To see Kanban please click [here](https://github.com/users/lukecdev/projects/1)

Once I completed a task I would tick the appropriate box and if all parts of this story were completed I would move it from **in progress** to **completed**.

At the end of a coding session I would update the user stories with a comment of:

 - What was done
 - What is left to be done

## User Stories

### Users
- I can **view a list of blog posts** so that I can **select which blog post** to read.
- I can **click on a post** so that **I can view the full article text**.
- I can **register an account** so that I can **add posts, comment, and like posts**.
- I can **leave comments on posts** so that **I can engage in discussion with users**.
- I want to be **able to submit a blog post to publish**.
- I can **view the number of likes on a post** to be able **engage with the blog community**.

### Admin
- I can **read, create, edit, and delete posts** so that **I can manage the blog's content**
- I can **approve or disapprove comments** so that **I can filter out objectionable comments**
- I can **delete messages** so that **I can clean out any unwanted comments**
- I can **create draft posts** so that **I can finish writing the content later**

### NINTH User stories
- I can **utilize a map API capability** so that **I can use the map to locate useful related locations**

## Features

### Navbar
Desktop View while user is logged out/unregistered: 
![Navbar](README_docs/photos/SC-PP4-nav.jpg.png)
- The desktop navigation consists of a a Home blog and Gallery button. 
- The user is shown the login and register links when not logged in.
- When user is logged in they are shown just the log out link.
- If the user is a superuser they will then also have access to creat a new post. 

### Homepage
![Homepage](README_docs/photos/SC-PP4-home.jpg)

### Landing Page
![Landing](README_docs/photos/landing-page-sc.jpg)

### Register
![SignUp](README_docs/photos/sc-signup.jpg)

### Sign In
![SignIn](README_docs/photos/sc-signin.jpg)

### Sign Out
![SignOut](README_docs/photos/sc-signout.jpg)

### Leave a Comment/ Like a Post
![Comment/Like](README_docs/photos/sc-comment-likes.jpg)

### Gallery
![Gallery](README_docs/photos/sc-gallery.jpg)


## Future Features

- Map API: This would be a feature for log-in users, where there is a map section that shows locations of campsites, supply stores, view points and simialr locations that would be useful for campervan owners.
- Gallery Image cards: This is in the gallery page. When a user clicks on a gallery image card, it would expand to show more images grouped with the first card. This would allow users to have more detailed photos of their van in the one card. Improving the UX of the page.

# C.R.U.D

## Posting

## Create
- Create Blog Post View

![Create](README_docs/photos/sc-create-post.jpg)

- Create Gallery Image

![CreateGallery](README_docs/photos/new-add-gallery.jpg)

## Read
- Read Post detail

![Read](README_docs/photos/sc-read-post.jpg)

- Read Gallery Section

![ReadGallery](README_docs/photos/read-gallery.jpg)

## Update
- Update Blog Post

![Update](README_docs/photos/sc-update-post.jpg)

- Update Gallery Image

![UpdateGallery](README_docs/photos/update-gallery.jpg)

## Delete
- Delete Blog Post

![Delete](README_docs/photos/sc-delete-post.jpg)

- Delete Gallery Image

![DeleteGallery](README_docs/photos/delete-gallery.jpg)


# Technologies Used
1. Python - Used for the logic in this project
2. Github - For code repository and code version control.
3. Heroku - To deploy the live application.
4. Gitpod - Cload based code editor used.
5. LucidCharts - Used for flow chart creation.
6. Django - Framework used to build this project. Provides a ready installed admin panel and includes many helper template tags that make writing code quick and efficient.
7. Bootstrap - Used as the base front end framework to work alongside Django.
8. Elephant SQL - Was used as the database for this project during development and in production.
9. Cloudinary - Used to host the static files for this project including user profile images.
10. Git - Used for version control throughout the project and to ensure a good clean record of work done was maintained.

## Installed Packages
- django<4' gunicorn
- dj_database_url psycopg2
- dj3-cloudinary-storage
- django-summernote
- django-allauth
- django-crispy-forms
- pillow


# Testing

## Manual Testing
> Each user story was manually tested in line with intended functionality on both desktop & mobile.
> As this project was driven by my own User Stories I  felt manual testing was applicable on all logic code.

>If the intended outcome completes then this will be flagged as pass. If it does not then this is a fail.

#### Account Registration Tests
| Test |Result  |
|--|--|
| User can create account | Pass |
| User can log into account| Pass|
|User can log out of account|Pass|

#### User Navigation Tests

| Test |Result  |
|--|--|
|User can navigate to blog posts |Pass|
|User access gallery |Pass|
|SuperUser can access admin panel |Pass|

#### Account Security Tests

| Test |Result  |
|--|--|
|Non logged in user cannot edit posts | Pass |
|Non superuser cannot access admin panel|Pass|

#### Admin Tests

| Test |Result  |
|--|--|
|Admin can add a new Post |Pass|
|Admin can add photos |Pass|
|Admin can edit edit posts |Pass|
|Admin can deleten posts |Pass|

### Google Lighthouse
![Lighthouse](README_docs/photos/sc-lighthouse.jpg)

# Bugs

### Html Checker
![html](README_docs/photos/html-check.jpg)

- When i ran the W3 Html validator, i got 2 error messages for stray </div> elements. I was not expecting these. 
- Upon a review, I could see that these tags where being added by Django at the end of my Post_detail html when it loads with the base.html.

### Gallery image upload not submitting 

- When bulding the Post form for the image upload page. I build the view with the 'generic.createview' class, this was already being used in the Blog Post view for new blog posts. This casused an issue that when the button was pressed to submit the new gallery image. A "Required Field enter" pops up and does not allow the image to be submited. This required field message seems to be pulled from the Post Model. It would require re organsiing both models which I unfortantly ran out of time to fix. The current way to upload new gallery images is through the admin panel and the image section.

# Deployment
To deploy the project through Heroku I followed these steps:

- Sign up / Log in to  [Heroku](https://www.heroku.com/)
- From the main Heroku Dashboard page select 'New' and then 'Create New App'
- Give the project a name - I decided on the devils kitchen and selected EU as that is the closes region to me.
- After this you select select create app. 
- The name for the app must be unique or you will not be able to continue.
- Heroku will create the app and bring you to the deploy tab. 
- From the submenu at the top, navigate to the resources tab.
- Add the database to the app, in the add-ons section search for 'Heroku Postgres', select the package that appears and add 'Heroku Postgres' as the database
- Click on the setting tab
- Open the config vars section copy the DATABASE_URL to the clipboard for use in the Django configuration.
- Inside the Django app repository create a new file called env.py
- within this file import the os library and set the environment variable for the DATABASE_URL pasting in the address copied from Heroku. 
- The line should appear as os.environ["DATABASE_URL"]= "Paste the link in here"
-   Add a secret key to the app using os.environ["SECRET_KEY"] = "your secret key goes here"
-   Add the secret key just created to the Heroku Config Vars as SECRET_KEY for the KEY value and the secret key value you created as the VALUE
-   In the settings.py file within the django app, import Path from pathlib, import os and import dj_database_url
-   insert the line if os.path.isfile("env.py"): import env
-   remove the insecure secret key that django has in the settings file by default and replace it with SECRET_KEY = os.environ.get('SECRET_KEY')
-   replace the databases section with DATABASES = { 'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))} ensure the correct indentation for python is used.
-   In the terminal migrate the models over to the new database connection
---
-   Navigate in a browser to cloudinary, log in, or create an account and log in.
-   From the dashboard - copy the CLOUDINARY_URL to the clipboard
-   In the env.py file - add os.environ["CLOUDINARY_URL"] = "paste in the Url copied to the clipboard here"
-   In Heroku, add the CLOUDINARY_URL and value copied to the clipboard to the config vars
-   Also add the KEY - DISABLE_COLLECTSTATIC with the Value - 1 to the config vars
-   this key value pair must be removed prior to final deployment
-   Add the cloudinary libraries to the list of installed apps, the order they are inserted is important, 'cloudinary_storage' goes above 'django.contrib.staitcfiles' and 'cloudinary' goes below it.
-   in the Settings.py file - add the STATIC files settings - the url, storage path, directory path, root path, media url and default file storage path.
-   Link the file to the templates directory in Heroku TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
-   Change the templates directory to TEMPLATES_DIR - 'DIRS': [TEMPLATES_DIR]
-   Add Heroku to the ALLOWED_HOSTS list the format will be the app name given in Heroku when creating the app followed by .herokuapp.com
-   In your code editor, create three new top level folders, media, static, templates
-   Create a new file on the top level directory - Procfile
-   Within the Procfile add the code - web: guincorn PROJECT_NAME.wsgi
-   In the terminal, add the changed files, commit and push to GitHub
-   In Heroku, navigate to the deployment tab and deploy the branch manually - watch the build logs for any errors.
-   Heroku will now build the app for you. Once it has completed the build process you will see a 'Your App Was Successfully Deployed' message and a link to the app to visit the live site.

#### Forking the repository
y forking the GitHub Repository you can make a copy of the original repository to view or change without it effecting the original repository.
You can do this by: 
-  Logging into GitHub or create an account. 
- Locate the repository at  [here](https://github.com/lukecdev/VanBuilds101)
-  At the top of the repository, on the right side of the page, select "Fork" from the buttons available. 
-  A copy of the repository should now be created in your own repository.

#### [](https://github.com/lukecdev/VanBuilds101)Create a clone of this repository
Creating a clone enables you to make a copy of the repository at that point in time - this lets you run a copy of the project locally: This can be done by:
- Navigate to [https://github.com/lukecdev/VanBuilds101](https://github.com/lukecdev/VanBuilds101)
- click on the arrow on the green code button at the top of the list of files
- select the clone by https option and copy the URL it provides to the clipboard
- navigate to your code editor of choice and within the terminal change the directory to the location you want to clone the repository to.
- type 'git clone' and paste the https link you copied from github
- press enter and git will clone the repository to your local machine

# Credits

- I used watched this [Youtube Video](https://www.youtube.com/watch?v=B40bteAMM_M&list=PLCC34OHNcOtr025c1kHSPrnP18YPB-NFi) which helped me build the basics of the blog creation for my site.
- I used watched this [Youtube Video](https://www.youtube.com/watch?v=sSquD2u5Ie0) which helped me build elements of the photo gallery.

## Media
Blog Image Credits
- https://magazine.vanketo.co/wp-content/uploads/2022/09/Campervan-conversion-kit.jpg
- https://d38b8me95wjkbc.cloudfront.net/uploads/blog_image/image/15425/section_6_lighting._Cap_-_Subtle_lighting_effect_in_Frosty_the_Transit_Campervan__available_for_hire_on_Camplify.jpeg
- https://vanlifeadventure.com/wp-content/uploads/2019/08/campervan-kitchen-ideas-yamanomad.jpg
- https://uploads-ssl.webflow.com/6105314daa8822ce4688e35e/61a33cf51782becd83d7dcfe_Fixed%20platform%20bed%20setup.jpg
- https://www.thevanconversionguide.com/wp-content/uploads/2021/12/Best-vans-for-camper-conversion.jpg
- https://images.squarespace-cdn.com/content/v1/60a7cdfd239cca53f325e024/c89cd935-3173-492e-b8bf-1221f9f868ad/vanspace+3D+camper+van+layout+with+bench+seats.png
- https://images.squarespace-cdn.com/content/v1/63b596be45c8ea33e4ce3f89/2473bd09-c103-4104-9f4e-997ec4669995/customcamperconversion.png
- https://images.squarespace-cdn.com/content/v1/639b5993ca2f2b0b78cc9374/1682749464740-2E5XUIP9N01RU2F764TS/Rolling+Bothy+campervan+conversion+DeWalt+cordless+power+tools.jpg

# Acknowledgments

- A huge thanks to [Chris Quinn](https://github.com/10xOXR) for his help, suggestions and patiece while I put together this project. 

- Also a huge thanks to the tutors at Code institute for your patience and help in fixing my code issues.

