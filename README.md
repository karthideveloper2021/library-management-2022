# Library-management-2022
This is a backend project in which I have created the required api with CRUD functionality using *Django* web frame work and also based on the task given.

>Note: This project is also hosted online. Incase if you experience some issue while starting the local server or got some errors means use this link https://library-management-2022.herokuapp.com to test the api.

This app contains two database model each have same CRUD functionality.
```
    model=Book
    model=User
```
It also contain another model named [Settings]("library/settings.py") which is used to store some default value like user preference. In this case I used it to set book return period.

## INITIAL SETUP

* create a virtual environment and activate it.
```
python -m venv virtual
```
* Install the packages mentioned in requirements.txt :-
```
pip install -r requirements.txt
```
create a new directory `library` and put the code inside this directory.

so the path files will be look like...
```
virtual-
library-
    book-
    dashboard-
    library-
    user-
    staticfiles-
    manage.py
    requirements.txt
    .gitignore
    Procfile
    README.md
```



## HOW TO STARTSERVER
This project was made on DJANAGO web framework. Refer the documentation if you have queries.

Before starting the local server, you have to setup the database first.
By default DJANGO has come with sqlite database and it will be configured in `settings.py` file like
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```
If you want to use other database like postgresql, then install the required packages and configure them in `library/settings.py`

To use postgresql, you need to install the package which you may already installed as it is mentioned in `requirements.txt`.
If not type this command in terminal
```
pip install psycopg2
```
After that configure them properly in `library/settings.py`
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '', #name of database
        'USER':'', #username
        'HOST':'', #host
        'PASSWORD': '' #password
    }
}
```

After that type this command to migrate the basic data & our app model data to database.

> python manage.py migrate

To start the local server, type this & your are ready to test the api.

> python manage.py runserver

## API

First thing we have to set the default value for `book return period`, as already mentioned.
> ### http://localhost/api/settings/init/
> send this request with default method as `GET`.

To update the value in future,
>### http://localhost/api/settings/update/{int:setID}/
`"setID":2201 ==> book return period`
```
Method: "PUT"
Headers:
{
    content-type:"application/json"
}
body:
{
    "Name":"book return period",
    "value":"15"
}
```
To view all the settings default parameters incase if more parameters are added in future,
> ### http://localhost/api/settings/list/
```
Method: "GET"
Headers: None
```
```
Responses:-
{
    "setID":2201,
    "Name":"book return period",
    "value":"15"
}
```

>### BASE_URL= http://localhost or https://library-management-2022.herokuapp.com
### Paths
* #### Book
     BASE_URL/api/book/ 
     >### https://localhost/api/book/add/
    ```
    Method: "POST"
    Headers={
        content-type: "application/json"
    }
    ```
    body:
    ```
        {
        "serial": 1001,
        "Name": "python",
        "author": "master",
        "date_of_pub": "2002-02-02",
        "description": "programming language",
        "bookStock": 100
    }
    ```
    ```
    {
        "serial": 1002,
        "Name": "c++",
        "author": "fwefe",
        "date_of_pub": "1990-02-02",
        "description": "programming language oops",
        "bookStock": 250
    }
    ```
    ```
    {
        "serial": 1003,
        "Name": "javascript",
        "author": "lpkwjeefg",
        "date_of_pub": "1990-03-12",
        "description": "new edition",
        "bookStock": 190
    }
    ```
    ```
    Response:-
    {
        "Detail":"Book added successfully.."
    }
    ```
    >### https://localhost/api/book/list/
    ```
    Method: "GET"
    Headers: None
    ```
    ```
    Response:-
    [
    {
        "serial": 1001,
        "Name": "python",
        "author": "master",
        "date_of_pub": "2002-02-02",
        "description": "programming language",
        "no_of_times_borrowed": 2,
        "bookStock": 100,
        "bookIssued": 1,
        "bookAvailable": 99,
        "created": "2022-01-14T16:17:08.682759",
        "modified": "2022-01-15T10:53:32.747952"
    },
    {
        "serial": 1002,
        "Name": "c++",
        "author": "fwefe",
        "date_of_pub": "1990-02-02",
        "description": "programming language oops",
        "no_of_times_borrowed": 0,
        "bookStock": 250,
        "bookIssued": 0,
        "bookAvailable": 250,
        "created": "2022-01-15T11:02:19.893959",
        "modified": "2022-01-15T11:02:19.893987"
    },
    {
        "serial": 1003,
        "Name": "javascript",
        "author": "lpkwjeefg",
        "date_of_pub": "1990-03-12",
        "description": "new edition",
        "no_of_times_borrowed": 0,
        "bookStock": 190,
        "bookIssued": 0,
        "bookAvailable": 190,
        "created": "2022-01-15T22:00:16.203403",
        "modified": "2022-01-15T22:00:16.203403"
    }
    ]
    ```
    
    >### https://localhost/api/book/{int:ser}/
    ```
    Method: "GET"
    Headers: None
    ```
    ```
    https://localhost/api/book/1002/
    Response:-
    {
        "serial": 1002,
        "Name": "c++",
        "author": "fwefe",
        "date_of_pub": "1990-02-02",
        "description": "programming language oops",
        "no_of_times_borrowed": 0,
        "bookStock": 250,
        "bookIssued": 0,
        "bookAvailable": 250,
        "created": "2022-01-15T11:02:19.893959",
        "modified": "2022-01-15T11:02:19.893987"
    }
    ```
    
    >### https://localhost/api/book/{int:serial}/delete/
    ser: 1003 //book serial number.

     `https://localhost/api/book/1003/delete/`
    ```
    Method: "DELETE"
    Headers: None
    ```
    ```
    Response:-
    {
        "Detail":"Book deleted successfully"
    }
    ```
    >### https://localhost/api/book/{int:serial}/update/
    `https://localhost/api/book/1002/update/`
    ```
    Method: "PUT"
    Headers:
    {
        content-type: "application/json"
    }
    body:
    {
        "Name": "C",
        "author": "fwefe",
        "date_of_pub": "1990-02-02",
        "description": "programming language",
        "bookStock": 250
    }
    ```
    ```
    Response:-
    {
        "Detail":"Book updated successfully.."
    }
    ```

    >### https://localhost/api/book/list/issued={int:status}/
    ```
    Method: "GET"
    Headers: None
    ```
    status=1 or 0 
    Examples:
    ```
    ..../list/issued=0/
    Response:-
    {
        "serial": 1002,
        "Name": "c++",
        "bookStock": 250,
        "bookIssued": 0,
        "bookAvailable": 250
    }
    ```
    ```        
    ..../list/issued=1/
    Response:-
    { 
        "serial": 1001,
        "Name": "python",
        "bookStock": 100,
        "bookIssued": 1,
        "bookAvailable": 99
    }
    ```


* #### User

    BASE_URL/api/user/ 
    >### https://localhost/api/user/add/
    ```
    Method: "POST"
    Headers: 
    {
        content-type:"application/json"
    }
    ```
    body:
    ```
    {
        "Name": "hulk",
        "regNo": 1201,
        "year": 2,
        "bookNo": 1001
    }
    ```
    ```
    {
        "Name": "tony",
        "regNo": 1202,
        "year": 4,
        "bookNo": 1002
    }
    ```
    ```
    Response:-
    {
        "Detail": "Book issued successfully.."
    }
    ```
    >### https://localhost/api/user/list/
    ```
    Method: "GET"
    Headers: None
    ```
    ```
    Responses:-
    [
        {
            "id": 8,
            "Name": "hulk",
            "regNo": 1201,
            "year": 2,
            "bookNo": 1001,
            "bookName": "python",
            "borrowDate": "2022-01-15T22:12:36.605540",
            "returnDate": "2022-01-30T23:59:59.999999",
            "returnStatus": false
        },
        {
            "id": 9,
            "Name": "tony",
            "regNo": 1202,
            "year": 4,
            "bookNo": 1002,
            "bookName": "C",
            "borrowDate": "2022-01-15T22:13:59.424049",
            "returnDate": "2022-01-30T23:59:59.999999",
            "returnStatus": false
        }
    ]
    ```

    >### https://localhost/api/user/{int:regNo}/

    This api will return details about the list of book in which the user hasn't returned. `returnStatus=False` only

    `http://127.0.0.1:8000/api/user/1201/`
    ```
    Method: "GET"
    Headers: None
    ```
    ```
    Response:-
    {
        "id": 8,
        "Name": "hulk",
        "regNo": 1201,
        "year": 2,
        "bookNo": 1001,
        "bookName": "python",
        "borrowDate": "2022-01-15T22:12:36.605540",
        "returnDate": "2022-01-30T23:59:59.999999",
        "returnStatus": false
    }

    ```
    >### https://localhost/api/user/{int:regNo}/records/
    This api will return all kinds of records that user made in the library that contains both `returnStatus = False & True`
    ```
    Method: "GET"
    Headers: None
    ```
    ```
    Response:-
    [
        {
            "id": 9,
            "Name": "tony",
            "regNo": 1202,
            "year": 4,
            "bookNo": 1002,
            "bookName": "C",
            "borrowDate": "2022-01-15T22:13:59.424049",
            "returnDate": "2022-01-30T23:59:59.999999",
            "returnStatus": false
        },
        {
            "id": 10,
            "Name": "tony",
            "regNo": 1202,
            "year": 4,
            "bookNo": 1001,
            "bookName": "python",
            "borrowDate": "2022-01-15T22:30:44.755220",
            "returnDate": "2022-01-30T23:59:59.999999",
            "returnStatus": true
        }
    ]
    ```
    
    >### https://localhost/api/user/{int:id}/delete/
    This api will delete a record using id.

    `http://127.0.0.1:8000/api/user/10/delete/`
    ```
    Method: "DELETE"
    Headers: None
    ```
    ```
    Response:-
    {
        "Detail": "Deleted successfully..."
    }
    ```
     >### https://localhost/api/user/{int:id}/update/
     As of now this api allow you to change any data of a particular record. This thing will be updated in future based on the instructions given.
    ```
    Method: "PUT"
    Headers: 
    {
        content-type:"application/json"
    }
    body:
    {
        "Name": "tony stark",
        "regNo": 1202,
        "year": 3,
        "bookNo": 1002,
        "returnDate": "2022-01-31T23:59:59.999999",
        "returnStatus": false
    }
    ```
    ```
    Response:-
    {
        "Detail": "Updated successfuly.."
    }
    ```
    >### https://localhost/api/user/{int:id}/update/return={int:status}

    * If status is given as 1, book will be considered as returned. If it is given as 0, book will be considered as renewed. 
    ```
    Method: "POST"
    Headers: None
    body:
    ```
    ```
    Response:-
    return=0 is given for renewal of the book.
    http://127.0.0.1:8000/api/user/11/update/return=0
    {
        "Detail": "Book renewed successfully"
    }
    return=1 is given for returning the book.
    http://127.0.0.1:8000/api/user/11/update/return=1
    {
        "Detail": "Book returned successfully.."
    }
    ```
    > whenever you renew a book, app will take care of extending the date by taking the default value from `Settings` model which has `book return period`  [settings code =>2201]. If you want to extend the date manaully, you can use the `update` api.
    