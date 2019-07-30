# Luogu-Difficulty-Tag 洛谷难度标签 <small>for Typecho</small>


[![Travis](https://img.shields.io/travis/Llf0703/Luogu-Difficulty-Tag.svg?style=flat-square)](https://travis-ci.org/Llf0703/Luogu-Difficulty-Tag)
![](https://img.shields.io/badge/php-7.0-4F5B93.svg?style=flat-square)
![](https://img.shields.io/badge/typecho->=0.9-467b96.svg?style=flat-square)
[![](https://img.shields.io/badge/LICENSE-GPL3.0-orange.svg?style=flat-square)](https://github.com/Llf0703/Luogu-Difficulty-Tag/blob/master/LICENSE)

## 使用方法

### 安装依赖

```
pip install -r requirements.txt
```

### 运行爬虫

先按注释说明修改 `config.yml` 中的设置，然后

```
python3 main.py
```

### 部署


写为php：适用于不会操作数据库的情况，会自动生成 `luogu.php`。

写为csv：会大幅度提升查询速度，方便管理。

将 `typecho-model-csv.php` 重命名为 `luogu.php`。

将 `data.csv` 上传至数据库 `typecho`，注意首行为数据表字段名。然后将数据表重命名为 `typecho_ldt` 。

---

将 `luogu.php` 放入主题文件夹中。先在主题的头部引入 `css/luogu.css` ，然后在需要显示的地方加上

```php
<?php $this->need('luogu.php'); ?>
```

## TODO

- [x] Mysql部署版本
- [ ] 自动上传至指定数据库
- [x] SPOJ,Codeforces,AtCoder的支持

## Update

- 2019.1.30：添加对自定义字段的验证，不会出现不写字段而有尚无评定tag的情况。
- 2019.4.14：增强爬虫鲁棒性，更新数据。
- 2019.7.30：针对洛谷新版页面更新爬虫，完全重构项目。

## LICENSE

GPL 3.0

> 在 [a517364](https://github.com/Llf0703/Luogu-Difficulty-Tag/commit/a517364feda8cec8fb8b547db4ebb7ac926185c1) 之前的代码使用 MIT 进行授权。