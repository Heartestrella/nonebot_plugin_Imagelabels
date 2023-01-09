# nonebot_plugin_Imagelabels

基于yolov5实现的图像标注插件

## 安装方法


安装：
使用pip ：
```
pip install nonebot_plugin_Imagelabels
```

在项目内导入：
```
nonebot.load_plugin('nonebot_plugin_Imagelabels')
```


在插件被成功导入到nonebot后将自动检查yolov5-master是否位于Bot根目录，如果没有，将自动下载yolov5-master文件夹于根目录并安装相关依赖


（请注意：执行上述操作时Bot处于堵塞状态，将无法接收并处理其他消息！！这种状态可能持续10多分钟 安装完成后将自动生成parameter.json于根目录    可以自己将yolov5文件夹放置于Bot根目录，并安装相关依赖）






## 效果及使用

图片标注+图片
如：

图片标注![training](https://user-images.githubusercontent.com/110215026/210508476-ad736b56-734b-4646-8aca-b8060ee940ca.jpg)

![image](https://user-images.githubusercontent.com/110215026/210511198-daca05ba-46b0-4876-8759-90041232cfd5.png)

等待服务端处理完成即可返回处理后的图像




(注意：处理图像期间Bot也为堵塞状态，无法处理其他消息，过程大约需要5-20s ，默认为CPU渲染，如果想更换GPU，自行百度)


其他：
首次使用需要下载yolov5s.pt / 其他   如果没有，yolov5将从github下下载，国内下载速度极慢，且可能被墙

可以自己用迅雷等其他工具下载pt文件，放置于yolov5-master目录下



## 下一阶段目标
获取视频文件并标注


## 特别感谢
- [Mrs4s / go-cqhttp](https://github.com/Mrs4s/go-cqhttp)
- [nonebot / nonebot2](https://github.com/nonebot/nonebot2)
- [yolov5 ](https://github.com/ultralytics/yolov5)


## 更新日志
v 0.1.6 :修复了一些可能遇到的问题，并添加了恢复默认功能，在代码出现非网络导致的下载问题时可尝试使用指令"恢复默认"来重置默认值从而解决bug

v 0.1.5 及以下 :可均视为0.1.5版本，没有更新任何东西，只是增加了依赖


## 关于错误代码
error code 001 ：可能由于没有管理员/root权限导致无法重置配件文件导致的
error code 002 ：可能由于网络环境较差无法下载yolov5所需文件导致


详细错误问题请参见Bot目录下的Imagelabels-err.txt
