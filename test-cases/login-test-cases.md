# Login Test Cases

## TC_001 - Valid Login
Preconditions:
- User is registered

Steps:
1. Go to the login page
2. Enter a valid username
3. Enter a valid password
4. Click the login button

Expected Result:
- User is successfully logged in

---

## TC_002 - Invalid Password
Preconditions:
- User is registered

Steps:
1. Go to the login page
2. Enter a valid username
3. Enter an invalid password
4. Click the login button

Expected Result:
- Error message is displayed
- User is not logged in

---

## TC_003 - Empty Username
Preconditions:
- Username field is empty

Steps:
1. Go to the login page
2. Enter a valid password
3. Leave username empty
4. Click the login button

Expected Result:
- "Username is required" message is displayed

---

## TC_004 - Empty Password
Preconditions:
- Password field is empty

Steps:
1. Go to the login page
2. Enter a valid username
3. Leave password empty
4. Click the login button

Expected Result:
- "Password is required" message is displayed

---

## TC_005 - Both Fields Empty
Preconditions:
- Both username and password fields are empty

Steps:
1. Go to the login page
2. Leave all fields empty
3. Click the login button

Expected Result:
- Validation error messages are displayed
