import httpx
import os


class Downloading(object):
    def Download_yolov5(Path,system_name):
        print('Downloading binaries from https://gitcode.net/mirrors/ultralytics/yolov5/-/archive/master/yolov5-master.zip to the root directory \n 正在将二进制文件从 https://gitcode.net/mirrors/ultralytics/yolov5/-/archive/master/yolov5-master.zip 下载到根目录')
        yolov5_resp = httpx.get(
            url='https://gitcode.net/mirrors/ultralytics/yolov5/-/archive/master/yolov5-master.zip').content
        with open('yolov5-master.zip', mode='wb') as yolov5:
            yolov5.write(yolov5_resp)
        print('The download has been completed, and the dependencies are being unzipped and installed from domestic sources \n 已完成下载，正在解压缩并从国内源安装相关依赖')
        if system_name == 'nt':
            os.system('tar -xzvf yolov5-master.zip')
        elif system_name == 'posix':
            os.system('unzip  yolov5-master.zip') 
        if system_name == 'nt':
            yolov5_path = Path + '\\yolov5-master'
            requirements_txt = yolov5_path + '\\requirements.txt'
        elif system_name == 'posix':
            yolov5_path  = Path + '/yolov5-master'
            requirements_txt = yolov5_path + '/requirements.txt'
        os.remove('yolov5-master.zip')
        os.system(f'pip3 install -r {requirements_txt} -i https://pypi.tuna.tsinghua.edu.cn/simple')

        print('Dependencies have begun to be installed from domestic sources \n 依赖已开始从国内源安装')

        return yolov5_path