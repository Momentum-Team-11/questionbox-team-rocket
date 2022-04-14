# Questionbox API

This application is an API built with Django REST Framework (DRF) that lets users post questions and answers that they are interested in.
All requests, except registration and log in, will require authentication

Unregistered users may see posted questions or answers but may not modify, favorite, accept or delete any without registration.

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

## Base URL
```shell
https://questionbox-rocket.herokuapp.com/
```

## API Endpoints

|  Method  |  Endpoint                                                 |  Description                            |  Deployed  |
| -------- | --------------------------------------------------------- | --------------------------------------- | ---------- |
|  POST    |  [/auth/users/](#register-a-new-user)                     |  register a new user                    |  Yes       |
|  POST    |  [/auth/token/login/](#log-in)                            |  login with existing user               |  Yes       |
|  POST    |  [/auth/token/logout/](#log-out)                          |  logout with existing user              |  Yes       |
|  GET     |  [/questions/](#list-all-questions)                       |  List all questions                     |  Yes       |
|  GET     |  [/questions/{id}](#retrieve-a-specific-question)         |  Retrieve a specific question           |  Yes       |
|  POST    |  [/questions/](#create-a-new-question)                    |  Add a new question                     |  Yes       |
|  PUT     |  [/questions/{id}](#update-an-existing-question)          |  Update an existing question            |  Yes       |
|  PATCH   |  [/questions/{id}](#update-an-existing-question)          |  Update part of an existing question    |  Yes       |
|  DELETE  |  [/questions/{id}](#delete-question)                      |  Delete an existing question            |  Yes       |
|  GET     |  [/questions/favorited/](#get-users-favorited-questions)  |  get list of users favorited questions  |  Yes       |
|  GET     |  [/questions/user/](#get-a-list-of-users-questions)       |  get list of a users questions          |  Yes       |
|  GET     |  [/answers/](#list-all-users-answers)                     |  List all answers                       |  Yes       |
|  GET     |  [/answers/{id}](#retrieve-a-specific-answer)             |  Retrieve a specific answer             |  Yes       |
|  POST    |  [/answers/](#create-a-new-answer)                        |  Add a new answer                       |  Yes       |
|  PUT     |  [/answers/{id}](#update-an-existing-answer)              |  Update an existing answer              |  Yes       |
|  PATCH   |  [/answers/{id}](#update-an-existing-answer)              |  Update part of an existing answer      |  Yes       |
|  DELETE  |  [/answers/{id}](#delete-an-existing-answer)              |  Delete an existing answer              |  Yes       |
|  GET     |  [/answers/favorited/](#list-users-favorited-answers)                                 |  get list of users favorited answers    |  Yes       |
|  GET     |  [/answers/user/](#list-all-users-answers)                |  get list of a users answers            |  Yes       |



<!-------------------------- Create Question ------------------------------>

 ## Create A New Question

[Back to Endpoints](#api-endpoints)

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

[Back to Endpoints](#api-endpoints)
 

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

[Back to Endpoints](#api-endpoints)

Does not require authentication.

### request

```
GET /questions/
```

### response

```json
[
    {
        "pk": 6,
        "title": "Favorite Band",
        "question": "What is your favorite band?",
        "user": "admin",
        "favorited": [
            "testuser2",
            "admin",
            "admin2"
        ]
    },
    ,
    {
        "pk": 2,
        "title": "True shape of the Earth",
        "question": "Is the Earth round or is it really flat?",
        "user": "admin",
        "favorited": [
            "admin"
        ]
    },
    {
        "pk": 12,
        "title": "Best Programming Language",
        "question": "What is the best programming language?",
        "user": "testuser",
        "favorited": [
            "testuser",
            "testuser2",
            "admin",
            "pickles",
            "admin2"
        ]
    },
]
```

<!-------------------------- List All User Answers ------------------------------>


## List All Users Answers

[Back to Endpoints](#api-endpoints)

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

[Back to Endpoints](#api-endpoints)

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

[Back to Endpoints](#api-endpoints)

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

[Back to Endpoints](#api-endpoints)

### request

```
POST auth/token/logout
```

### response

```txt
204 No Content
```



<!--------------------------- Get Question ------------------------------>

## Retrieve a specific question

[Back to Endpoints](#api-endpoints)

### request

User must be user or guest

```txt
GET /questions/id 
```

### response

```txt
200 Message
```

```json

{
    "pk": 6,
    "title": "Favorite Band",
    "question": "What is your favorite band?",
    "created": "2022-04-09T16:21:41.800747-05:00",
    "user": "admin",
    "favorited": [
        "testuser2",
        "admin",
        "admin2"
    ],
    "answers": [
        {
            "pk": 7,
            "question": 6,
            "answer": "Nickleback",
            "created": "2022-04-09T18:13:20.262000-05:00",
            "user": "admin",
            "favorited": [],
            "accepted": false
        },
        {
            "pk": 11,
            "question": 6,
            "answer": "ZZ Top",
            "created": "2022-04-11T00:41:55.284873-05:00",
            "user": "admin2",
            "favorited": [
                "testuser",
                "testuser2",
                "admin",
                "pickles",
                "admin2"
            ],
            "accepted": true
        },
        {
            "pk": 12,
            "question": 6,
            "answer": "Sublime",
            "created": "2022-04-11T00:49:23.728945-05:00",
            "user": "admin2",
            "favorited": [
                "pickles"
            ],
            "accepted": false
        }
    ]
}

```

<!--------------------------- Update Question ------------------------------>

## Update an existing question

[Back to Endpoints](#api-endpoints)

### request

User must be logged in 

Required Fields: question

```txt
PUT /question/id/ 
```

```json
{
    "pk": 6,
    "title": "Favorite Band",
    "question": "What is your favorite band?",
    "user": "admin",
    "favorited": [
        "testuser2",
        "admin",
        "admin2"
    ]
}
```

### response

```txt
200 Message
```

```json
{
    "pk": 6,
    "title": "Favorite Band",
    "question": "What is your favorite band?",
    "user": "admin",
    "favorited": [
        "testuser2",
        "admin",
        "admin2"
    ]
}

```


<!--------------------------- Delete Question ------------------------------>

## Delete Question

[Back to Endpoints](#api-endpoints)

### request

User must be logged in 

Required Fields: question

```txt
DELETE /question/id/
```

### response

```txt
204 No Content
```



<!--------------------------- Get Favorited ------------------------------>

## Get-users-favorited-questions

[Back to Endpoints](#api-endpoints)

### request

User must be logged in 


```txt
GET /questions/favorited/
```

### response

```txt
200 Message
```

```json
[
    {
        "pk": 12,
        "title": "Best Programming Language",
        "question": "What is the best programming language?",
        "user": "testuser",
        "favorited": [
            "testuser",
            "testuser2",
            "admin",
            "pickles",
            "admin2"
        ]
    },
    {
        "pk": 20,
        "title": "GOAT",
        "question": "Who is the GOAT?",
        "user": "admin",
        "favorited": [
            "admin2"
        ]
    },
    {
        "pk": 11,
        "title": "Favorite Band",
        "question": "What is your favorite band?",
        "user": "admin",
        "favorited": [
            "admin2"
        ]
    },
    {
        "pk": 6,
        "title": "Favorite Band",
        "question": "What is your favorite band?",
        "user": "admin",
        "favorited": [
            "testuser2",
            "admin",
            "admin2"
        ]
    }
]
```



<!--------------------------- User Questions List ------------------------------>

## Get a list of users questions

[Back to Endpoints](#api-endpoints)

### request

User must be logged in 

```txt
GET /questions/user/ 
```

### response

```txt
200 Message
```

```json
[
    {
        "pk": 2,
        "title": "True shape of the Earth",
        "question": "Is the Earth round or is it really flat?",
        "user": "admin",
        "favorited": [
            "admin"
        ]
    },
    {
        "pk": 12,
        "title": "Best Programming Language",
        "question": "What is the best programming language?",
        "user": "testuser",
        "favorited": [
            "testuser",
            "testuser2",
            "admin",
            "pickles",
            "admin2"
        ]
    },
    {
        "pk": 6,
        "title": "Favorite Band",
        "question": "What is your favorite band?",
        "user": "admin",
        "favorited": [
            "testuser2",
            "admin",
            "admin2"
        ]
    }
]

```




<!--------------------------- Get Answer ------------------------------>

## Retrieve a specific answer

[Back to Endpoints](#api-endpoints)

### request

```txt
GET /answers/id
```

### response

```txt
200 Message
```

```json
{
    "pk": 5,
    "question": 2,
    "answer": "Pickle",
    "created": "2022-04-09T18:00:10.900412-05:00",
    "user": "admin",
    "favorited": [
        "testuser",
        "testuser2",
        "admin"
    ],
    "accepted": false
}

```



<!--------------------------- Change Answer ------------------------------>

## Update an existing answer

[Back to Endpoints](#api-endpoints)

### request

User must be logged in 

Required Fields: Question, answer

```txt
PUT /answers/id 
PATCH /answers/id 
```

```json
{
    "pk": 5,
    "question": 2,
    "answer": "Pickle",
    "created": "2022-04-09T18:00:10.900412-05:00",
    "user": "admin",
    "favorited": [
        "testuser",
        "testuser2",
        "admin"
    ],
    "accepted": false
}
```

### response

```txt
200 Message
```

```json
{
    "pk": 5,
    "question": 2,
    "answer": "Pickle",
    "created": "2022-04-09T18:00:10.900412-05:00",
    "user": "admin",
    "favorited": [
        "testuser",
        "testuser2",
        "admin"
    ],
    "accepted": false
}
```



<!--------------------------- Delete Answer ------------------------------>

## Delete an existing answer

[Back to Endpoints](#api-endpoints)

### request

User must be logged in 

Required Fields:

```txt
DELETE /answers/id/ 
```

### response

```txt
204 No content
```



<!--------------------------- Users Favorited Answers ------------------------------>

## List users favorited answers

[Back to Endpoints](#api-endpoints)

### request

User must be logged in 


```txt
GET /answers/favorited/
```

### response

```txt
200 Message
```

```json
[
    {
        "pk": 11,
        "question": 6,
        "answer": "ZZ Top",
        "created": "2022-04-11T00:41:55.284873-05:00",
        "user": "admin2",
        "favorited": [
            "testuser",
            "testuser2",
            "admin",
            "pickles",
            "admin2"
        ],
        "accepted": true
    }
]
```




<!--------------------------- Template ------------------------------>

## Header

[Back to Endpoints](#api-endpoints)

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


