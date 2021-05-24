# Overview
I've played in a band, Mimelight, for almost a decade now.  I've always wanted to
build a webpage with links to social media and a media player for visitors to listen to our music.  

This is a collection of webpages designed to showcase my band's music.  The home page contains basic information about the band and also includes an audio player that plays media uploaded through the Django administration.  The second page is a list showing the Song database.

In order to view the pages you must enter this command prompt within your project directory:
python manage.py runserver

Once your server is up and running copy this code with the desired path to view you work:
* http://127.0.0.1:8000/...

Url paths for the project:
* http://127.0.0.1:8000/home/
* http://127.0.0.1:8000/songs/

[Software Demo Video](https://www.youtube.com/watch?v=4dAp6daDs8I)

# Web Pages
The Home page Show case the members of the band and provides an interactive audio player for users to cycle through music to listen to.

The Song List page uses the Song class database to display the song titles and duration.

# Development Environment
* Atom was used as the IDE
* HTML was used to build the individual pages.
* JavaScript was used to build the audio player.
* Python was used to build class models for backend databases, method views and url mapping.   

# Useful Websites
* [Django](https://docs.djangoproject.com/en/3.2/)
* [How to Build a Music Player Using Django](https://www.section.io/engineering-education/how-to-build-a-music-player-using-django/)
* [The New Boston - Django Tutorial](https://www.youtube.com/watch?v=qgGIqRFvFFk&list=PL6gx4Cwl9DGBlmzzFcLgDhKTTfNLfX1IK)
* [Coding Entrepreneurs - Try Django Tutorial](https://www.youtube.com/playlist?list=PLEsfXFp6DpzTD1BD1aWNxS2Ep06vIkaeW/)

# Future Work
* Make an upload form on the song list page for front end use
* Make a blog page connected with social media accounts
* Ecommerce page for selling band merchandise
