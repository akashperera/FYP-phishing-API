
import pickle
from Feature_Extractor import extract_features
import numpy as np


def get_prediction(url, model_path):

    file = open(model_path, "rb")
    model = pickle.load(file)
    file.close()

    url_features = np.array (extract_features(url)) .reshape(1,16)
    print(url_features)

 
    prediction = model.predict(url_features)
    prob_phishing = model.predict_proba(url_features)[0,1]
    prob_non_phishing = model.predict_proba(url_features)[0,0]
    
    print(prediction[0])

    label = ''
    if (prediction[0] == 0):
        print(prob_non_phishing)
        print("non phish")
        label =  pred = "It is {0:.2f} % safe to go ".format(prob_non_phishing*100)
    else:
        print(prob_phishing)
        print("phish")
        label =  pred = "It is {0:.2f} % unsafe to go ".format(prob_phishing*100)

    i = round(prob_non_phishing * 100,3)
    print(label)
    print("There is ",i,"% chance,the url is malicious !")

    return {'ypred': str(prediction[0]),
                        'y_pro_phishing': str(prob_phishing),
                        'y_pro_non_phishing': str(prob_non_phishing),
                        'label': str(label)
                        }

#print(get_prediction("https://www.google.com", ""))