Feature: Login Functionality

    Scenario Outline: Login with multiple users
        Given user is on the login page
        When user enters "<username>" and "<password>"
        And user clicks on login button
        Then user should see "<result>"

        Examples:
            | username       | password     | result  |
            | standard_user  | secret_sauce | success |
            | locked_out_user| secret_sauce | Failure |