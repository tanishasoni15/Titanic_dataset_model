import streamlit as st
import pandas as pd
import pickle

model = pickle.load(open("titanic_model.pkl", "rb"))

st.title("Titanic Survival Prediction")

pclass = st.selectbox("Passenger Class", [1, 2, 3])

sex = st.selectbox("Sex", ["male", "female"])

age = st.slider("Age", 1, 80, 25)

sibsp = st.slider("Siblings/Spouses Aboard", 0, 10, 0)

parch = st.slider("Parents/Children Aboard", 0, 10, 0)

fare = st.slider("Fare", 0, 500, 50)

embarked = st.selectbox("Embarked", ["C", "Q", "S"])

sex = 0 if sex == "male" else 1

embarked_c = 1 if embarked == "C" else 0
embarked_q = 1 if embarked == "Q" else 0
embarked_s = 1 if embarked == "S" else 0

input_data = pd.DataFrame({
    "Pclass": [pclass],
    "Sex": [sex],
    "Age": [age],
    "SibSp": [sibsp],
    "Parch": [parch],
    "Fare": [fare],
    "Embarked_C": [embarked_c],
    "Embarked_Q": [embarked_q],
    "Embarked_S": [embarked_s]
})

if st.button("Predict"):

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("Passenger Survived ✅")
    else:
        st.error("Passenger Did Not Survive ❌")
