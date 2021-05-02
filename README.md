# DjangoCaseStudy

This repository is a webapplication built using Django framework to showcase CRUD operations. I have used **Postgresql** database, however one can use the default sqlite3 database by making changes in the setting,py file as follows

* setting.py file
  ```sh
  DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'mydatabase',
    }
}
  ```

<!-- Steps to run the application -->
## Step 1

Git clone this repository
* git clone
  ```sh
  git clone https://github.com/Poohi5/MatchBatchDjango
  ```

## Install dependent libraries

1. Run the following command
2. Clone the repo
   ```sh
   pip install requirements.txt
   ```
3. Change directory to teslasite, make sure you have manage.py file here.
   ```sh
   python manage.py runserver
   ```
4. Run the following command in browser to view the application
   ```sh
   http://127.0.0.1:8000/
   ```

   
<!-- Webapplication screenshots -->
<br />
 <h3 align="center">Home Page</h3>
    <img src="https://github.com/Poohi5/MatchBatchDjango/blob/main/HomePage.png" alt="homepage" width="800" height="500">

<br />
 <h3 align="center">Match Result Page</h3>
    <img src="https://github.com/Poohi5/MatchBatchDjango/blob/main/MatchResultPage.png" alt="matchresult" width="800" height="500">

<br />
 <h3 align="center">Add New Records Page</h3>
    <img src="https://github.com/Poohi5/MatchBatchDjango/blob/main/addnewrecords.png" alt="matchresult" width="800" height="500">
 
<br />
 <h3 align="center">Edit Exiting Records Page</h3>
    <img src="https://github.com/Poohi5/MatchBatchDjango/blob/main/editdetails.png" alt="matchresult" width="800" height="500">
