import csv
with open('research-and-development-survey-2019-csv.csv','r') as csv_file:
    files=csv.DictReader(csv_file)
    with open('new_dict.csv','w') as new_file:
        field_names=['Table','Breakdown','Year',"Value",'Unit']
        new=csv.DictWriter(new_file,fieldnames=field_names,delimiter=' ')
        new.writeheader()
        for line in files:
            del line['Secondary_Breakdown']
            new.writerow(line)
