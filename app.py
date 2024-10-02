import streamlit as st
import pandas as pd
import joblib

# 加载模型
@st.cache(allow_output_mutation=True)
def load_model():
    return joblib.load('gbr_model.pkl')

# 应用标题
st.title("GBR 模型预测应用")

# 输入参数
st.sidebar.header('输入参数')

def user_input_features():
    feature1 = st.sidebar.number_input('特征 1')
    feature2 = st.sidebar.number_input('特征 2')
    # 添加更多特征...
    
    data = {
        'feature1': feature1,
        'feature2': feature2,
        # 添加更多特征...
    }
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

# 显示输入参数
st.subheader('输入的参数')
st.write(df)

# 加载模型并进行预测
model = load_model()
prediction = model.predict(df)

# 显示预测结果
st.subheader('预测结果')
st.write(prediction)
