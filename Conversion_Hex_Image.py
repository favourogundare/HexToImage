import pyodbc
import pandas as pd

# Author: Favour Ogundare
# Version: Python 3.9
# Run using Pycharm @ https://www.jetbrains.com/pycharm/

# Sets up connection to your Database
cnxn_str = ("Driver={SQL Server};"
            "Server=YourServerName;"
            "Database=YourDatabaseName;"
            "Trusted_Connection=yes;")
cnxn = pyodbc.connect(cnxn_str)
cursor = cnxn.cursor()

# PRINTS OUT PHOTOS IN DATA FRAME
# CONVERTS HEX TO JPEG
# DISPLAY OPTION CHANGE LETS YOU SEE MORE RECORDS

def set_pandas_display_options() -> None:
    """Set pandas display options."""
    # Ref: https://stackoverflow.com/a/52432757/
    display = pd.options.display

    display.max_columns = 1000
    display.max_rows = 1000
    display.max_colwidth = 199
    display.width = 1000
    # display.precision = 2  # set as needed
    # display.float_format = lambda x: '{:,.2f}'.format(x)  # set as needed


set_pandas_display_options()

# check to see what your table looks like here
# again = pd.read_sql("select * from yourtablename", cnxn)
# data_frame = pd.DataFrame(again, columns=['ColumnPrimaryID', 'ColumnNameforPhoto','HexValueColumnName'])

# print(data_frame)
data = pd.read_sql("select * from yourtablename", cnxn)
df = pd.DataFrame(data)

# The only values you need are the name of the outputfile (ColumnNameforPhoto), hex value and ID field


def generate():
    content_of_rows = {}
    for row in df.itertuples():
        index = row[0]
        ColumnPrimaryID = row[1]
        ColumnNameforPhoto = row[2]
                              HexValueColumnName = row[2]
        content_of_rows.update(
            {index: {"ColumnPrimaryID": ColumnPrimaryID, "ColumnNameforPhoto": ColumnNameforPhoto, "HexValueColumnName": HexValueColumnName.hex()}})
        print(content_of_rows)
        print("\n")
        print("\n")

        photo = HexValueColumnName.hex()
        identi = ColumnNameforPhoto
        file = '.jpg'
                              
                              #files will be converted to jpg from whichever format theyre in

        integers = []

        while photo:
            value = int(photo[:2], 16)
            integers.append(value)
            photo = photo[2:]

        cdata = bytearray(integers)
        resultant = "{0}{1}".format(str(identi), file)
        print(resultant)

        with open(resultant, 'wb') as fh:
            print(fh.write(cdata))


generate()

