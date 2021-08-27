# Milestone 4 Project – TechArray

TechArray website has been build as a final project with Code Institue. Knowledge used in this project has been gained solely from the Code Academy.

It is fully responsive website with full-stack functionality, focusing on being user-friendly. The website is a PC Components store.

A demo of the website can be found here [TechArray](https://samisinnari-techarray.herokuapp.com/)


![Am-I-Responsive](assets/images/am-i-responsive.jpg)
The image above is a screenshot from [Am I Responsive](http://ami.responsivedesign.is/#)


---

## Contents

- [**User Experience (UX)**](<#user-experience-(ux)>)

  - [Project Idea](#project-goals)
  - [Structure](#structure)
  - [User Goals](#user-goals)
  - [User Stories](#user-stories)
  - [Design](#design)
  - [Wireframes](#wireframes)

- [**Features**](#features)

  - [Existing Features](#features)
  - [Features added then removed](#features)
  - [Features Left to Implement](#features)

- [**Technologies**](#technologies-used)

  - [Languages Used](#technologies-used)
  - [Frameworks, Libraries and Programs Used](#technologies-used)

- [**Testing**](#testing)

- [**Deployment**](#deployment)

- [**Credits**](#credits)

---


# User Experience (UX) <br>

## Project Idea

TechArray is a website that promotes PC Components. The focus of the website is to sell newest ( or latest) PC parts for personal or business use. 

Website users will have the option to create an account in order to preview their previous orders and they will have the option to save their delivery details for faster purchase in the future.

The project Idea has been expanded into a website due to my passion for PCs and everything connected to a PC.


## Structure

There are 6 main pages including the home page and a login/registration page. Other than these, there is a base page which serves as the base for all the other pages. 

### **The home page**
 The home page section will showcase the main values of the company. It is created with attractive and modern design, with button that connects to the shop.

### **About page**

The link "About" will transfer the user to the section on home page, which explaines the quality of our products.

### **FAQ**

Frequ. asked question page will do what it's name says. It should give users answers to the most common questions. Due to lack of time, this section has been customized only with HTML & CSS. In the **future, FAQ page will be developed with Django App so we can update it if needed.

### **Shop page**

Shop section will show users the products we offer. To make navigation easier for users, I have added 5 buttons (+ "All Items" button) so they can categories all the products. They will be presented with Image of the product, name, what section it belongs and the price. If user clicks on the product, they will be transferred onto a product detail page, where they can choose the quantity of the product before adding it to the cart. Moreover, If they want to go back, they are given option to go to "All items", that same product family or back to the shop.

### **Shopping bag page**

If user decides to purchase a product, they can add product to the shopping bag. Once they click "Add to Bag", a notification is given showing that the product has been added and what other items are in the cart already ( if previously added). Moreover, once user clicks "Go to secure checkout", they open a Shopping Bag which shows details of the products. Details include : Picture, Name, Price, Quantity and Subtotal. Below product detail, they are given "Bag Total", "Delivery(Free/NotFree)" and "Grand Total". There, they can decided whether to go back ( "Keep Shopping" ) or whether to make a purchase by proceeding to "Secure Checkout".

### ****Checkout page****

Here the user can enter their billing details to complete the checkout. If they need to update the cart at any point before billing, they have the option to go back to the Shop by clicking on a button. Nevertheless, the users are provided with an option to save their details by logging into the site. If they don't want that option, they can click on Complete Order button to complete the transaction which triggers an automatic mail to their email address provided with the necessary details. If they want to save the details for future, they can register or login from the page or from the navbar. 

### **Login page**

Every visiting person is recommended to sing in. On sign in page, they have the option to save login info (like email address/username) with "Remember me" box. Moreover, they have the link to reset their password if forgotten, and they have the option to Sing Up if they still don't have an account. To sign up, they will have to provide relevant personal info, and conformation email will be sent to their email address. Once email is confirmed, they will enter their login details and at this point the account is activated.

### **Profile page**

The logged in users can update their billing details from this page. If they have made any previous purchases, those details are also presented in this page. 

### **Logout page**

For users logged in, they can click on the logout button which will transfer them to the page where they have to confirm the signout. Once confirmed, they will be logged out successfully.

### **Blog page**

The blog page is an app created to give a personality to the website. It will focus on PC connected ideas and thoughts. The focus of a blog is to promote interactivity on the website hence bringing people together to share thoughts. Info about blog posts are give, like : Username of a person posting, time and date. Once users click "Read More", they wil be able to read full blog post.


### **Comments**

Comments are specifically connected with the blogs to give users availibility to interact on the website. They can exchange thoughts and ideas via comment section. To control comments, the **Site owner** is approving every comment seperately.

### **Contact page**

This page provides a form which they can fill in to contact the companys customer support department, whether they have any inquiries or similar.

### **Management section**

This section is available only for admin person. The admin of the website has options to : 
 - Add, Delete or Edit products
 - Approve or disapprove comments posted
 - Add blogs content.

<br>

## User Goals


* Purchase a product
* Learn more about the products offered.
* Interact on a website
* Gain more knowledge by reading some articles.

## User Stories

 **New user stories**
  - As a new user, I want to be able to learn more about the company I'd like to purchase from.
  - As a new user, I want to be easily navigated throughtout the website.
  - As a new user, I want to see the products offered with ease.
  - As a new user, I want to register for an account so that I can save my personal information for my future orders.
  - As a new user, I want to read FAQ to see if I get some questions already answered.
  - As a new user, I want to be able to contact the company if I have any question.
  - As a new user, I want to check the social media sites of the company, and see their opening hours as I prefer talking to a human.

 **Registered user stories**

  - As a registered user, I want to be able to have my delivery details prefilled so that I can save time in entering my details
  - As a registered user, I want to be able to view my past orders so that I can keep track of my orders with the site
  - As a registered user, I want to be able to easily update my profile information so that I can update my personal details
  - As a registered user, I want to be able to easily log in and out of my account so that I can access my personal information and order history

 **Shopped user stories**

  - As a shopper, I want to contact the website owner so that I can ask them a question.
  - As a shopper, I want to see all components available so that I can decide which product I might purchase.
  - As a shopper, I want to view details of a product so that I can learn more about that particular product.
  - As a shopper, I want to choose the number of products I want to order.
  - As a shopper, I want to be able to delete products from my cart so that I can update the products I would like to purchase
  - As a shopper, I want to receive an order confirmation so that I can be sure my order has gone through.
  - As a shopper, I want to learn more about TechArray through blog articles and testimonials.
  - As a shopper, I want to contact the website owner so that I can ask them a question if I have any.


## The Site Owner:

**Site owner goals**

- Attract large quantity of users with appealing website design with stable functinality.
- Adding and removing of products.
- Managing the website content
- Update the blog section with new content.


**Site owner user stories**

- As a site owner, I want to easily list my products for sale. 
- As a site owner, I want to impress new users with modern looking website.
- As a site owner, I want to be able to easily remove, edit and add products as some may be out of stock or otherwise.
- As a site owner, I want to navigate users throughout the webiste with ease via navigation panel.
- As a site owner, I want to highlight FAQ for users hence lower the customer support demand via separate link.
- As a site owner, I want to add secure checkout to the website.
- As a site owner, I want to add free delivery if delivery treshold is reached.
- As a site owner, I want to send auto emails to users so that I can inform them of successful registration and order confirmation.
- As a site owner, I want to sort the products available on the site by category so that I can view just the products in that category.
- As a site owner, I want to spread knowledge of a PC and PC building by making a Blog.



  #### [Back to Contents](#contents)
<br>

## Deployment 


I used Gitpod to develop the site using Python 3 and deployed to Heroku via Github. <br>

### Local deployment
1. To run the site locally, you can either download a zip file of this repository by clicking 'download.zip' button at the top of the page and extracting the zip file to your chosen folder or clone this repository. See the steps to clone the repo here : https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository. <br>
If you are cloning the site, make sure you have Python 3 installed for this to work. 

2. Then create a virtual environment with your IDE. Open your preferred IDE, then open a terminal session in the unzip folder or cd to the correct location. 

3. Install the required dependencies with the following command:
```
pip3 install -r requirements.txt
```

4. Create an env.py file and add the following with your own values:
```
import os  
os.environ["DEVELOPMENT"] = "True"    
os.environ["SECRET_KEY"] = "<your value>"    
os.environ["STRIPE_PUBLIC_KEY"] = "<your value>"    
os.environ["STRIPE_SECRET_KEY"] = "<your value>"    
os.environ["STRIPE_WH_SECRET"] = "<your value>" 
os.environ["EMAIL_USER"] = "<your value>"
os.environ["EMAIL_PASS"] = "<your value>"
```
(Django Secret Keys can be generated with websites such as [miniwebtool](https://miniwebtool.com/django-secret-key-generator/).)

5. Add the env.py files to .gitignore so that it is not published at any stage. This is to keep the secret keys and values safe.

6. You need to make migrations to set up the SQLite3 tables. You can do that by:
```
python3 manage.py makemigrations
python3 manage.py migrate
```

7. Create a superuser for your project by using the following command:

```
python3 manage.py createsuperuser
```

8. You can now run this locally by the following command:

```
python3 manage.py runserver
```

9. Once the site is running locally, go to the end of the url and type in /admin to add templates, blogs, comments etc.


### Deploying this project to Heroku 

Once you have set up locally, you can deploy to Heroku by following the below steps:

1. Create an account in Heroku if you dont have one or sign in if you have an existing one

2. In Heroku, create a new app with a unique name and set your registration

3. To use the Postgres database for deployment, select 'Heroku Postgres' as a free add-on.

4. Go to Settings in Heroku, click on 'Reveal Config Variables' and enter the following values

| **Key** | **Value** |
--- | ---
 AWS_ACCESS_KEY_ID | your AWS bucket ID
 AWS_SECRET_ACCESS_KEY | your AWS secret key
 DATABASE_URL | your Heroku Postgres database url
 EMAIL_HOST_PASS | your password to use your gmail account for emails
 EMAIL_HOST_USER | your email address
 SECRET_KEY | secret key used for your Django project
 STRIPE_PUBLIC_KEY | obtained through your Stripe account
 STRIPE_SECRET_KEY | obtained through your Stripe account
 STRIPE_WH_SECRET | obtained through your Stripe account
 USE_AWS | True

 5. You need to login to Stripe, go to the developers section to get the pubic key ad secret key. For the AWS secret key, you need to login to AWS and create a new bucket. Creating a new S3 bucket documentation can be found [here](https://docs.aws.amazon.com/AmazonS3/latest/gsg/CreatingABucket.html)

 6. In Gitpod, create a requirements.txt file:
```
pip3 freeze --local > requirements.txt
```

7. Create a Procfile:
```
echo web: gunicorn tech_array.wsgi:application> Procfile
```

8. As with local deployment, make migrations to set up the Postgres database:
```
python3 manage.py makemigrations
python3 manage.py migrate
```

9. Create a superuser similar to the way in local deployment

10. Run the server

11. As with the local deployment, add /admin to the url to go to the admin and add or edit 

12. Add and commit your changes

13. Login to Heroku by using the command 
```
heroku login -i
```
14. Once logged in, link your Heroku app created above as the remote repository with this command:
```
heroku git:remote -a <your app name here>
```
15. Complete the deployment by pushing the projekt to Heroku:
```
git push heroku master
``` 
16. In Heroku, go to the Deploy tab and connect your app to your GitHub repository and **Enable Automatic Deployment** as the deployment method to automatically push the changes to Heroku from Github

17. Your site would now be deployed to Heroku

#### [Back to Contents](#contents)