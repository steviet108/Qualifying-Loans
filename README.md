# *Qualifying-Loans-App*

![Fintech image from Getty stock images](Desktop/Qualifying-Loans/fintech-image.png?raw=true "Title")

This Loan Qualifying Application uses the CLI or Command Line Interface to match applicants with qualifying loans. It is an example of modular code that has functions in separate files as to work more efficiently and also to enable easier maintenance.
The user downloads the app from the GitHub Repository,(see below) and runs the app in there terminal, and answers a few questions regarding there credit score, monthly debt, monthly income, home value and the desired loan amount. The application takes this info and calculates the debt to income ratio and the loan to value ratio and uses these with a few other factors to present a list of qualifying loans. The user then has the option to save this list to a new csv file, or opt out of saving to a file, and in the event the user does not qualify for a loan, the application lets the user know that as well.

---
##  Technologies 

This Application uses Python 3.7 with the following packages:

*fire* - For the command line interface.

*questionary* - For interactive user prompts and dialogs.

---
##  Installation 

Before running this application please install the following dependencies.

``` pip install fire ```

``` pip install questionary ```

---
##  Usage 

To use this Loan Qualifying Application clone the repository from Github and run app.py in the command line or terminal. Download Repository here.
[github](https://github.com/steviet108/Qualifying-Loans.git)


### Here is an example of the user interaction with the CLI : ###
---
```(dev) stephenthomas@steviet108eth-MacBook-Pro loan_qualifier_app % python3 app.py
? What's your credit score? 850
? What's your current amount of monthly debt? 800
? What's your total monthly income? 8000
? What's your desired loan amount? 250000
? What's your home value? 750000
The monthly debt to income ratio is 0.10
The loan to value ratio is 0.33.
Found 18 qualifying loans
? Do you want to save the file? Yes
? Please enter the file name to save the loans stevie
Your loan information is  saved in /data/stevie.csv
```
---
## Contributors 

Stephen Thomas

[Trilogy Education Services](https://www.trilogyed.com/)

[UC Berkeley Extension](https://extension.berkeley.edu/)


---
##  License 

MIT
