# VinOp Wine Delivery App

<img src="static/readme/home-page.png">

Visit the deployed site: https://vinop-p5-65ef4c64b7a7.herokuapp.com/

## Introduction

To begin the presentation of this project, I will take the liberty of sharing a bit about my life first. I am a cook; that has been my profession for at least the last 10 years of my life. It's quite far from coding, but both have something in common: they are great tools for building things.

I can no longer keep working in a kitchen, so I had to seek a different path. I never got to have my own restaurant; perhaps in the future it will exist physically, but for now, you can visit it online.

The development of this project could be said to have started five months ago with the first project (link: https://fenasti.github.io/Catering/index.html). After developing the website for some clients with a catering project called Flamingo, we can see that the business has prospered, and they have been able to move to their own permanent location.

Logically, this new business needs a rebranding and to refresh its concept for this new stage.

## Development

### Proposal

The logo and the playful essence of its presentation would be preserved, focusing on a pink inspired by the color of the flamingo. The color palette would be chosen based on the same color from the logo (#E94578), a bright pink that evokes the vibrant colors of summer.

In search of a minimalist palette, a complementary color generator was asked to provide a color that would play with pink, black, and white. The color it generated (#33202A) was a perfect purple to add a touch of sobriety to the strong pink, which suggests the opposite.

<img src="static/images/readme/Colors.png">

The project began with the ideation phase, during which I outlined on paper the essential components that should be included.

- A base.html template with a nav-bar and a footer
- A Home/Index template as the homepage.
- Reservations app and template with a form to request a reservation.
- An about.html where is some information of the restaurant.
- Access to a web version of the menu.

<img src="static/images/readme/home-page.png">

I decided to separate it in 3 main url link paths and to provide the menu as a donwload pdf link also in the nav-bar.
As the Signup, Signin and Logout pages and all the client user functions would be exclusive related to the Reservation view, i solved to blend and display all together in the same place with conditional URL paths.

### Agile

First is to create the repository of the project using the code-institute template provided. Creation of the Project instance and connect it to the project repository. Using Agile to separate themain functions in the most basic tasks to build the apps with the issues User Story template that was was previous created, and display it in the Issues board separating them in All, In Progress, Done and Not Implemented for the functions that were not possible to add to the project because of lack of time or current experience.

https://github.com/users/fenasti/projects/2

### Process

The first steps of creating the Django project where very straight forward.

In order:
- Run the repository in gitpod with the providen template.

- Install Django using the pip command: **pip install django**.

- Create a New Django Projec using: **django-admin startproject (in this case "restaurant")** and make the fisrt migration.

- Connect to postgress with the provided database url in the env.py file and in the same way providing the url into the config vars from Heroku.

- Provide the dev enviroment url in the ALLOWED_HOST variable in settings allong with the Heroku url.

- Create the requirements.txt file, create the path in the Procfile using gunicorn and freeze the installed apps.

- Now is possible to create the Superuser using: **python3 manage.py createsuperuser**

- Migrate the changes and now is the moment to start creating the django apps.

### Apps

To create an app in Django, the process is always the same. It starts with the command:
**python3 manage.py startapp (app name)**
Next, you need to register the app in the INSTALLED_APPS section of the settings.py file.

#### Development Steps:
Model Creation: Begin by defining your models in models.py. This is the foundation of your app's data structure.

View Code: Write the necessary view logic in views.py to handle requests and return responses.

URL Configuration: Create a urls.py file within your app (it doesn’t come by default) to define the URL patterns for your views.

Template Setup: Implement the URLs in the base.html template and create the respective HTML templates in the appropriate templates folder. These templates will be rendered from your views.

Migrate any new changes and use the makemigrations command.

#### Forms:
To handle forms within your app, start by creating a forms.py file. Define your forms as classes that accept model fields as requirements.

<img src="static/images/readme/reservtions-page.png">

#### Admin Registration:
To utilize Django's admin features, you must also register your models in admin.py within your app. This registration allows you to manage your models through the Django admin interface.

## Project description
 
My project consists of three main apps: **About, Index y Reservation**.

<img src="static/images/readme/about-page.png">

The **About** and **Index** models are quite similar and can be defined more as content models, where the title, text, and images in each template can be altered from the superuser access. Their only difference is that the **About** app uses a function-based view because it wasn't planned to hold too much content.

In contrast, the **Index** app utilizes a class-based view, allowing for extension, where each post functions as a whole. In the template, it loops through each created model, displaying one on one side and the other as a mirror image on the opposite side.

<img src="static/images/readme/home-page-2.png">

Both are entirely customizable from the admin page, and thanks to the **Sommernote** plugin, the displayed texts can be edited dynamically with greater ease.

The **Reservation** app, in contrast, is the one that holds most of the project's functionality. It consists of two main models: the **ReservationContent** class, which is similar to the other two mentioned earlier and serves solely to display content, and the **ReservationRequest**, which provides the necessary fields for authentication and the ability to perform CRUD operations (Create, Read, Update, Delete) on reservation requests.

<img src="static/images/readme/sign-in.png">

The approval of the reservation is made by the admin in the adminpage by the checklist approved model field and it shows the reservation now without the fade class. The metadata in the **ReservationRequest** model gives all the neccesary information to contact the client back and to schedule the requested datetime.

<img src="static/images/readme/admin-reservetion-meta.png">
<img src="static/images/readme/reservation-aproval.png">

I decided to use the Comment model's base relationship from the walkthrough blog project and adapt it to only display reservations to the logged-in user. Permission for editing and deleting reservations is also restricted to users, and these actions are only possible if the user is logged in.

<img src="static/images/readme/reservation-edit.png">
<img src="static/images/readme/delete-modal.png">

| Field             | Type                 |
|:-----------------:|:--------------------:|
| client            | ForeignKey(User)     |
| email             | EmailField           |
| details           | TextField            |
| reservation_date  | DateField            |
| reservation_time  | TimeField            |
| created_on        | DateTimeField        |
| approved          | BooleanField         |

The only relation is with the user that is named as client, if this is deleted, all the reservations related to the client will be erased on cascade  afterwards.

## Technologies

### Programming Languages and Frameworks

- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
- [CSS](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/CSS_basics)
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Django](https://www.djangoproject.com/)
- [Bootstrap](https://getbootstrap.com/)

### Main packages in the requirements.txt file

- Cloudinary: used for managing media (like images) in Django projects.

- Dj-database-url: used for deployment to Heroku.

- Django-allauth: An app for handling user authentication, registration, account management, and logins.

- Django-crispy-forms: A Django package that helps with creating dynamic and styled forms

- Django-summernote: Editor for the Django admin that allows rich-text editing.

- Gunicorn: Python translator for running Django applications in production environments.

- Psycopg: A PostgreSQL adapter for Python, allowing Django to interact with a PostgreSQL database.

- Whitenoise: A middleware that helps serve static files directly from Django in production environments like Heroku.

## Testing

Please refer to [TESTING.md](TESTING.md)

## Problems / Bugs

### #1
The first problem i had after trying the early deploymnet was that i was using the wrong name project in the Procfile. I was using a previous project name as a copy-paste way without realizing the importance of the path

### #2
After installing Postgress and migrate the changes of the first model formulated, i faced another bug wich took me a lot of time to solve, until i added the 8000 port to the CSRF_TRUSTED_ORIGINS besides the ALLOWED_HOSTS.

### #3
When creating the superuser and migrate the first modelof Django, I deployed the project to Heroku and an "Internat Server Error" was shown. I solved it providing a SECRET_KEY variable to the Vars settings in Heroku.

### #4
I couldn't visualize the view of my Home model, this was because the template provided in the class view of the index app was not written as a relative path.

### #5
After a whole day trying to implement the callendar input i decided to come back to the main stage using the command **"git log"** to view my later logs and as i didn't commit during the whole time because there were no succesfull stages, i used the command **"git checkout --."** and came back to the previous stage.
First i tried to use an extension called Tempus Dominus but it was too complicated to install thru all the JavaScript and all the metadata needed. The main problem was that afer to be able to show a callendar input, the data was given all date and time together and somehow the default format couldn't accept it in any way i tried, even changing the default format to many different acceptance criterias.
After returning to the previous stage i decided to separate the specifications input to both time and date respectively separated and combine them afterwards to use them as the database reservation_datetime object required.

<img src="static/images/readme/date-picker.png">

## Future implementations

As shown in my Agile project board there were 3 functions that were way out of my knowledge to implement.

- An automatic response when the reservation is possible due a callendar which has all the schedulled reservations and which can provide inmediate response when a spot is free or taken.

- Email confirmation with an autogenerated template with the details of the reservation that is sended to the client mail adress.

- A Google maps API that shows the exact location of the restaurant in the about page.

## Deployment

- Installing the requiremnts packages like gunicorn and whitenoise.

- Create the Heroku app and link it to the github repository.

- Add heroku to ALLOWED_HOST and the packages as middelware.

- Create the Procfile.

- Add any variable required in the var setting in Heroku as the password or the postgress url.

- Use collect static for deployments when debug is set to False.

- Manually deploy from the branch in the Deploy link from the app.

## Credits

### Tutorials

- https://www.youtube.com/watch?v=pEwA4-Mmnj8

- https://djangotricks.blogspot.com/2019/10/working-with-dates-and-times-in-forms.html

- https://getbootstrap.com/docs/5.3/getting-started/introduction/
Basically all the documentation created by the Bootstrap comunity is very useful and gentle for the user.

### Inspirational projects

- https://github.com/kera-cudmore/TheQuizArms?tab=readme-ov-file#testing

- https://github.com/markdaniel1982/MD82-P4/tree/main

- Of course the Codestar Blog project provided by Code Institute wich was very fun to make and understand.

- https://crumber.com
I'm not quite sure how I came across this webpage, but its simplicity served as great inspiration for the design of this project.

- https://www.rolls-berlin.de
An example of a real restaurant webpage, as a curious fact i worked with the owners of this business and they are beautiful people and they serve delicious food.

