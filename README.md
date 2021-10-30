<h1 align="center">Django Rest Api</h1><br />

## LIVE<br/>
[https://restapi-rishi.herokuapp.com](https://restapi-rishi.herokuapp.com) <br />

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

-asgiref==3.4.1<br />
-cffi==1.15.0<br />
-configparser==5.0.2<br />
-cryptography==35.0.0<br />
-Django==3.2.8<br />
-djangorestframework==3.12.4<br />
-gunicorn==20.1.0<br />
-jwt==1.3.1<br />
-psycopg2-binary==2.9.1<br />
-pycparser==2.20<br />
-pytz==2021.3<br />
-sqlparse==0.4.2<br />
-whitenoise==5.3.0<br />

## How to run<br />

If running on local machine do<br />

```python
python3 manage.py runserver
./manage.py runserver
```

## CRUD operations available in this API<br />
### The following roles are  allowed<br />
- Admin
	1.  API: Add an advisor
		- Method:
			- POST
		- Authentication:
			- not needed for this assignment
		- Endpoint:
			- /admin/advisor/
		- Request:
			- Advisor name
			- Advisor Photo URL
		- Response:
			- No Response
			- Just return 200_OK if the request is successful
			- Return 400_BAD_REQUEST if any of the above fields are missing
- User
	1. API: Can register as a user
		- Method:
			- POST
		- Endpoint:
			- /user/register/
		- Request:
			- Name
			- Email
			- Password
		- Response:
			- Body:
				- JWT Authentication Token
				- User id
			- Status
				- 200_OK if the request is successful
				- 400_BAD_REQUEST if any of the above
                fields are missing
	2. API: Can log in as a user
		- Method:
			- POST
		- Endpoint:
			-/user/login/
		- Request:
			- Email
			- Password
		- Response:
			- Body:
				- JWT Authentication Token
				- User id
			- Status
				- 200_OK if  the request is successful
				- 400_BAD_REQUEST if any of the above fields are missing
				- Return 401_AUTHENTICATION_ERROR if the
                email/password combination was wrong
	3. API: Get the list of advisors
		- Method:
			- GET
		- Endpoint:
			- /user/<user-id>/advisor
		- Request:
			- None
		- Response:
			- Body:
				- An array of advisor objects with each object having
					- Advisor Name
					- Advisor Profile Pic
					- Advisor Id
			- Status
				- 200_OK if the request is successful
	4. API: Can book call with an advisor
		- Method:
			- POST
		- Endpoint:
			- /user/<user-id>/advisor/<advisor-id>/
		- Request:
			- Booking time (a DateTime string)
		- Response:
			- Body:
				- None
			- Status
				- 200_OK if the request is successful
	5. API: Can get all the booked calls
		- Method:
			- GET
		- Endpoint:
			- /user/<user-id>/advisor/booking/
		- Request:
			- None
		- Response:
			- Body:
				- An array of advisor objects with each object having
					- Advisor Name
					- Advisor Profile Pic
					- Advisor Id
					- Booking time
					- Booking id
			- Status
				- 200_OK if the request is successful




