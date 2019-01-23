import csv

file_name = "email_data.csv"#email_data_sample.csv, email_data.csv

#First name,Last name,Company,Job title,Email address - home,Email status - home,Email permission status - home,Email address - other,Email status - other,Email permission status - other,Email address - work,Email status - work,Email permission status - work,Phone - fax,Phone - home,Phone - mobile,Phone - work,Street address line 1 - Home,City - Home,State/Province - Home,Zip/Postal Code - Home,Country - Home,Street address line 1 - Home 2,City - Home 2,State/Province - Home 2,Zip/Postal Code - Home 2,Country - Home 2,Street address line 1 - Other,City - Other,State/Province - Other,Zip/Postal Code - Other,Country - Other,Street address line 1 - Other 2,City - Other 2,State/Province - Other 2,Zip/Postal Code - Other 2,Street address line 1 - Work,City - Work,State/Province - Work,Zip/Postal Code - Work,Country - Work,Website,Custom field 1,Custom field 2,Custom field 3,Date of update,Tags,Email Lists,Source Name,Created At,Updated At
data = []#[ {}, {}, etc.]

with open(file_name) as csv_file: #imports data into dict format, each item is a contact
    csv_reader = csv.DictReader(csv_file, delimiter=',')
    total_count = 0
    for row in csv_reader:
        total_count += 1
        data.append(row)
    print("Data successfully imported in dict format, total of: ", total_count, " from: ", file_name)

possible_email_keys = ("Email address - home", "Email address - other", "Email address - work")

for contact in data: #we check that each contact has at least one email address, and remove those without
    brokenContacts = []
    if len("".join(map(lambda x: row[x], possible_email_keys))) == 0:
        brokenContacts.append(contact)
for brokenContact in brokenContacts:
    data.remove(brokenContact)
print("There were a total of ", len(brokenContacts), "broken contacts")






    