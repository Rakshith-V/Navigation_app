# Navigation Application using Django REST API

> **Note:** The **Navigation Application** was built in a very short time due to the 2 days deadline and the work was done purely after work on both the days(around 8 hours.) This is the assignment done by simultaneously learning django tutorials because of my knowledge in python but lack of experience in django and its MVT framework. I will list some of the features implemented and it's working.

An application that provies turn-by-turn directions,ETA and shortest path on the map after choosing the source and destination point on an interactive and responsive satellite view map(can be made into street easily.) It also implements  basic login features using Django rest framework that user Oauth(token) in activation links sent through emails(Only production). The application, on successful login lets you use the navigation features on a map and find efficient routes. It is also centered so as to point to perpule to find places closeby.

>Requirements.txt file contains the dependencies to run it locally.

# Login

The home page has a navbar with log-in button. Onclick the user is prompted to a login form. There is also a provision for a creating accounts. The user on signing up is sent an email through the specified SMTP server , configured in Production mode settings.
In development settings when hosted offline the template of the mail and the activation link can be found in *Navigation_App\source\content\tmp\emails* 
***[Default login is sent through email for ease of use]***


## Admin

/admin subdomain gives access to the all the models of the app like users and activation.
***[Default login is sent through email for ease of use]***


## Maps

On login , you can view and explore the map functionality implemented using
[MapBox API](https://docs.mapbox.com/api/)


## UI

As the project was built in a short amount of time and had to learn python from scratch , it is functionality focused and the aesthetic part is lacking. Some of my other UI's -

 - [http://ez-health.herokuapp.com/](http://ez-health.herokuapp.com/) > (Skillenza hackathon)
 - [https://www.clayworks.space/](https://www.clayworks.space/)
 
