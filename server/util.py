__author__ = 'maheshwickramasinghe'

import pandas as pd
import pickle

def predict_prob_compliance(fine, discount, judgment_amount, late_fee):

    with open('./model/blight_ticket_violation_model.pickle', 'rb') as file:
        model = pickle.load(file)

    compliance = 'Low'
    df = pd.DataFrame({"fine_amount":[fine],
                      "discount_amount": [discount],
                      "judgment_amount": [judgment_amount],
                      "late_fee": [late_fee],
                      "total": [fine + judgment_amount - discount + late_fee]
                     })
    #this order of feature is very important
    df = df[['fine_amount', 'discount_amount', 'judgment_amount', 'late_fee', 'total']]
    pred_prob = round(model.predict_proba(df)[:,1][0], 4)

    if pred_prob >= 0.65:
        compliance = 'High'
    elif pred_prob >= 0.45:
        compliance = 'Moderate'

    return compliance
    