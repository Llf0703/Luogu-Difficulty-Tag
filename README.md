# Luogu-Difficulty-Tag 洛谷难度标签 <small> for typecho</small>

![](https://img.shields.io/badge/php-7.0-4F5B93.svg?style=flat-square)
![](https://img.shields.io/badge/typecho-1.2-467b96.svg?style=flat-square)
![](https://img.shields.io/badge/AmazeUI-2.4.2-10a0ea.svg?style=flat-square)
![](https://img.shields.io/badge/LICENSE-MIT-brightgreen.svg?style=flat-square)
![](https://img.shields.io/badge/update-2019.4.14-orange.svg?style=flat-square)

## 项目结构

```
.
├── luogu.py
├── luogu.php
├── README.md
├── LICENSE
├── css
    └── luogu.css
└── api
    └── luogu.php
```

``luogu.php``是主体文件，``luogu.py``是爬虫，``api/``是api所在文件夹。

## 使用方法

**需要一个搭建好的typecho博客。**

1. 将``luogu.php``放入主题文件夹``/usr/theme/xxx/``中
2. 在``head``中引入AmazeUI2.4.2或更高的css

```html
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/amazeui/2.7.2/css/amazeui.css">
```

3. 引入``css/luogu.css``

```html
<link rel="stylesheet" href="css/luogu.css">
```

4. 在需要放置标签的地方写

```php
<?php $this->need('luogu.php')?>
```

如我的``index.php``:

> 在分类为题解的标题右侧加上这个tag，demo：https://llf0703.com

```html
<h1 class="post-index-title">
    <a itemtype="url" href="<?php $this->permalink() ?>"><?php $this->title() ?></a>
    <?php if ($this->category=='sol'):?>
        <?php $this->need('luogu.php')?>
    <?php endif;?>
</h1>
```

5. 在您写的题解文章下的自定义字段添加字段名为``luogu``，值为题号的自定义字段就可以看到效果了。

> 题号就是洛谷题目页面url里最后部分，官方题目以``P``开头，Remote Judge题目以OJ名开头，接题目编号。如``P1000``-超级玛丽游戏，``UVA100``-The 3n+1 problem

## 爬虫的使用方法

**爬虫与能否使用这个项目无直接关系，若您没有这个需求或没有python与php相关基础请不要尝试**

**为了保证洛谷的服务器稳定和您的账号与IP安全，请不要删除爬虫的停顿相关代码！**

1. 直接运行``luogu.py``，会自动生成``luogu.php``
2. 将仓库中``luogu.php``尾部复制到生成的``luogu.php``中即可

其中``luogu.php``全是题号与难度对应的数组，关于typecho自定义字段的查询请参考项目中``luogu.php``；关于通过GET获取数据并返回相应按钮请参考``api/luogu.php``。

## API

### 地址

https://llf0703.com/luogu.php?id=

### 使用方法

在``id=``后加上洛谷的题目编号，可以直接复制洛谷题目页面url上的。

- 官方题库P1000：https://llf0703.com/luogu.php?id=P1000
- Remote Judge UVa100：https://llf0703.com/luogu.php?id=UVA100

### 搭建自己的API

将``api/luogu.php``放入服务器中并按照上述方法访问所在位置即可。

## 运作过程

### 原理

通过洛谷题号索引洛谷上的题目难度。

### 步骤：

1. 爬取了洛谷官方题库和Remote Judge中UVa的题目难度，用数字标号，并储存在``luogu.php``中
2. 因为用的时同一个html框架AmazeUI，所以直接照搬样式就行了
3. 在主题文件中引入，并检索自定义字段，然后给出前端代码即可。

## TODO

- [ ] Mysql部署版本
- [ ] SPOJ,Codeforces,AtCoder的支持

## Update

2019.1.30：添加对自定义字段的验证，不会出现不写字段而有尚无评定tag的情况。

2019.4.14：增强爬虫鲁棒性，更新数据。

## LICENSE

MIT