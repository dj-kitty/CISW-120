#This is the rewritten version of the debugging exercise that has the data in a dictionary instead of a list


db_return = {

    "Name": "Susan James",
    "Email": "sjames@bigcompany.com",
    "Phone": "212-555-1234",
    "Title": "VP Technical Services",
    "Staff": 25000

}

print("Customer Contact Information")
print("============================")
print(f"Customer Name: {db_return["Name"]}")
print(f"Title: {db_return["Title"]}")
print(f"Email: {db_return["Email"]}")
print(f"Phone: {db_return["Phone"]}")
print(f"Company has approx. {db_return["Staff"]} staff.")