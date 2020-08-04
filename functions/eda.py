"""
General and reusable exploratory data analysis functionality
"""
import pandas as pd 

def missing_perc(df):
     """
     Return a dataframe with percentage of missing values
     in each column in a sorted order

     Args:
     df: dataframe
     Returns:
     dataframe with percentage of missing values in each column
     """

     missing = df.isnull().sum()
     missing = missing[missing > 0] * 100 / df.shape[0]
     missing.sort_values(inplace=True)
     return pd.DataFrame(missing, columns=['missing_perc'])


def unique_val(df, outputcol='n_unique_vals'):
     """
     Count the number of distinct values in each column in a sorted order

     Args:
     df: dataframe
     col: string, column name of the output dataframe
     Returns:
     dataframe with the number of distinct values in each column
     """

     columns = df.columns
     undict = {}
     for col in columns:
         undict[col] = df[col].astype(str).nunique()
     undf = pd.DataFrame.from_dict(undict,
         'index',
         columns=[outputcol])
     undf.sort_values(by=[outputcol], inplace=True)
     return undf


def impute_missing(df, column, method='median', val=0):
     """
     Return a dataframe where the target column missing values have been imputed

     Args:
     df: dataframe
     colum: string, target column with missing values to be filled
     method: string, imputation method (mean, median or numeric)
     val: integer, value to be set for numeric method imputation
     Returns:
     Dataframe where the target column missing values have been imputed
     """

     if method == 'median':
         df[column] = df[column].fillna(df[column].median())
     elif method == 'mean':
         df[column] = df[column].fillna(df[column].mean())
     elif method == 'mode':
         df[column] = df[column].fillna(df[column].mode()[0])
     elif method == 'numeric':
         df[column] = df[column].fillna(val)
     else:
         raise RuntimeError(
         'Enter a valid imputation method,'
         'median, mean, mode and numeric are supported.'
         ' Missing values were not replaced.')
     return df



