import os

basedir = os.path.abspath(os.path.dirname(__file__))

# 默认的本地数据库
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database.db')

# mssql：佛山西的指纹数据库，oracle：原来的指纹数据库
SQLALCHEMY_BINDS = {'mssql': 'mssql+pyodbc://sa:sa2005@10.172.36.223:1433/AccessData?driver=SQL+Server',
                    'mssql_pi': 'mssql+pyodbc://sa:sa2005@10.172.36.223:1433/PersonInfo?driver=SQL+Server',
                    'oracle': 'oracle+cx_oracle://XXGL:xxgl@10.172.36.221:1521/ORCL'}
# 数据库信息反馈关闭
SQLALCHEMY_TRACK_MODIFICATIONS = False

# 启用CSSRP和密匙
CSPR_ENABLED = True
SECRET_KEY = 'Devil_never_cry'

DEBUG = True
