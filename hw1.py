import csv

cwb_filename = '107061136.csv'
header = []

with open(cwb_filename) as csvfile:
    mycsv = csv.DictReader(csvfile)
    header = mycsv.fieldnames
    target_data = [['C0A880', 0], ['C0F9A0', 0], ['C0G640', 0], ['C0R190', 0], ['C0X260', 0]] 
    # set up the target data
    for row in mycsv:
        temp = float(row['TEMP'])
        # turn string into float
        if temp != -99.000 and temp != -999.000:  # remove -99.000 and -999.000
            for i in range(5):  # for loop
                if row['station_id'] == target_data[i][0] and temp > target_data[i][1]:
                    # search the target station id and compare to it maximum
                    target_data[i][1] = temp
                    # if it is larger than its maximum, cover the previous one
    for i in range(5):  # check if there is no maximum
        if target_data[i][1] == 0:
            target_data[i][1] = 'None'  # if yes, outupt none
    print(target_data)  # output the result