# importing necessary libraries
import joblib
import pandas as pd
import streamlit as st


#load the model
KMeansCls = joblib.load('cluster.pkl')

#page configuration
st.set_page_config(page_title = 'Customer Behaviour Analysis Web App', layout='centered')
st.title('CUSTOMER BEHAVIOR ANALYSIS',layout = 'center')

# customer segmentation function
def segment_customers(input_data):
    
    prediction=KMeansCls.predict(pd.DataFrame(input_data, columns=['Income', 'Age', 'Month_Customer', 'TotalSpendings', 'Children']))
    print(prediction)
    pred_1 = 0
    if prediction == 0:
            pred_1 = 'Highly Active'

    elif prediction == 1:
            pred_1 = 'Moderately Active'

    elif prediction == 2:
            pred_1 = 'Least Active'

    return pred_1
def main():
    
    
    st.image("""https://www.araya.org/wp-content/uploads/2021/04/in-store-marketing.jpg""")
    Income = st.text_input("Type In The Household Income")
    Children = st.radio( "Select Number Of children In Household",('0', '1','2','3') )
    #Month_Customer = st.text_input( "Type In The Month of customer's enrollment with the company")
    Month_Customer = st.number_input("Month of customer's Enrollment",1,12)
    Age = st.slider( "Select Age",18,85)
    TotalSpendings= st.text_input( "Type In The TotalSpendings")
    

    
    
    result = ""

    
    if st.button("Click Here"):
        result=segment_customers([[Income,Age,Month_Customer,TotalSpendings,Children]])
    
    st.success(result)
if __name__ == '__main__':
        main ()






