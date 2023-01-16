import os
import json
import shutil
from time import asctime as now_time


class Recover(object):
    def recover(Pictures_folder_state, parameter_state, parameter_json_text, yolov5_Path, system_name):
        try:
            if Pictures_folder_state == True:
                shutil.rmtree('Target_picture')
                os.mkdir('Target_picture')
            elif Pictures_folder_state == False:
                os.mkdir('Target_picture')

            if parameter_state == True:
                os.remove('parameter.json')
                with open('parameter.json', 'w', encoding='utf-8') as fu:
                    json.dump(parameter_json_text, fu, ensure_ascii=False)
            elif parameter_state == False:
                with open('parameter.json', 'w', encoding='utf-8') as fu:
                    json.dump(parameter_json_text, fu, ensure_ascii=False)

            if system_name == 'nt':
                detect = yolov5_Path + '\\runs' + '\\detect'
                shutil.rmtree(detect)
                os.mkdir('detect')
            elif system_name == 'posix':
                detect = yolov5_Path + '/runs' + '/detect'
                shutil.rmtree(detect)
                os.mkdir('detect')
        except Exception as er:
            with open('Imagelabels-err.txt', mode='a+', encoding='utf-8') as err:
                err.write(str(now_time()) + ':' + str(er))
            print(f'可能由于没有权限所引发的异常，请尝试以管理员/root 身份运行bot,以讲错误追加到 Imagelabels-err.txt \n 错误代码：001 \n Possibly because of an exception thrown by not having permissions, try running bot as administrator/root to append the error to the Imagelabels-err.txt \n Error code: 001')
