import streamlit as st
import pandas as pd

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })

option1 = st.selectbox(
    'Which number do you like best?',
     df['first column'])

option2 = st.selectbox(
    'Which number do you like best?',
     df['second column'])

'You selected First: ', option1
'You selected Second: ', option2