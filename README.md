# nonebot_plugin_Imagelabels

基于yolov5实现的图像标注插件



在插件被成功导入到nonebot后将自动检查yolov5-master是否位于Bot根目录，如果没有，将自动下载yolov5-master文件夹于根目录并安装相关依赖


（请注意：执行上述操作时Bot处于堵塞状态，将无法接收并处理其他消息！！这种状态可能持续10多分钟 安装完成后将自动生成parameter.json于根目录    可以自己将yolov5文件夹放置于Bot根目录，并安装相关依赖）










使用:

图像标注+图片
如：

图像标注![training](https://user-images.githubusercontent.com/110215026/210508476-ad736b56-734b-4646-8aca-b8060ee940ca.jpg)


等待服务端处理完成即可返回处理后的图像

(注意：处理图像期间Bot也为堵塞状态，无法处理其他消息，过程大约需要5-20s ，默认为CPU渲染，如果想更换GPU，自行百度)
