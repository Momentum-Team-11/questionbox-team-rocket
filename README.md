# Questionbox API

This application is an API built with Django REST Framework (DRF) that lets users post questions and answers that they are interested in.
All requests, except registration and log in, will *eventually* require authentication

### Required Headers

Requests to endpoints requiring authentication should set the `Authorization` header to `Token <token>`, where `<token>` is the token received in the login response.

POST requests with a body should set the `Content-Type` header to `application/json`.


## Table Of Contents

- [Questionbox API](#questionbox-api)
    - [Required Headers](#required-headers)
  - [Table Of Contents](#table-of-contents)
  - [Models](#models)
  - [Base URL](#base-url)
    - [Endpoints](#endpoints)
  - [Backend Notes](#backend-notes)
  - [Create A New Question](#create-a-new-question)
    - [request](#request)
    - [response](#response)
  - [Create A New Answer](#create-a-new-answer)
    - [request](#request-1)
    - [response](#response-1)
  - [List All Questions](#list-all-questions)
    - [request](#request-2)
    - [response](#response-2)
  - [List All User's Answers](#list-all-users-answers)
    - [request](#request-3)
    - [response](#response-3)
  - [Register a new user](#register-a-new-user)
    - [request](#request-4)
    - [response](#response-4)
  - [Log In](#log-in)
    - [request](#request-5)
    - [response](#response-5)
  - [Log Out](#log-out)
    - [request](#request-6)
    - [response](#response-6)
  - [Header](#header)
    - [request](#request-7)
    - [response](#response-7)


## Models

- **User**
- **Question**
    - Fields
      - title: TextField
      - question: CharField
      - created: DateTimeField
      - user: FK
      - favorited: M2M
- **Answer**
    - Fields
      - answer: CharField
      - created: DateTimeField
      - question: FK
      - user: FK
      - favorited: M2M
      - accepted: Bool

## Base URL
```shell
https://questionbox-rocket.herokuapp.com/
```

## Backend Notes

|  Method  |  Endpoint  |  Description  |  Deployed  |  Notes  |
| -------- | ---------- | ------------- | ---------- | ------- |
|POST|/auth/users/|register a new user|Yes||
|POST|/auth/token/login/|login with existing user|Yes||
|POST|/auth/token/logout/|logout with existing user|Yes||
|GET|/questions/|List all questions|Yes||
|GET|/questions/{id}|Retrieve a specific question|Yes||
|POST|/questions/|Add a new question|Yes||
|PUT|/questions/{id}|Update an existing question|Yes||
|PATCH|/questions/{id}|Update part of an existing question|Yes||
|DELETE|/questions/{id}|Delete an existing question|Yes||
|GET|/questions/favorited/|get list of users favorited questions|Yes||
|GET|/questions/user/|get list of a users questions|Yes||
|GET|/answers/|List all answers|Yes||
|GET|/answers/{id}|Retrieve a specific answer|Yes||
|POST|/answers/|Add a new answer|Yes||
|PUT|/answers/{id}|Update an existing answer|Yes||
|PATCH|/answers/{id}|Update part of an existing answer|Yes||
|DELETE|/answers/{id}|Delete an existing answer|Yes||
|GET|/answers/favorited/|get list of users favorited answers|Yes||
|GET|/answers/user/|get list of a users answers|Yes||






### Endpoints

|  Method  |  URL                                             |  Description                                      |  Deployed  |  Notes                                                    |  Response                                                                |
| -------- | ------------------------------------------------ | ------------------------------------------------- | ---------- | --------------------------------------------------------- | ------------------------------------------------------------------------ |
|  POST    |  [/questions/](#create-a-new-question)           |  create a new question                            |  Yes       |  just something to verify it went through. Header maybe?  |                                                                          |
|  GET     |  [/questions/:Q_id/](#list-all-users-answers)    |  returns a question with all its answers          |  Yes       |  slug/pk later?                                           |                                                                          |
|  DELETE  |  /question/:Q_id/                                |  edit an existing question                        |            |                                                           |  response feedback                                                       |
|  POST    |  [/question/:Q_id/answer](#create-a-new-answer)  |  create a new answer to a question                |  Yes       |                                                           |                                                                          |
|  GET     |  /question/                                      |  get a list of all questions the user has posted  |  Yes       |  working without :U_id, check if ok?                      |                                                                          |
|  GET     |  [/questions/](#list-all-questions)              |  get a list of all questions                      |  Yes       |                                                           |                                                                          |
|  GET     |  /answers/                                       |  return a list of all of a users answers          |  Yes       |                                                           |                                                                          |
|  GET     |  /answers/:user_slug                             |  may not be needed anymore                        |  x         |  currently returning all questions                        |  adam needs: question title, question id as well as rest of answer info  |
|  POST    |  /answer/:A_id                                   |  change details about an individual answer        |            |                                                           |                                                                          |
|  DELETE  |  /answer/:A_id                                   |  delete details about an individual answer        |            |                                                           |                                                                          |
|  POST    |  /favorite/:Q_id                                 |  favorite a question                              |            |                                                           |                                                                          |
|  POST    |  /favorite/:A_id                                 |  favorite a answer                                |            |                                                           |                                                                          |
|  DELETE  |  /favorite/:Q_id                                 |  un-favorite a question                           |            |                                                           |                                                                          |
|  DELETE  |  /favorite/:A_id                                 |  un-favorite a answer                             |            |                                                           |                                                                          |
|  GET     |  /favorites/                                     |  retrieve all favorites                           |            |                                                           |  see samplejson.json for specific notes                                  |
|  GET     |  /favorite/questions                             |  retrieve all favorited questions                 |            |                                                           |                                                                          |
|  GET     |  /favorite/answers                               |  retrieve all favorited answers                   |            |                                                           |                                                                          |
|  POST    |  [auth/users](#register-a-new-user)              |  register a new user                              |  Yes       |                                                           |                                                                          |
|  POST    |  [auth/token/login](#log-in)                     |  login with existing user                         |  Yes       |                                                           |                                                                          |
|  POST    |  [auth/token/logout/](#log-out)                  |  logout                                           |  Yes       |  needs endpoint description                               |                                                                          |


|PUT|/questions/||Yes||

<!-------------------------- Create Question ------------------------------>

 ## Create A New Question

### request

User must be logged in order to create a question.

title and question fields are required.

```
POST /question/
```

```json
{
  "title": "Favorite Band",
  "question": "What is your favorite band?",
  "favorited": []
}
```

### response

```json
201 Created

{
	"pk": 11,
	"title": "Favorite Band",
	"question": "What is your favorite band?",
	"created": "2022-04-09T16:58:51.359484-05:00",
	"user": "admin",
	"favorited": []
}

```



<!-------------------------- Create Answer ------------------------------>

 ## Create A New Answer

### request

User must be logged in order to create a answer.

Required Fields: answer, question

```
POST /answer/
```

```json
{
  "answer": "Nickleback",
  "question": 6,
  "favorited": [],
  "accepted": false
}
```

### response

```json
201 Created

{
	"pk": 6,
	"answer": "Nickleback",
	"created": "2022-04-09T18:10:03.447584-05:00",
	"question": 6,
	"user": "admin",
	"favorited": [],
	"accepted": false
}

```



<!-------------------------- List Questions ------------------------------>


## List All Questions

Does not require authentication.

### request

```
GET /questions/
```

### response

```json
[
  {
      "pk": 1,
      "title": "Color of the Sky",
      "question": "What is the color of the sky?",
      "created": "2022-04-08T02:43:28.460825-05:00",
      "user": "testuser",
      "favorited": []
  },
]
```

<!-------------------------- List All User Answers ------------------------------>


## List All User's Answers

Requires a user to be registered and logged in.

### request

```
GET /answers/
```

### response

```json
[
	{
		"pk": 1,
		"answer": "Round",
		"created": "2022-04-07T03:41:46.600077-05:00",
		"question": 2,
		"user": "admin",
		"favorited": [],
		"accepted": false
	},
	{
		"pk": 5,
		"answer": "Pickle",
		"created": "2022-04-09T18:00:10.900412-05:00",
		"question": 2,
		"user": "admin",
		"favorited": [
			2,
			3,
			1
		],
		"accepted": false
	}
]
```


<!-------------------------- Register ------------------------------>

 ## Register a new user

### request

Username and password are required.

```json
POST auth/users

{
  "username": "admin",
  "password": "admin"
}
```

### response

```json
201 Created

{
  "email": "",
  "username": "admin",
  "id": 3
}

```

<!-------------------------- LOGIN ------------------------------>
## Log In

### request

```
POST auth/token/login
```

```json
{
  "username": "admin",
  "password": "admin"
}
```

### response

```json
200 OK
400 Bad Request

{
  "auth_token": "c312049c7f034a3d1b52eabc2040b46e094ff34c"
}
``` 



<!-------------------------- LOGOUT ------------------------------>
## Log Out 

### request

```
POST auth/token/logout
```

### response

```txt
204 No Content
```






<!--------------------------- Template ------------------------------>

## Header

### request

User must be logged in 

Required Fields:

```txt
POST 
```

```json

```

### response

```txt
200 Message
```

```json


```


