## MODULE WITH PYTHON PARAMETERS RELEVANT FOR THE PROBLEM

f



"------------------------------------------------------------------------------"
############################
## Definitions dictionary ##
############################


features_dict = {
    "MS SubClass": {
        "relevant": False,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 15,
        "data_obj_type": "category",
        "notes": "Después de una exploración, se observó que no hay una relación clara entre las 16 categorías de la columna y el precio de venta.",
        "ml_label": False,
        "pipeline": "-"
    },
    "MS Zoning": {
        "relevant": True,
        "data_default_type": "object",
        "null_perc": 0.0,
        "len_uniques": 7,
        "data_obj_type": "category",
        "notes": "-",
        "ml_label": False,
        "pipeline": "cat_pipe"
    },
    "Lot Frontage": {
        "relevant": False,
        "data_default_type": "float64",
        "null_perc": 0.21,
        "len_uniques": 113,
        "data_obj_type": "float64",
        "notes": "Se realizó una gráfica scatter de esta variable y el precio de venta. No se observó una correlación relevante.",
        "ml_label": False,
        "pipeline": "-"
    },
    "Lot Area": {
        "relevant": True,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 929,
        "data_obj_type": "int64",
        "notes": "-",
        "ml_label": False,
        "pipeline": "num_pipe"
    },
    "Street": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.0,
        "len_uniques": 2,
        "data_obj_type": "object",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "Alley": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.94,
        "len_uniques": 3,
        "data_obj_type": "object",
        "notes": "Tiene demasiados valores vacíos.",
        "ml_label": False,
        "pipeline": "-"
    },
    "Lot Shape": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.0,
        "len_uniques": 4,
        "data_obj_type": "object",
        "notes": "La descripción de los datos indica que no es una variable relevante. Se realizó GEDA también.",
        "ml_label": False,
        "pipeline": "-"
    },
    "Land Contour": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.0,
        "len_uniques": 4,
        "data_obj_type": "object",
        "notes": "La descripción de los datos indica que no es una variable relevante. Se realizó GEDA también.",
        "ml_label": False,
        "pipeline": "-"
    },
    "Utilities": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.0,
        "len_uniques": 2,
        "data_obj_type": "object",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "Lot Config": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.0,
        "len_uniques": 5,
        "data_obj_type": "object",
        "notes": "La descripción de los datos indica que no es una variable relevante. Se realizó GEDA también.",
        "ml_label": False,
        "pipeline": "-"
    },
    "Land Slope": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.0,
        "len_uniques": 3,
        "data_obj_type": "object",
        "notes": "La descripción de los datos indica que no es una variable relevante. Se realizó GEDA también.",
        "ml_label": False,
        "pipeline": "-"
    },
    "Neighborhood": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.0,
        "len_uniques": 27,
        "data_obj_type": "object",
        "notes": "El autor explica que esta variable sería relevante si tuviéramos un mapa.",
        "ml_label": False,
        "pipeline": "-"
    },
    "Condition 1": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.0,
        "len_uniques": 9,
        "data_obj_type": "object",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "Condition 2": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.0,
        "len_uniques": 8,
        "data_obj_type": "object",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "Bldg Type": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.0,
        "len_uniques": 5,
        "data_obj_type": "object",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "House Style": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.0,
        "len_uniques": 8,
        "data_obj_type": "object",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "Overall Qual": {
        "relevant": True,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 10,
        "data_obj_type": "int64",
        "notes": "La matriz de correlación muestra claramente que hay una muy buena relación de esta variable y el precio de venta. (> 0.6)",
        "ml_label": False,
        "pipeline": "num_pipe"
    },
    "Overall Cond": {
        "relevant": False,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 9,
        "data_obj_type": "int64",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "Year Built": {
        "relevant": True,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 108,
        "data_obj_type": "int64",
        "notes": "Se observó una corrlación importante entre el precio y esta variable en el GEDA.",
        "ml_label": False,
        "pipeline": "num_pipe"
    },
    "Year RemodAdd": {
        "relevant": False,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 61,
        "data_obj_type": "int64",
        "notes": "No se observó una relación de esta variable y el precio de venta.",
        "ml_label": False,
        "pipeline": "-"
    },
    "Roof Style": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.0,
        "len_uniques": 6,
        "data_obj_type": "object",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "Roof Matl": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.0,
        "len_uniques": 4,
        "data_obj_type": "object",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "Exterior 1st": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.0,
        "len_uniques": 14,
        "data_obj_type": "object",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "Exterior 2nd": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.0,
        "len_uniques": 15,
        "data_obj_type": "object",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "Mas Vnr Type": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.01,
        "len_uniques": 5,
        "data_obj_type": "object",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "Mas Vnr Area": {
        "relevant": False,
        "data_default_type": "float64",
        "null_perc": 0.01,
        "len_uniques": 279,
        "data_obj_type": "float64",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "Exter Qual": {
        "relevant": True,
        "data_default_type": "object",
        "null_perc": 0.0,
        "len_uniques": 4,
        "data_obj_type": "category",
        "notes": "-",
        "ml_label": False,
        "pipeline": "cat_pipe"
    },
    "Exter Cond": {
        "relevant": True,
        "data_default_type": "object",
        "null_perc": 0.0,
        "len_uniques": 4,
        "data_obj_type": "category",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "Foundation": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.0,
        "len_uniques": 6,
        "data_obj_type": "object",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "Bsmt Qual": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.03,
        "len_uniques": 6,
        "data_obj_type": "object",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "Bsmt Cond": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.03,
        "len_uniques": 6,
        "data_obj_type": "object",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "Bsmt Exposure": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.03,
        "len_uniques": 5,
        "data_obj_type": "object",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "BsmtFin Type 1": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.03,
        "len_uniques": 7,
        "data_obj_type": "object",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "BsmtFin SF 1": {
        "relevant": False,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 609,
        "data_obj_type": "int64",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "BsmtFin Type 2": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.03,
        "len_uniques": 7,
        "data_obj_type": "object",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "BsmtFin SF 2": {
        "relevant": False,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 133,
        "data_obj_type": "int64",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "Bsmt Unf SF": {
        "relevant": False,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 680,
        "data_obj_type": "int64",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "Total Bsmt SF": {
        "relevant": True,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 646,
        "data_obj_type": "int64",
        "notes": "La matriz de correlación muestra claramente que hay una muy buena relación de esta variable y el precio de venta. (> 0.6)",
        "ml_label": False,
        "pipeline": "num_pipe"
    },
    "Heating": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.0,
        "len_uniques": 6,
        "data_obj_type": "object",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "Heating QC": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.0,
        "len_uniques": 5,
        "data_obj_type": "object",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "Central Air": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.0,
        "len_uniques": 2,
        "data_obj_type": "object",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "Electrical": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.0,
        "len_uniques": 4,
        "data_obj_type": "object",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "1st Flr SF": {
        "relevant": True,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 675,
        "data_obj_type": "int64",
        "notes": "La matriz de correlación muestra claramente que hay una muy buena relación de esta variable y el precio de venta. (> 0.6)",
        "ml_label": False,
        "pipeline": "num_pipe"
    },
    "2nd Flr SF": {
        "relevant": False,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 370,
        "data_obj_type": "int64",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "Low Qual Fin SF": {
        "relevant": False,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 17,
        "data_obj_type": "int64",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "Gr Liv Area": {
        "relevant": True,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 782,
        "data_obj_type": "int64",
        "notes": "La matriz de correlación muestra claramente que hay una muy buena relación de esta variable y el precio de venta. (> 0.6)",
        "ml_label": False,
        "pipeline": "num_pipe"
    },
    "Bsmt Full Bath": {
        "relevant": False,
        "data_default_type": "float64",
        "null_perc": 0.0,
        "len_uniques": 4,
        "data_obj_type": "int64",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "Bsmt Half Bath": {
        "relevant": False,
        "data_default_type": "float64",
        "null_perc": 0.0,
        "len_uniques": 3,
        "data_obj_type": "int64",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "Full Bath": {
        "relevant": False,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 5,
        "data_obj_type": "int64",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "Half Bath": {
        "relevant": False,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 3,
        "data_obj_type": "int64",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "Bedroom AbvGr": {
        "relevant": False,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 7,
        "data_obj_type": "int64",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "Kitchen AbvGr": {
        "relevant": False,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 3,
        "data_obj_type": "int64",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "Kitchen Qual": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.0,
        "len_uniques": 4,
        "data_obj_type": "object",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "TotRms AbvGrd": {
        "relevant": False,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 11,
        "data_obj_type": "int64",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "Functional": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.0,
        "len_uniques": 6,
        "data_obj_type": "object",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "Fireplaces": {
        "relevant": False,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 4,
        "data_obj_type": "int64",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "Fireplace Qu": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.47,
        "len_uniques": 6,
        "data_obj_type": "object",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "Garage Type": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.04,
        "len_uniques": 7,
        "data_obj_type": "object",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "Garage Yr Blt": {
        "relevant": False,
        "data_default_type": "float64",
        "null_perc": 0.04,
        "len_uniques": 96,
        "data_obj_type": "float64",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "Garage Finish": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.04,
        "len_uniques": 4,
        "data_obj_type": "object",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "Garage Cars": {
        "relevant": True,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 5,
        "data_obj_type": "int64",
        "notes": "La matriz de correlación muestra claramente que hay una muy buena relación de esta variable y el precio de venta. (> 0.6)",
        "ml_label": False,
        "pipeline": "num_pipe"
    },
    "Garage Area": {
        "relevant": True,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 399,
        "data_obj_type": "int64",
        "notes": "La matriz de correlación muestra claramente que hay una muy buena relación de esta variable y el precio de venta. (> 0.6)",
        "ml_label": False,
        "pipeline": "num_pipe"
    },
    "Garage Qual": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.04,
        "len_uniques": 5,
        "data_obj_type": "object",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "Garage Cond": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.04,
        "len_uniques": 6,
        "data_obj_type": "object",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "Paved Drive": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.0,
        "len_uniques": 3,
        "data_obj_type": "object",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "Wood Deck SF": {
        "relevant": False,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 248,
        "data_obj_type": "int64",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "Open Porch SF": {
        "relevant": False,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 188,
        "data_obj_type": "int64",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "Enclosed Porch": {
        "relevant": False,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 118,
        "data_obj_type": "int64",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "3Ssn Porch": {
        "relevant": False,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 17,
        "data_obj_type": "int64",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "Screen Porch": {
        "relevant": False,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 75,
        "data_obj_type": "int64",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "Pool Area": {
        "relevant": False,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 6,
        "data_obj_type": "int64",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "Pool QC": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 1.0,
        "len_uniques": 4,
        "data_obj_type": "object",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "Fence": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.8,
        "len_uniques": 5,
        "data_obj_type": "object",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "Misc Feature": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.95,
        "len_uniques": 5,
        "data_obj_type": "object",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "Misc Val": {
        "relevant": False,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 25,
        "data_obj_type": "int64",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "Mo Sold": {
        "relevant": False,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 12,
        "data_obj_type": "int64",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "Yr Sold": {
        "relevant": False,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 5,
        "data_obj_type": "int64",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "Sale Type": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.0,
        "len_uniques": 7,
        "data_obj_type": "object",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "Sale Condition": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.0,
        "len_uniques": 1,
        "data_obj_type": "object",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "Id": {
        "relevant": False,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 1203,
        "data_obj_type": "int64",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "SalePrice": {
        "relevant": False,
        "data_default_type": "float64",
        "null_perc": 0.0,
        "len_uniques": 1203,
        "data_obj_type": "float64",
        "notes": "This is the variable we are trying to predict.",
        "ml_label": True,
        "pipeline": "num_pipe"
    }
}



feat_dict = {
    "MSSubClass": {
        "relevant": False,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 15,
        "data_obj_type": "category",
        "notes": "Después de una exploración, se observó que no hay una relación clara entre las 16 categorías de la columna y el precio de venta.",
        "ml_label": False,
        "pipeline": "-"
    },
    "MSZoning": {
        "relevant": True,
        "data_default_type": "object",
        "null_perc": 0.0,
        "len_uniques": 7,
        "data_obj_type": "category",
        "notes": "-",
        "ml_label": False,
        "pipeline": "cat_pipe"
    },
    "LotFrontage": {
        "relevant": False,
        "data_default_type": "float64",
        "null_perc": 0.21,
        "len_uniques": 113,
        "data_obj_type": "float64",
        "notes": "Se realizó una gráfica scatter de esta variable y el precio de venta. No se observó una correlación relevante.",
        "ml_label": False,
        "pipeline": "-"
    },
    "LotArea": {
        "relevant": True,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 929,
        "data_obj_type": "int64",
        "notes": "-",
        "ml_label": False,
        "pipeline": "num_pipe"
    },
    "Street": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.0,
        "len_uniques": 2,
        "data_obj_type": "object",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "Alley": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.94,
        "len_uniques": 3,
        "data_obj_type": "object",
        "notes": "Tiene demasiados valores vacíos.",
        "ml_label": False,
        "pipeline": "-"
    },
    "LotShape": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.0,
        "len_uniques": 4,
        "data_obj_type": "object",
        "notes": "La descripción de los datos indica que no es una variable relevante. Se realizó GEDA también.",
        "ml_label": False,
        "pipeline": "-"
    },
    "LandContour": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.0,
        "len_uniques": 4,
        "data_obj_type": "object",
        "notes": "La descripción de los datos indica que no es una variable relevante. Se realizó GEDA también.",
        "ml_label": False,
        "pipeline": "-"
    },
    "Utilities": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.0,
        "len_uniques": 2,
        "data_obj_type": "object",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "LotConfig": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.0,
        "len_uniques": 5,
        "data_obj_type": "object",
        "notes": "La descripción de los datos indica que no es una variable relevante. Se realizó GEDA también.",
        "ml_label": False,
        "pipeline": "-"
    },
    "LandSlope": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.0,
        "len_uniques": 3,
        "data_obj_type": "object",
        "notes": "La descripción de los datos indica que no es una variable relevante. Se realizó GEDA también.",
        "ml_label": False,
        "pipeline": "-"
    },
    "Neighborhood": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.0,
        "len_uniques": 27,
        "data_obj_type": "object",
        "notes": "El autor explica que esta variable sería relevante si tuviéramos un mapa.",
        "ml_label": False,
        "pipeline": "-"
    },
    "Condition1": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.0,
        "len_uniques": 9,
        "data_obj_type": "object",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "Condition2": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.0,
        "len_uniques": 8,
        "data_obj_type": "object",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "BldgType": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.0,
        "len_uniques": 5,
        "data_obj_type": "object",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "HouseStyle": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.0,
        "len_uniques": 8,
        "data_obj_type": "object",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "OverallQual": {
        "relevant": True,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 10,
        "data_obj_type": "int64",
        "notes": "La matriz de correlación muestra claramente que hay una muy buena relación de esta variable y el precio de venta. (> 0.6)",
        "ml_label": False,
        "pipeline": "num_pipe"
    },
    "OverallCond": {
        "relevant": False,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 9,
        "data_obj_type": "int64",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "YearBuilt": {
        "relevant": True,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 108,
        "data_obj_type": "int64",
        "notes": "Se observó una corrlación importante entre el precio y esta variable en el GEDA.",
        "ml_label": False,
        "pipeline": "num_pipe"
    },
    "YearRemodAdd": {
        "relevant": False,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 61,
        "data_obj_type": "int64",
        "notes": "No se observó una relación de esta variable y el precio de venta.",
        "ml_label": False,
        "pipeline": "-"
    },
    "RoofStyle": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.0,
        "len_uniques": 6,
        "data_obj_type": "object",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "RoofMatl": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.0,
        "len_uniques": 4,
        "data_obj_type": "object",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "Exterior1st": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.0,
        "len_uniques": 14,
        "data_obj_type": "object",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "Exterior2nd": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.0,
        "len_uniques": 15,
        "data_obj_type": "object",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "MasVnrType": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.01,
        "len_uniques": 5,
        "data_obj_type": "object",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "MasVnrArea": {
        "relevant": False,
        "data_default_type": "float64",
        "null_perc": 0.01,
        "len_uniques": 279,
        "data_obj_type": "float64",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "ExterQual": {
        "relevant": True,
        "data_default_type": "object",
        "null_perc": 0.0,
        "len_uniques": 4,
        "data_obj_type": "category",
        "notes": "-",
        "ml_label": False,
        "pipeline": "cat_pipe"
    },
    "ExterCond": {
        "relevant": True,
        "data_default_type": "object",
        "null_perc": 0.0,
        "len_uniques": 4,
        "data_obj_type": "category",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "Foundation": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.0,
        "len_uniques": 6,
        "data_obj_type": "object",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "BsmtQual": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.03,
        "len_uniques": 6,
        "data_obj_type": "object",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "BsmtCond": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.03,
        "len_uniques": 6,
        "data_obj_type": "object",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "BsmtExposure": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.03,
        "len_uniques": 5,
        "data_obj_type": "object",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "BsmtFinType1": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.03,
        "len_uniques": 7,
        "data_obj_type": "object",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "BsmtFinSF1": {
        "relevant": False,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 609,
        "data_obj_type": "int64",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "BsmtFinType2": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.03,
        "len_uniques": 7,
        "data_obj_type": "object",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "BsmtFinSF2": {
        "relevant": False,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 133,
        "data_obj_type": "int64",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "BsmtUnfSF": {
        "relevant": False,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 680,
        "data_obj_type": "int64",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "TotalBsmtSF": {
        "relevant": True,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 646,
        "data_obj_type": "int64",
        "notes": "La matriz de correlación muestra claramente que hay una muy buena relación de esta variable y el precio de venta. (> 0.6)",
        "ml_label": False,
        "pipeline": "num_pipe"
    },
    "Heating": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.0,
        "len_uniques": 6,
        "data_obj_type": "object",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "HeatingQC": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.0,
        "len_uniques": 5,
        "data_obj_type": "object",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "CentralAir": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.0,
        "len_uniques": 2,
        "data_obj_type": "object",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "Electrical": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.0,
        "len_uniques": 4,
        "data_obj_type": "object",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "1stFlrSF": {
        "relevant": True,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 675,
        "data_obj_type": "int64",
        "notes": "La matriz de correlación muestra claramente que hay una muy buena relación de esta variable y el precio de venta. (> 0.6)",
        "ml_label": False,
        "pipeline": "num_pipe"
    },
    "2ndFlrSF": {
        "relevant": False,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 370,
        "data_obj_type": "int64",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "LowQualFinSF": {
        "relevant": False,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 17,
        "data_obj_type": "int64",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "GrLivArea": {
        "relevant": True,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 782,
        "data_obj_type": "int64",
        "notes": "La matriz de correlación muestra claramente que hay una muy buena relación de esta variable y el precio de venta. (> 0.6)",
        "ml_label": False,
        "pipeline": "num_pipe"
    },
    "BsmtFullBath": {
        "relevant": False,
        "data_default_type": "float64",
        "null_perc": 0.0,
        "len_uniques": 4,
        "data_obj_type": "int64",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "BsmtHalfBath": {
        "relevant": False,
        "data_default_type": "float64",
        "null_perc": 0.0,
        "len_uniques": 3,
        "data_obj_type": "int64",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "FullBath": {
        "relevant": False,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 5,
        "data_obj_type": "int64",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "HalfBath": {
        "relevant": False,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 3,
        "data_obj_type": "int64",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "BedroomAbvGr": {
        "relevant": False,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 7,
        "data_obj_type": "int64",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "KitchenAbvGr": {
        "relevant": False,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 3,
        "data_obj_type": "int64",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "KitchenQual": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.0,
        "len_uniques": 4,
        "data_obj_type": "object",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "TotRmsAbvGrd": {
        "relevant": False,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 11,
        "data_obj_type": "int64",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "Functional": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.0,
        "len_uniques": 6,
        "data_obj_type": "object",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "Fireplaces": {
        "relevant": False,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 4,
        "data_obj_type": "int64",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "FireplaceQu": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.47,
        "len_uniques": 6,
        "data_obj_type": "object",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "GarageType": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.04,
        "len_uniques": 7,
        "data_obj_type": "object",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "GarageYrBlt": {
        "relevant": False,
        "data_default_type": "float64",
        "null_perc": 0.04,
        "len_uniques": 96,
        "data_obj_type": "float64",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "GarageFinish": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.04,
        "len_uniques": 4,
        "data_obj_type": "object",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "GarageCars": {
        "relevant": True,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 5,
        "data_obj_type": "int64",
        "notes": "La matriz de correlación muestra claramente que hay una muy buena relación de esta variable y el precio de venta. (> 0.6)",
        "ml_label": False,
        "pipeline": "num_pipe"
    },
    "GarageArea": {
        "relevant": True,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 399,
        "data_obj_type": "int64",
        "notes": "La matriz de correlación muestra claramente que hay una muy buena relación de esta variable y el precio de venta. (> 0.6)",
        "ml_label": False,
        "pipeline": "num_pipe"
    },
    "GarageQual": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.04,
        "len_uniques": 5,
        "data_obj_type": "object",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "GarageCond": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.04,
        "len_uniques": 6,
        "data_obj_type": "object",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "PavedDrive": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.0,
        "len_uniques": 3,
        "data_obj_type": "object",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "WoodDeckSF": {
        "relevant": False,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 248,
        "data_obj_type": "int64",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "OpenPorchSF": {
        "relevant": False,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 188,
        "data_obj_type": "int64",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "EnclosedPorch": {
        "relevant": False,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 118,
        "data_obj_type": "int64",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "3SsnPorch": {
        "relevant": False,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 17,
        "data_obj_type": "int64",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "ScreenPorch": {
        "relevant": False,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 75,
        "data_obj_type": "int64",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "PoolArea": {
        "relevant": False,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 6,
        "data_obj_type": "int64",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "PoolQC": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 1.0,
        "len_uniques": 4,
        "data_obj_type": "object",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "Fence": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.8,
        "len_uniques": 5,
        "data_obj_type": "object",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "MiscFeature": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.95,
        "len_uniques": 5,
        "data_obj_type": "object",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "MiscVal": {
        "relevant": False,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 25,
        "data_obj_type": "int64",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "MoSold": {
        "relevant": False,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 12,
        "data_obj_type": "int64",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "YrSold": {
        "relevant": False,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 5,
        "data_obj_type": "int64",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "SaleType": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.0,
        "len_uniques": 7,
        "data_obj_type": "object",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "SaleCondition": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.0,
        "len_uniques": 1,
        "data_obj_type": "object",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "Id": {
        "relevant": False,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 1203,
        "data_obj_type": "int64",
        "notes": "-",
        "ml_label": False,
        "pipeline": "-"
    },
    "SalePrice": {
        "relevant": False,
        "data_default_type": "float64",
        "null_perc": 0.0,
        "len_uniques": 1203,
        "data_obj_type": "float64",
        "notes": "This is the variable we are trying to predict.",
        "ml_label": True,
        "pipeline": "num_pipe"
    }
}