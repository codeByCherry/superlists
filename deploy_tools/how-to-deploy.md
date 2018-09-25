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
        
