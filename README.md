# it_solution_test

## Description 

This test task is a web application built on FastAPI, using MongoDB for data storage, Redis for caching, Nginx as a proxy server, and a Telegram bot based on aiogram.

## Tech Stack

+ **FastAPI** - web framework for creating APIs
+ **MongoDB** - database
+ **Redis** - data caching
+ **Nginx** - proxy server
+ **aiogram**  - library for Telegram bot
+ **Docker/Docker Compose** - containerization

## Application

+ **Api**
    - Acceased http://localhost:8000
    - Endpoint:
        * **GET** `/api/v1/messages/` : get all messages
        * **POST** `/api/v1/message/` : send new message
+ **Telegram bot**
    - Create telegram bot `@BotFather`
    - Use the commands:
        * `/get` - get all messages
        * `/add <message>` - send new message

## Installation

1) Clone the repository 
    ```bush
    git clone https://github.com/SuvorovJenya/it_solution_test.git
    ```
2) Add bot's token to .env file 
3) Build project
    ```bush
    docker-compose up --build
    ```