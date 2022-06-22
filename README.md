# Api users

## How to run this project.

```sh
pip install -r requirements.txt
export FLASK_APP=app
flask run

```
## Create a database
```sh
Mysql> CREATE DATABASE NameHere
```

## Configure your database instance

- /config.py<br/>
- /instance/config.py

## Endpoints

* [Auth](#auth)
    1. [Register](#1-register)
    1. [Login](#2-login)
    1. [Refresh](#3-refresh)
    1. [Logout](#4-logout)
    1. [Logout2](#5-logout2)
* [Users](#users)
    1. [Users list](#1-users-list)
    1. [User by id](#2-user-by-id)

--------



## Auth



### 1. Register



***Endpoint:***

```bash
Method: POST
Type: RAW
URL: http://127.0.0.1:5000/api/v1/register
```



***Body:***

```js        
{
    "user_name": "Jose",
    "login": "thecaasantos",
    "password": "slc89slo",
    "user_role": 1
}
```



### 2. Login



***Endpoint:***

```bash
Method: POST
Type: RAW
URL: http://127.0.0.1:5000/api/v1/login
```



***Body:***

```js        
{
    "login": "thecaasantos",
    "password": "slc89slo"
}
```



### 3. Refresh



***Endpoint:***

```bash
Method: POST
Type: 
URL: http://127.0.0.1:5000/api/v1/refresh
```


***Headers:***

| Key | Value | Description |
| --- | ------|-------------|
| Authorization | Bearer |  |
|  | eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY1NTg5NzE0OCwianRpIjoiZmY0YjI0MTQtYjcxOC00Y2M2LWE1OWItNmZiYzExZTQyMGM2IiwidHlwZSI6InJlZnJlc2giLCJzdWIiOnsidXNlcl9yb2xlIjoxLCJ1c2VyX25hbWUiOiJKb3NlIiwiaWRfdXNlciI6MSwicGFzc3dvcmQiOiJwYmtkZjI6c2hhMjU2OjI2MDAwMCRsamtZUkFDdkZQWEpaU3BMJDA4MTgwMWUyNmZmYjJjYTFkOWI2MDlhNGMwNDgyZGU5YzM3NDUwNjU0NzAyMmQ5ODRmOTVjZTNjNmIzZTU0MDIiLCJsb2dpbiI6InRoZWNhYXNhbnRvcyJ9LCJuYmYiOjE2NTU4OTcxNDgsImV4cCI6MTY1ODQ4OTE0OH0.OcoWX_3-rM5BISgpNPmy3Ki7pfJJN7pdJzk1O0ijI5YC1cIgp114NtXQF5h5p6XyPm9X7Dv_KPG9aJDVYZbLiQ |  |



### 4. Logout



***Endpoint:***

```bash
Method: DELETE
Type: 
URL: http://127.0.0.1:5000/api/v1/logout
```


***Headers:***

| Key | Value | Description |
| --- | ------|-------------|
| Authorization | Bearer |  |
|  | eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY1NTg5NzE2OSwianRpIjoiMjYyYmMxNjQtODZkZC00N2IyLThiYjEtNzI5ZGE1YzlkYjYzIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6eyJ1c2VyX3JvbGUiOjEsInVzZXJfbmFtZSI6Ikpvc2UiLCJpZF91c2VyIjoxLCJwYXNzd29yZCI6InBia2RmMjpzaGEyNTY6MjYwMDAwJGxqa1lSQUN2RlBYSlpTcEwkMDgxODAxZTI2ZmZiMmNhMWQ5YjYwOWE0YzA0ODJkZTljMzc0NTA2NTQ3MDIyZDk4NGY5NWNlM2M2YjNlNTQwMiIsImxvZ2luIjoidGhlY2Fhc2FudG9zIn0sIm5iZiI6MTY1NTg5NzE2OSwiZXhwIjoxNjU1ODk4OTY5fQ.BQu0uTnuBIehn7L-jQ2889AJFIIHngkse9s_npmAlu6Wyo43CdLQnuC0KErYxK9XGl5aVYmJVgj-7wfbKfs1fA |  |



### 5. Logout2



***Endpoint:***

```bash
Method: DELETE
Type: 
URL: http://127.0.0.1:5000/api/v1/logout2
```


***Headers:***

| Key | Value | Description |
| --- | ------|-------------|
| Authorization | Bearer |  |
|  | eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY1NTg5NzE2OSwianRpIjoiMjYyYmMxNjQtODZkZC00N2IyLThiYjEtNzI5ZGE1YzlkYjYzIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6eyJ1c2VyX3JvbGUiOjEsInVzZXJfbmFtZSI6Ikpvc2UiLCJpZF91c2VyIjoxLCJwYXNzd29yZCI6InBia2RmMjpzaGEyNTY6MjYwMDAwJGxqa1lSQUN2RlBYSlpTcEwkMDgxODAxZTI2ZmZiMmNhMWQ5YjYwOWE0YzA0ODJkZTljMzc0NTA2NTQ3MDIyZDk4NGY5NWNlM2M2YjNlNTQwMiIsImxvZ2luIjoidGhlY2Fhc2FudG9zIn0sIm5iZiI6MTY1NTg5NzE2OSwiZXhwIjoxNjU1ODk4OTY5fQ.BQu0uTnuBIehn7L-jQ2889AJFIIHngkse9s_npmAlu6Wyo43CdLQnuC0KErYxK9XGl5aVYmJVgj-7wfbKfs1fA |  |



## Users



### 1. Users list



***Endpoint:***

```bash
Method: GET
Type: 
URL: http://127.0.0.1:5000/api/v1/users
```


***Headers:***

| Key | Value | Description |
| --- | ------|-------------|
| Authorization | Bearer |  |
|  | eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY1NTg5NzE0OCwianRpIjoiNWMxYjhlODUtMmM4Ni00ZmFlLTljMmUtMWEwMGIzNTA1MjYyIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6eyJ1c2VyX3JvbGUiOjEsInVzZXJfbmFtZSI6Ikpvc2UiLCJpZF91c2VyIjoxLCJwYXNzd29yZCI6InBia2RmMjpzaGEyNTY6MjYwMDAwJGxqa1lSQUN2RlBYSlpTcEwkMDgxODAxZTI2ZmZiMmNhMWQ5YjYwOWE0YzA0ODJkZTljMzc0NTA2NTQ3MDIyZDk4NGY5NWNlM2M2YjNlNTQwMiIsImxvZ2luIjoidGhlY2Fhc2FudG9zIn0sIm5iZiI6MTY1NTg5NzE0OCwiZXhwIjoxNjU1ODk4OTQ4fQ.ZeYjFq0dLdgoVp8EyzE4BUbP3xuirbBT4_WizQz3ZH8HYppVeMiAFnRKFql457xddYE5W95MKL57FzbX6IBWbw |  |



### 2. User by id



***Endpoint:***

```bash
Method: GET
Type: 
URL: http://127.0.0.1:5000/api/v1/users/1
```


***Headers:***

| Key | Value | Description |
| --- | ------|-------------|
| Authorization | Bearer |  |
|  | eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY1NTg5NzE0OCwianRpIjoiNWMxYjhlODUtMmM4Ni00ZmFlLTljMmUtMWEwMGIzNTA1MjYyIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6eyJ1c2VyX3JvbGUiOjEsInVzZXJfbmFtZSI6Ikpvc2UiLCJpZF91c2VyIjoxLCJwYXNzd29yZCI6InBia2RmMjpzaGEyNTY6MjYwMDAwJGxqa1lSQUN2RlBYSlpTcEwkMDgxODAxZTI2ZmZiMmNhMWQ5YjYwOWE0YzA0ODJkZTljMzc0NTA2NTQ3MDIyZDk4NGY5NWNlM2M2YjNlNTQwMiIsImxvZ2luIjoidGhlY2Fhc2FudG9zIn0sIm5iZiI6MTY1NTg5NzE0OCwiZXhwIjoxNjU1ODk4OTQ4fQ.ZeYjFq0dLdgoVp8EyzE4BUbP3xuirbBT4_WizQz3ZH8HYppVeMiAFnRKFql457xddYE5W95MKL57FzbX6IBWbw |  |



---
[Back to top](#user)









