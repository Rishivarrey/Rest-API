<h1 align="center">Django RestApi</h1><br />
## LIVE<br />
<https://restapi-rishi.herokuapp.com> <br />
## Motivation 🎯  <br />
- App suggestion based on interview assignment <br />
- Deployment with Procfile on heroku <br />
- Working with tools that are free for open source <br />
## Features ✨ <br />
-Basic CRUD operations  <br />
-Advisor registration   <br />
-User Registration  <br /> 
-User can login and book a call with an advisor <br /> 

## Requirements <br />

asgiref==3.4.1<br />
cffi==1.15.0<br />
configparser==5.0.2<br />
cryptography==35.0.0<br />
Django==3.2.8<br />
djangorestframework==3.12.4<br />
gunicorn==20.1.0<br />
jwt==1.3.1<br />
psycopg2-binary==2.9.1<br />
pycparser==2.20<br />
pytz==2021.3<br />
sqlparse==0.4.2<br />
whitenoise==5.3.0<br />

## How to run<br />

If running on local machine do<br />

```python
python3 manage.py runserver
./manage.py runserver
```
##CRUD operations available in this API<br />
a. The following roles are should be allowed<br />
i. Admin<br />
    1. API: Add an advisor<br />
         a. Method:<br />
            i. POST<br />
         b. Authentication<br />
            i. not needed for this assignment<br />
        c. Endpoint:<br />
            i. /admin/advisor/<br />
        d. Request:<br />
            i. Advisor name<br />
            ii. Advisor Photo URL<br />
        e. Response:<br />
            i. No Response<br />
            ii. Just return 200_OK if the request is successful<br />
            iii. Return 400_BAD_REQUEST if any of the above
                fields are missing<br />
ii. User<br />
    1. API: Can register as a user<br />
        a. Method:<br />
            i. POST<br />
        b. Endpoint:<br />
            i. /user/register/<br />
        c. Request:<br />
            i. Name<br />
            ii. Email<br />
            iii. Password<br />
        d. Response:<br />
            i. Body:<br />
                1. JWT Authentication Token<br />
                2. User id<br />
            ii. Status<br />
                1. 200_OK if the request is successful<br />
                2. 400_BAD_REQUEST if any of the above<br />
                fields are missing<br />
    2. API: Can log in as a user<br />
         a. Method:<br />
            i. POST<br />
         b. Endpoint:<br />
            i. /user/login/<br />
        c. Request:<br />
            i. Email<br />
            ii. Password<br />
        d. Response:<br />
            i. Body:<br />
                1. JWT Authentication Token<br />
                2. User id<br />
            ii. Status<br />
                1. 200_OK if  the request is successful<br />
                2. 400_BAD_REQUEST if any of the above fields are missing<br />
                3. Return 401_AUTHENTICATION_ERROR if the
                email/password combination was wrong<br />
    3. API: Get the list of advisors<br />
        a. Method:<br />
            i. GET<br />
        b. Endpoint:<br />
            i. /user/<user-id>/advisor<br />
        c. Request:<br />
            i. None<br />
        d. Response:<br />
            i. Body:<br />
                1. An array of advisor objects with each object having<br />
                    a. Advisor Name<br />
                    b. Advisor Profile Pic<br />
                    c. Advisor Id<br />
            ii. Status<br />
                1. 200_OK if the request is successful<br />
    4. API: Can book call with an advisor<br />
        a. Method:<br />
            i. POST<br />
        b. Endpoint:<br />
            i. /user/<user-id>/advisor/<advisor-id>/<br />
        c. Request:<br />
            i. Booking time (a DateTime string)<br />
        d. Response:<br />
            i. Body:<br />
                1. None<br />
            ii. Status<br />
                1. 200_OK if the request is successful<br />
    5. API: Can get all the booked calls<br />
        a. Method:<br />
            i. GET<br />
        b. Endpoint:<br />
            i. /user/<user-id>/advisor/booking/<br />
        c. Request:<br />
            i. None<br />
        d. Response:<br />
            i. Body:<br />
                1. An array of advisor objects with each object having<br />
                    a. Advisor Name<br />
                    b. Advisor Profile Pic<br />
                    c. Advisor Id<br />
                    d. Booking time<br />
                    e. Booking id<br />
            ii. Status
                1. 200_OK if the request is successful




