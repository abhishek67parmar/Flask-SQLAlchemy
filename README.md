# Login - Logout Api
This api is made in flask (Python web framework).

## Required libraries
Flask
Flask-Restful (for Restful Api)
Flask-JWT (for authorization purpose)
Flask-SQLAlchemy (To work with database using ORM)
passlib (To make password more secure)

# Api Endpoints

#### 1. /logon (Post)
  - for user User Registration
  - send username and password as json data

#### 2. /auth (Post)
  - default jwt endpoint for authorization
  - send username and password as json data

#### 3. /store/<string:name>
  -  **get**: gives store detail
  -  **post**: send store name to add
  -  **delete**: delete given store

#### 4. /item/<string:name>
  -  **get**: gives items detail add Authorization (JWT refresh_token) in request header
  -  **post**: send price and store id to add
  -  **push**: send price and store id to update
  -  **delete**: delete given item

#### 5. /items (get)
  - returns all items

#### 6. /stores (get)
  - returns all stores
