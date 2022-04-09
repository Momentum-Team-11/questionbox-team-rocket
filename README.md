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
  - [List All Questions](#list-all-questions)
    - [request](#request)
    - [response](#response)
  - [List All Answers](#list-all-answers)
    - [request](#request-1)
    - [response](#response-1)
  - [Register a new user](#register-a-new-user)
    - [request](#request-2)
    - [response](#response-2)
  - [Log In](#log-in)
    - [request](#request-3)
    - [response](#response-3)
  - [Create A New Question](#create-a-new-question)
    - [request](#request-4)
    - [response](#response-4)


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

### Endpoints

|  Method  |  URL                     |  Description                                              |  Deployed  |  Notes                              |Response|
| -------- | ------------------------ | --------------------------------------------------------- | ---------- | ----------------------------------- |-|
|  POST    |  /question/              |  create a new question                                    |            |                                     |just something to verify it went through. Header maybe?|
|  GET     |  /question/:Q_id/        |  returns a question with all the answers answers          |            |  slug/pk later?                     ||
|  DELETE  |  /question/:Q_id/        |  edit an existing question                                |            |                                     |response feedback|
|  POST    |  /question/:Q_id/answer  |  create a new answer to a question                        |            |                                     ||
|  GET     |  /questions/             |  get a list of all questions                              |  Yes       |                                     ||
|  GET     |  /questions/:user_slug/    |  get a list of all questions the user has posted          |            |  slugify ||
|  GET     |  /answers/               |  return a list of all answers in app|  Yes       |  can remove later  ||
|  GET     |  /answers/:user_slug               |  return answers a user has given and question they're to  |  |  currently returning all questions  |adam needs: question title, question id as well as rest of answer info|
|  POST    |  /answer/:A_id           |  change details about an individual answer                |            |                                     ||
|  DELETE  |  /answer/:A_id           |  delete details about an individual answer                |            |                                     ||
|  POST    |  /favorite/:Q_id         |  favorite a question                                      |            |                                     ||
|  POST    |  /favorite/:A_id         |  favorite a answer                                        |            |                                     ||
|  DELETE  |  /favorite/:Q_id         |  un-favorite a question                                   |            |                                     ||
|  DELETE  |  /favorite/:A_id         |  un-favorite a answer                                     |            |                                     ||
|  GET     |  /favorites/             |  retrieve all favorites                                   |            |                                     |see samplejson.json for specific notes|
|  GET     |  /favorite/questions     |  retrieve all favorited questions                         |            |                                     ||
|  GET     |  /favorite/answers       |  retrieve all favorited answers                           |            |                                     ||







<!-------------------------- List Questions ------------------------------>


## List All Questions

Does not require authentication.

### request

```txt
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

<!-------------------------- List All Answers ------------------------------>


## List All Answers

Does not require authentication.

### request

```txt
GET /answers/
```

### response

```json
[
  {
      "pk": 2,
      "answer": "Blue",
      "created": "2022-04-08T04:11:44.397450-05:00",
      "question": 1,
      "user": "testuser",
      "favorited": [],
      "accepted": true
  }
]
```


<!-------------------------- Register ------------------------------>

 ## Register a new user

### request

Username and password are required.

```
POST api/auth/users

{
  "username": "admin",
  "password": "admin"
}
```

### response

```
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
POST auth/login
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
  "email": "",
  "username": "admin",
  "id": 3
}

```