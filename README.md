### Vue + Django REST framework 前后端分离的大型电商项目

#### 项目介绍

- 本项目是一个网上生鲜超市，可以完成加购物车，收藏，下单，结算等购物的相关功能，本项目采用手机号动态验证码注册，支付宝支付，第三方登录等功能，为大家提供了一个完美的大型电商超市。

#### 项目知识点

- xadmin后台管理系统
- 使用Vue框架搭建的前端
- Django框架
- REST framework前后端分离
- 富文本DjangoUeditor
- Mysql数据库（数据库内容我已经导出为sql文件）

#### 项目环境

> 后端

- Python3.5
- Windows10
- 项目使用到的库，都在requirement.txt文件中，建立好虚拟环境之后，执行`pip install -r requirement.txt`命令即可。

> 前端

- 安装node.js
- 安装cnpm
- 安装vue-cli
- 执行`npm run dev`命令启动前端程序



#### 项目注意点

- 创建项目
    - 使用pycharm创建项目的时候一定不要勾选使用admin，本项目使用的是xadmin
    - 在settings里面需要替换系统的用户```AUTH_USER_MODEL = 'users.UserProfile'```
    - 使用的xadmin文件一定要复制我文件中的，原生的xadmin我做了修改

- 创建应用
    - 使用命令创建应用goods，trade，users，user_operation，
    - 项目中我是把应用放在了apps这个包里面，所以在settings注册的时候一定要加上apps这个包名


- 导入数据
    - 一定不要忘记在settings里面先初始化路径
    - 执行脚本文件进行导入数据，一定要先执行category文件，导入类别，再导入商品
    - 导入的时候可能会报错
    ```
    django.core.exceptions.ImproperlyConfigured: Requested setting UEDITOR_SETTINGS, but settings are not configured. You must either define the environment variable DJANGO_SETTINGS_MODULE or call settings.configure() before accessing settings.
    ```
    是因为导入的位置不对，```from apps.goods.models import GoodsCategory```导入的位置一定不能出错


- 跨域问题
    - 使用的服务器配置解决跨域问题，在前端也可以实现
    - 在settings里面设置csrf，配置好跨域


- 后台数据
    - 添加首页数据时，品牌，每个分类一定要大于等于3个品牌，显示出来比较好看
    - 新品最好显示2个
    - 首页商品广告是指的首页中那个每个分类后面的大图片，必须要在后台添加了数据才可以显示，一定要注意



















