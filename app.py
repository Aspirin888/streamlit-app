import streamlit as st
import pandas as pd
import joblib

# 加载GBR模型
@st.cache(allow_output_mutation=True)
def load_model():
    return joblib.load('gbr_model.pkl')

# 应用标题
st.title("氧化锌胶体粒径预测")

# 输入参数
st.sidebar.header('输入参数')

def user_input_features():
    CZn = st.sidebar.number_input('CZn (mol/l)', min_value=0.0, max_value=10.0, value=0.0)
    Calkali = st.sidebar.number_input('Calkali (mol/l)', min_value=0.0, max_value=10.0, value=0.0)
    Molar_ratio = st.sidebar.number_input('Molar_ratio (摩尔比)', min_value=0.0, max_value=10.0, value=0.0)
    Temperature = st.sidebar.number_input('Temperature (K)', min_value=0, max_value=100, value=25)
    Time = st.sidebar.number_input('Time (min)', min_value=0, max_value=800, value=10)
    
    data = {
        'CZn': CZn,
        'Calkali': Calkali,
        'Molar_ratio': Molar_ratio,
        'Temperature': Temperature,
        'Time': Time
    }
    features = pd.DataFrame(data, index=[0])
    return features

# 获取输入数据
input_df = user_input_features()

# 显示输入的参数
st.subheader('输入的参数')
st.write(input_df)

# 加载模型并进行预测
model = load_model()
prediction = model.predict(input_df)

# 显示预测结果
st.subheader('预测的Average_size (平均粒径)')
st.write(prediction)
