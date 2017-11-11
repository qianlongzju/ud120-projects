#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print 'total number:', len(enron_data)
person = enron_data.keys()[0]

print "\n".join(enron_data[person].keys())
print 'feature number:', len(enron_data[person])
print 'poi:', sum([1 for person in enron_data if enron_data[person]['poi']])

print enron_data['PRENTICE JAMES']['total_stock_value']
print enron_data['COLWELL WESLEY']['from_this_person_to_poi']
print enron_data['SKILLING JEFFREY K']['exercised_stock_options']

for person in enron_data:
    if ("lay" in person.lower() or "skilling" in person.lower()
            or "fastow" in person.lower()):
        print person, enron_data[person]['total_payments']

print sum([1 for person in enron_data if enron_data[person]['salary'] != 'NaN'])
print sum([1 for person in enron_data if enron_data[person]['email_address'] != 'NaN'])
print sum([1 for person in enron_data if enron_data[person]['total_payments'] == 'NaN' and enron_data[person]['poi']]) 
print sum([1 for person in enron_data if enron_data[person]['total_payments'] == 'NaN'])
