import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.types import NVARCHAR, Float, Integer

# dtypedict = {
#     'freq_dc': Float()
# }
# 初始化数据库连接，使用pymysql模块
# MySQL的用户：root, 密码:147369, 端口：3306,数据库：test
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:as3232141*@127.0.0.1:3306/gushiyi?charset=utf8'
# SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@127.0.0.1:3306/agine_test?charset=utf8'

engine = create_engine(SQLALCHEMY_DATABASE_URI)

path = './data/zufang.xlsx' # p_sv
# sheet_name 表示在excel里的第几张工作表 从0开始，表里的header要和数据库的表头对上
df = pd.read_excel(io=path)
#将需要特定的列转换数据类型 有时候不是那么智能，所以要强制转换
# df[['freq_dc', 'freq_sc']] = df[['freq_dc', 'freq_sc']].apply(pd.to_numeric)
 #p_seq_data_qc 表名 ，index=False 不使用df的索引
df.to_sql('poll_info', engine, index=True,if_exists='append')  #replace 会替换表结构