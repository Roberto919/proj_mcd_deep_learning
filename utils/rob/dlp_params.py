## MODULE WITH PYTHON PARAMETERS RELEVANT FOR THE PROBLEM





"------------------------------------------------------------------------------"
############################
## Definitions dictionary ##
############################


##
features_dict = {
    "Id": {
        "relevant": False,
        "data_default_type": "int64",
        "data_obj_type": "int64",
        "ml_label": False,
        "pipeline": "num_pipe"
    },
    "MSSubClass": {
        "relevant": False,
        "data_default_type": "int64",
        "data_obj_type": "int64",
        "ml_label": False,
        "pipeline": "cat_pipe"
    },
    "MSZoning": {
        "relevant": True,
        "data_default_type": "object",
        "data_obj_type": "category",
        "ml_label": False,
        "pipeline": "cat_pipe"
    },
    "LotFrontage": {
        "relevant": True,
        "data_default_type": "float64",
        "data_obj_type": "float64",
        "ml_label": False,
        "pipeline": "num_pipe"
    },
    "LotArea": {
        "relevant": True,
        "data_default_type": "int64",
        "data_obj_type": "int64",
        "ml_label": False,
        "pipeline": "num_pipe"
    },
    "Street": {
        "relevant": False,
        "data_default_type": "object",
        "data_obj_type": "category",
        "ml_label": False,
        "pipeline": "cat_pipe"
    },
    "Alley": {
        "relevant": False,
        "data_default_type": "object",
        "data_obj_type": "category",
        "ml_label": False,
        "pipeline": "cat_pipe"
    },
    "LotShape": {
        "relevant": True,
        "data_default_type": "object",
        "data_obj_type": "category",
        "ml_label": False,
        "pipeline": "cat_pipe"
    },
    "LandContour": {
        "relevant": True,
        "data_default_type": "object",
        "data_obj_type": "category",
        "ml_label": False,
        "pipeline": "cat_pipe"
    },
    "Utilities": {
        "relevant": True,
        "data_default_type": "object",
        "data_obj_type": "category",
        "ml_label": False,
        "pipeline": "cat_pipe"
    },
    "LotConfig": {
        "relevant": True,
        "data_default_type": "object",
        "data_obj_type": "category",
        "ml_label": False,
        "pipeline": "cat_pipe"
    },
    "LandSlope": {
        "relevant": True,
        "data_default_type": "object",
        "data_obj_type": "category",
        "ml_label": False,
        "pipeline": "cat_pipe"
    },
    "Neighborhood": {
        "relevant": True,
        "data_default_type": "object",
        "data_obj_type": "category",
        "ml_label": False,
        "pipeline": "cat_pipe"
    },
    "Condition1": {
        "relevant": True,
        "data_default_type": "object",
        "data_obj_type": "category",
        "ml_label": False,
        "pipeline": "cat_pipe"
    },
    "Condition2": {
        "relevant": True,
        "data_default_type": "object",
        "data_obj_type": "category",
        "ml_label": False,
        "pipeline": "cat_pipe"
    },
    "BldgType": {
        "relevant": True,
        "data_default_type": "object",
        "data_obj_type": "category",
        "ml_label": False,
        "pipeline": "cat_pipe"
    },
    "HouseStyle": {
        "relevant": True,
        "data_default_type": "object",
        "data_obj_type": "category",
        "ml_label": False,
        "pipeline": "cat_pipe"
    },
    "OverallQual": {
        "relevant": True,
        "data_default_type": "int64",
        "data_obj_type": "int64",
        "ml_label": False,
        "pipeline": "num_pipe"
    },
    "OverallCond": {
        "relevant": True,
        "data_default_type": "int64",
        "data_obj_type": "int64",
        "ml_label": False,
        "pipeline": "num_pipe"
    },
    "YearBuilt": {
        "relevant": True,
        "data_default_type": "int64",
        "data_obj_type": "int64",
        "ml_label": False,
        "pipeline": "num_pipe"
    },
    "YearRemodAdd": {
        "relevant": True,
        "data_default_type": "int64",
        "data_obj_type": "int64",
        "ml_label": False,
        "pipeline": "num_pipe"
    },
    "RoofStyle": {
        "relevant": True,
        "data_default_type": "object",
        "data_obj_type": "category",
        "ml_label": False,
        "pipeline": "cat_pipe"
    },
    "RoofMatl": {
        "relevant": True,
        "data_default_type": "object",
        "data_obj_type": "category",
        "ml_label": False,
        "pipeline": "cat_pipe"
    },
    "Exterior1st": {
        "relevant": True,
        "data_default_type": "object",
        "data_obj_type": "category",
        "ml_label": False,
        "pipeline": "cat_pipe"
    },
    "Exterior2nd": {
        "relevant": True,
        "data_default_type": "object",
        "data_obj_type": "category",
        "ml_label": False,
        "pipeline": "cat_pipe"
    },
    "MasVnrType": {
        "relevant": True,
        "data_default_type": "object",
        "data_obj_type": "category",
        "ml_label": False,
        "pipeline": "cat_pipe"
    },
    "MasVnrArea": {
        "relevant": True,
        "data_default_type": "float64",
        "data_obj_type": "float64",
        "ml_label": False,
        "pipeline": "num_pipe"
    },
    "ExterQual": {
        "relevant": True,
        "data_default_type": "object",
        "data_obj_type": "category",
        "ml_label": False,
        "pipeline": "cat_pipe"
    },
    "ExterCond": {
        "relevant": True,
        "data_default_type": "object",
        "data_obj_type": "category",
        "ml_label": False,
        "pipeline": "cat_pipe"
    },
    "Foundation": {
        "relevant": True,
        "data_default_type": "object",
        "data_obj_type": "category",
        "ml_label": False,
        "pipeline": "cat_pipe"
    },
    "BsmtQual": {
        "relevant": True,
        "data_default_type": "object",
        "data_obj_type": "category",
        "ml_label": False,
        "pipeline": "cat_pipe"
    },
    "BsmtCond": {
        "relevant": True,
        "data_default_type": "object",
        "data_obj_type": "category",
        "ml_label": False,
        "pipeline": "cat_pipe"
    },
    "BsmtExposure": {
        "relevant": True,
        "data_default_type": "object",
        "data_obj_type": "category",
        "ml_label": False,
        "pipeline": "cat_pipe"
    },
    "BsmtFinType1": {
        "relevant": True,
        "data_default_type": "object",
        "data_obj_type": "category",
        "ml_label": False,
        "pipeline": "cat_pipe"
    },
    "BsmtFinSF1": {
        "relevant": True,
        "data_default_type": "int64",
        "data_obj_type": "int64",
        "ml_label": False,
        "pipeline": "num_pipe"
    },
    "BsmtFinType2": {
        "relevant": True,
        "data_default_type": "object",
        "data_obj_type": "category",
        "ml_label": False,
        "pipeline": "cat_pipe"
    },
    "BsmtFinSF2": {
        "relevant": True,
        "data_default_type": "int64",
        "data_obj_type": "int64",
        "ml_label": False,
        "pipeline": "num_pipe"
    },
    "BsmtUnfSF": {
        "relevant": True,
        "data_default_type": "int64",
        "data_obj_type": "int64",
        "ml_label": False,
        "pipeline": "num_pipe"
    },
    "TotalBsmtSF": {
        "relevant": True,
        "data_default_type": "int64",
        "data_obj_type": "int64",
        "ml_label": False,
        "pipeline": "num_pipe"
    },
    "Heating": {
        "relevant": True,
        "data_default_type": "object",
        "data_obj_type": "category",
        "ml_label": False,
        "pipeline": "cat_pipe"
    },
    "HeatingQC": {
        "relevant": True,
        "data_default_type": "object",
        "data_obj_type": "category",
        "ml_label": False,
        "pipeline": "cat_pipe"
    },
    "CentralAir": {
        "relevant": True,
        "data_default_type": "object",
        "data_obj_type": "category",
        "ml_label": False,
        "pipeline": "cat_pipe"
    },
    "Electrical": {
        "relevant": True,
        "data_default_type": "object",
        "data_obj_type": "category",
        "ml_label": False,
        "pipeline": "cat_pipe"
    },
    "1stFlrSF": {
        "relevant": True,
        "data_default_type": "int64",
        "data_obj_type": "int64",
        "ml_label": False,
        "pipeline": "num_pipe"
    },
    "2ndFlrSF": {
        "relevant": True,
        "data_default_type": "int64",
        "data_obj_type": "int64",
        "ml_label": False,
        "pipeline": "num_pipe"
    },
    "LowQualFinSF": {
        "relevant": True,
        "data_default_type": "int64",
        "data_obj_type": "int64",
        "ml_label": False,
        "pipeline": "num_pipe"
    },
    "GrLivArea": {
        "relevant": True,
        "data_default_type": "int64",
        "data_obj_type": "int64",
        "ml_label": False,
        "pipeline": "num_pipe"
    },
    "BsmtFullBath": {
        "relevant": True,
        "data_default_type": "int64",
        "data_obj_type": "int64",
        "ml_label": False,
        "pipeline": "num_pipe"
    },
    "BsmtHalfBath": {
        "relevant": True,
        "data_default_type": "int64",
        "data_obj_type": "int64",
        "ml_label": False,
        "pipeline": "num_pipe"
    },
    "FullBath": {
        "relevant": True,
        "data_default_type": "int64",
        "data_obj_type": "int64",
        "ml_label": False,
        "pipeline": "num_pipe"
    },
    "HalfBath": {
        "relevant": True,
        "data_default_type": "int64",
        "data_obj_type": "int64",
        "ml_label": False,
        "pipeline": "num_pipe"
    },
    "BedroomAbvGr": {
        "relevant": True,
        "data_default_type": "int64",
        "data_obj_type": "int64",
        "ml_label": False,
        "pipeline": "num_pipe"
    },
    "KitchenAbvGr": {
        "relevant": True,
        "data_default_type": "int64",
        "data_obj_type": "int64",
        "ml_label": False,
        "pipeline": "num_pipe"
    },
    "KitchenQual": {
        "relevant": True,
        "data_default_type": "object",
        "data_obj_type": "category",
        "ml_label": False,
        "pipeline": "cat_pipe"
    },
    "TotRmsAbvGrd": {
        "relevant": True,
        "data_default_type": "int64",
        "data_obj_type": "int64",
        "ml_label": False,
        "pipeline": "num_pipe"
    },
    "Functional": {
        "relevant": True,
        "data_default_type": "object",
        "data_obj_type": "category",
        "ml_label": False,
        "pipeline": "cat_pipe"
    },
    "Fireplaces": {
        "relevant": True,
        "data_default_type": "int64",
        "data_obj_type": "int64",
        "ml_label": False,
        "pipeline": "num_pipe"
    },
    "FireplaceQu": {
        "relevant": True,
        "data_default_type": "object",
        "data_obj_type": "category",
        "ml_label": False,
        "pipeline": "cat_pipe"
    },
    "GarageType": {
        "relevant": True,
        "data_default_type": "object",
        "data_obj_type": "category",
        "ml_label": False,
        "pipeline": "cat_pipe"
    },
    "GarageYrBlt": {
        "relevant": True,
        "data_default_type": "float64",
        "data_obj_type": "float64",
        "ml_label": False,
        "pipeline": "num_pipe"
    },
    "GarageFinish": {
        "relevant": True,
        "data_default_type": "object",
        "data_obj_type": "category",
        "ml_label": False,
        "pipeline": "cat_pipe"
    },
    "GarageCars": {
        "relevant": True,
        "data_default_type": "int64",
        "data_obj_type": "int64",
        "ml_label": False,
        "pipeline": "num_pipe"
    },
    "GarageArea": {
        "relevant": True,
        "data_default_type": "int64",
        "data_obj_type": "int64",
        "ml_label": False,
        "pipeline": "num_pipe"
    },
    "GarageQual": {
        "relevant": True,
        "data_default_type": "object",
        "data_obj_type": "category",
        "ml_label": False,
        "pipeline": "cat_pipe"
    },
    "GarageCond": {
        "relevant": True,
        "data_default_type": "object",
        "data_obj_type": "category",
        "ml_label": False,
        "pipeline": "cat_pipe"
    },
    "PavedDrive": {
        "relevant": True,
        "data_default_type": "object",
        "data_obj_type": "category",
        "ml_label": False,
        "pipeline": "cat_pipe"
    },
    "WoodDeckSF": {
        "relevant": True,
        "data_default_type": "int64",
        "data_obj_type": "int64",
        "ml_label": False,
        "pipeline": "num_pipe"
    },
    "OpenPorchSF": {
        "relevant": True,
        "data_default_type": "int64",
        "data_obj_type": "int64",
        "ml_label": False,
        "pipeline": "num_pipe"
    },
    "EnclosedPorch": {
        "relevant": True,
        "data_default_type": "int64",
        "data_obj_type": "int64",
        "ml_label": False,
        "pipeline": "num_pipe"
    },
    "3SsnPorch": {
        "relevant": True,
        "data_default_type": "int64",
        "data_obj_type": "int64",
        "ml_label": False,
        "pipeline": "num_pipe"
    },
    "ScreenPorch": {
        "relevant": True,
        "data_default_type": "int64",
        "data_obj_type": "int64",
        "ml_label": False,
        "pipeline": "num_pipe"
    },
    "PoolArea": {
        "relevant": True,
        "data_default_type": "int64",
        "data_obj_type": "int64",
        "ml_label": False,
        "pipeline": "num_pipe"
    },
    "PoolQC": {
        "relevant": True,
        "data_default_type": "object",
        "data_obj_type": "category",
        "ml_label": False,
        "pipeline": "cat_pipe"
    },
    "Fence": {
        "relevant": True,
        "data_default_type": "object",
        "data_obj_type": "category",
        "ml_label": False,
        "pipeline": "cat_pipe"
    },
    "MiscFeature": {
        "relevant": True,
        "data_default_type": "object",
        "data_obj_type": "category",
        "ml_label": False,
        "pipeline": "cat_pipe"
    },
    "MiscVal": {
        "relevant": True,
        "data_default_type": "int64",
        "data_obj_type": "int64",
        "ml_label": False,
        "pipeline": "num_pipe"
    },
    "MoSold": {
        "relevant": True,
        "data_default_type": "int64",
        "data_obj_type": "int64",
        "ml_label": False,
        "pipeline": "num_pipe"
    },
    "YrSold": {
        "relevant": True,
        "data_default_type": "int64",
        "data_obj_type": "int64",
        "ml_label": False,
        "pipeline": "num_pipe"
    },
    "SaleType": {
        "relevant": True,
        "data_default_type": "object",
        "data_obj_type": "category",
        "ml_label": False,
        "pipeline": "cat_pipe"
    },
    "SaleCondition": {
        "relevant": True,
        "data_default_type": "object",
        "data_obj_type": "category",
        "ml_label": False,
        "pipeline": "cat_pipe"
    },
    "SalePrice": {
        "relevant": False,
        "data_default_type": "int64",
        "data_obj_type": "int64",
        "ml_label": True,
        "pipeline": "num_pipe"
    }
}


## NOTES: Manual updates
#### MSSubClass --> relevant: False