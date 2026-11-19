# Let's imagine we are a software company that sells security products to large businesses.
# We track our customer contact information in a marketing database.

# Imagine that when we ask a database to give us back some data, we have the option to select either
# a list or a dictionary. Both return the same five values:
# Customer name, email, phone, title, total number of users at their company

# This is what a list from that database might look like.
# We may not be able to change the order the database returns data in. A dictionary would likely
# be a better fit for making our code a little more readable.
# But for now now, just fix the error 

db_return = ['Susan James', 'sjames@bigcompany.com', '212-555-1234', 'VP Technical Services', 25000]

print("Customer Contact Information")
print("============================")
print(f"Customer Name: {db_return[0]}")
print(f"Title: {db_return[3]}") #changed the return index from 4 to 3
print(f"Email: {db_return[1]}")
print(f"Phone: {db_return[2]}")
print(f"Company has approx. {db_return[4]} staff.") #changed return index from 5 to 4

# Once the error is fixed:
# Rewrite this so the data is stored in a dictionary, not in a list.
# You can keep the same variable name, but use key names that correspond to the thing you're actually 
# storing, e.g. 'cust_name'. Then use the dictionary and its keys to retrieve the data.
# You can duplicate the code above down here and work on it, or make a duplicate of the whole file
# and submit more than one debugging exercise. Your choice.