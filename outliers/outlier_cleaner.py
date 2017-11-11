#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []
    ### your code goes here
    import numpy as np
    errors = np.abs(predictions - net_worths).squeeze()
    index = np.argsort(errors)
    cleaned_index = index[:int(len(index)*0.9),]
    ages = ages[cleaned_index]
    net_worths = net_worths[cleaned_index]
    errors = errors[cleaned_index]
    for age, net_worth, error in zip(ages, net_worths, errors):
        cleaned_data.append((age, net_worth, error))
    return cleaned_data

