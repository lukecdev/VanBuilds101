[![Wireframe](README_docs/wireframes/van-blog-sc-2.png)

[![login example](README_docs/photos/van-blog-sc.png)




###########

# VAN BUILDS 101

Van Builds 101 is a blog website that posts articles to provide its users with information about building a campervan. The website also provides addinalal information to campervan owners to build their ideal adventures.

## **[Live Site]

---

## **[Repository]

## Table of contents
<a name="contents">Back to Top</a>
 1. [ UX ](#ux) 

# UX
<a name="ux"></a>

the design design philosophy fir this site is a easy to navigate and read site. As this site will be hosting articles that provides information, I want to make getting to the particular blog and reading it a minimal effort.

### Site Goal
The goal of the site is to create a platform for online communication. To create an engaging experience to provide a userful edication for the Vanlife community. 

## Project Planning

### Database 

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
| image |ImageField|
| author |ForeignKey|
| approved |BooleanField|

# UX Design

## Agile Methodology
- The principles of agile methodology were implemented during the project. By assigning user stories to issues and utilizing the GitHub Kanban board, the necessary project goals could be easliy prioritized. Labels were used to fine tune the priority of each user story.

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

### Footer

### Homepage

### Post Detail View

### Register

### Sign In

### Sign Out

### Leave a Comment


## Future Features

# C.R.U.D

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

# Testing

## Manual Testing

###########
![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)




## Gitpod Reminders

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

In Gitpod you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In Gitpod, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you so do not share it. If you accidentally make it public then you can create a new one with _Regenerate API Key_.

------

## Release History

We continually tweak and adjust this template to help give you the best experience. Here is the version history:

**September 20 2023:** Update Python version to 3.9.17.

**September 1 2021:** Remove `PGHOSTADDR` environment variable.

**July 19 2021:** Remove `font_fix` script now that the terminal font issue is fixed.

**July 2 2021:** Remove extensions that are not available in Open VSX.

**June 30 2021:** Combined the P4 and P5 templates into one file, added the uptime script. See the FAQ at the end of this file.

**June 10 2021:** Added: `font_fix` script and alias to fix the Terminal font issue

**May 10 2021:** Added `heroku_config` script to allow Heroku API key to be stored as an environment variable.

**April 7 2021:** Upgraded the template for VS Code instead of Theia.

**October 21 2020:** Versions of the HTMLHint, Prettier, Bootstrap4 CDN and Auto Close extensions updated. The Python extension needs to stay the same version for now.

**October 08 2020:** Additional large Gitpod files (`core.mongo*` and `core.python*`) are now hidden in the Explorer, and have been added to the `.gitignore` by default.

**September 22 2020:** Gitpod occasionally creates large `core.Microsoft` files. These are now hidden in the Explorer. A `.gitignore` file has been created to make sure these files will not be committed, along with other common files.

**April 16 2020:** The template now automatically installs MySQL instead of relying on the Gitpod MySQL image. The message about a Python linter not being installed has been dealt with, and the set-up files are now hidden in the Gitpod file explorer.

**April 13 2020:** Added the _Prettier_ code beautifier extension instead of the code formatter built-in to Gitpod.

**February 2020:** The initialisation files now _do not_ auto-delete. They will remain in your project. You can safely ignore them. They just make sure that your workspace is configured correctly each time you open it. It will also prevent the Gitpod configuration popup from appearing.

**December 2019:** Added Eventyret's Bootstrap 4 extension. Type `!bscdn` in a HTML file to add the Bootstrap boilerplate. Check out the <a href="https://github.com/Eventyret/vscode-bcdn" target="_blank">README.md file at the official repo</a> for more options.

------

## FAQ about the uptime script

**Why have you added this script?**

It will help us to calculate how many running workspaces there are at any one time, which greatly helps us with cost and capacity planning. It will help us decide on the future direction of our cloud-based IDE strategy.

**How will this affect me?**

For everyday usage of Gitpod, it doesn’t have any effect at all. The script only captures the following data:

- An ID that is randomly generated each time the workspace is started.
- The current date and time
- The workspace status of “started” or “running”, which is sent every 5 minutes.

It is not possible for us or anyone else to trace the random ID back to an individual, and no personal data is being captured. It will not slow down the workspace or affect your work.

**So….?**

We want to tell you this so that we are being completely transparent about the data we collect and what we do with it.

**Can I opt out?**

Yes, you can. Since no personally identifiable information is being captured, we'd appreciate it if you let the script run; however if you are unhappy with the idea, simply run the following commands from the terminal window after creating the workspace, and this will remove the uptime script:

```
pkill uptime.sh
rm .vscode/uptime.sh
```

**Anything more?**

Yes! We'd strongly encourage you to look at the source code of the `uptime.sh` file so that you know what it's doing. As future software developers, it will be great practice to see how these shell scripts work.

---

Happy coding!
