import pandas as pd
import os

# Import Adnymics dataset
def def_dat(start_date, end_date, start_time, end_time, path):
    """
    This function defines the data of interest
    The data is manually imported from the Chronos server
    eg https://chronos.adnymics.com/v1/feedback/2019-11-18T00:00:00/2019-11-20T00:00:00

    Parameters:
    start_date (str), format='%d-%m-%Y'
    end_date (str), format='%d-%m-%Y'

    Returns:
    filename (str) to be imported

    Julien Hernandez Lallement
    ORSAY, Willstaett, Germany
    09-12-2019
    """
    # The data is manually imported from the Chronos server
    # eg https://chronos.adnymics.com/v1/feedback/2019-11-18T00:00:00/2019-11-20T00:00:00
    # Make sure timestamps are in right format
    start_date = pd.to_datetime(start_date, format='%d-%m-%Y').strftime('%Y-%m-%d')
    end_date   = pd.to_datetime(end_date,   format='%d-%m-%Y').strftime('%Y-%m-%d')
    start_time = start_time
    end_time = end_time
    # Set path
    # path = 'u:\\Projects\\CRM_communication_strategy\\datasets\\adnymics'
    # Set filename
    filename = str(start_date)+start_time+'__'+str(end_date)+end_time + '.json'
    # Set dir
    os.chdir(path)
    print('curr dir: ' + str(os.getcwd()))
    # List files in dir
    files = os.listdir()
    # Define final path
    orderbook_file = 'd:\\Projects\\datasets\\adnymics\\' + filename
    return orderbook_file, filename
