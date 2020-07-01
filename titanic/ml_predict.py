def pred_model(pclass,sex,age,sibsp,parch,fare,embarked,title):
    import pickle
    x = [[pclass,sex,age,sibsp,parch,fare,embarked,title]]
    randomforest = pickle.load(open('titanic_model.sav','rb'))
    prediction = randomforest.predict(x)
    if prediction==1:
        return "Survived"
    else:
        return "Not Survived"
