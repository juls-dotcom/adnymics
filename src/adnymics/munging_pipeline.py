import pandas as pd


# Extract coupon codes
def extract_coupons(dataf):
    """
    This function extract coupon as pd.Series and concatenates
    Parameters:
    dataf (pandas dataframe), which contains main data

    Returns
    dataf (pandas dataframe), which contains main data

    Julien Hernandez Lallement
    ORSAY, Willstaett, Germany
    11-12-2019
    """
    coupon_code = pd.DataFrame(dataf['coupon_code']
                               .apply(pd.Series))
    return pd.concat([dataf, coupon_code], axis=1, join='outer').reset_index(drop=True)


# Extract item_numbers
def extract_item_number(dataf):
    """
    This function extract each of the 4 items into separate columns
    Parameters:
    dataf (pandas dataframe), which contains main data

    Returns
    dataf (pandas dataframe), which contains main data

    Julien Hernandez Lallement
    ORSAY, Willstaett, Germany
    11-12-2019
    """
    item_number = pd.DataFrame(dataf['recommendations']
                               .apply(pd.Series)).T
    dataf = (dataf
             .assign(item_0=item_number.apply(pd.Series).iloc[0].apply(pd.Series)['item_number'])
             .assign(item_1=item_number.apply(pd.Series).iloc[1].apply(pd.Series)['item_number'])
             .assign(item_2=item_number.apply(pd.Series).iloc[2].apply(pd.Series)['item_number'])
             .assign(item_3=item_number.apply(pd.Series).iloc[3].apply(pd.Series)['item_number'])
             )
    return dataf.reset_index()


# Clean dataset
def drop_cols(dataf):
    """
    This function drops columns
    Parameters:
    dataf (pandas dataframe), which contains main data

    Returns
    dataf (pandas dataframe), which contains main data

    Julien Hernandez Lallement
    ORSAY, Willstaett, Germany
    11-12-2019
    """
    dataf = dataf.drop(columns=['recommendations',
                                'index',
                                'coupon_code',
                                'language', ])
    #                                 'is_printed'])
    return dataf


def split_data(dataf):
    """
    This function splits the data into printed & not printed in separate dataframes
    Parameters:
    dataf (pandas dataframe), which contains main data

    Returns
    data_false (pandas dataframe), which contains not printed data
    data_true  (pandas dataframe), which contains     printed data

    Julien Hernandez Lallement
    ORSAY, Willstaett, Germany
    11-12-2019
    """
    data_false = dataf.loc[dataf['is_printed'] == False].drop(columns={'is_printed'})
    # data_false = data_false.drop(columns = {'is_printed'})
    data_true = dataf.loc[dataf['is_printed'] == True].drop(columns={'is_printed'})
    # data_true  = data_true.drop(columns = {'is_printed'})
    return data_false, data_true
