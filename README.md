# we_are_social
App created using Django, deployed using Heroku

This is a full stack Social Entrepreneurship membership site that allows for the exchange of ideas that benefit both businesses and society as a whole.


KEY COMPONENTS
The user stories (and components) involved in interacting with the site are as follows:
*	A member registers to become part of the site community using an Accounts App
*	Membership activated and maintained via recurring payments (payments may be used to fund projects) using an Accounts App where users can pay using Stripe and Paypal
*	Members can blog about their experiences, interests, and general ideas using a Blog App. I used a reusable_blog_app which I used from https://github.com/MikeHibbert/reusable_blog_app.git while following one of the lessons in my course material.
*	Members can engage in discussion about, and the potential progress of, projects and project categories of interest within the membership community using a Forum App
*	Members can vote on whether a project will go ahead or not based on member voting using a Polls App
*	Users may choose to become members under various categories using the Memberships App
*	Both members, and non-members of the site can contact each other using the Contact App to find out more before purchasing memberships
*	People can see data visualizations showing the projects undertaken/proposed/completed
*	People may contact the site by using Social Media Links at the bottom of each page, and as a way of seeing the latest news on projects



KEY TECHNOLOGIES
These include:
*	MySQL, sqlite for the database to store user data
*	AngularJS, HMTL3, CSS3 at the front end
*	Javascript libraries such as d3.js, dc.js queue.js and crossfilter.js to build interactive charts as part of the data visualizations
*	MongoDB to process large amounts of data for the data visualizations
*	Django(Python) for the full stack framework
* Heroku for deployment

DEVELOPMENT
SET DJANGO_SETTINGS_MODULE=settings.dev

