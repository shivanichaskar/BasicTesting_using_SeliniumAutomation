Feature: Verifying registration functionality

    @Sanity
    Scenario: Registration with valid data
        Given User is on Registration page
        When User enters username
        And User enters email
        And User enters password
        And User clicks on Signup button
        Then User should be registered successfully

    @Sanity @Smoke
    Scenario: Registration with duplicate username
        Given User is on Registration page
        When User enters duplicate username
        And User enters email
        And User enters password
        And User clicks on Signup button
        Then User should be registered successfully

    @abcd
    Scenario: Registration with duplicate username
        Given User is on Registration page
        When User enters duplicate username
        And User enters email
        And User enters password
        And User clicks on Signup button
        Then User should be registered successfully
