# Test Plan - Login Functionality

## 1. Introduction
This test plan defines the scope, approach, resources, and schedule for testing the application's Login functionality.

---

## 2. Objective
The objective of this testing is to verify that the login feature works correctly under valid and invalid input conditions.

---

## 3. Scope

### In Scope:
- Valid login
- Invalid login
- Empty username
- Empty password
- Both fields are empty
- Error message validation

### Out of Scope:
- Password reset functionality
- User registration feature
- Performance/load testing

---

## 4. Test Approach
Testing will include:
- Manual testing for test case validation
- Functional testing of login workflow
- Negative testing for invalid inputs
- Basic automation using JUnit

---

## 5. Test Environment
- Operating System: Windows / MacOS
- Browser: Chrome (latest version)
- Tools: GitHub, JUnit
- Environment: Local + Docker-based setup

---

## 6. Test Deliverables
- Test cases
- Test execution results
- Bug reports
- Automation scripts

---

## 7. Risks
- UI changes may affect test cases
- Environment inconsistency without Docker setup
- Limited test data

---

## 8. Entry Criteria
- Application is deployed and accessible
- Test environment is ready

---

## 9. Exit Criteria
- All test cases executed
- No critical defects remaining
- Test results documented
