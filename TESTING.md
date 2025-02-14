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

## User Story Testing

### EPIC | Viewing and Navigation
*As a Site User, I can intuitively navigate around the site so that I can find content.*

- A navigation bar is visible on every page of the site which is fully responsive on different screen sizes.

![header](/media/image-32.png)

*As a Site User, I want to browse a list of available products so that I can choose one to explore further.*

- On the "All Products" page, users are shown a comprehensive list of products retrieved from the database, providing an easy overview of the available options.

![all product](/media/all_product.png)

*As a shopper, I can click on a product so that I can read the full product details.*

- When the user clicks on an individual product they are taken to the full product details.

![Product Detail](/media/product_detail.png)

*As a shopper, I want to view products by category so that I can easily browse items that match my interests.*

- By clicking the 'LEGOS OR OTHER TOYS' link in the navigation bar, a dropdown menu displays all available categories. Selecting a category redirects the user to a dedicated products page showcasing items from that specific category, with the category name clearly displayed as the page heading.

![Categories](/media/categories_toys.png)

 ![products](/media/special_offer.png)
 
*As a shopper I can search all products so that I can find what I am looking for*

- Located above the navbar is a search bar. On smaller screens, this bar becomes a search icon which when clicked will drop down the full bar. Any searched word will match itself to any text in the product's title, or description and display the results on the product's page.

![Search](/media/image-33.png)

*As a shopper, I can sort all products so that I can view products based on price or title.*

- A sort box is located on the products page where users can sort all products by price,age in ascending or descending order and by title (A-Z). 

![sort](/media/sort.png)


*As a site user, I can read legos story from other customers to learn about their experiences with LEGO products and services.*

- When users navigate to the "LEGO Stories" page, they can view testimonials shared by previous customers. Each story highlights the LEGO products or services mentioned, along with the date and the customer's name.

![Testimonials](/media/testimonial.png)

### EPIC | User Account and Profile
*As a site user I can register an account so that I can have a personal account.*

- A sign up button is located in the user options drop down menu in the Navbar. When the user clicks the button they are taken to the sign up page.

![alt text](/media/image-38.png)

*As a site user I can log in or log out of my account so that I can keep my account secure.*
- If the user has registered an account they can log in or log out by clicking the links in the user options drop down menu in the Navbar.

![alt text](/media/image-39.png) 

![alt text](/media/image-40.png)

*As a site user I can see my login status so that I know if I'm logged in or out.*

- Whenever a user logs in or logs out a toast message will appear notifying the user or their action.
- Their user name will display in the navbar.
- When signed in the options in the user menu will change to show Profile and Log Out buttons.

![Logged In](/media/toast_message.png)

- *As a site user, I want to save my personal details in my user profile so that I don’t need to re-enter them for future orders.**

  - Users can enter and save their personal details directly on their profile page. These details will automatically prepopulate when placing future orders.  
  - While placing a new order, users can check a box under the delivery information to save the details they've just entered for future use.  

![Delivery Details](/media/delivery_info.png)

*As a site user I can view my order history so that I can remember what purchases I've made.*

- Once a user has created an account and placed an order, they can view the order history on their profile page.
- Clicking the order number will take you to a summary page of that order.

![Order History](/media/order_info.png)

*As a site user I can recover my password in case I forget it so that I can recover access to my account.*

- On the sign-in page, a link to recover your password is located underneath the sign-in button. This uses the AllAuth functionality to reset the user's password. 

### EPIC | Purchasing
*As a shopper, I can add a number of products in different quantities to my shopping bag so that I can purchase them all together when I am ready.*

- Within the product detail page there is a quantity selector and an Add to Bag button. Shoppers can adjust the quantity by using the buttons located on either side of the input, or by typing in the amount.
- When the user clicks on the add to bag button, the chosen quantity of the product is added to the user's shopping bag.

![Product Detail](/media/product_me.png)

*As a shopper I can view a running total of my shopping bag as I am shopping so that I can see how much it costs in total.*

- As the user adds products to their bag, a toast message appears in the top right-hand corner of the screen informing the user that the item has been added, giving them a snapshot of the bag contents and the total cost of the bag.

![bag total](/media/bag.png)

*As a shopper I can view the contents of my shopping bag at any time so I can see what is included and the total cost.*
- When the user clicks on the shopping bag icon in the nav bar they are taken to the shopping bag page which shows the products which the user has added to their cart, unit price, quantity and subtotal.
- The bottom of the page shows the bag total, delivery costs and then the grand total.

![shopping bag](/media/shopping_cart.png)


*As a shopper, I can see a summary of my shopping cart when I checkout so that I know what products are included and the total cost before I commit to purchasing.*
- On the Checkout page the user can see a summary of the line items within their order including a thumbnail image, the product name, the quantity, the unit cost and the overall total order cost on the right-hand side.

![checkout](/media/checkout_cart.png)

*As a shopper, I can easily enter my payment information securely so that I can purchase my chosen products quickly with no issues.*
- When the user navigates to the checkout page, they can see the Stripe Elements UI where they can enter their card details securely and pay for their order.
- The user receives feedback if the card number is valid/invalid.

*As a shopper checkout as a guest so I don't have to sign up for an account.*
- Shoppers do not need an account to purchase any items. Regardless of whether a user is signed in, the checkout process remains the same.
-  When the user completes the checkout form and presses submit their order should be completed.

*As a shopper, I can view an order confirmation after checkout so that I know my purchase was successful.*
- When the user submits the checkout form, they are redirected to a Checkout Success page where they can see an order confirmation and a summary of their order.

![order_confirmation](/media/delivery_details.png)

*As a shopper, I can receive an email confirmation of my order so that I have a record of my purchase.*
- When the user has submitted their order they will receive a confirmation email to the email address they entered in their order form containing all the details of the order.


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