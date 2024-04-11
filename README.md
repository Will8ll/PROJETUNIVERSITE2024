# PROJETUNIVERSITE2024
Welcome to the repository for the UEPME university website project developed with Django.

Description
This project aims to create a dynamic website for UEPME, providing information about the university, its programs, news, and other relevant details. It is developed using the Django framework to ensure a robust and scalable web application.

Features
Display information about the university, its history, and mission.
Provide details about academic programs, admissions, and faculty.
Showcase news, events, and achievements of the university.
Allow users to contact the university administration.

Installation
Clone the repository:

git clone https://github.com/your-username/PROJETUNIVERSITE2024.git

Install dependencies:
pip install -r requirements.txt

Apply migrations:
python manage.py migrate

Run the development server:
python manage.py runserver
Access the website at http://localhost:8000/.

Deployment
The website can be deployed to Heroku using the following steps:

Create a new Heroku app.

Set the Heroku git remote:
heroku git:remote -a your-heroku-app-name

Push the code to Heroku:
git push heroku main

Run migrations on Heroku:
heroku run python manage.py migrate
Open the deployed website using heroku open.

Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes.

License
This project is licensed under the MIT License - see the LICENSE file for details.

