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

| Page             |    W3C Screnshots                                    |             
| -----------------|------------------------------------------------------|
| Home             |  ![alt text](/media/image-1.png)                     |
| Lego Testimonial |  ![alt text](/media/image-1.png)                     |            
| Other Toys       |  ![alt text](/media/image-1.png)                     |
| Legos            |  ![alt text](/media/image-1.png)                     |
| All Product      |  ![alt text](/media/image-1.png)                     |
| Buidling Toys    |  ![alt text](/media/image-1.png)                     |
| Sports Toys      |  ![alt text](/media/image-1.png)                     |
| Cart             |  ![alt text](/media/image-1.png)                     |



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

|  File      | Jigsaw Screenshot                              |  Note
|------------|------------------------------------------------|-------------------
| Base.css   | ![alt text](/media/image-5.png)                |  No error
| profile.css| ![alt text](/media/image-3.png)                |  No error                                                    
|            |                                                |


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

### Site Navigation

| Element                          | Action                        | Expected Result                                              | Pass/Fail |
|----------------------------------|-------------------------------|--------------------------------------------------------------|-----------|
| NavBar                           |                               |                                                              |           |
| Site Name (logo area)            | Click                         | Redirect to home                                             | Pass      |
| Search Box Function              | Enter Text and Click Search   | Search both the product's title and description for a match. | Pass      |
| My Account Dropdown              | Click                         | Open profile dropdown                                        | Pass      |
| Sign Up Link                     | Click                         | Redirect to Sign Up page                                     | Pass      |
|                                  |                               | (Not visible if user in session)                             | Pass      |
| login Link                       | Click                         | Redirect to login page                                       | Pass      |
|                                  |                               | (Not visible if user in session)                             | Pass      |
| Add Product                      | Click                         | Redirect to add_product page                                 | Pass      |
|                                  |                               | (Only visible if superuser in session)                       | Pass      |
| My Profile Link                  | Click                         | Redirect to user profile page                                | Pass      |
|                                  |                               | (Only visible if user in session)                            | Pass      |
| Logout Link                      | Click                         | Redirect to logout confirm page                              | Pass      |
|                                  |                               | (Only visible if user in session)                            | Pass      |
| Bag Link                         | Click                         | Redirect to bag page                                         | Pass      |
|                                  |                               |                                                              |           |
| Mobile Top Header                |                               |                                                              |           |
| Search Icon Button               | Click                         | Open up search box                                           | Pass      |
| Search Box Function              | Enter Text and Click Search   | Search both the product's title and description for a match. | Pass      |
| My Account Dropdown              | Click                         | Open profile dropdown                                        | Pass      |
| Sign Up Link                     | Click                         | Redirect to Sign Up page                                     | Pass      |
|                                  |                               | (Not visible if user in session)                             | Pass      |
| login Link                       | Click                         | Redirect to login page                                       | Pass      |
|                                  |                               | (Not visible if user in session)                             | Pass      |
|                                  |                               | (Only visible if superuser in session)                       | Pass      |
| My Profile Link                  | Click                         | Redirect to user profile page                                | Pass      |
|                                  |                               | (Only visible if user in session)                            | Pass      |
| Logout Link                      | Click                         | Redirect to logout confirm page                              | Pass      |
|                                  |                               | (Only visible if user in session)                            | Pass      |
| Bag Link                         | Click                         | Redirect to bag page                                         | Pass      |
|                                  |                               |                                                              | Pass      |
|                                  |                               |                                                              |           |
|                                  |                               |                                                              |           |