import pandas as pd
import os


def write_to_disk(dataf, filename):
    """
    This function writes the data to disk
    Parameters:
    dataf(pandas dataframe), which contains main data
    filename (str), name of the file to be written

    Returns
    generation of i number of files

    Julien Hernandez Lallement
    ORSAY, Willstaett, Germany
    11-12-2019
    """
    filename = str(filename)
    # Unwrap tuple
    data_false = dataf[0]
    data_true = dataf[1]
    # Write to Disk
    with pd.ExcelWriter(filename.split(sep='.')[0]+str('.xlsx')) as writer:  # doctest: +SKIP
        data_true.to_excel(writer, sheet_name = 'is_printed=True')
        data_false.to_excel(writer, sheet_name = 'is_printed=False')
        #  unknown.to_excel   (writer, sheet_name = 'unknown_val')

    print('file wrote to disk: ' + filename.split(sep='.')[0]+str('.xlsx'))
    print(os.getcwd())
