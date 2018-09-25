配置说明
==========

## 需要的包

* nginx
* python3.6
* virtualenv + pip
* git

以 ubuntu 为例:
```bash
sudo apt-get install nginx git python3 python3-venv
```

fix pip error
```bash
#   pip broken by 'NewConnectionError
#   解决这个问题
#   sudo vi /ect/resolv.conf
#   servername 8.8.8.8
#   servername 114.114.114.114
```

## nginx 配置
* 参考 gunicorn-upstart.template.conf
* 把 sitename 替换成所需要的域名 for instance: www.oocoding.com

## 创建文件结构
假设存在的用户帐号是 /home/username

```
/home/username
        |
        |----sitename
                |--------- database
                |--------- source
                            |--------- manager.py
                            |--------- others
                |--------- static
                |--------- virtualenv
```

## 使用fab 实现部署
在过渡服务器的基础上进行生产部署，因为过渡服务器已经安装好了可用的 python3 pip fabric3等环境可以。

* 执行 pip 安装指令 *pip install fabric3*
* 创建 *fabfile.py*
* 在 fabfile.py 的路径下，执行自动部署指令 *fab deploy:host=www.oocoding.com*

上面基本都是套路， deploy 是 fabfile.py 的自定义方法，后面跟随参数，指定了 env.host 环境变量
        
## 部署后，配置 nginx 和 gunicorn

* 使用 nginx_setting.txt 模板替换到目标地址,将SITENAME 替换成 *www.oocoding.com*
* 使用到 gunicorn.template.service

```bash
$ sed "s/SITENAME/www.oocoding.com/g" \
source/deploy_tools/nginx.template.conf \
| sudo tee /etc/nginx/sites-available/superlists.com

$ sudo ln -s  /etc/nginx/sites-available/superlists.com \
/etc/nginx/sites-enabled/superlists.com

$ sed "s/SITENAME/www.oocoding.com/g" \
source/deploy_tools/gunicorn.template.service \
| sudo tee /etc/systemd/system/gunicorn-superlists.service

$ sudo systemctl daemon-reload
$ sudo systemctl reload nginx
$ sudo systemctl enable gunicorn-superlists.service
$ sudo systemctl start gunicorn-superlists.service
# systemctl list-units --type=service 可查看启动过的服务

```
