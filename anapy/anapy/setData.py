'''
    Receive three positional arguments 
    <df> dataframe who contain the data to work with
'''
def set_meta_data(df ,  business_name, column):
    business_metadata = {
        "business" : df[df["empresa"] == business_name],
}   
    business_metadata["column"] = business_metadata["business"][column]
    return business_metadata