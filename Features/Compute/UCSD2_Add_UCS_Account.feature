Feature: Add Compute UCS Account in UCSD

@sanity
Scenario: Create Compute UCS Account in UCSD
          Given user should be logged in successfully
          When user click Administration Main Menu
          And user click Physical Accounts Sub Menu
          And user Navigate to the Physical Accounts Tab.
          And user Click Add Button
          And user Click ucs submit button
          And user enter Valid UCS account name
          And user enter Valid UCS Server Address
          And user enter Valid Username
          And user enter Valid Password
          And user select Transport type
          And user click ucs add button
          Then UCS Account should be added successfully





