# Overview

This API was developed using the Django framework, using the PostgreSQL database. This Rest API is a CRUD solution for the URL context

## Functionalities

### List URLs

`GET /api/urls/`

`GET /api/urls/{id}/`

### Add a URL

`POST /api/urls/`

### Edit a URL

`PUT /api/urls/{id}/`

### Delete a URL

`DELETE /api/urls/{id}/`

## Installation Instructions

### Requirements

To run the Django API you need to have Docker and Docker Compose installed

### `git clone https://github.com/devjunioralves/esx-challenge-backend.git`

### `cd esx-challenge-backend`

### `cp .env.example .env`

### `docker compose up --build`

## Future improvements

### 1 - Automated Testing

#### Create unit and integration tests for all endpoints and use cases.

### 2 - API Documentation

#### Develop API documentation.

### 3 - Error Handling

#### Implement custom error handling for better information and standardization

### 4 - Additional validations in the serializer

#### Include checks for duplicity before creating a new URL.

#### Add validations to ensure that the URLs are valid
