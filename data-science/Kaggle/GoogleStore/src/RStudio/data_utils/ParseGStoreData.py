import pandas as pd
import json


# Expand column with its sub-columns
def expand_column(df, column_values, new_dict, column_name):
    for value in column_values:
        column_dict = json.loads(value)
        for key in new_dict.keys():
            if key not in column_dict.keys():
                new_dict[key].append(None)
            else:
                new_dict[key].append(column_dict[key])

    # Create N x M (# of sub-columns) for new DataFrame
    extended_data = [[new_dict[key][i] for key in new_dict.keys()] for i in range(0, df.shape[0])]
    new_df = pd.DataFrame(data=extended_data, columns=new_dict.keys())

    # Relabel columns
    new_column_label = {x: column_name + '_' + x for x in new_dict.keys()}
    new_df.rename(columns=new_column_label, inplace=True)

    # Drop old column from original data set
    df = df.drop(columns=[column_name], axis=1)

    return df.join(new_df)


# Expanded totals column with sub-columns
def extend_totals(original_data):
    # Dictionary with sub-columns in totals column
    totals_expanded = {'visits': [], 'hits': [], 'pageviews': [], 'bounces': [],
                       'newVisits': [], 'transactionRevenue': []}

    return expand_column(original_data, original_data.totals.values, totals_expanded, 'totals')


# Expanded geoNetwork column with sub-columns
def extend_geo(original_data):
    # Dictionary with sub-columns in geoNetwork
    geo_extended = {'continent': [], 'subContinent': [], 'country': [], 'region': [], 'metro': [], 'city': [],
                    'cityId': [], 'networkDomain': [], 'latitude': [], 'longitude': [], 'networkLocation': []}

    return expand_column(original_data, original_data.geoNetwork.values, geo_extended, 'geoNetwork')


# Expanded device column with sub-columns
def extend_device(original_data):
    # Dictionary with sub-columns in device
    device_extended = {'browser': [], 'browserVersion': [], 'browserSize': [], 'operatingSystem': [],
                       'operatingSystemVersion': [], 'isMobile': [], 'mobileDeviceBranding': [],
                       'mobileDeviceModel': [], 'mobileInputSelector': [], 'mobileDeviceInfo': [],
                       'mobileDeviceMarketingName': [], 'flashVersion': [], 'language': [], 'screenColors': [],
                       'screenResolution': [], 'deviceCategory': []}

    return expand_column(original_data, original_data.device.values, device_extended, 'device')


# Expand traffic source column with with sub-columns
def extend_traffic_source(original_data):
    traffic_source_extended = {'campaign': [], 'source': [], 'medium': [], 'keyword': [], 'adwordsClickInfo': [],
                               'isTrueDirect': [], 'referralPath': [], 'adContent': [], 'campaignCode': []}

    return expand_column(original_data, original_data.trafficSource.values, traffic_source_extended, 'trafficSource')


# Expand original data set
def extend_original_data_to_new_csv(original_data):
    new_df = extend_totals(original_data)
    new_df = extend_device(new_df)
    new_df = extend_traffic_source(new_df)
    new_df = extend_geo(new_df)
    
    # Data frame to csv
    new_df.to_csv('../../data/RStudio/train_extended.csv')
