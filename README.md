# Library-management-2022
This project is a backend project which I have created required api with CRUD functionality using *Django* web frame work and also based on the task given.

>Note: This project is also hosted online. Incase if you experience some issue while starting the local server or got some errors means use this link [library-management-2022]("https://library-management-2022.herokuapp.com") to test the api.

This app contains two database model each have same CRUD functionality.
```
    model=Book
    model=User
```
## API
>### BASE_URL= https://localhost or https://library-management-2022.herokuapp.com
### Paths
* #### Book
     BASE_URL/api/book/ 
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
    }
    ]
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
    >### https://localhost/api/book/add/
    ```
    Method: "POST"
    Headers={
        content-type: "application/json"
    }
    body:
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
    >### https://localhost/api/book/{int:ser}/delete/
    ```
    Method: "DELETE"
    Headers: None
    ```
    ```
    ser: "book serial number"
    Example: https://localhost/api/book/1003/delete/
    Response:-
    {
        "Detail":"Book deleted successfully"
    }
    ```
    >### https://localhost/api/book/{int:ser}/update/
    ```
    Method: "PUT"
    Headers:
    {
        content-type: "application/json"
    }
    body:
    {
        "serial": 1002,
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

* #### User

    >  BASE_URL/api/user/ 
    'list/'
    '<int:reg>/'
    '<int:reg>/records/'
    'add/'
    '<int:reg>/<int:ser>/delete/'
    '<int:reg>/<int:ser>/update/'
    '<int:reg>/<int:ser>/update/return=<int:status>'
       