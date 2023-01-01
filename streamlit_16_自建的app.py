import streamlit as st
from datetime import datetime, timedelta
from random import randint
import pandas as pd
import matplotlib.pyplot as plt

st.title('我的第一个Streamlit APP')

# 第一部分: MarkDown测试
"""
### markdown 
[markdown学习](https://www.runoob.com/markdown)
***
- _斜体_
- **加粗**
- ___斜体加粗___
***
> 区块
> + line1
> + line2
>> + line3
>> + line4
***

### 图片测试  

![QYTANG LOGO](https://www.qytang.com/Public/home/images/logo0.png "QYTANG")
***
"""


# 缓存计算结果
@st.cache
def return_cpu(hours):
    now = datetime.now()
    x_datetime_list = []
    r1_y_cpu_list = []
    r2_y_cpu_list = []
    for i in range(hours):
        x_datetime_list.append(now + timedelta(hours=i+1))
        r1_y_cpu_list.append(randint(0, 100))
        r2_y_cpu_list.append(randint(0, 100))
    df = pd.DataFrame({
        'datetime': x_datetime_list,
        'R1': r1_y_cpu_list,
        'R2': r2_y_cpu_list,
    })

    df = df.set_index('datetime')

    return df


hours = st.slider('hours')

# 获取数据
# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = return_cpu(hours)
# Notify the reader that the data was successfully loaded.
data_load_state.text('Loading data...done!')

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

# MarkDown Emoji
# https://gist.github.com/rxaviers/7360908
st.subheader('CPU利用率线形图:sheep:')
st.line_chart(data)


# 饼状图:
st.subheader('协议分布饼状图:smiling_imp:')
protocol_list = ['HTTP', 'ICMP', 'SSH', 'SMTP']
counts = [15, 30, 45, 10]
explode = (0, 0.1, 0, 0)  # 裂开的度(我们用第二个ICMP为例)

fig1, ax1 = plt.subplots()
ax1.pie(counts,  # 数量的列表
        explode=explode,  # 裂开效果的列表
        labels=protocol_list,  # 分类的列表
        autopct='%1.1f%%',  # 精确刀小数点后面1位
        shadow=True,  # 有阴影
        startangle=90)  # 从90度开始逆时针排布
ax1.axis('equal')  # 长和宽相等, 确保是一个正圆

# 绘制饼状图
st.pyplot(fig1)
