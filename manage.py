from app.admin  import create_app, db
from flask_script import Manager, Shell
from flask_migrate import MigrateCommand
import config

# 需要创建和更新表时，引入对应的表类型


# 创建主程序和管理接口
app = create_app(config)
manager = Manager(app)


def make_shell_context():
    return dict(app=app, db=db)


manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)
'''
启动命令：
    runserver

数据库命令：
    install    创建数据库文件
    migrate    迁移数据库操作 
    upgrade    更新数据库内容
    downgrade  撤销数据库操作
'''
if __name__ == '__main__':
    manager.run()