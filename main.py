
import streamlit as st
import pandas as pd

st.title("Software Quality Assurance") 
st.markdown("**A Supporting Tool for Detecting defects in software requirements specification**")
with st.form(key='nlpForm'):
			Requirements = st.text_area("Enter Requirement")
			submit_button = st.form_submit_button(label='Detect defects')

df = pd.read_excel('Data_Set.xlsx')


Unbounded_Lists = df['Unbounded Lists'].values.tolist()
Unbounded_Lists_Coreect = df['Unbounded Lists correction'].values.tolist()

weak_words = df['weak words '].values.tolist()
weak_words_Coreect = df['weak words correction'].values.tolist()

ambiguity_optionality = df['Ambiguity optionality'].values.tolist()
ambiguity_optionality_Coreect = df['Ambiguity optionality correction'].values.tolist()

ambiguity_over_generalization = df['Ambiguity over generalization'].values.tolist()
ambiguity_over_generalization_Coreect = df['Ambiguity over generalization correction'].values.tolist()

col1,col2 = st.columns(2)
Coreect="null"

def Find_Defects(Requirements, list_of_words):
  global Coreect
  if any(element in Requirements for element in list_of_words)==True:
    
    if list_of_words==weak_words:
      for word in Requirements.split():
        if any(element in word for element in df['weak words '])== True :
          Coreect=df['weak words correction'].where(df['weak words ']== word ).dropna()
      return ('Bad',set(Requirements.split()).intersection(list_of_words),' weak words')

    elif list_of_words==Unbounded_Lists:
       for word in Requirements.split():
         if any(element in word for element in df['Unbounded Lists'])== True :
          Coreect=df['Unbounded Lists correction'].where(df['Unbounded Lists']== word ).dropna()
       return ('Bad',set(Requirements.split()).intersection(list_of_words),' Unbounded Lists')

    elif list_of_words==ambiguity_over_generalization:
      for word in Requirements.split():
        if any(element in word for element in df['Ambiguity over generalization'])== True :
          Coreect=df['Ambiguity over generalization correction'].where(df['Ambiguity over generalization']== word ).dropna()
      return ('Bad',set(Requirements.split()).intersection(list_of_words),' ambiguity generalization')

    elif list_of_words==ambiguity_optionality:
      for word in Requirements.split():
        if any(element in word for element in df['Ambiguity optionality'])== True :
          Coreect=df['Ambiguity optionality correction'].where(df['Ambiguity optionality']== word ).dropna()
      return ('Bad',set(Requirements.split()).intersection(list_of_words),' ambiguity optionality')
   



 
if submit_button:
  with col2:
    st.info("Correct examples")
  with col1:
      st.warning("Result")  
      if ((Find_Defects(Requirements,weak_words)is None) and (Find_Defects(Requirements,Unbounded_Lists)is None )and(Find_Defects(Requirements,ambiguity_over_generalization)is None) and (Find_Defects(Requirements,ambiguity_optionality)is None)):
        st.write("There are no Defects")
      else:
        if Find_Defects(Requirements,weak_words)is not None:
          st.write(Find_Defects(Requirements,weak_words))
          with col2:
           st.write(Coreect)
      
        if Find_Defects(Requirements,Unbounded_Lists)is not None:
          st.write(Find_Defects(Requirements,Unbounded_Lists))
          with col2:
           st.write(Coreect)

        if Find_Defects(Requirements,ambiguity_over_generalization)is not None:
          st.write(Find_Defects(Requirements,ambiguity_over_generalization))
          with col2:
           st.write(Coreect)

        if Find_Defects(Requirements,ambiguity_optionality)is not None:
          st.write(Find_Defects(Requirements,ambiguity_optionality))
          with col2:
           st.write(Coreect)
  


  
    



