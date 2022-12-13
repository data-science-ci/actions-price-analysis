import pandas as pd
import numpy as np
from anapy import means
from scipy.stats import variation


def get_central_tendency_measures(series):
    return pd.Series({
        "mean" : series.mean(),
        "mode" : series.mode(dropna=True),
        "median" : series.median(),
        "max" : series.max(),
        "min" : series.min()
    })

def get_variability_measures(series):

    return pd.Series({
        "variance" : series.var(),
        "standard deviation" : series.std(),
        "shifiting_range" : np.unique(means.shifting_range(np.array(series))),
        "CV": variation(series) 
    })

