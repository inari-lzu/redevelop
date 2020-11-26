import pandas as pdimport csv
import sys
import os


fileName = sys.argv[1]

df = pd.read_excel(fileName, None)
sheet_names = list(df.keys())

for sheetName in sheet_names:

    data_xls = pd.read_excel(fileName, sheet_name=sheetName, index_col=0)
    data_xls.to_csv('example.csv', encoding='utf-8')

    file = open("example.csv", "r", encoding="utf-8")
    records = csv.reader(file)
    sql_states = []

    insert_states = "INSERT INTO play_in ({}) \n".format(str(next(records))[1:-1]) \
                  + "VALUES ({})"

    for row in records:
        row = str(row)[1:-1]
        new_record = insert_states.format(row)
        sql_states.append(new_record + ";\n\n")

    file.close()

    with open(sheetName+".sql", 'w') as file:
        for record in sql_states:
            file.write(record)

os.remove("example.csv")
