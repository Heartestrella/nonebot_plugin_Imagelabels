from nonebot.params import CommandArg
from nonebot import on_command
from nonebot.adapters.onebot.v11 import Message, MessageSegment
import os
import json
from nonebot.adapters.onebot.v11.helpers import extract_image_urls as geturls
import httpx
from nonebot_plugin_Imagelabels.Download import Downloading

system_name = os.name
parameter = os.path.exists('parameter.json')
Pictures_folder = os.path.exists('Target_picture')

Path = os.getcwd()

if Pictures_folder == True:
    pass
elif Pictures_folder == False:
    os.mkdir('Target_picture')

Yolov5_folder = os.path.exists('yolov5-master')

if Yolov5_folder == True:
    if system_name == 'nt':
        yolov5_Path = Path + '\\yolov5-master'
    elif system_name == 'posix':
        yolov5_Path = Path + '/yolov5-master'
    parameter_json = {
        "sumber": 1,
        "Save_as": "Detect_targets",  # 自定义文件存放名称 (建议不修改)
        "yolov5_Path": f"{yolov5_Path}"  
        }        
    with open('parameter.json', 'w', encoding='utf-8') as fu:
        json.dump(parameter_json, fu, ensure_ascii=False)

elif Yolov5_folder == False:
    yolov5_path = Downloading.Download_yolov5(Path,system_name)
    if parameter == True:
        pass
    elif parameter == False:
        parameter_json = {
        "sumber": 1,
        "Save_as": "Detect_targets",  # 自定义文件存放名称 (建议不修改)
        "yolov5_Path": f"{yolov5_path}"  
        }        
    with open('parameter.json', 'w', encoding='utf-8') as fu:
        json.dump(parameter_json, fu, ensure_ascii=False)

trigger = on_command('图片标注')
@trigger.handle()
async def Get_image(image: Message = CommandArg()):

    image_url = geturls(image)
    image_url = ''.join(str(i) for i in image_url)
    with open('parameter.json', mode='r', encoding='UTF-8') as fa:
        parameter = json.load(fa)
    sumber = parameter['sumber']
    Save_as = parameter['Save_as']
    yolov5_Path = parameter['yolov5_Path']
    New_sumber = int(sumber) + 1
    if system_name == 'nt':
        Image_path = Path + '\\' + 'Target_picture\\' + \
            Save_as + str(sumber) + '.png'
    elif system_name == 'posix':
        Image_path = Path + '/' + 'Target_picture/' + \
            Save_as + str(sumber) + '.png'

    image_resp = httpx.get(image_url).content
    with open(Image_path, mode='wb') as f:
        f.write(image_resp)
    New_json = {
        "sumber": New_sumber,
        "Save_as": Save_as,
        "yolov5_Path": yolov5_Path
    }
    with open('parameter.json', 'w', encoding='utf-8') as fu:
        json.dump(New_json, fu, ensure_ascii=False)

    await Make(sumber, yolov5_Path, Save_as)


async def Make(sumber, yolov5_Path, Save_as):
    if system_name == 'nt':
        image_path = 'Target_picture\\'+Save_as + str(sumber) + '.png'
        detect_path = yolov5_Path + '\detect.py'
    elif system_name == 'posix':
        image_path = 'Target_picture/'+Save_as + str(sumber) + '.png'
        detect_path = yolov5_Path + '/detect.py'

    shell = f'python {detect_path} --source ./{image_path}'
    os.system(shell)
    if int(sumber) == 1:
        if system_name == 'nt':
            Finished_picture_path = yolov5_Path + \
                '\\runs\\detect\\exp\\' + Save_as + str(sumber) + '.png'
        elif system_name == 'posix':
            Finished_picture_path = yolov5_Path + \
                '/runs/detect/exp/' + Save_as + str(sumber) + '.png'
    elif int(sumber) >= 2:
        if system_name == 'nt':
            Finished_picture_path = yolov5_Path + \
                f'\\runs\\detect\\exp{sumber}\\' + \
                Save_as + str(sumber) + '.png'
        elif system_name == 'posix':
            Finished_picture_path = yolov5_Path + \
                f'/runs/detect/exp{sumber}/' + Save_as + str(sumber) + '.png'
    print(Finished_picture_path)
    await trigger.send(MessageSegment.image('file:///'+Finished_picture_path))
