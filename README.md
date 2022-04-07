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


### Endpoints

| Method | URL           | Description                                    | Notes |
|--------|---------------|------------------------------------------------|-|
| POST   | /question/    | create a new question   ||
| GET    | /question/:Q_id/   | returns a question with all the answers answers                   |slug/pk later?|
| PATCH  | /question/:Q_id/   | edit an existing question   ||
| DELETE | /question/:Q_id/   | edit an existing question   ||
| GET    | /questions/   | get a list of all questions                    ||
| GET    | /questions/:user_id/ | get a list of all questions the user has posted |slug/pk later?|
| GET    | /answers/ | return all the answers a user has given as well as the question they were to  ||
| GET    | /favorites/ | retrieve all favorites            ||
| GET    | /favorite/questions | retrieve all favorited questions            ||
| GET    | /favorite/answers | retrieve all favorited answers            ||
