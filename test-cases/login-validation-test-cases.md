# Login Validation Test Cases

## TC_010 - Invalid Username

Preconditions:
- User is registered

Test Data:
- Username: invalidUser
- Password: Password!

Steps:
1. Go to the login page
2. Enter an invalid username
3. Enter a valid password
4. Click the login button

Expected Result:
- Error message is displayed
- User is not logged in


## TC_011 - Invalid Username and Password

Preconditions:
- User credentials are invalid

Test Data:
- Username: invalidUser
- Password: wrongPassword123

Steps:
1. Go to the login page
2. Enter an invalid username
3. Enter an invalid password
4. Click the login button

Expected Result:
- Error message is displayed
- User is not logged in


## TC_012 - Username With Leading Spaces

Preconditions:
- User is registered

Test Data:
- Username: tomsmith
- Password: Password!

Steps:
1. Go to the login page
2. Enter a username with leading spaces
3. Enter a valid password
4. Click the login button

Expected Result:
- Input validation is handled correctly
- Login is rejected, or spaces are trimmed


## TC_013 - Password With Trailing Spaces

Preconditions:
- User is registered

Test Data:
- Username: tomsmith
- Password: "Password! "

Steps:
1. Go to the login page
2. Enter a valid username
3. Enter a password with trailing spaces
4. Click the login button

Expected Result:
- Authentication fails
- Error message is displayed


## TC_014 - Very Long Username

Preconditions:
- The login page is accessible

Test Data:
- Username: 256+ characters
- Password: Password!

Steps:
1. Go to the login page
2. Enter a username longer than the allowed limit
3. Enter a valid password
4. Click the login button

Expected Result:
- Validation message is displayed
- Login is not allowed


## TC_015 - SQL Injection Attempt

Preconditions:
- The login page is accessible

Test Data:
- Username: ' OR '1'='1
- Password: ' OR '1'='1

Steps:
1. Go to the login page
2. Enter SQL injection strings in the username and password fields
3. Click the login button

Expected Result:
- Login attempt is blocked
- No authentication bypass occurs
- Error message is displayed
