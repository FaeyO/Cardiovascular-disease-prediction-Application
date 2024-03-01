import pickle
import streamlit as st
import sys
from pathlib import Path
#import path


#dir = path.Path(__file__).abspath()
#sys.path.append(dir.parent.parent)
# Add parent directory to sys.path
dir = Path(__file__).resolve().parent.parent
sys.path.append(str(dir))

model = pickle.load(open('C:\\Users\\USER\\Desktop\\ML_projects\\Cardio_data\\LGBM_model.pkl','rb'))

def main():
    st.set_page_config(page_title="Cardiovascular disease prediction App")

    st.title("Cardiovascular disease prediction App")

    form = st.form('CVD')

    Age = form.number_input('Age', min_value=1, max_value=100, value=35)
    Height = form.number_input('Height', min_value=40.0, max_value=250.0, value=164.0)
    Weight = form.number_input('Weight', min_value=10.0, max_value=200.0, value=74.0)
    Systolic = form.slider('Systolic', min_value=30, max_value=200, value=120)
    Diastolic = form.slider('Diastolic', min_value=50, max_value=180, value=80)
    Gender = form.text_input('Gender (Male:1, Female:0)')
    Cholesterol_normal = form.text_input('Cholesterol Normal(Yes:1, No:0)')
    Cholesterol_very_high = form.text_input('Cholesterol very high(Yes:1, No:0)')
    Glucose_normal = form.text_input('Glucose Normal(Yes:1, No:0)')
    Glucose_very_high = form.text_input('Glucose very high(Yes:1, No:0)')
    Smoke = form.text_input('Smoke (Yes:1, No:0)')
    Alcohol = form.text_input('Alcohol (Yes:1, No:0)')
    Physical_Activity = form.text_input('Physical Activity (Yes:1, No:0)')
    
    if form.form_submit_button('Predict'):
        # Convert non-numeric features to numeric data types
        Age = int(Age)
        Height = int(Height)
        Weight = int(Weight)
        Systolic = int(Systolic)
        Diastolic = int(Diastolic)
        Gender = int(Gender)  #Gender is encoded as numeric values (e.g., Male: 1, Female: 0)
        Cholesterol_normal = int(Cholesterol_normal)
        Cholesterol_very_high = int(Cholesterol_very_high)
        Glucose_normal = int(Glucose_normal)
        Glucose_very_high = int(Glucose_very_high)
        Smoke = int(Smoke)
        Alcohol = int(Alcohol)
        Physical_Activity = int(Physical_Activity)


        makepredictions = model.predict([[Age,Height,Weight,Systolic,Diastolic,Gender,Cholesterol_normal,Cholesterol_very_high,
                                          Glucose_normal,Glucose_very_high,Smoke,Alcohol,Physical_Activity
                                          ]])

        output = round(int(makepredictions[0]))


        st.success("Your predicted Cardiovascular disease status is {}".format(output))

        
if __name__ == '__main__':
    main()
