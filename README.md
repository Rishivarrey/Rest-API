<h1 align="center">Django RestApi</h1>
## LIVE
<https://restapi-rishi.herokuapp.com>
## Motivation 🎯
- App suggestion based on interview assignment
- Deployment with Procfile on heroku
- Working with tools that are free for open source
## Features ✨
-Basic CRUD operations
-Advisor registration
-User Registration
-User can login and book a call with an advisor

## Requirements

asgiref==3.4.1
cffi==1.15.0
configparser==5.0.2
cryptography==35.0.0
Django==3.2.8
djangorestframework==3.12.4
gunicorn==20.1.0
jwt==1.3.1
psycopg2-binary==2.9.1
pycparser==2.20
pytz==2021.3
sqlparse==0.4.2
whitenoise==5.3.0

## How to run

If running on local machine do

```python
python3 manage.py runserver
./manage.py runserver
```
##CRUD operations available in this API
a. The following roles are should be allowed
i. Admin
    1. API: Add an advisor
         a. Method:
            i. POST
         b. Authentication
            i. not needed for this assignment
        c. Endpoint:
            i. /admin/advisor/
        d. Request:
            i. Advisor name
            ii. Advisor Photo URL
        e. Response:
            i. No Response
            ii. Just return 200_OK if the request is successful
            iii. Return 400_BAD_REQUEST if any of the above
                fields are missing
ii. User
    1. API: Can register as a user
        a. Method:
            i. POST
        b. Endpoint:
            i. /user/register/
        c. Request:
            i. Name
            ii. Email
            iii. Password
        d. Response:
            i. Body:
                1. JWT Authentication Token
                2. User id
            ii. Status
                1. 200_OK if the request is successful
                2. 400_BAD_REQUEST if any of the above
                fields are missing
    2. API: Can log in as a user
         a. Method:
            i. POST
         b. Endpoint:
            i. /user/login/
        c. Request:
            i. Email
            ii. Password
        d. Response:
            i. Body:
                1. JWT Authentication Token
                2. User id
            ii. Status
                1. 200_OK if  the request is successful
                2. 400_BAD_REQUEST if any of the above fields are missing
                3. Return 401_AUTHENTICATION_ERROR if the
                email/password combination was wrong
    3. API: Get the list of advisors
        a. Method:
            i. GET
        b. Endpoint:
            i. /user/<user-id>/advisor
        c. Request:
            i. None
        d. Response:
            i. Body:
                1. An array of advisor objects with each object having
                    a. Advisor Name
                    b. Advisor Profile Pic
                    c. Advisor Id
            ii. Status
                1. 200_OK if the request is successful
    4. API: Can book call with an advisor
        a. Method:
            i. POST
        b. Endpoint:
            i. /user/<user-id>/advisor/<advisor-id>/
        c. Request:
            i. Booking time (a DateTime string)
        d. Response:
            i. Body:
                1. None
            ii. Status
                1. 200_OK if the request is successful
    5. API: Can get all the booked calls
        a. Method:
            i. GET
        b. Endpoint:
            i. /user/<user-id>/advisor/booking/
        c. Request:
            i. None
        d. Response:
            i. Body:
                1. An array of advisor objects with each object having
                    a. Advisor Name
                    b. Advisor Profile Pic
                    c. Advisor Id
                    d. Booking time
                    e. Booking id
            ii. Status
                1. 200_OK if the request is successful




