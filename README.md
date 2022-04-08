# Questionbox API

This application is an API built with Django REST Framework (DRF) that lets users post questions and answers that they are interested in.
All requests, except registration and log in, will *eventually* require authentication

### Required Headers

Requests to endpoints requiring authentication should set the `Authorization` header to `Token <token>`, where `<token>` is the token received in the login response.

POST requests with a body should set the `Content-Type` header to `application/json`.


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

### Base URL
```shell
https://questionbox-rocket.herokuapp.com/
```

### Endpoints

|  Method  |  URL                     |  Description                                              |  Deployed  |  Notes                              |
| -------- | ------------------------ | --------------------------------------------------------- | ---------- | ----------------------------------- |
|  POST    |  /question/              |  create a new question                                    |            |                                     |
|  GET     |  /question/:Q_id/        |  returns a question with all the answers answers          |            |  slug/pk later?                     |
|  PATCH   |  /question/:Q_id/        |  edit an existing question                                |            |                                     |
|  DELETE  |  /question/:Q_id/        |  edit an existing question                                |            |                                     |
|  POST    |  /question/:Q_id/answer  |  create a new answer to a question                        |            |                                     |
|  DELETE  |  /question/:Q_id/answer  |  delete an answer to a question                           |            |                                     |
|  GET     |  /questions/             |  get a list of all questions                              |  Yes       |                                     |
|  GET     |  /questions/:user_id/    |  get a list of all questions the user has posted          |            |  slug/pk later?                     |
|  GET     |  /answers/               |  return answers a user has given and question they're to  |  Yes       |  currently returning all questions  |
|  GET     |  /answer/:A_id           |  return details about an individual answer                |            |                                     |
|  POST    |  /answer/:A_id           |  change details about an individual answer                |            |                                     |
|  DELETE  |  /answer/:A_id           |  delete details about an individual answer                |            |                                     |
|  POST    |  /favorite/:Q_id         |  favorite a question                                      |            |                                     |
|  POST    |  /favorite/:A_id         |  favorite a answer                                        |            |                                     |
|  DELETE  |  /favorite/:Q_id         |  un-favorite a question                                   |            |                                     |
|  DELETE  |  /favorite/:A_id         |  un-favorite a answer                                     |            |                                     |
|  GET     |  /favorites/             |  retrieve all favorites                                   |            |                                     |
|  GET     |  /favorite/questions     |  retrieve all favorited questions                         |            |                                     |
|  GET     |  /favorite/answers       |  retrieve all favorited answers                           |            |                                     |


## List all Questions

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
      "user": 2,
      "favorited": []
  },
]
```

## List all Answers

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
      "user": 2,
      "favorited": [],
      "accepted": true
  },
]
```











<!-- ## Register a new user

### request

Username and password are required.

```
POST api/auth/users

{
  "username": "baby_yoda",
  "password": "grogu"
}
```

### response

```
201 Created

{
  "email": "",
  "username": "baby_yoda",
  "id": 6
}

```

## Log In

### request

```
POST auth/login

{
  "username": "admin",
  "password": "admin"
}
```

### response

```json
{
  "auth_token": "c312049c7f034a3d1b52eabc2040b46e094ff34c"
}
``` -->