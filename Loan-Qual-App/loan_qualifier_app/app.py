# -*- coding: utf-8 -*-
"""Loan Qualifier Application.

This is a command line application to match applicants with qualifying loans.

Example:
    $ python app.py
"""
# the following are important dependencies that help the app do what its meant to do.
import sys
from pathlib import Path

import fire
import questionary

# the folllowing is a command to import two functions from the filio.py file, inside the utils folder,
# inside the qualifier folder.
from qualifier.utils.fileio import load_csv, save_csv

# here is a command to import two functions, calculate_monthly_debt_ratio and calculate_loan_to_value from 
# the calculators file, inside the utils folder, inside the qualifiers folder.
from qualifier.utils.calculators import (
    calculate_monthly_debt_ratio,
    calculate_loan_to_value_ratio,
)

from qualifier.filters.max_loan_size import filter_max_loan_size
from qualifier.filters.credit_score import filter_credit_score
from qualifier.filters.debt_to_income import filter_debt_to_income
from qualifier.filters.loan_to_value import filter_loan_to_value


def load_bank_data():
    """Ask for the file path to the latest banking data and load the CSV file.

    Returns:
        The bank data from the data rate sheet CSV file.
    """


    csvpath = "./data/daily_rate_sheet.csv"
    csvpath = Path(csvpath)
    if not csvpath.exists():
        sys.exit(f"Oops! Can't find this path: {csvpath}")

    return load_csv(csvpath)


def get_applicant_info():
    """Prompt dialog to get the applicant's financial information.

    Returns:
        Returns the applicant's financial information.
    """

    credit_score = questionary.text("What's your credit score?").ask()
    debt = questionary.text("What's your current amount of monthly debt?").ask()
    income = questionary.text("What's your total monthly income?").ask()
    loan_amount = questionary.text("What's your desired loan amount?").ask()
    home_value = questionary.text("What's your home value?").ask()

    credit_score = int(credit_score)
    debt = float(debt)
    income = float(income)
    loan_amount = float(loan_amount)
    home_value = float(home_value)

    return credit_score, debt, income, loan_amount, home_value


def find_qualifying_loans(bank_data, credit_score, debt, income, loan, home_value):
    """Determine which loans the user qualifies for.

    Loan qualification criteria is based on:
        - Credit Score
        - Loan Size
        - Debit to Income ratio (calculated)
        - Loan to Value ratio (calculated)

    Args:
        bank_data (list): A list of bank data.
        credit_score (int): The applicant's current credit score.
        debt (float): The applicant's total monthly debt payments.
        income (float): The applicant's total monthly income.
        loan (float): The total loan amount applied for.
        home_value (float): The estimated home value.

    Returns:
        A list of the banks willing to underwrite the loan.

    """

    # Calculate the monthly debt ratio
    monthly_debt_ratio = calculate_monthly_debt_ratio(debt, income)
    print(f"The monthly debt to income ratio is {monthly_debt_ratio:.02f}")

    # Calculate loan to value ratio
    loan_to_value_ratio = calculate_loan_to_value_ratio(loan, home_value)
    print(f"The loan to value ratio is {loan_to_value_ratio:.02f}.")

    # Run qualification filters
    bank_data_filtered = filter_max_loan_size(loan, bank_data)
    bank_data_filtered = filter_credit_score(credit_score, bank_data_filtered)
    bank_data_filtered = filter_debt_to_income(monthly_debt_ratio, bank_data_filtered)
    bank_data_filtered = filter_loan_to_value(loan_to_value_ratio, bank_data_filtered)

    print(f"Found {len(bank_data_filtered)} qualifying loans")

    return bank_data_filtered

# The following options have been hard coded into the save_qualifying_loans function to increase usability.
# A. Gives user a chance to save to csv file
# B. If No qualifying loans exist, when prompting a user to save file, program should notify
    # user and Exit.
# C. User has a list of qualifying loans and when prompted to save, should be able to opt out of saving file.
# D. User has a list of qualifying loans and when chooses to save, questionary should prompt for a file path.
# E. User has a list of qualifying loans and function should save the results to a csv file.

def save_qualifying_loans(qualifying_loans):
    """Saves the qualifying loans to a CSV file.

    Args:
        qualifying_loans (list of lists): The qualifying bank loans.
    """
    totalLoansQualified = len(qualifying_loans)
    if totalLoansQualified == 0:
        questionary.print("Sorry you don't qualify for any loans now, try again later.")
        return

    answer = questionary.confirm("Do you want to save the file?").ask()

    if answer is True:
        fileName = questionary.text("Please enter the file name to save the loans").ask()
        questionary.print("Your loan information is  saved in /data/" + fileName + ".csv")
        save_csv(fileName, qualifying_loans)
    else:
        questionary.print("You are qualified for the following loans, please note we are not saving to file this time")
        for element in range(len(qualifying_loans)):
            print(qualifying_loans[element])
    return


def run():
    """The main function for running the script."""

    # Load the latest Bank data
    bank_data = load_bank_data()

    # Get the applicant's information
    credit_score, debt, income, loan_amount, home_value = get_applicant_info()

    # Find qualifying loans
    qualifying_loans = find_qualifying_loans(
        bank_data, credit_score, debt, income, loan_amount, home_value
    )

    # Save qualifying loans
    save_qualifying_loans(qualifying_loans)


if __name__ == "__main__":
    fire.Fire(run)


# /Users/stephenthomas/opt/anaconda3/envs/dev/lib/python3.9/site-packages
