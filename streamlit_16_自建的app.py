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
protocol_list = 'HTTP', 'ICMP', 'SSH', 'SMTP'
counts = [15, 30, 45, 10]
explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'ICMP')

fig1, ax1 = plt.subplots()
ax1.pie(counts,
        explode=explode,
        labels=protocol_list,
        autopct='%1.1f%%',
        shadow=True,
        startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

st.pyplot(fig1)
