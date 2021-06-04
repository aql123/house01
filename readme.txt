项目所使用的技术：
python、Django、MySQL
项目运行环境：
pycharm、anaconda3、mysql
搭建环境操作步骤：
Anacomda3环境搭建：
    1.进入Anadomda官网：Anaconda | The World's Most Popular Data Science Platform，选择适合自己的版本下载。
    2.打开安装包，点击“I Agree”。
    3.选择“All Users”，点击“next”
    4.选择安装目录。
    5.勾选Add Anaconda to my PATH environment variable和Register Anaconda as my default Python 3.5 
    6.install默认安装即可
pycharm环境搭建：
    1.进入pycharm官网：https://www.jetbrains.com/pycharm/，选择适合自己的版本下载。
    2.打开安装包，点击“next”。
    3.选择安装目录。
    4.选择适合自己的系统位数。系统32位就选32-bit,系统64位就选64-bit。
    5.install默认安装即可。
    6.打开pycharm.
    7.选择filev→settings→project settings→Python Interpreter→选择Anacomda3→OK。
MySQL环境搭建：
    1.下载MySQL：https://dev.mysql.com/downloads/（官网）
安装MySQL
    2.运行安装包，选择安装类型， 选择安装的产品， 执行安装， 安装完成，进行下一步，execute他们，执行下一步，继续next，在配置子菜单中，一直next
继续下一步，next，输入数据库密码，设置服务的名称，一般还用mysql，还有开机启动服务的开关，安装这些东西，finish后回到主菜单，依然next，最后结束。
或者：直接下载PHPstudy，该程序包集成最新的Apache+PHP+MySQL+phpMyAdmin+ZendOptimizer,一次性安装,无须配置即可使用。
启动系统：
1.启动数据库
2.打开项目进入demo目录下
3.在demo文件夹下执行python manage.py runserver

账号：admin    密码：123456