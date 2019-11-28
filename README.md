# Jake's Artwork - https://jake-matthews-project-4.herokuapp.com/
### Welcome to my final project submission for Code-Institute. In this project i was tasked with creating a full stack project using Django and other forms of code. For my project idea I decided to create a website that sold artwork. 
### This full stack website is capable of storing data within a database and displaying it on the front end.  I created the ability for users to create an account, which is required to purchase artwork. I also created a blog within the website for users to read. There is also an option for users to purchase the artwork, which is done using Stripe.

# UX Design
### This site was created with the intention of allowing users to purchase artwork created by 'me'. With this in mind, my website is typically aimed at young adults to elderly, however younger generations may also view the artwork, so I made sure it was user friendly to all ages. Typically users who go onto my site are either wishing to view artwork, which is easily done on the homepage or on the artwork page, or purchase artwork, which is also easily done through the click of view details, and then purchase. 



# Mockups

### My mockups are located in: artwork\static\mockups


# User Stories

#### Joseph is doing a project on local artists within his area, and wants to find out information on an artists life.
* My website would make it easy for Joseph to do research on a local artist as my website holds a blog section, which would tell a story of my journey as an artist, in a daily blog style format. 

#### Margaret is an elderly woman who wishes to purchase some new artwork for her home. She isnt very technology smart and so wants a website she can easily navigate without much problems. 
* My website would make it easy for Margaret to purchase artwork for her home as my website was designed to be easily navigated. Artwork can be purchased from the homepage of my website, making it incredibly easily navigated. 

#### Lauren is currently sitting her exams in art, and is researching trying to find inspiration for her final piece of work.
* My website would be great for Lauren as it has multiple pieces of artwork available for her to take inspiration from, and using the blog, she can gain an understanding of why that piece of artwork was created, with my inspiration behind it. 

# Features
* one of my features on my website includes the ability to sign up/create an account. This feature allows for users to purchase artwork, and if I was to have had more time, users would have also had the chance to leave likes/comments on each artwork so that they could discuss the artwork between themselves.

* Another feature of my website is the ability to purchase pieces of artwork easily through online payment. This feature was crucial as the true intent of the website was to allow consumers to buy artwork. 

* A further feature of my website is the navigation bar. This was created to allow users easy access to all the website has to offer, with a simple click of a button. This was done to make information architecture high.

* Another feature of my website is the comments section. This section allows for users to leave comments on any piece of artwork. Whether that be a positive comment, or a constructive comment.

* A final feature of my website is the like option. This option allows for any user to like any piece of artwork. With this in mind, my site is set so that the most liked artwork appears first, making it easier for users to see the more popular artwork. 

# Future Ideas
* One feature I would have implemented had this site been a real running site would be a system in which the comments can be moderated. This would be done with the ability of a report button, would anyone leave a comment that is deemed rude or inappropriate. This would tie in with users displaying their own artwork. 

* Another idea I would have implemented had I had enough time would be the ability to "add to bucketlist". This feature would be where users would be able to save their favourite pieces of artwork to their accounts, displaying them on their profiles.

* A final idea I would have created would be the ability to view profiles and share artwork. This feature would allow for users to add their own creations to their profile for others to see, comment on and like. This would create a feel of a community within the website, which would give users the ability to gain recognition, and also give them another reason to return to the site more regularly.

# Technologies Used

* HTML was used in order to create the web page.

* CSS was used in order to create the styling for certain parts of the webpage.

* Python/Django was used in order to create my views for my database 

* Javascript was used in order to allow stripe to sucessfully request a payment

* Stripe was used in order to allow users to make payments

* Bootstrap was used in order to help me style my webpage using columns and rows

* gunicorn was used in order to successfully allow Heroku to launch my project

* dotenv was used in order to allow me to create my env keys to store sensitive data

* Heroku was used in order to allow my website to be live

* Dj-database-url was used in order to successfully link my database to my live website







# Testing

### Throughout the project I have manually tested extensively in order to try find bugs that may cause problems for my website, and have fixed them accordingly. Each time I introduced a new feature, I tested it thoroughly, with the intention of trying to break the website, so that when my website is live, Users are unable to break it themselves.

I aimed to make my web pages as responsive as possible. This time round I didnt opt to use the "mobile first" approach as the focus for this project was on the functions within the webpage, rather than the webpage itself. If this project was to have been real, the Mobile first approach would have been used in order to maximise responsiveness for users.

I also ran tests, such as:

1. Open Chrome dev tools:
    1. Change the screen size.
    1. All elements on the page move according to screen size.
    1. no overlap is present.
    
1. Open view artwork_detail:
    1. click purchase
    1. Enter Stripe testing credentials
    1. Accept payment
    1. see if wrong details gets accepted- it doesnt
    1. payment is secure
    
# Deployment

### In the process of deployment, I had to ensure that any sensitive data was successfully hidden behind environment variables, so that was done using dotenv. I then had to set up Heroku environment variables so that my live site would work. I then had to create a procfile, so that Heroku was able to launch successfully.   
### In order to successfully deploy my code locally; using the master branch of my github, pull the code. Then in settings.py add yourself to allowed hosts(typically localhost) and then run the command: "python3 manage.py runserver".

# Acknowledgements

* I would like to give a huge thank you to my tutor, Spencer. Who has gone above and beyond to ensure the completion of this project, helping me whenever and wherever possible.

* I would like to thank those students who gave me support during confusing times throughout the duration of the project.

* I would like to thank code-institute and the Learning People, for allowing me an extension due to unforseen circumstance.


# Credits

* All code within this project has been written by myself. 
 
* I took inspiration from other students via SLACK in order to build my app.

* I took help from my mentor, Spencer, who helped me ensure that my views were correctly laid out, and he aided me in setting up both my comments section and my like artwork section. 

* I would like to give credit to Stackoverflow users, who have helped me figure out problems that I was unable to figure out myself, both with some views being miscoded, and Heroku deployment. 

* All of the example images shown within my website was directly taken from Google Images, I do not own the right to these Images, as I did not create them. 











