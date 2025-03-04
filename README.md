文字识别工具
项目简介
本项目是一个基于 Python 的简单文字识别工具，利用百度 AI 的通用文字识别 API 实现图像中的文字提取。用户可以选择图片文件，并将识别到的文字保存为文本文件。

功能
选择本地图片文件（支持 PNG, JPG, JPEG, BMP 格式）
调用百度 AI 识别图片中的文字
将识别到的文字保存到本地文本文件
用户友好的图形用户界面（GUI）
依赖
Python 3.x
tkinter（通常随 Python 安装）
baidu-aip（百度 AI SDK）
安装
确保已安装 Python 3.x。
安装百度 AI SDK：
pip install baidu-aip
使用说明
获取百度 AI API Key
注册并登录百度智能云，创建应用以获取 APP_ID、API_KEY 和 SECRET_KEY。
运行程序

在终端中运行：
python 文字识别工具.py

设置 API 信息

在应用程序界面中，输入从百度获取的 APP_ID、API_KEY 和 SECRET_KEY，然后点击“设置API信息”按钮。
选择图片

点击“选择图片”按钮，选择要识别的图片文件。
保存识别结果

识别完成后，程序会提示您选择保存文本结果的路径，并将识别到的文字内容保存为 .txt 文件。
注意事项
请确保网络连接正常，以便访问百度的 API 服务。
对于较大的图片，识别过程可能需要一些时间，请耐心等待识别完成。
API 调用可能会受限于百度的使用政策和额度，使用时请参考其官方文档。
示例界面
文字识别工具界面截图 
![image](https://github.com/user-attachments/assets/4cb56bca-1004-4eb3-a800-328850f0e84b)

联系方式
如有问题或反馈，请联系 1025242676@qq.com
