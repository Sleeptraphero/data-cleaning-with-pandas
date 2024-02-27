import pandas as pd
import openpyxl as opy

df = pd.read_excel(r"C:\Users\radlm\Downloads\Customer Call List.xlsx")

# Removes Duplicates
df = df.drop_duplicates()

# Removes not needed Column
df = df.drop(columns = "Not_Useful_Column")

# Strip unwanted Chars from Last_Name Column

df["Last_Name"] = df["Last_Name"].str.strip("...")
df["Last_Name"] = df["Last_Name"].str.strip("/")
df["Last_Name"] = df["Last_Name"].str.strip("_")

# Short Version
df["Last_Name"] = df["Last_Name"].str.strip("123._/")

# Remove unwanted Chars from Phone Number Column
df['Phone_Number'] = df['Phone_Number'].str.replace('[^a-zA-Z0-9]', '', regex=True) 

# Insert - at specific locations within the phone numbers
# Change Int Values to Strings

df["Phone_Number"] = df['Phone_Number'].apply(lambda x: str(x))
df["Phone_Number"] = df['Phone_Number'].apply(lambda x: x[0:3] + "-" + x[3:6]+ "-" + x[6:10])

# Strip all versions of Nan--
df["Phone_Number"] = df["Phone_Number"].str.replace("nan---","").str.replace("Na---","").str.replace("nan--","").str.replace("Na--","")

# Clean Address Column
# Splits Address into three Columns on every , for a maximum of two ,

df[["Street_Address", "State","Zip_Code"]] = df["Address"].str.split(",",n=2, expand=True)
df = df.drop(columns="Address")

# Replace Values in Paying Costumer / Do_not_Contact

df["Paying Customer"] = df["Paying Customer"].str.replace("Yes", "Y").str.replace("No", "N").str.replace("N/a", "")

df["Do_Not_Contact"] = df["Do_Not_Contact"].str.replace("Yes", "Y").str.replace("No", "N")

# Fill NaN (NotaNumber) values with an empty string
df = df.fillna("")

# Remove people who dont want to be called or dont have a phone number

for x in df.index:
    if df.loc[x, "Do_Not_Contact"] == "Y":
        df.drop(x, inplace=True)

for x in df.index:
    if df.loc[x, "Phone_Number"] == "":
        df.drop(x, inplace=True)

# Resets Index
df.reset_index(drop=True)