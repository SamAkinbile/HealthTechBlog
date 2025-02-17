- [User Story Testing](#user-story-testing)
  * [EPIC | Viewing and Navigation](#epic--viewing-and-navigation)
  * [EPIC | User Account and Profile](#epic--user-account-and-profile)
  * [EPIC | Purchasing](#epic--purchasing)
- [Testing](#testing)
  * [Code Validation](#code-validation)
    + [PYTHON VALIDATION](#python-validation)
    + [CSS](#css)
  * [Responsiveness](#responsiveness)
  * [Lighthouse Audit](#lighthouse-audit)
  * [Browser Testing](#browser-testing)
  * [Manual Testing](#manual-testing)
    + [Site Navigation](#site-navigation)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>



# Testing

Return back to the [README.md](README.md) file.

## Code Validation

I have used the recommended [HTML W3C Validator](https://validator.w3.org/nu/#textarea) to validate all of my HTML files.Unforturnately, The errors contain in this project comes from walkthrough boutique - ado . I am not able to fix it. I do not have the expertise to do it.

| Page             |    W3C Screnshots                                                             |             
| -----------------|-------------------------------------------------------------------------------|
| Welcome Page     |  ![alt text](static/css/images/w3c_validation.png)                            |
| Blog Main Page   |  ![alt text](static/css/images/w3c_validation.png)                            |            
| Blog Page        | ![alt text](static/css/images/w3c_validation.png)                             |
| Sign in Page     | ![alt text](static/css/images/w3c_validation.png)                             |
| Sign up Page     | ![alt text](static/css/images/w3c_validation.png)                             |
| Add a Blog post  |  ![alt text](static/css/images/w3c_validation.png)                            |
| Edit Blog        |  ![alt text](static/css/images/w3c_validation.png)                            |




### PYTHON VALIDATION
Python testing was done using CI Python Linter to ensure there were no syntax errors.

| App           |        Screenshots                                     |                |
|---------------|--------------------------------------------------------|----------------|
|  Bag          | ![alt text](/media/python.png)                         | No error       |
|  Blog         | ![alt text](/media/python.png)                         | No error       |  
|  Checkout     | ![alt text](/media/python.png)                         | No error       |
| emarket       | ![alt text](/media/python.png)                         | No error       |
| homepage      | ![alt text](/media/python.png)                         | No error       |
|  products     | ![alt text](/media/python.png)                         | No error       |
| profiles      | ![alt text](/media/python.png)                         | No error       |
| templates     | ![alt text](/media/python.png)                         | No error       |
|               |                                                        |                |



### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

|  File      | Jigsaw Screenshot                                                         |  Note
|------------|---------------------------------------------------------------------------|-------------------
| style.css   | static/css/images/style.css_validating_no_error.png                      |  No error
                                                    


## Responsiveness

I've tested my deployed project on multiple devices to check for responsiveness issues.

|  Device                    | Screenshot                                    | 
|----------------------------|-----------------------------------------------|
| Samsung Galaxy (DevTools)  | ![alt text](/media/image-6.png)               |
| Google Pixel               | ![alt text](/media/image-7.png)               |
|  Tablet                    | ![alt text](/media/image-8.png)               |
|   iPhone                   | ![alt text](/media/image-9.png)               |             
|  Nest Hub                  | ![alt text](/media/image-10.png)              |

## Lighthouse Audit

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues.

| Page                 |  Size   |      Screenshot                                          |  
|----------------------|---------|----------------------------------------------------------|
|   Home               | Mobile  |  ![alt text](/media/image-12.png)                        |
|   Home               | Desktop |  ![alt text](/media/image-13.png)                        |
| All Products         |Mobile   |  ![alt text](/media/image-14.png)                        |
| All Products         | Desktop |  ![alt text](/media/image-15.png)                        |
|  Legos               |Mobile   |  ![alt text](/media/image-16.png)                        |
|  Legos               | Desktop |  ![alt text](/media/image-17.png)                        |
| Lego Testinmonial    | Mobile  |  ![alt text](/media/image-18.png)                        |
| Lego Testimonial     |Desktop  |  ![alt text](/media/image-19.png)                        |


## Browser Testing

The Website was tested on Google Chrome, Firefox, Safari browsers with no issues noted.

## Manual Testing



## NavBar, NavLinks, NavButtons 

| Tested Item | Expected Outcome                                      | Outcome     |
| ----------- | ----------------------------------------------------- | ----------- |
| Home        | Clickable,                                            | as expected |
| NavLink     | Opens Home page,                                      | as expected |
|             | Or refreshes it if user is already on Home page,      | as expected |
|             | Color of Home NavLink darkens once it's selected,     | as expected |
|             | Opens in the current tab                              | as expected |         
|             |                                                       |             |
| About       | Clickable,                                            | as expected |
| NavLink     | Opens About page,                                     | as expected |
|             | Or refreshes it if user is already on About page,     | as expected |
|             | Color of About NavLink darkens once it's selected,    | as expected |
|             | Opens in the current tab                              | as expected | 
|             |                                                       |             |
| Resources   | Clickable,                                            | as expected |
| NavLink     | Opens Resources page,                                 | as expected |
|             | Or refreshes it if user is already on Resources page, | as expected |
|             | Color of Resources NavLink darkens once it's selected,| as expected |
|             | Opens in the current tab                              | as expected | 
|             |                                                       |             |
| Sign In     | Clickable,                                            | as expected |
| NavLink     | Visible only when user is not Signed In,              | as expected |
|             | Opens up a Sign In form,                              | as expected |
|             | which shows an option to Sign Up if no account,       | as expected | 
|             | Color of Sign In NavLink darkens once it's selected,  | as expected |
|             | Once logged in, Sign Out replaces Sign In on NavBar,  | as expected |
|             | Message appears "Successfully signed in as (username)"| as expected |
|             | Signed in as (username) appears on the right side,    | as expected |
|             | And is visible on all Pages while user is signed in,  | as expected |
|             | Sign Up option is visible if not signed in            | as expected |
|             |                                                       |             |
| Sign Out    | Sign Out is visible only when user is Signed In,      | as expected |
| NavLink     | Color of Sign Out NavLink darkens once it's selected, | as expected |
|             | Opens in the current tab,                             | as expected | 
|             | Sign Out form Opens with an option to Sign Out,       | as expected |
|             | Or refreshes the Sign Out page if user already on Sign| as expected |
|             | Out page,                                             |             |
|             | Sign Out option remains on the page,                  | as expected |
|             | for the user until Sign Out button is clicked,        |             |
|             | after which message pops up: "You have signed out.",  | as expected |
|             | And Sign In option appears instead of Sign Out,       | as expected |
|             | And now on the right side can see "Not signed in",    | as expected |
|             | And Sign Up option is now available in NavBar         | as expected |
|             |                                                       |             |
| Logo        | Clickable,                                            | as expected |
|             | Opens Home page,                                      | as expected |
|             | Or refreshes Home page if user is already on Home page| as expected |
|             | Opens in the current tab                              | as expected | 
|             |                                                       |             |
| NEXT >>     | Visible only on Home page (accessed via               | as expected |
|             | Home page or Logo),                                   |             |
|             | Clickable,                                            | as expected |
|             | Available to user when signed in,                     | as expected |
|             | And when not signed in,                               | as expected |
|             | On the next page << PREV NavButton appears instead    | as expected |
|             |                                                       |             |
| << PREV     | Visible only on Home page after NEXT >> is clicked,   | as expected |
|             | And the user can see the next page,                   |             |
|             | Clickable,                                            | as expected |
|             | Available to user when signed in,                     | as expected |
|             | And when not signed in,                               | as expected |
|             | << PREV is replaced by NEXT >> on the first Home page | as expected |
|             |                                                       |             |
| NavBar Text | Not Clickable,                                        | as expected |
|             | sharing beautiful moments remains the same,           | as expected |
|             | Visible in top right corner on all pages              | as expected |


## Blog Posts, Comments, Edit and Delete Options, Approving of Comments

| Tested Item | Expected Outcome                                      | Outcome         |
| ----------- | ----------------------------------------------------- | --------------  |
| Blog Post   | Clickable Blog Post title,                            | as expected     |
|             | Opens in a new tab,                                   | as expected     |
|             | Title, author, time of creation are visible,          | as expected     |
|             | Blog Posts text is visible and clear,                 | as expected     |
|             | Full Image of the blog post is visible                | not as expected |
|             | beside the title, on different screen sizes,          |                 |
|             | Image of the blog post is visible on different        | not as expected |
|             | screen sizes,                                         |                 |
|             |                                                       |                 |
| Comment     | Clickable,                                            | as expected     |


## About Page, Collaboration Form

| Tested Item | Expected Outcome                                                  | Outcome     |
| ----------- | ----------------------------------------------------------------- | ----------- |
| About       | About page opens when About is clicked on in the NavBar,          | as expected |
| Page        | Page available when Signed in or not Signed in,                   | as expected |
|             | Admin can access via NavBar and via Django.                       | as expected |
|             |                                                                   |             |
|             | NavLink About in the NavBar darkens to show user is on About page,| as expected |
|             | NavText remains in the top right corner,                          | as expected |
|             | Top right corner, below NavText, user can see if Signed in        | as expected |
|             | or signed out                                                     | as expected |
|             |                                                                   |             |
| Image       | Default image is displayed on the left side or                    | as expected |
|             | above the text (if smaller screen size),                          | as expected |
|             | only Developer can add/edit/change/delete Images on About page,   | as expected |
|             |                                                                   |             |
| Text        | Developer's view on what this website/project is about,           | as expected |
|             | disclaimer Collaboration Forms won't be replied to,               | as expected |
|             | only Developer can add/edit/delete About page text,               | as expected |
|             | date and time of the update of the text are on the right,         | as expected |
|             | below the text about the website                                  | as expected |
|             |                                                                   |             |
| Form        | Collaboration Form is part of About page,                         | as expected |
|             | located below text about the website,                             | as expected |
|             | Visitor might need to scroll to see the form,                     | as expected |
|             | Form is accessable when Signed in,                                | as expected |
|             | and when not Signed in.                                           | as expected |
|             |                                                                   |             |
| Name        | Name field is part of the Collaboration form,                     | as expected |
| field       | Visitor can type in Name* field,                                  | as expected |
|             | Name field is mandatory if visitor wants to submit form,          | as expected |
|             | Name field is marked with an asterisk to show it's mandatory,     | as expected |
|             | pop up appears if trying to submit without name:                  | as expected |
|             | "Please fill in this field",                                      | as expected |
|             |                                                                   |             |
| Email       | Email field is part of the Collaboration form,                    | as expected |
| field       | Visitor can type in Email* field,                                 | as expected |
|             | Email field is mandatory if want to submit form,                  | as expected |
|             | Email field is marked with an asterisk to show it's mandatory,    | as expected |
|             | pop up appears if trying to submit without email:                 | as expected |
|             | "Please fill in this field",                                      | as expected |
|             | pop up appears if no text before '@' in the email:                | as expected |
|             | "Please enter a part followed by '@'. '@...' is incomplete"       | as expected |
|             | pop up appears when no '@' in the email:                          | as expected |
|             | "Please include an '@' in the email...",                          | as expected |
|             | pop up appears if no text after '@' in the email:                 | as expected |
|             | "Please enter a part following '@'. '...@' is incomplete"         | as expected |
|             |                                                                   |             |
| Message     | Message field is part of the Collaboration Form,                  | as expected |
| field       | Visitor can type in Message* field,                               | as expected |
|             | Message field is mandatory if want to submit form,                | as expected |
|             | Message fiels is marked with an asterisk, to show it's mandatory  | as expected |
|             | pop up appears if trying to submit without message:               | as expected |
|             | "Please fill in this field"                                       | as expected |
|             |                                                                   |             |
| Submit Here | 'Submit Here' button is accessible below the Collaboration Form.  | as expected |
| button      | Visitor can click on 'Submit Here' button.                        | as expected |
|             | If Name, Email and Message fields have text in them,              |             |
|             | and Email matches all required aspects                            | as expected |
|             | then Collaboration Form is submitted once 'Submit Here' is clicked| as expected |
|             | and pop up appears:                                               | as expected |
|             | "Collaboration Form received. Reviewed within 48 hours."          | as expected |
|             | If form is not filled as requested,                               |             |
|             | pop up would appear, after visitor clicks on 'Submit Here',       | as expected |
|             | informing visitor to adjust the field,                            |             |
|             | that is not filled as required                                    | as expected |

## Resources page

| Tested Item | Expected Outcome                                      | Outcome     |
| ----------- | ----------------------------------------------------- | ----------- |
|             | Logo, NavLinks, NavText displayed on top of the page, | as expected |
|             | Signed in or Not Signed in displayed on the right     | as expected |
|             | Resources NavLink is darkened,                        | as expected |
|             | to show visitor which page they are on                |             |
|             |                                                       |             |
|             | Titles of various links are displayed on the page.    | as expected |
|             | Links to each Resource are displayed,                 | as expected |
|             | links are clickable.                                  | as expected |
|             | On the click, selected link opens in a new tab,       | as expected |
|             | in YouTube,                                           | as expected |
|             | Resources page remains open in a previous tab,        | as expected |
|             | If visitor has YouTube subcsription,                  | as expected |
|             | link content starts on YouTube after link is clicked, | as expected |
|             | if visitor has no YouTube subscription,               | as expected |
|             | random ad chosen by YouTube may play first,           | as expected |
|             | which is out of Developer's expertise                 | as expected |
|             |                                                       |             |
|             | Note on the right below links,                        | as expected |
|             | stating Resources added by Site's admin               | as expected |


## Sign Up page

| Tested Item | Expected Outcome                                                 | Outcome     |
| ----------- | ---------------------------------------------------------------- | ----------- |
| Sign Up     | Logo, NavBar, NavLinks, NavText displayed,                       | as expected |
| page        | or NavLinks and NavText in the Side Menu,                        | as expected |
|             | if smaller screen                                                | as expected |
|             | On the right,                                                    | as expected |
|             | below Side Menu or NavText,                                      | as expected |
|             | 'Not signed in' is displayed.                                    | as expected |
|             |                                                                  |             |
|             | Below Sign Up Title, text Welcomes users,                        | as expected |
|             | gives an option to 'Sign In' if user already has an account,     | as expected |
|             | with a clickable 'Sign In' link.                                 | as expected |
|             |                                                                  |             |
| Sign Up     | Sign Up form is displayed,                                       | as expected |
| Form        | with Username, Email, Password, Password(again) fields,          | as expected |
|             | and grayed out field names where Visitor can type.               | as expected |
|             |                                                                  |             |
| Username    | Visitor can type in what Username they would like.               | as expected |
|             | Username is required, even though there's no asterisk            | as expected |
|             | highlighting that Username is required.                          | as expected |
|             | When cursor is on Username field,                                | as expected |
|             | 'Please fill in this field' appears below the field.             | as expected |
|             | Letters, Numbers and certain special characters are allowed.     | as expected |
|             | If different special characters are entered,                     | as expected |
|             | Notice appears above Username field:                             | as expected |
|             | 'Enter a valid username. This value may contain only letters,    | as expected |
|             | numbers, and @/./+/-/_ characters.'                              |             |
|             |                                                                  |             |
|             | If Username is entered and 'Sign Up' clicked,                    | as expected |
|             | without filling in Password fields,                              | as expected |
|             | "Please fill in this field" pops up below Password field.        | as expected |
|             |                                                                  |             |
|             | If nothing is entered in Username field,                         | as expected |
|             | and user clicks on 'Sign Up' button,                             | as expected |
|             | pop up appears near Username field: "Please fill in this field." | as expected |
|             |                                                                  |             |
|             | When User has tried a few Usernames to sign up with,             | as expected |
|             | these Usernames show up as options, when cursor is in Username   | as expected |
|             | field,                                                           |             |
|             | and User has an option to choose one of them,                    | as expected |
|             | by moving cursor to the selected one,                            | as expected |
|             | and clicking on it,                                              | as expected |
|             | and selected Username then appears in Username field.            | as expected |
|             | If this Username is already not taken by someone else,           | as expected |
|             | User can sign up with that Username.                             | as expected |
|             | If this Username is already taken by someone else,               | as expected |
|             | and new User clicks on 'Sign Up' button, with that Username      | as expected |
|             | displayed on their Username field,                               | as expected |
|             | message will show above Username:                                | as expected |
|             | "A user with that username already exists."                      | as expected |
|             | User can try to sign up with a different Username then.          | as expected |
|             |                                                                  |             |
|             |                                                                  |             |
| Email       | Email field is optional,                                         | as expected |
| (optional)  | User can type in their email,                                    | as expected |
|             | or leave it blank.                                               | as expected |
|             | If Visitor chooses to fill in email:                             | as expected |
|             | pop up appears if no text before '@' in the email:               | as expected |
|             | "Please enter a part followed by '@'. '@...' is incomplete"      | as expected |
|             | pop up appears when no '@' in the email:                         | as expected |
|             | "Please include an '@' in the email...",                         | as expected |
|             | pop up appears if no text after '@' in the email:                | as expected |
|             | "Please enter a part following '@'. '...@' is incomplete".       | as expected |
|             | Suggestions for email are displayed below the Email field,       | as expected |
|             | while adjusting email to match the requirements,                 | as expected |
|             | even before clicking on 'Sign Up'                                | as expected |
|             |                                                                  |             |
| Password    | Password field is required,                                      | as expected |
|             | even though there's no asterisk                                  | as expected |
|             | highlighting that Password is required.                          | as expected |
|             | User can type in what password they would like,                  | as expected |
|             | all typed password characters, are masked as black dots,         | as expected |
|             | for sercurity.                                                   | as expected |
|             |                                                                  |             |
|             | Below Password field, guidelines for Password are listed.        | as expected |
|             | If Password entered doesn't match Password guidelines,           | as expected |
|             | and user clicks on 'Sign Up' button,                             | as expected |
|             | User is notified of Password not matching guidelines,            | as expected |
|             | and one or more guidelines are shown above the Password field,   | as expected |
|             | Highlighting issues with Users chosen Password,                  | as expected |
|             | even if password macthes some of the guidelines:                 | as expected |
|             |                                                                  |             |
|             | If Password is too short, message above Password field states:   | as expected |
|             | 'This password is too short. It must contain at least            | as expected |
|             | 8 characters.'                                                   |             |
|             |                                                                  |             |
|             | If Password is too common, message above Password field states:  | as expected |
|             | 'This password is too common.'                                   | as expected |
|             |                                                                  |             |
|             | If Password is long enough, yet too similar to the username,     | as expected |
|             | message above Password field states:                             | as expected |
|             | 'This password is too similar to the username.'                  | as expected |
|             |                                                                  |             |
|             | If Password field is left blank,                                 | as expected |
|             | and user clicks on 'Sign Up' button,                             | as expected |
|             | pop up appears near Password field: "Please fill in this field." | as expected |
|             |                                                                  |             |
|             | If Password is only numbers,                                     | as expected |
|             | message above Password field states:                             | as expected |
|             | 'This password is too common.'                                   | as expected |
|             | 'This password is entirely numeric.'                             | as expected |
|             |                                                                  |             |
| Password    | If User does not fill in the Password(again) field,              | as expected |
| (again)     | pop up appears below Password(again) field,                      | as expected |
|             | 'Please fill in this field.'                                     | as expected |
|             |                                                                  |             |
|             | User has an option to correct the Username, Email, Password      | as expected |
|             | and Password(again) mutliple times to try to 'Sign Up'           | as expected |
|             | If Username, Password, Password(again) and Email(if chosen)      | as expected |
|             | are entered as required, and user clicks on 'Sign Up' button,    | as expected |
|             | Home page opens,                                                 | as expected |
|             | "Successfully signed in as ...." is shown below NavBar,          | as expected |
|             | or below logo and Side Menu (on a smaller screen),               | as expected |
|             | "Signed in as ..." is displayed on the rightside below pop-up,   | as expected |
|             | NavBar shows 'Sign Out' instead of 'Sign Up' and 'Sign In'.      | as expected |
|             | and user is now allowed to comment on any published posts.       | as expected |



## Sign In page

| Tested Item | Expected Outcome                                                 | Outcome     |
| ----------- | ---------------------------------------------------------------- | ----------- |
| Sign In     | Logo, NavBar, NavLinks, NavText displayed,                       | as expected |
| page        | or NavLinks and NavText in the Side Menu,                        | as expected |
|             | if smaller screen                                                | as expected |
|             | On the right,                                                    | as expected |
|             | below Side Menu or NavText,                                      | as expected |
|             | 'Not signed in' is displayed.                                    | as expected |
|             |                                                                  |             |
|             | Below Sign In Title, text welcomes users back,                   | as expected |
|             | mentions that comments can be made only when Signed In,          | as expected |
|             | and gives New Users an option to Sign Up.                        | as expected |
|             | Sign Up link is clickable,                                       | as expected |
|             | and brings New users to Sign Up form.                            | as expected |
|             |                                                                  |             |
| Sign In     | Sign In form is displayed,                                       | as expected |
| Form        | Username field is displayed,                                     |             |
|             | with grayed out 'Username' in the box.                           | as expected |
|             |                                                                  |             |
| Username    | User can type in their Username,                                 | as expected |
|             | or choose their Username from the options shown,                 | as expected |
|             | after clicking in Username box,                                  | as expected |
|             | if user has previously opted for 'Remember Me:'                  | as expected |
|             |                                                                  |             |
|             | If incorrect Username is entered,                                | as expected |
|             | and user clicks on 'Sign In' button:                             | as expected |
|             | "The username and/or password you specified are not correct."    | as expected |
|             | appears above 'Username' field                                   | as expected |
|             |                                                                  |             |
|             | If nothing is entered in Username field,                         | as expected |
|             | and user clicks on 'Sign In' button,                             | as expected |
|             | pop up appears near Username field: "Please fill in this field." | as expected |
|             |                                                                  |             |
| Password    | Password field is displayed,                                     | as expected |
|             | User can type in their password,                                 | as expected |
|             | all characters typed, are masked as black dots.                  | as expected |
|             |                                                                  |             |
|             | If incorrect password is entered,                                | as expected |
|             | and user clicks on 'Sign In' button,                             | as expected |
|             | "The username and/or password you specified are not correct."    | as expected |
|             | appears above 'Username field',                                  | as expected |
|             | User has an option to correct the password and try again.        | as expected |
|             |                                                                  |             |
|             | If password field is left blank,                                 | as expected |
|             | and user clicks on 'Sign In' button,                             | as expected |
|             | pop up appears near Password field: "Please fill in this field." | as expected |
|             |                                                                  |             |
|             | User has an option to click in checkbox beside 'Remember Me:'    | as expected |
|             | Check appears in the checkbox if user clicks on it.              | as expected |
|             | 'Sign In' button is available below 'Remember Me:'               | as expected |
|             |                                                                  |             |
|             | If correct Username and correct Password are entered,            | as expected |
|             | and user clicks on 'Sign In' button,                             | as expected |
|             | Home page opens,                                                 | as expected |
|             | "Successfully signed in as ...." pops up below NavBar,           | as expected |
|             | or below logo and Side Menu (on a smaller screen),               | as expected |
|             | "Signed in as ..." is displayed on the rightside below pop-up,   | as expected |
|             | NavBar shows 'Sign Out' instead of 'Sign Up' and 'Sign In'.      | as expected |
|             | and user is now allowed to comment on any published posts.       | as expected |

