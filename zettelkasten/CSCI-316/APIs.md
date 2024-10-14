---
id: APIs
aliases: []
tags: []
---

# API

API stands for application programming interface that lets our programs and software
communicate and transfer data.
![[api.png]]

It shares data between applications, systems, and devices through requests and responses.

- requests are sent to API to retrieve data and return to user

We have an **API client** that can start the request to the API server.

- request can be trigged in various ways (search, button, another api)

An **API request** will typically have a few components:

- an **endpoint** which is a URL that gives access to specific resources.
- a **method** that indicates the type of operation the client/user wants to perfom.
  - GET, POST, PUT, DELETE, PATCH
- **parameters** are variables that are passed into the **endpoint**
- the **request headers** are key-value pairs that provide extra details
  - content type, authentication credentials
- a **request body** that includes data to create, update, and or delete a resource.

The API server recieves the request and handles the authentication, validation, and retrieves
or modifies the data.

API will finally return a response to the client which will contain:

1. status code
2. response header - providing additional information about server's response
3. response body - the actual data or error message

## REST API

Known as RESTful API, is a interface that is used to make data, algorithms, media, and other
digital resources through **web URLs**.

Six guiding constraints required to make an API RESTful:

1. uniformed interface (UI)
2. client-server based
   - design pattern to seperate concerns, client and server to work independently.
3. stateless
   - each request must contain all necessary information to understand and complete the request
   - server cannot take advantage of any previously stored context on the **server**
   - server cannot hold information on client state
4. caching
   - labeling resources as cacheable or not
5. layered system
   - each component cannot see beyond the immediate layer they are interacting with
