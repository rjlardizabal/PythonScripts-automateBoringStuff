#! python3
# removeCsvHeader.py - Removes the header from all CSV files in the current
#working directory

import csv,os

os.makedirs('headerRemoved', exist_ok=True)


for csvFileName in os.listdir('.'):
    if not csvFileName.endswith('.csv'):
        continue

    print('Removing header from ' + csvFileName)

    csvRows = []
    csvFileObj = open(csvFileName)
    readerObj = csv.reader(csvFileObj)
    for row in readerObj:
        if readerObj.line_num == 1:
            continue
        csvRows.append(row)
    csvFileObj.close()
    csvFileObj = open(os.path.join('headerRemoved',csvFileName), 'w', newline='')
    csvWriter = csv.writer(csvFileObj)
    csvWriter.writerows(csvRows)
    csvFileObj.close()
