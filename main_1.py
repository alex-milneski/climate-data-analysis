import pandas as pd
import os
import glob

# setting up directory and batch read_csv function for all data tables...

path = os.getcwd()
csv_files = glob.glob(os.path.join(path, "*.CSV"))

# empty lists which will house the multiple dataframes (cleaned data and filtered data)
cleaned_csv = []
bc_csv = []


for file in csv_files:

    # the first 31 rows of each csv files include lines of text and a legend which make dataframe analysis impossible
    # this first line of code removes the text/legend at top of data tables

    df = pd.read_csv(file, skiprows=31)

    # add new columns specifying year and month based on csv filenames

    df['Year'] = os.path.basename(file)
    df['Year'] = df['Year'].str.slice(11, 15)
    df['Month'] = os.path.basename(file)
    df['Month'] = df['Month'].str.slice(16, )
    df['Month'] = df['Month'].str.rstrip('.CSV')
    cleaned_csv.append(df)

# filter all tables so that only rows where the Province is BC

for cleaned_file in cleaned_csv:
    bc = cleaned_file.loc[cleaned_file['Prov'] == 'BC']
    bc_csv.append(bc)

# concatenate all tables

merged = pd.concat(bc_csv, ignore_index=True)

#
merged.to_csv("BC_data.csv")



