This is a demo project for full user registration/login and minmial work flow for credit card creation.
It is made by Django and Django Rest Framework as a REST api based web backend. 

# How to run it

- This project is written in Python 3.6, Django 2.1
- Poject is tested in Windows 10 Home and Ubuntu 18 LTS

Follow the following steps to run the project:
1. create a virtual environemnt with python
2. run `pip install -r requirements.txt`
3. since db is included, you can just run `python manage.py runserver`

# Endpoints

- User Registration: `/api/auth/registration/`
- User login: `/api/auth/login/`
- List of credit cards: `/card/`
- Any particular credit card: `/card/{card_id}`

# Notes

- Due to time restriction, the setup is not optimized. For example, the credentials should be setup as environmental variable and stay outside of version control software (i.e. django settings SECRET_KEY, stripe keys)
- project is not dockerized
- project uses `sqlite` db which should not be used in production
- project test database should be the same as the production/development database
- No test code is written due to time restriction
  - pytest congifuration is done
  - all endpoints and functions are manually tested to make sure validation works fine