import streamlit as st
# st.title("mehdi")
# col1,col2=st.columns(2)
# with col1:
    
#     st.write("hello")
#     my_bt=st.button("click me")
#     if my_bt:
#         st.write("سلام")
#     else:
#         st.write("بای")
#     st.text_input("firstname")
#     st.text_input("lastname")

# col1=st.columns(1)
# with col1:
weight=st.number_input("enter weight(KG):")
height=st.number_input("enter height(CM):")
my_bt2=st.button("calculate BMI")
if my_bt2:
    bmi=weight/((height/100)**2)
    st.info(bmi)
    if bmi<18.5:
        st.write("به خودت برس داری میمیری")
        st.image("./pages/pic/thin.jpeg") 
    elif 18.5 < bmi < 25:
        st.write('این تیپ درسته عین خودمی')
        st.image("./pages//pic/handsome.jpeg") 
    elif 25< bmi:
        st.write ("نترکی از چاقی صلوات")
        st.image("./pages//pic/fat.jpeg") 
