# Backend Questionbox Documentation

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

| Method | URL           | Description                                    | Notes |
|--------|---------------|------------------------------------------------|-|
| POST   | /question/    | create a new question   ||
| GET    | /question/:Q_id/   | returns a question with all the answers answers                   |slug/pk later?|
| PATCH  | /question/:Q_id/   | edit an existing question   ||
| DELETE | /question/:Q_id/   | edit an existing question   ||
| POST   | /question/:Q_id/answer    | create a new answer to a question   ||
| DELETE   | /question/:Q_id/answer    | delete an answer to a question   ||
| GET    | /questions/   | get a list of all questions                    ||
| GET    | /questions/:user_id/ | get a list of all questions the user has posted |slug/pk later?|
| GET    | /answers/ | return all the answers a user has given as well as the question they were to  ||
| POST    | /favorite/:Q_id | favorite a question     ||
| POST    | /favorite/:A_id | favorite a answer     ||
| DELETE    | /favorite/:Q_id | un-favorite a question     ||
| DELETE    | /favorite/:A_id | un-favorite a answer     ||
| GET    | /favorites/ | retrieve all favorites            ||
| GET    | /favorite/questions | retrieve all favorited questions            ||
| GET    | /favorite/answers | retrieve all favorited answers            ||

<hr>

| col 1 | col 2 | col 3 |
|-|-|-|
|text|text|yes|
|text|text|yes|
|text|text|yes|
|text|text|yes|