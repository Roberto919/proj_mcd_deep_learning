## MODULE WITH ML RELATED PARAMETERS AND FUNCTIONALITIES.





"------------------------------------------------------------------------------"
#############
## Imports ##
#############


from sklearn.preprocessing import (
    OrdinalEncoder,
    StandardScaler,
    OneHotEncoder
)

from sklearn.pipeline import Pipeline

from d2l import tensorflow as d2l
import tensorflow as tf





"------------------------------------------------------------------------------"
###################
## ML Parameters ##
###################


## Number of cross validations
cv_rounds = 10

## Grid Search CV - Parameters grid
param_grid = [
    {
        "n_estimators": [50, 100, 150, 500],
        "max_features": [2, 4, 6, 8]
    },
    {
        "bootstrap": [False],
        "n_estimators": [3, 10],
        "max_features": [2, 3, 4]
    }
]

## Model parameters
#### Random forest regressor
max_features = 6
n_estimators = 100



## Neural network parameters
loss = tf.keras.losses.MeanSquaredError()

k = 5
num_epochs = 100
lr = 5
weight_decay = 0
batch_size = 64




"------------------------------------------------------------------------------"
##############
## Pipeline ##
##############


## Numerical pipeline.
num_pipeline = Pipeline([
        ("std_scaler", StandardScaler()),
    ])

## Categorical pipeline
cat_pipeline = Pipeline([
        ("one_hot_encoder", OneHotEncoder()),
    ])





"------------------------------------------------------------------------------"
############
## Models ##
############


##
def get_net():
    net = tf.keras.models.Sequential()
    net.add(tf.keras.layers.Dense(
        1, kernel_regularizer=tf.keras.regularizers.l2(weight_decay)))
    return net



##
def log_rmse(y_true, y_pred):
    # To further stabilize the value when the logarithm is taken, set the
    # value less than 1 as 1
    clipped_preds = tf.clip_by_value(y_pred, 1, float('inf'))
    return tf.sqrt(tf.reduce_mean(loss(tf.math.log(y_true), tf.math.log(clipped_preds))))



##
def train(net, train_features, train_labels, test_features, test_labels, num_epochs, learning_rate, weight_decay, batch_size):
    train_ls, test_ls = [], []
    train_iter = d2l.load_array((train_features, train_labels), batch_size)
    # The Adam optimization algorithm is used here
    optimizer = tf.keras.optimizers.Adam(learning_rate)
    net.compile(loss=loss, optimizer=optimizer)
    for epoch in range(num_epochs):
        for X, y in train_iter:
            with tf.GradientTape() as tape:
                y_hat = net(X)
                l = loss(y, y_hat)
            params = net.trainable_variables
            grads = tape.gradient(l, params)
            optimizer.apply_gradients(zip(grads, params))
        train_ls.append(log_rmse(train_labels, net(train_features)))
        if test_labels is not None:
            test_ls.append(log_rmse(test_labels, net(test_features)))
    return train_ls, test_ls



##
def get_k_fold_data(k, i, X, y):
    """ Extraemos el bloque i de los k posibles """
    assert k > 1
    fold_size = X.shape[0] // k
    X_train, y_train = None, None
    for j in range(k):
        idx = slice(j * fold_size, (j + 1) * fold_size)
        X_part, y_part = X[idx, :], y[idx]
        if j == i:
            X_valid, y_valid = X_part, y_part
        elif X_train is None:
            X_train, y_train = X_part, y_part
        else:
            X_train = tf.concat([X_train, X_part], 0)
            y_train = tf.concat([y_train, y_part], 0)
    return X_train, y_train, X_valid, y_valid



##
def k_fold(k, X_train, y_train, num_epochs, learning_rate, weight_decay, batch_size):
    """ Regresamos la perdida promedio de entrenamiento y validacion """
    train_l_sum, valid_l_sum = 0, 0
    for i in range(k):
        data = get_k_fold_data(k, i, X_train, y_train)
        net = get_net()
        train_ls, valid_ls = train(net, *data, num_epochs, learning_rate,
                                   weight_decay, batch_size)
        train_l_sum += train_ls[-1]
        valid_l_sum += valid_ls[-1]
        if i == 0:
            d2l.plot(list(range(1, num_epochs + 1)), [train_ls, valid_ls],
                     xlabel='epoch', ylabel='rmse', xlim=[1, num_epochs],
                     legend=['train', 'valid'], yscale='log')

        # Imprime la perdida en la iteracion i. Es decir, la perdida de
        # entrenamiento con los K-1 bloques que se usaron para entrenar
        # y el i-esimo bloque se uso para validar

        print(f'fold {i + 1}, train log rmse {float(train_ls[-1]):f}, '
              f'valid log rmse {float(valid_ls[-1]):f}')

    return train_l_sum / k, valid_l_sum / k



##
def train_and_pred(train_features, test_feature, train_labels, test_data, num_epochs, lr, weight_decay, batch_size):
    net = get_net()
    train_ls, _ = train(net, train_features, train_labels, None, None,
                        num_epochs, lr, weight_decay, batch_size)
    d2l.plot(np.arange(1, num_epochs + 1), [train_ls],
             xlabel='epoch',
             ylabel='log rmse',
             xlim=[1, num_epochs],
             yscale='log')
    print(f'train log rmse {float(train_ls[-1]):f}')
    # Apply the network to the test set
    preds = net(test_features).numpy()
    # Reformat it to export to Kaggle
    test_data['SalePrice'] = pd.Series(preds.reshape(1, -1)[0])
    submission = pd.concat([test_data['Id'], test_data['SalePrice']], axis=1)
    submission.to_csv('submission.csv', index=False)