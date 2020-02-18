# Alicante Properties

The purpose of this project purely fictitious and is for educational purposes only. It serves as the Final Milestone Project entitled Full-Stack Frameworks at the Code Institute.

This web application has been created using Python 3.7 for the back-end with Django 2.1 framework. Postgres has been used for the SQL database. Bootstrap has been implemented for the front-end. 

The live project can be viewed on Heroku at [link](https://alicante-prop5.herokuapp.com) here.

## UX/UI

The theme of the site is for realors offering for sale properties in the Alicante and Benidorm region: for a holiday home or for whatever reason. I decided not to swamp the users with the whole of Spain, so I decided to focus on a popular affordable choice for mainly British clientele, the Alicante and Benidorm region. 

This website has been designed fictitiously with business logic in mind for a local business property sales office based in Alicante for people searching for a Spanish home. The site could potentially be transformed into a live site for a real case scenario for the potential business website buyers, i.e. the realtors if they like the preliminary site.


The website allows you (an outside user) to list your property as an extra service and receive messages from potential buyers (pending). The website has several search parameters, e.g. price, bedrooms. For simplicity, I decided to not add rentals to the site.

I first browsed through existing websites which feature Spanish properties: www.aplaceinthesun.com/spain, www.idealista.com, www.kyero.com, www.lucasfox.com.

**Layout design**: the site theme is dark blue, grey, turquoise in colour. The theme itself was largely based on that designed by Brad Traversy in a Udemy video series about American Properties. I also changed the colours in the Admin area to dark blue and white. The changes are present in the css file. I also designed a logo which is present on the last photo of the majority of listings, also as an icon tab, although might not function due to AWS storage issues. All of the pre-design and UI stages can be seen as sketches in the **Planning** folder in this Github account's directory.


## Responsiveness
The app works all phones and screens.

## CRUD Functionality

### CUSTOMER USERS/AUTHENTICATION ALL USERS
Whether registered or not users can view a list of properties already on the database from a search on the homepage by keywords and dropdown searches. A user can choose to register, then as a logged in user can, while accessing a single listing, has the option to ``make an enquiry`` about that property. This is where I implemented a modal which sends a message to one of the realtors. The authentication process has been implemented much the same as with other apps of this calibre. I also included Javascript with timing for a flash alert message saying the user is logged in and also when the user is logged out. This also applies to all users. A form for making an enquiry exists, but a user cannot ask twice, as a post directs to the realtor and the flash message informs the user they have already made an enquiry.

The realtor can view the info in the Admin area. In addition, general customer users have the option to add their own property to the database for £10, although the purpose of this was to demonstrate stripe api e-commerce integration and a user front-end form plus a save to the backend. Future development sees this user added property integrated with the listings. Also user edit and delete from the front-end.

### STAFF USERS/AUTHENTICATION
Luckily for staff users they have access to Django’s admin area, where they can add their listings, check their messages, and this is a built-in CRUD feature of Django which makes it easier for small companies office management of the site. The can also update and delete the self-user added properties, a self-user has to contact office staff to amend after paying the £10.

Thus, staff users can create, read, update and delete any property that they have listed from the database collection via the admin panel. A ```superuser``` has full admin rights and can access all admin functions.


### E-commerce/Stripe API
Stripe e-commerce functionality has been added to the users’ cart page. Using the test purpose digits, a user can create a test payment which comes through as a test payment to my stripe account. If this was a live account, the test keys and numbers simply have to be replaced with live accounts.

#### Static Storage/Photos/Media
Static files cannot be deployed to Heroku, they are linked to Heroku via the config vars as an AWS bucket (S3 Boto), where the original photos and static files are stored.

#### Features Left to Implement
General-Users ability to edit and delete a £10 listing from the front-end. They have to call the office to amend the ad, as staff have access to the model via the admin area. As I have already demonstrated several models and forms and alert pop-ups with javascript for the logins, I felt this task has been competed in the other apps of this project.

Present to a real property website client as a proposal website, to be taken on as a fully-functioning large scale app with the appropriate business licences for real business use as a working live site.


## Technologies Used
* [Python 3.7](https://www.python.org/download/releases/3.0/) Language
* [Django 2.1.1](http://djangoprogect.com) Web framework
* [HTML5](https://en.wikipedia.org/wiki/HTML5) Webpage markup language
* [CCS3](https://www.w3.org/Style/CSS/) Styling and layout
* [Bootstrap](https://www.getbootstrap.com) Front-end component library
* [JavaScript](https://www.javascript.com/) with jQuery and HTML scripts 
* [jQuery](https://jquery.com/) Navbar dropdown
* [Jinja2](https://palljtsprojects.com/p/jinja/) templating engine for Python 
* [Postgres](https://www.postgresql.com/) Database source file
* [AWS](https://www.aws.amazon.com) Amazon S3 Boto Static File Storage Service


#### Responsiveness
The UX fonts and card feature, plus the navbar and hamburger are all scalable, responsive and easy to navigate throughout the site. In the preliminary stages of the site I called a photo for the background image, although, it did not scale as I wanted and also the jumbotron had issues, finally, all is clear, simple and easy to navigate. The site follows responsive design and works for desktop viewing on browsers: google chrome, firefox and explorer as well as mobiles having checked the rending on the iPhone: from 6 plus to X, Samsung Galaxy: all versions, iPad: all versions, Google: Pixel 2 and 3. 

#### Coding Tests
The HTML, CSS code for this application has been checked via W3C Markup and reported no significant errors. The Python code has been tested via working on the code in stages and running the app on the front-end. Back-end terminal testing and running were standard procedures throughout the app development. 

More detailed automated tests have been added to integrate some basic python functionality tests. These tests have been inspired by coding examples in a python series by *Teclado*, “The Complete Python Course” on Udemy.


#### Database Testing
The database is set up in **Postgres** and is comprised of property listings. Environment variables were created in a ```.env``` file which was hidden in ```.gitignore``` and not available on github pages. The connection string was added to the config vars on Heroku which is accessible only to the owner of the site.

## Deployment
Installing the project can be done via the following stages:
Download this repository via the green download button on the head of this page.
````Login to Heroku.com presuming you have pre-registered
On the Heroku dashboard click on Create New App
Enter a unique name and your region (nearest), click Create
Go back to your command line terminal where your app is, enter Heroku
then Heroku login, enter your credentials for Heroku
In your terminal (using powershell on windows 10, may differ slightly for Mac etc.)
pip freeze --local > requirements.txt
echo web: python manage.py runserver > Procfile
git add .
git commit -m "initial commit"
git push -u heroku master
heroku ps:scale web=1
Set debug to False in production/live within the main file (eg manage.py)
In your Heroku app set the config vars to IP : 0.0.0.0, 
PORT : 8000 and POSTGRES :postgres://[yourusername]:[youpassword]
@the string that your got from, i.e <whatever the collection name is>.
Find the More tab> Restart all Dynos
This should see the app live at https://<whatever-you-called-it>.herokuapp.com/
 ````
 
# Credits and Acknowledgements

**Stack Overflow**, **CI** for coding issues

**Antonio Mélé**, Django2 by Example

**Spencer Bariball**, Tutor at Code Institute

**Brad Traversy**, Django Python Tutorial Udemy

**Teclado**, The Complete Python Course Tutorial Udemy

**Victor Freitas**
* [User Based Uploads] (https://www.youtube.com/watch?v=KQJRwWpP8hs)


## Images
All images used in this application are copyright of their respective website owners.

## License
This project is released under the * [MIT licence](https://github.com/fion21/Alican-prop-5/LICENSE).


## Disclaimer
The purpose of the project is for educational purposes only.

