import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

def main() :
    st.title('차트 그리기 1')
    df=pd.read_csv('Github/streamlit/streamlit_data/iris.csv')
    st.dataframe(df.head())
    
    # sepal_length와 sepla_width의 관계를 차트로 그리시오.
    fig = plt.figure()
    plt.scatter(data=df,x='sepal_length',y='sepal_width')
    plt.title('Sepal Length VS Sepal Width')
    plt.xlabel('sepal length')
    plt.ylabel('sepal width')
    st.pyplot(fig)

    fig2 = plt.figure()
    sb.regplot(data=df,x='sepal_length',y='sepal_width')
    st.pyplot(fig2)

    fig3 = plt.figure()
    plt.hist(data=df,x='petal_length',bins=10,rwidth=0.8)
    st.pyplot(fig3)

    fig4 = plt.figure(figsize=(10,4))
    plt.subplot(1,2,1)
    plt.hist(data=df,x='petal_length',bins=10,rwidth=0.8)

    plt.subplot(1,2,2)
    plt.hist(data=df,x='petal_length',bins=20,rwidth=0.8)
    st.pyplot(fig4)


    # df의 species 컬럼의 각 종별로 몇개의 데이터가 있는지
    # 차트로 나타내시오.

    fig5=plt.figure()
    df['species'].value_counts().plot(kind='bar')
    st.pyplot(fig5)

    fig6=plt.figure()
    df['petal_length'].hist()
    st.pyplot(fig6)


if __name__ == '__main__' :
    main()