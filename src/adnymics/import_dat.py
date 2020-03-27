import pandas as pd


def import_dat(orderbook_file):
    """
    This function imports the data of interest.

    Parameters:
    filename (str), from file to be imported

    Returns:
    df (pandas dataframe), which contains main data
    df_guide (pandas dataframe), which contains guide data

    Julien Hernandez Lallement
    ORSAY, Willstaett, Germany
    09-12-2019
    """
    orderbook = pd.read_json(orderbook_file, orient='records')
    orderbook = orderbook['brochures'].apply(pd.Series)
    # Some entries are clearly wrong. Get rid of them.
    # unknown_entries = orderbook[(orderbook['campaign_id'] == -1)]
    # orderbook = orderbook[~(orderbook['campaign_id'] == -1)]
    return orderbook  # , unknown_entries
