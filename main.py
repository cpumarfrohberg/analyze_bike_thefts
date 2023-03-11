import pickle, time, logging
from warnings import filterwarnings
filterwarnings(action='ignore')

import pandas as pd

from sklearn.metrics import f1_score, confusion_matrix, roc_auc_score

logging.basicConfig(level = logging.DEBUG)

from utils import DataModeler, WEIGHTS


def main():
    model_data = DataModeler()
    prepped_data = model_data.prepare_data()
    split_dict = model_data.split_timestamp_data(X = prepped_data['feature_matrix'], 
                                                y = prepped_data['labels'])
    X_train, X_val, y_train, y_val = (split_dict['X_train_fe'], split_dict['X_val_fe'], 
                                    split_dict['y_train'], split_dict['y_val'])
    
    time.sleep(2)
    logging.debug("model fit on X_train and X_val")
    clf_LR = model_data.model_fit(
        X_train = X_train, 
        y_train = y_train,
        weights=WEIGHTS
        )
    
    time.sleep(2)
    logging.debug("making predictions on X_train and X_val")
    pred_X_train = model_data.predictions(
        fit_model = clf_LR,
        X = X_train
        )
    pred_X_val = model_data.predictions(
        fit_model = clf_LR,
        X = X_val
        )
    
    f1_score_train = f1_score(y_train, pred_X_train).round(2)
    f1_score_val = f1_score(y_val, pred_X_val).round(2)

    time.sleep(2)
    logging.info(f"The f1 - score based on training set is: {(f1_score_train).round(2)}")
    time.sleep(2)
    logging.info(f"The f1 - score based on validation set is: {(f1_score_val).round(2)}")

    time.sleep(2)   
    logging.info(f"Confusion Matrix on validation set: \n{confusion_matrix(y_val, pred_X_val)}")
    time.sleep(2)   
    logging.info(f"Area Under Curve (validation set): {roc_auc_score(y_val, pred_X_val).round(2)}")

    time.sleep(1)   
    logging.info("saving full model")
    with open("./artifacts/churn-model.bin", "wb") as f_out:
        pickle.dump(clf_LR, f_out) 
    time.sleep(2)   
    logging.info("full model saved as churn-model.bin")

if __name__ == "__main__":
    main()
    
    

    





