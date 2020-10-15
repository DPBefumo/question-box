# QuestionBox

## Project Goals

Created an application where people can crowdsource their questions and get answers. This application was created using Python in a Django Framework to allow a fluid functionality of each page.  The database to store questions and answers was created using PostgreSQL.  The live site was uploaded to a live site using Heroku.

## Project Features

This web application has the ability of:

* Users viewing questions and answers
* Registered users can ask questions
* Registered users can add answers to any question
* The question's creator can mark answers as correct
* Registered users can "star" questions and answers they like


## How questions and answers work

Questions have a title and a body. It allows the users to use [Markdownify](https://markdownify.js.org/) for authoring question bodies. I also want to prevent people from putting unauthorized HTML into your Markdown code. I used [Bleach](https://bleach.readthedocs.io/en/latest/clean.html) to achieve this. Questions cannot be edited once they have been asked. A question can be deleted by its author. If it is deleted, all associated answers should also be deleted.

Answers just have a body and are connected to a question. Answers can also use Markdown.

Every question and every answer should be associated with a user.  A user should be able to view all their questions on a user profile page.

Users can search the site for questions. When they search, this should search the questions and all answers for them. 

## To Dos
* Clean up the UX with a better design
* Increase the functionality of the profile page
* When a user answers a question, the question's author receives an email with a link to the answer
* [Allow users to authenticate via Google or other third-party auth](https://www.intenct.nl/projects/django-allauth/)
