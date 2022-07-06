# DRF_QUIZ_WITH_JWT_AUTHENTICATION
InsatallationL:
clone the repo
Activate virtual environment
Run pip install -r requirements.txt
Run python manage.py runserver

USER VIEW:
In this project user can register by doing a post request to  http://127.0.0.1:8000/user/register with body,
{
    "name":"name",
    "username":"username",
    "email":"email",
    "password":"password"
}
after successfully login  user will make a post request to http://127.0.0.1:8000/user/login with user credintial as body,
example,
{
    "email":"email",
    "password":"password"
}
If login details are correct and the user will get a jwt token,this token will be stored in cookies for 1 hour,by this time user can make any get request to view quiz data with answer,
for any random quiz,
http://127.0.0.1:8000/quiz/r/Bangla/
for specific subject quiz,
http://127.0.0.1:8000/quiz/q/Bangla/

ADMIN PANEL:
In admin panel admin will add group science/arts to group this has one to many relations with subject,and subject has one to many relation with quiz.Admin can add subject,and then can add as many quiz 
with is right boolean field for the right answer.
