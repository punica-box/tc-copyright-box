# tc-copyright-box

A box came from TC SHENZHEN Hackathon 2018. This box is contributed by [songroger](https://github.com/songroger).

     _  _         _        _   _               _____ ___ 
    | || |__ _ __| |____ _| |_| |_  ___ _ _   |_   _/ __|
    | __ / _` / _| / / _` |  _| ' \/ _ \ ' \    | || (__ 
    |_||_\__,_\__|_\_\__,_|\__|_||_\___/_||_|   |_| \___|
       ___  ___ ______    ______                __          
      |_  |/ _ <  ( _ )  / __/ /  ___ ___  ___ / /  ___ ___ 
     / __// // / / _  | _\ \/ _ \/ -_) _ \/_ // _ \/ -_) _ \
    /____/\___/_/\___/ /___/_//_/\__/_//_//__/_//_/\__/_//_/

## 简介

使用区块链的不可否认性，利用智能合约，解决版权的授权/验证问题。

- 版权物。版权物即版权标的物品，在此合约内，以唯一哈希值的形式存在。
- 权限。版权物的权限分为两种，使用权和所有权。所有权可以签发使用权，所有权可以进行转让，使用权不可转让。
- 验证。验证用户U对版权物C的权限，及所有权或使用权或无权限。

功能点：

- 版权签发

用户U1可以对自己的版权创作物C1进行签发，声明所有权。

- 版权转让

在用户U2付出等价物后，可以向用户U1购买版权C1，此时，所有权从U1转让至U2。

- 版权授权

版权C1的所有者U1可以对其他人如U3进行使用授权，授权后，U1对C1的所有权不变，U2获得C1的使用权。

- 版权收回

在到期后，U3拥有的C1使用权会自动取消。

- 版权验证

验证用户U1是否有对版权C1的所有权。

验证用户U2是否有对版权C1的所有权。

验证用户U3是否有队版权C1的使用权。

## 快速开始

### 创建运行环境

```shell
virtualenv --no-site-packages venv

.\venv\Scripts\activate

pip install -r requirements.txt
```

### 设置环境变量

更新 `project/server/config.py`，并运行：

```shell
export APP_SETTINGS="project.server.config.DevelopmentConfig"
```

或者

```sh
export APP_SETTINGS="project.server.config.ProductionConfig"
```

注意：如果以 `ProductionConfig` 来运行，需要首先设置在环境变量中设置 `MYSQL_PWD`：

```shell
export MYSQL_PWD="mysql pwd"
```

### 创建数据库

```shell
python manage.py create_db
python manage.py db init
python manage.py db migrate
python manage.py create_admin
python manage.py create_data
```

### 运行应用

```shell
python manage.py runserver
```

访问应用： [http://localhost:5000/](http://localhost:5000/)

如果希望指定端口，可以使用下面的命令：

```shell
python manage.py runserver -h 0.0.0.0 -p 8080
```

### 测试

- 无覆盖率测试:

```shell
python manage.py test
```

- 覆盖率测试:

```shell
python manage.py cov
```