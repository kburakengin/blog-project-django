# blog-project-django

  A simple, clean blog project with Django. A user simply can register and login, create a new post. Every user has their own profile page and they can change their profile photos and cover photos to their likings. You can click on the author's username under the post and see their available posts on a different page. There is a password reset option on the login page, if you forgot your password click on Forgot Password? and enter your email , you will recieve an email with the instructions to reset your password.

  It's deployed on Heroku and for the profile and cover photos, it's using AWS S3 Bucket.

  
## App is deployed on Heroku
```bash
$ go to https://kbedjangoblogapp.herokuapp.com/
```


## If you want to run this on your local server

##### Clone the repo

```bash
$ git clone https://github.com/Kburak/blog-project-django.git
$ cd blog-project-django
```

##### Create the virtualenv and activate it
```bash
$ python3 -m venv venv
$ . venv/bin/activate
```

##### Or on Windows cmd::
```bash
    $ py -3 -m venv venv
    $ venv\Scripts\activate.bat
```

##### Install dependencies
```bash
$ pip install -r requirements.txt
```

##### Set Up Your Environment Variables
```bash
$ create your env variables for AWS_SECRET_ACCESS_KEY, AWS_ACCESS_KEY_ID, EMAIL_USER, EMAIL_PASSWORD, AWS_STORAGE_BUCKET_NAME, DEBUG_VALUE

```

####Create a Super User to access admin panel
```bash
$ python manage.py createsuperuser
```

####Make Migrations
```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

####Run the app
```bash
$ python manage.py runserver
```
