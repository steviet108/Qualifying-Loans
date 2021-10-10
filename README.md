# *Qualifying-Loans-App*

![Fintech image from Getty stock images](fintech-image.png)

This Loan Qualifying Application uses the CLI or Command Line Interface to match applicants with qualifying loans. It is an example of modular code that has functions in separate files as to work more efficiently and also to enable easier maintenance.
The user downloads the app from the GitHub Repository,(see below) and runs the app in their terminal, and answers a few questions regarding their credit score, monthly debt, monthly income, home value and the desired loan amount. The application takes this info and calculates the debt to income ratio and the loan to value ratio and uses these to present a list of qualifying loans. The user then has the option to save this list to a new csv file, or opt out of saving to a file, and in the event the user does not qualify for a loan, the application lets the user know that as well.

---
##  Technologies 

This Application uses Python 3.7 with the following packages:

``` fire ```          - For the command line interface.

``` questionary ```   - For interactive user prompts and dialogs.

---
##  Installations 

Before running this application please install the following dependencies.

``` pip install fire ```

``` pip install questionary ```

---
##  Usage 

To use this Loan Qualifying Application clone the repository from Github and run app.py in the command line or terminal. First click the blue Github link and that will take you to steviet108 github page. Next select Qualifying-Loans from the different repositories , and then click the green CODE tab, copy the URL and then head on back to your local terminal, and type : git clone (paste the url) and hit enter. Now you have pulled the files to your computer. Navigate to that directory in your terminal and run app.py, enter your information and viola, you have a list of loans that you qualify for. Don't forget to select yes when prompted to save to csv file. Now you have a file to show all your friends.. 
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
