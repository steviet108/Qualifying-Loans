# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv

# This load_csv function is so the app knows where to go to retrieve the banks max loan amount, Loan to value, 
# required credit score, ect.. 
def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data

# save_csv function saves the users loans to a separate csv file, in the data folder.
def save_csv(fileName, qualifying_loans):
    # Change the default path here
    fileToSave = "./data/" + fileName + ".csv"
    with open(fileToSave, 'w+') as save_csv:
        writer = csv.writer(save_csv)

        for element in range(len(qualifying_loans)):
            writer.writerow(qualifying_loans[element])


