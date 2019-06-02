# JDramaReminder
人人日剧更新提醒脚本。

## 效果

<img src="https://i.loli.net/2019/06/02/5cf3b3d76be5891673.jpg" alt="捕获.jpg" title="捕获.jpg" width='80%'/>

基本就是提醒自己哪些日剧更新了。

## 基本逻辑

- 使用`addBangumi.py` 脚本添加日剧信息，信息保存到`bangumiData.p`中
- 使用`checkUpdate.py` 获取`bangumiData.p`中日剧的更新信息。

<img src="https://i.loli.net/2019/06/02/5cf3b5ae364a135806.jpg" alt="捕获.jpg" title="捕获.jpg" width='50%'/>

## 添加日剧信息

使用脚本`addBangumi.py`，直接在shell里运行

```shell
python addBangumi.py --name 日剧名 --url 日剧的url
```

其中 `--name`是必要参数，`--url` 是可选参数，但是如果不是删除日剧信息的话，`--url`也是必须的



## 查看更新信息

使用脚本`checkUpdate.py`即可，或者直接用bat批处理文件。