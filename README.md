# Web Dev Lab

### Todo
 - Add tests for Django and Nuxt.js
 - Fix linting issue on Nuxt.js
 - Fix liniting issues for Django project
 - Seed data to the database
 - Frontend design with bootstrap

### Features
 - Selling courses
 - Blog on http://blog.webdevlab.org
 - Create short tutorial
 - Create developer team (career opportunity)
 - Create most advanced User Authentication system (Cookie based, refresh token)
 - Forum on http://forum.webdevlab.org
 - User role (Admin, Student, Viewer)
 - Do nuxt js seo for all pages

### Requirements
 - Quill text editor
 - Use time function [Intl](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl)
 - Design layout for admin
 - Main menu for home

### Database Modeling (PostgresSQL)
 - Articles Table:
    - article_id (Primary Key)
    - title
    - content
    - publication_date
    - author_id (Foreign Key referencing the Authors Table)
    - category_id (Foreign Key referencing the Categories Table)

 - Authors Table:
    - author_id (Primary Key)
    - name
    - email
    - bio

 - Comments Table:
    - comment_id (Primary Key)
    - article_id (Foreign Key referencing the Articles Table)
    - author_name
    - email
    - comment_text
    - comment_date

 - Categories Table:
    - category_id (Primary Key)
    - name

 - Tags Table:
    - tag_id (Primary Key)
    - name

 - ArticleTags Table (a junction table to implement many-to-many relationship between Articles and Tags):
   - article_id (Foreign Key referencing the Articles Table)
   - tag_id (Foreign Key referencing the Tags Table)

### Flake setup
 - pip install flake8 flake8-django
 - nano setup.cfg
 - flake8 .
 - nano setup.cfgpip install pre-commit
 - flake8 .
 - pip install pre-commit
 - pip freeze > requirements.txt
 - pre-commit install


### Requirements
 - Create a mail services for **contact@webdevlab.com**