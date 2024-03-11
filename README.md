# Customer Data Cleansing

Clean and format the customer call list, which is stored in an Excel file. It employs various data cleaning techniques to ensure the data is standardized and ready for use.
Usage

    Ensure you have Python installed on your system.
    Install the required dependencies by running:

pip install pandas openpyxl

Download the script file (clean_customer_data.py) and the Excel file (Customer Call List.xlsx).
Update the file path in the script to point to your Excel file:

python

df = pd.read_excel(r"YOUR_FILE_PATH\Customer Call List.xlsx")

Run the script using Python:

    python clean_customer_data.py

Data Cleaning Steps

    Remove Duplicates: Removes duplicate rows from the dataset.
    Remove Unwanted Columns: Drops columns that are not needed for further analysis.
    Strip Unwanted Characters from Last Name Column: Removes specific characters from the Last Name column.
    Strip Unwanted Characters from Phone Number Column: Removes non-alphanumeric characters from the Phone Number column.
    Insert Hyphens in Phone Numbers: Inserts hyphens at specific positions to format phone numbers.
    Clean Address Column: Splits the Address column into Street Address, State, and Zip Code columns.
    Standardize Values in Paying Customer and Do Not Contact Columns: Replaces values in these columns to standardize the data.
    Fill NaN Values: Replaces NaN values with an empty string.
    Remove Do Not Contact Entries: Removes entries where the 'Do Not Contact' flag is set to 'Y'.
    Remove Entries with No Phone Number: Removes entries with no phone number provided.
    Reset Index: Resets the index of the DataFrame.
