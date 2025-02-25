# HealthTech


Discover the world of HealthTech on our blog! Dive into the latest breakthroughs and cutting-edge innovations in healthcare technology, from basic health gadgets to advanced medical devices. Our blog is your ultimate resource for staying informed and inspired on your health tech journey.



The live link can be found here - [HealthTech](https://healthtechblog-5cf577763b3c.herokuapp.com/)

![alt text](static/css/images/image-20.png)

  * [User Stories](#user-stories)
    + [Post Management](#post-management)
    + [Post Details and Comments](#post-details-and-comments)
    + [Like System](#like-system)
    + [Newsleter and Contact:](#newsleter-and-contact-)
  * [Design](#design)
    + [Colour Scheme](#colour-scheme)
    + [Imagery](#imagery)
    + [Fonts](#fonts)
    + [Wireframes](#wireframes)
- [Agile Methodology](#agile-methodology)
- [Features](#features)
  * [Header](#header)
  * [Home Page](#home-page)
  * [User Account Pages](#user-account-pages)
  * [Blog Main Page](#blog-main-page)
- [Testing](#testing)
- [Deployment - Heroku](#deployment---heroku)
  * [Create the Heroku App:](#create-the-heroku-app-)
  * [Attach the Postgres database:](#attach-the-postgres-database-)
  * [Update Heroku Config Vars](#update-heroku-config-vars)
  * [Deploy](#deploy)
- [Forking this repository](#forking-this-repository)
- [Cloning this repository](#cloning-this-repository)
- [Languages](#languages)
- [Frameworks - Libraries - Programs Used](#frameworks---libraries---programs-used)
- [Credits](#credits)
- [Acknowledgments](#acknowledgments)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>


### Project Board


| **To Do**                     | **In Progress**               | **Testing**                  | **Done**                      |
|-------------------------------|-------------------------------|------------------------------|-------------------------------|
| **Post Management**           |                               |                              |                               |
| - Add draft post functionality| - Implement post creation     | - Test post creation         | - Post creation implemented   |
| - Add post status toggle      | - Implement post editing      | - Test post editing          | - Post editing implemented    |
| - Add post deletion           | - Implement post deletion     | - Test post deletion         | - Post deletion implemented   |
| **Post Details and Comments** |                               |                              |                               |
| - Add comment approval        | - Implement comment system    | - Test comment functionality | - Comment system implemented  |
| - Add comment editing         | - Implement comment editing   | - Test comment editing       | - Comment editing implemented |
| - Add comment deletion        | - Implement comment deletion  | - Test comment deletion      | - Comment deletion implemented|
| **Like System**               |                               |                              |                               |
| - Add like/unlike feature     | - Implement like/unlike       | - Test like/unlike feature   | - Like/unlike implemented     |
| **Newsletter and Contact**    |                               |                              |                               |
| - Add newsletter subscription | - Implement newsletter form   | - Test newsletter form       | - Newsletter form implemented |
| - Add contact form            | - Implement contact form      | - Test contact form          | - Contact form implemented    |
| **Design**                    |                               |                              |                               |
| - Finalize color scheme       | - Add imagery to homepage     | - Test responsiveness        | - readme  & testing      |
| - Add fonts (Lato)    |                               |                              |                               |
| **Deployment**                |                               |                              |                               |
| - Set up PostgreSQL database  | - Deploy to Heroku            | - Test deployed app          | - Initial deployment done     |

---

### **Detailed Task Breakdown**

#### **Post Management**
- **To Do**:
  - Add draft BLOG post functionality.
  - Add blog post status toggle (draft/published).
  - Add blog post deletion confirmation.
- **In Progress**:
  - Implement post creation (`post_create` view).
  - Implement post editing (`post_update` view).
  - Implement post deletion (`post_delete` view).
- **Testing**:
  - Test post creation, editing, and deletion.
- **Done**:
  - Post creation, editing, and deletion functionality implemented.

#### **Post Details and Comments**
- **To Do**:
  - Add comment approval functionality.
  - Add comment editing functionality.
  - Add comment deletion functionality.
- **In Progress**:
  - Implement comment system (`PostDetail` view).
  - Implement comment editing (`comment_edit` view).
  - Implement comment deletion (`comment_delete` view).
- **Testing**:
  - Test comment submission, approval, editing, and deletion.
- **Done**:
  - Comment system implemented.

#### **Like System**
- **To Do**:
  - Add like/unlike feature.
- **In Progress**:
  - Implement like/unlike functionality (`PostLike` view).
- **Testing**:
  - Test like/unlike functionality.
- **Done**:
  - Like/unlike feature implemented.

#### **Newsletter and Contact**
- **To Do**:
  - Add newsletter subscription form.
  - Add contact form.
- **In Progress**:
  - Implement newsletter form (`newsletter_subscription` view).
  - Implement contact form (`contact` view).
- **Testing**:
  - Test newsletter subscription and contact form submission.
- **Done**:
  - Newsletter and contact forms implemented.

#### **Design**
- **To Do**:
  - Finalise color scheme (gold, light grey, dark grey).
  - Add fonts (Lato for branding ).
- **In Progress**:
  - Add imagery to homepage.
- **Testing**:
  - Test responsiveness on different devices.
- **Done**:
  - README & TESTING completed.

#### **Deployment**
- **To Do**:
  - Set up PostgreSQL database.
- **In Progress**:
  - Deploy to Heroku.
- **Testing**:
  - Test deployed app for functionality and performance.
- **Done**:
  - Initial deployment completed.

### **Task Assignment**
| **Task**                      | **Assigned To** | **Deadline** | **Status**   |
|-------------------------------|-----------------|--------------|--------------|
| Implement post creation       | Myself          | 2023-02-09   | Done         |
| Test comment functionality    | Myself           | 2025-02-10   | Done         |
| Add like/unlike feature       | Myself           | 2025-02-11   | Done         |
| README & TESTING completed    | Myself          | 2025-02-28   | Done         |




### User Stories

#### Post Management
- Given I am logged in, when I visit the post creation page, then I should be able to create a new post with a title, content, and an image.

- Given I am logged in, when I create a post, then the slug should be generated from the title and should be unique.

- Given I am logged in, when I visit my post's edit page, then I should be able to update the content, title, and image.

- Given I am logged in, when I visit my post's detail page, then I should be able to delete my post if I am the author.

#### Post Details and Comments
- Given I am viewing a post, when I visit the post detail page, then I should be able to see the post content, approved comments, and a comment form.

- Given I am logged in, when I submit a comment on a post, then my comment should be saved and appear after approval.

- Given I am the author of a comment, when I visit the comment edit page, then I should be able to update my comment content.

#### Like System
- Given I am logged in, when I visit a post detail page, then I should be able to like or unlike the post.


#### Newsleter and Contact:
- As a store owner, I can add products through an easy-to-use interface so that I can manage the store's contents.



### Design

- Given I visit the newsletter subscription page, when I submit the subscription form, then I should receive a success message and be subscribed to the newsletter.

- Given I visit the contact page, when I submit the contact form, then my message should be saved and I should receive a success message.

#### Colour Scheme

Colour palette from Colors

![alt text](static/css/images/colour_scheme.png) 

The color scheme of our blog is thoughtfully crafted using a balanced mix of gold, light grey, and dark grey. These colors are carefully selected to create a neutral yet engaging atmosphere, allowing the blog content and visuals to shine without distractions.

- Gold Accents: Gold accents add a touch of elegance and luxury, evoking a sense of joy and excitement, while staying true to the playful spirit of our blog.

- Light Grey Background: Light grey is used throughout the background to maintain a clean and modern design.

- Dark Grey Elements: Dark grey is employed for text and key sections, ensuring clear readability and visual balance.

We have prioritised strong contrast between the background colors and text to maximize user accessibility. This neutral color palette ensures a user-friendly experience, allowing the blog content to stand out while providing a smooth and enjoyable browsing experience for all visitors.

### Data Schema and Relationships

![alt text](static/css/images/data_schema_blog_post.webp)

## **1. User Model Relationships**  
- **User ↔ Post (1:M)** → Users can create multiple blog posts.  
- **User ↔ Comment (1:M)** → Users can leave multiple comments.  
- **User ↔ Like (M:M)** → Users can like multiple posts.  
- **User ↔ Review (1:M)** → Users can leave multiple reviews.  
- **User ↔ NewsletterSubscription (1:M)** → Users can subscribe to newsletters.  

## **2. Blog Post Model**  
- **Post ↔ Comment (1:M)** → A post can have multiple comments.  
- **Post ↔ Like (M:M)** → A post can be liked by multiple users.  
- **Post ↔ Review (1:M)** → A post can have multiple reviews.  

## **3. Comment Model**  
- **Comment ↔ Post (M:1)** → A comment belongs to one post.  
- **Comment ↔ User (M:1)** → A comment belongs to one user.  

## **4. Review Model**  
- **Review ↔ Post (M:1)** → A review belongs to one post.  
- **Review ↔ User (M:1)** → A review is written by one user.  

## **5. Newsletter Subscription Model**  
- **NewsletterSubscription ↔ User (M:1)** → A user can subscribe to multiple newsletters.  

## **6. Contact Model**  
- Stores visitor inquiries with **name, email, and message** (no login required).  



## **Entity Relationship Summary**  
| **Model** | **Relationships** |  
|------------|------------------|  
| **User** | 1:M Posts, 1:M Comments, M:M Likes, 1:M Reviews, 1:M Newsletter Subscriptions |  
| **Post** | 1:M Comments, M:M Likes, 1:M Reviews |  
| **Comment** | M:1 Posts, M:1 Users |  
| **Review** | M:1 Users, M:1 Posts |  
| **NewsletterSubscription** | M:1 Users |  
| **Contact** | Independent |  


## **Key Features**  
- **CRUD operations** on **Posts, Comments, Likes, and Reviews**.  
- **Secure authentication** for post editing, deletion, and commenting.  
- **Slug-based URLs** for SEO-friendly blog post links.  
- **Admin approval** required for comments.  


#### Imagery
Our blog homepage features a prominent static image that showcases an exciting and engaging visual centerpiece. The color scheme of the site, with its vibrant green and yellow tones, perfectly complements this main image, reflecting the playful and imaginative nature of our content.

- Green and Yellow Tones: These colors bring a lively and energetic feel to the site, enhancing the overall user experience.

- Vibrant and Playful: The chosen color scheme reflects the playful and imaginative spirit of our blog, creating an inviting and dynamic environment for our visitors.

By harmonising the main image with the color scheme, we ensure that our blog not only looks appealing but also provides an enjoyable and engaging experience for all users. Our thoughtful design choices help to highlight the creativity and excitement that our content offers
#### Fonts
For the blog, we've chosen to use the Lato font for branding elements, which provides a modern and clean look. Additionally, the Roboto font is used for the body text to ensure optimal readability and a smooth browsing experience. Both fonts are imported via Google Fonts to guarantee a consistent appearance across various devices.

#### Wireframes

![alt text](<wireframe - blog post.webp>)

+---------------------------------------------------+
|                  Blog Title / Logo               |
|---------------------------------------------------|
| Home | About | Blog | Categories | Contact       |
+---------------------------------------------------+

### [ Home Page ]
-------------------------------------
| - Featured Post                                  |
| - Blog Posts List (Paginated)                    |
|   - [Post 1] [Post 2] [Post 3]                   |
|   - [Post 4] [Post 5] [Post 6]                   |
-------------------------------------

### [ Post Detail Page ]
-------------------------------------
| - Post Title | Author | Date | ❤️ Like Button   |
| - Post Content + Image                           |
| - Comments Section                               |
|   - [User1: Comment] [Edit] [Delete]            |
|   - [User2: Comment]                             |
|   - [Add Comment] [Submit]                       |
-------------------------------------

### [ Create/Edit Post ]
-------------------------------------
| - Title Input                                    |
| - Content Text Area                              |
| - Image Upload                                   |
| - [Submit] [Save as Draft]                      |
-------------------------------------

### [ Delete Post ]
-------------------------------------
| Are you sure you want to delete this post?      |
| - [Yes, Delete] [Cancel]                        |
-------------------------------------

### [ Newsletter Subscription ]
-------------------------------------
| - Email Input [Subscribe]                        |
-------------------------------------

### [ Contact Page ]
-------------------------------------
| - Name, Email, Message Form                      |
| - [Submit]                                       |
-------------------------------------

## Wireframes photo 

<details>
 <summary>Home Page</summary>

![alt text](static/css/images/image-3.png)
</details>

<details>
 <summary>Blog Page</summary>

![alt text](static/css/images/image-2.png)
</details>


<details>
 <summary>Blog</summary>

![alt text](static/css/images/image-4.png)
</details>

<details>
 <summaryAdd Add a Blog Post></summary>

![alt text](static/css/images/image-5.png)
</details>

<details>
 <summary>Log in Page</summary>
 
![alt text](static/css/images/image-6.png)
</details>



<details>
 <summary>Create a post management</summary>

![alt text](static/css/images/image-7.png)
</details>



## Agile Methodology
Github projects was used to manage the development process using an agile approach. Please see link to project board [here](https://github.com/users/SamAkinbile/projects/2/views/1)




## Features

### Header

![alt text](static/css/images/image-8.png)

**Logo**
- A customised logo was created using Code Institute template.
- This logo is positioned in the top left of the navigation bar. The logo is linked to the home page for ease of navigation for the user.

**Navigation Bar**

- The navigation bar is visible at the top of every page and includes links to the other pages.

![alt text](static/css/images/image-9.png)


**User Icon**

- The options to Sign up or Log in will change to the option to log out once a user has logged in.


![alt text](static/css/images/image-10.png)

### Home Page

![alt text](static/css/images/image-11.png)

The blog-themed home page showcases an engaging call-to-action section, encouraging visitors to "Read Now" or explore "More Blog Posts." This feature is emphasized with the bold announcement "NEW POSTS," paired with an image of a creatively designed blog layout, inspiring both curiosity and creativity.



### User Account Pages

**Register**

![alt text](static/css/images/image-12.png)

**Sign In**

![alt text](static/css/images/image-13.png)


**Sign Out**

![alt text](static/css/images/image-14.png)

- Django allauth was installed and used to create the Sign up, Log in and Log out functionality. 
- Success messages inform the user if they have logged in/ logged out successfully.


### Blog Main Page
 
![alt text](static/css/images/home.png)

- The 'Blog Main Page' link will display a list of all blog post from the database.

![alt text](static/css/images/image-15.png)

- Each blog shows an image of the product, its title, excerpt,like, comment and edit and delete for logged in user



**Edit|Delete button for Blog post**
![alt text](static/css/images/image-16.png)

Edit|Delete button for post added. This gives opporturnity for a logged in user to edit, delete, thier blog post.

**Edit|Delete button for comment**
![alt text](static/css/images/image-17.png)

Edit|Delete button for post added. This gives opporturnity for a logged in user to edit, delete, thier comment post.

**Update and Remove Buttons**

**Confirmation**

![alt text](static/css/images/image-18.png)
- confirmation if aboiut to delete a blog post

![alt text](static/css/images/image-19.png)
- Confirmation if about to delete a comment post


## Testing
Testing and results can be found [text](TESTING.md)

## Deployment - Heroku

To deploy this page to Heroku from its GitHub repository, the following steps were taken:

### Create the Heroku App:
- Log in to [Heroku](https://dashboard.heroku.com/apps) or create an account.
- On the main page click the button labelled New in the top right corner and from the drop-down menu select "Create New App".
- Enter a unique and meaningful app name.
- Next, select your region.
- Click on the Create App button.

### Attach the Postgres database:
- In the Resources tab, under add-ons, type in Postgres and select the Heroku Postgres option.
- Copy the DATABASE_URL located in Config Vars in the Settings Tab.
- Go back to your IDE and install 2 more requirements:
    - `pip3 install dj_databse_url`
    - `pip3 install psycopg2-binary` 
- Create requirements.txt file by typing `pip3 freeze --local > requirements.txt`
- Add the DATABASE_URL value and your chosen SECRET_KEY value to the env.py file. 
- In settings.py file import dj_database_url, comment out the default configurations within database settings and add the following: 

```
DATABASES = {
    'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
}
```
- Run migrations and create a superuser for the new database. 
- Create an if statement in settings.py to run the postgres database when using the app on heroku or sqlite if not

```
    if 'DATABASE_URL' in os.environ:
        DATABASES = {
            'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
        }
    else:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': BASE_DIR / 'db.sqlite3',
            }
    }
```

- Create requirements.txt file by typing `pip3 freeze --local > requirements.txt`
- Create a file named "Procfile" in the main directory and add the following: `web: gunicorn project-name.wsgi:application`
- Add Heroku to the ALLOWED_HOSTS list in settings.py in the format ['app_name.heroku.com', 'localhost']

- Push these changes to Github.

### Update Heroku Config Vars
Add the following Config Vars in Heroku:

|     Variable name     |                           Value/where to find value                           |
|:---------------------:|:-----------------------------------------------------------------------------:|
| DATABASE_URL          | Postgres generated (as per step above)                                        |
| EMAIL_HOST_PASS       | Password from email client                                                    |
| EMAIL_HOST_USER       | Site's email address                                                          |
| SECRET_KEY            | Random key generated as above                                                 |


### Deploy
- NB: Ensure in Django settings, DEBUG is False
- Go to the deploy tab on Heroku and connect to GitHub, then to the required repository. 
- Scroll to the bottom of the deploy page and either click Enable Automatic Deploys for automatic deploys or Deploy Branch to deploy manually. Manually deployed branches will need re-deploying each time the repo is updated.
- Click View to view the deployed site.

The site is now live and operational.

## Forking this repository
- Locate the repository at this link [Health Blog](https://github.com/SamAkinbile/HealthTechBlog)
- At the top of the repository, on the right side of the page, select "Fork" from the buttons available. 
- A copy of the repository is now created.

## Cloning this repository
To clone this repository follow the below steps: 

1. Locate the repository at this link [Health Blog](https://github.com/SamAkinbile/HealthTechBlog)
2. Under **'Code'**, see the different cloning options, HTTPS, SSH, and GitHub CLI. Click the prefered cloning option, and then copy the link provided. 
3. Open **Terminal**.
4. In Terminal, change the current working directory to the desired location of the cloned directory.
5. Type **'git clone'**, and then paste the URL copied from GitHub earlier. 
6. Type **'Enter'** to create the local clone. 

## Languages

- Python
- HTML5
- CSS3
- Javascript

## Frameworks - Libraries - Programs Used
- [Django](https://www.djangoproject.com/): Main python framework used in the development of this project
- [Django-allauth](https://django-allauth.readthedocs.io/en/latest/installation.html): authentication library used to create the user accounts
- [JQuery](https://jquery.com/)
- [PostgreSQL](https://www.postgresql.org/) was used as the database for this project.
- [SQLite](https://www.sqlite.org/index.html) - was used as the database during production.
- [Heroku](https://dashboard.heroku.com/login) - was used as the cloud based platform to deploy the site on.
- [Responsinator](http://www.responsinator.com/) - Used to verify responsiveness of website on different devices.
- [Chrome Dev Tools](https://developer.chrome.com/docs/devtools/) - Used for overall development and tweaking, including testing responsiveness and performance.
- [Font Awesome](https://fontawesome.com/) - Used for icons in information bar.
- [GitHub](https://github.com/) - Used for version control and agile tool.
- [Google Fonts](https://fonts.google.com/) - Used to import and alter fonts on the page.
- [W3C](https://www.w3.org/) - Used for HTML & CSS Validation.
- [Jshint](https://jshint.com/) - used to validate javascript
- [Coolors](https://coolors.co/) - Used to create colour palette.
- [Favicon](https://favicon.io/) - Used to create the favicon.
- [Lucidchart](https://lucid.app/documents#/dashboard) - used to create the database schema design
- [Techsini](https://techsini.com/multi-mockup/index.php) - Site mockup generator
- [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) used to manage Django Forms
- [Bootstrap 4.6](https://getbootstrap.com/docs/4.6/getting-started/introduction/): CSS Framework for developing responsiveness and styling
- [Hatchful](https://hatchful.shopify.com/): Used to generate custom logo
- [Tables Generator](https://www.tablesgenerator.com/markdown_tables): Used to convert excel testing tables to markdown
- [Sitemap Generator](www.xml-sitemaps.com): used to create sitemap.xml 
- [Privacy Policy Generator](https://www.privacypolicygenerator.info/): Used to create the site's privacy policy
- [Mailchimp](https://mailchimp.com/?currency=EUR): Used to create the newsletter signup functionality.
- [chatgpt](openai.com): Openai


## Credits

- [W3Schools](https://www.w3schools.com/)
- [Django Docs](https://docs.djangoproject.com/en/4.0/)
- [Bootstrap 4.6 Docs](https://getbootstrap.com/docs/4.6/getting-started/introduction/)
- [Stack Overflow](https://stackoverflow.com/)
- [Pexels](https://www.pexels.com/): Imagery on the site was sourced from Pexels.com
- [Unsplashed](https://unsplash.com/): Imagery on the site was sourced from Unsplash
- [Code Institute - Codestar Walkthrough Project](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+FSD101_WTS+5/courseware/713441aba05441dfb3a7cf04f3268b3f/824fccecd0fe4e44871eeabcbf69d830/)
- [Code Institute - Codestar Walkthrough Project](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+FST101+2/courseware/b31493372e764469823578613d11036b/fe4299adcd6743328183aab4e7ec5d13/)
- [Stack Overflow](https://stackoverflow.com/questions/19619428/html5-form-validation-pattern-alphanumeric-with-spaces): To prevent form being submitted with whitespace
- [opeanai.com](https://openai.com/)
- [chatghpt](https://chatgpt.com/)

### Find testing here[text](TESTING.md)

## Acknowledgments

Many thanks to Code institute Tutoring service for support and advice. Thanks to The Code Institute slack community.