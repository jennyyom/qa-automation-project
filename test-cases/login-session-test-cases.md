TC_006 - Remember Me Checkbox
Preconditions:
* User is registered

Test Data:
* Username: tomsmith
* Password: Password!
* Remember Me: Checked

Steps:
1. Go to the login page
2. Enter a valid username and password
3. Check the "Remember Me" checkbox
4. Click the login button
5. Close the browser and reopen the login page

Expected Result:
* Username field is pre-filled on return
* User does not need to log in again

---

TC_007 - Access After Logout
Preconditions:
* User is logged in

Test Data:
* Username: tomsmith
* Password: Password!

Steps:
1. Log in with valid credentials
2. Click the logout button
3. Click the browser back button

Expected Result:
* User is redirected to the login page
* Protected page is not accessible after logout

---

TC_008 - Re-login After Session Timeout
Preconditions:
* User is logged in
* Session timeout is configured

Test Data:
* Username: tomsmith
* Password: Password!

Steps:
1. Log in with valid credentials
2. Leave the session idle until timeout
3. Attempt to perform an action or navigate

Expected Result:
* User is redirected to the login page
* Session expired message is displayed

---

TC_009 - Back Button Behavior After Login
Preconditions:
* User is logged in

Test Data:
* Username: tomsmith
* Password: Password!

Steps:
1. Log in with valid credentials
2. Land on the dashboard/home page
3. Click the browser back button

Expected Result:
* User is not taken back to the login page
* User remains on the authenticated page



