import pandas as pd
'''
receive a series object, who can be, a column in an dataframe
return central_tendency_measures for this column
'''
def get_central_tendency_measures(series):
    return pd.Series({
        "mean" : series.mean(),
        "mode" : series.mode(dropna=True),
        "median" : series.median(),
        "max" : series.max(),
        "min" : series.min()
    })
'''
receive a series object, who can be, a column in an dataframe
returns the variability mostly comum measures for this object
'''
