<<<<<<< HEAD
# Restful store Api
=======
# Login - Logout Api
>>>>>>> 7749412280a79bf8d17963d8feb810442b68fcbb
This api is made in flask (Python web framework).

## Required libraries
Flask
<<<<<<< HEAD
Flask-Restful (for Restful Api)S
=======
Flask-Restful (for Restful Api)
>>>>>>> 7749412280a79bf8d17963d8feb810442b68fcbb
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
