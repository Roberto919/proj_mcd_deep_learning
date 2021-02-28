## MODULE WITH PYTHON FUNCTIONS RELEVANT FOR THE PROBLEM





"------------------------------------------------------------------------------"
#############
## Imports ##
#############


## Python libraries

import pandas as pd

import json

import numpy as np


## Ancillary modules

from houses_params import features_dict





"------------------------------------------------------------------------------"
###############################
## General purpose functions ##
###############################


## Pretty print a dictionary and preserving special characters
def json_dump_dict(dictionary):
    """
    Pretty print a dictionary and preserving special characters
        args:
            dictionary (dictionary): dict that will be pretty printed
        returns:
            -
    """

    print(json.dumps(dictionary, indent=4, ensure_ascii=False).encode("utf8").decode())

    return



## Creating features dictionary
def features_dictrionary(data):
    """
    Creating features dictionary
        args:
            data (dataframe): table with all data that will populate the dictionary.
        returns:
            -
    """

    def_dict = {}

    for col in data.columns:
        def_dict[col] = {
            "relevant": False,
            "data_type": str(data[col].dtype),
            "null_perc": round(data[col].isnull().sum()/data.shape[0], 2),
            "len_uniques": len(data[col].unique())
        }

    json_dump_dict(def_dict)

    return



## Transform columns' names to standard format
def clean_col_names(dataframe):
    """
    Transform columns' names to standard format (lowercase, no spaces, no points)
        args:
            dataframe (dataframe): df whose columns will be formatted.
        returns:
            dataframe (dataframe): df with columns cleaned.
    """

    ## Definition of cleaning funcitons that will be applied to the columns' names
    fun1 = lambda x: x.lower() ## convert to lowercase
    fun2 = lambda x: re.sub("( |¡|!|¿|\?|\.|,|;|:)", "_", x) ## eliminate spaces and punctuation signs for underscore
    fun3 = lambda x: unicodedata.normalize("NFD", x).encode("ascii", "ignore").decode("utf-8") ## substitute accents for normal letters
    funcs = [fun1, fun2, fun3]

    ## Applying the defined functions to the columns' names
    for fun in funcs:
        dataframe.columns = [fun(col) for col in dataframe.columns]

    return dataframe



## Display clean cross validation scores
def display_scores(scores):
    print("Scores:", scores)
    print("Mean:", scores.mean())
    print("Standard deviation:", scores.std())





"------------------------------------------------------------------------------"
################################
## Data preparation functions ##
################################


## Cleaning and preparing dataset
def clean_data(data):
    """
    Cleaning and preparing dataset
        args:
            data (dataframe): raw data for the model.
        returns:
            data_clean (dataframe): processed and cleaned data for the model.
    """


    ## Copy of raw data
    data_clean = data.copy()


    ## Eliminating houses with "Gr Liv Area" larger than 4,000
    data_clean = data_clean[data_clean["Gr Liv Area"] < 4_000]


    ## Maintain "Sale Condition" with tag "Normal"
    data_clean = data_clean[data_clean["Sale Condition"] == "Normal"]


    ## Simplifying tags based on rule
    data_clean["MS Zoning"] = np.where(data_clean["MS Zoning"] == "RL", 1, 0) #solo ahí se ven diferencias


    ## Selecting only the columns marked as relevant == True
    rc = [key for key in features_dict if features_dict[key]["relevant"] == True]
    data_clean = data_clean.loc[:, rc]


    ## Convert columns to objective data type
    for col in data_clean:
        data_clean[col] = data_clean[col].astype(features_dict[col]["data_obj_type"])


    return data_clean



## Transforming target variable
def transform_target_var(data, config="ap"):
    """
    Transforming target variable
        args:
            data (dataframe): data with target variable included.
            config (string): configuration of whether the function will be applied or
        returns:
            data (dataframe): data with target variable transformed.
    """


    ## Name of feature that will be predicted
    for feat in features_dict:
        if features_dict[feat]["ml_label"] == True:
            predict_feature = feat


    ## Log transform target variable
    data[predict_feature] = np.log1p(data[predict_feature])


    return data



## Formatting results for upload to kaggle
def format_predicts(predictions):
    """
    Formatting results for upload to kaggle
        args:
            predictions (array): numpy array with prices predictions.
        retrns:
            predictions_res (dataframe): formatted dataframe with predictions.
    """


    ## Dataframe with formatted predictions.
    predictions_res = pd.DataFrame(
        {
            "id": range(1, predictions.shape[0] + 1),
            "SalePrice": predictions
        }
    )


    ## Leaving column "id" as index
    predictions_res.set_index("id", inplace=True)


    return predictions_res



## Creating lists of variables by type.
def features_to_pipes(features_dict):
    """
    Creating lists of variables by type.
        args:
            features_dict (dictionary): specifications of all the problem's features.
        returns:
            housingc_num (list): numerical features.
            housingc_cat (list): categorical features.
    """
    num_pipe = []
    cat_pipe = []

    for feat in features_dict:

        if (features_dict[feat]["relevant"] == True) & \
          ((features_dict[feat]["data_obj_type"] == "float64") | (features_dict[feat]["data_obj_type"] == "int64")) & \
          (features_dict[feat]["pipeline"] == "num_pipe") & \
          (features_dict[feat]["ml_label"] != True):
            num_pipe.append(feat)

        elif (features_dict[feat]["relevant"] == True) & \
          (features_dict[feat]["pipeline"] == "cat_pipe") & \
          (features_dict[feat]["data_obj_type"] == "category"):
            cat_pipe.append(feat)

    relevant_feats = [feat for feat in features_dict if features_dict[feat]["relevant"] == True]
    print("\nFeatures included in the model ({}) --> {}\n".format(len(relevant_feats), relevant_feats))
    print("Features to numerical pipeline ({}) --> {}\n".format(len(num_pipe), num_pipe))
    print("Features to categorical pipeline ({}) --> {}\n\n".format(len(cat_pipe), cat_pipe))

    return num_pipe, cat_pipe
