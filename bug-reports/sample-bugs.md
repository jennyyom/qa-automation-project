# Bug Report - Login Functionality

---

## BUG_001

**Title:** Login button does not respond when fields are empty  
**Severity:** High  
**Related TC** TC_005

### Steps to Reproduce:
1. Go to the login page
2. Leave username and password empty
3. Click the login button

### Expected Result:
- Error message should be displayed

### Actual Result:
- Nothing happens when clicking login

---

## BUG_002

**Title:** Incorrect error message for invalid password  
**Severity:** Medium  
**Related TC** TC_002

### Steps to Reproduce:
1. Go to the login page
2. Enter a valid username
3. Enter an incorrect password
4. Click login

### Expected Result:
- "Invalid credentials" message

### Actual Result:
- Generic or unclear error message displayed
