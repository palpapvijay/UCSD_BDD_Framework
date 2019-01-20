Feature: Verify UCSD Login Features
         Feature Listfile (List of feature filenames/directories)

Background:
          Given user is on UCSD Login Page

@sanity
Scenario: Login with Invalid UCSD Credentials
          When user enters Invalid UCSD username
          And user enters valid UCSD password
          And user click submit button
          Then UCSD should provide valid error message.

@sanity
Scenario: Login with Valid UCSD Credentials
          When user enters valid UCSD username
          And user enters valid UCSD password
          And user click submit button
          Then user should be logged in successfully







