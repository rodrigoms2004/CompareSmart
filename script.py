import pandas as pd

def returnDataFrameFromCSV(csv_file, separator):
    elements = pd.read_csv(csv_file, sep=separator) #index_col = 0)

    # create a list with all CSV file headers
    csv_headers_list = list(elements.columns.values)

    # create a empty list
    rows_list = []
    for key, value in elements.iterrows():

        # create a empty dictionary
        dict_row = {}
        for header in csv_headers_list:
            dict_row[header] = value[header]
        # end for

        # add dictionary to the list
        rows_list.append(dict_row)

    # end for

    # returns a dataframe
    return pd.DataFrame(rows_list)
# end def


# https://pandas.pydata.org/pandas-docs/stable/merging.html

# Convert SmartCenter CSV to a readable CSV in BASH SHELL
# cat inventory.csv | sed 's/\"="//g' | sed 's/\"//g' > inventory2.csv

customerInfo = returnDataFrameFromCSV('./customer_msisdn.csv', ',')
smartInventory = returnDataFrameFromCSV('./inventory2.csv', ';')
result = pd.merge(smartInventory, customerInfo, on='msisdn') 

df_result = result[[
'currentApn', 'currentIp',
'gprsStatus_lastConnStart','gprsStatus_lastConnStop',
'gprsStatus_status','icc','imei','imeiChangeDate',
'imsi','msisdn']]

# https://cmdlinetips.com/2018/02/how-to-subset-pandas-dataframe-based-on-values-of-a-column/

df_Disconnected = df_result[df_result['gprsStatus_status'] == 'DISCONNECTED']
df_prior = df_Disconnected[df_Disconnected['gprsStatus_lastConnStop'] <= '2019-01-13T00:00:00.000Z']

df_prior.to_csv('./results.csv', sep='\t', encoding='utf-8')