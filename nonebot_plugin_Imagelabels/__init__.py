# -*- coding: utf-8 -*-
from nonebot.params import CommandArg, Received
from nonebot import on_command
from nonebot.adapters.onebot.v11 import Message, MessageSegment, Bot, GroupMessageEvent, Event
import os
import json
from nonebot.adapters.onebot.v11.helpers import extract_image_urls as geturls
import httpx
from nonebot_plugin_Imagelabels.Download import Downloading
from nonebot_plugin_Imagelabels.recover import Recover
from nonebot_plugin_Imagelabels.get_video_group import Get_Video
from time import asctime as now_time
import torch
from asyncio import sleep as asyncsel
import threading


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
        "yolov5_Path": f"{yolov5_Path}",
        'file_past': []
    }
    with open('parameter.json', 'w', encoding='utf-8') as fu:
        json.dump(parameter_json, fu, ensure_ascii=False)

elif Yolov5_folder == False:
    yolov5_path = Downloading.Download_yolov5(Path, system_name)
    if parameter == True:
        pass
    elif parameter == False:
        parameter_json = {
            "sumber": 1,
            "Save_as": "Detect_targets",  # 自定义文件存放名称 (建议不修改)
            "yolov5_Path": f"{yolov5_path}",
            'file_past': []
        }
    with open('parameter.json', 'w', encoding='utf-8') as fu:
        json.dump(parameter_json, fu, ensure_ascii=False)

Recover.recover(Pictures_folder, parameter,
                parameter_json, yolov5_Path, system_name)

trigger = on_command('图片标注')


@trigger.handle()
async def Get_image(image: Message = CommandArg()):
    global parameter
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
        "yolov5_Path": yolov5_Path,
        'file_past': []
    }
    with open('parameter.json', 'w', encoding='utf-8') as fu:
        json.dump(New_json, fu, ensure_ascii=False)

    await Make(sumber, yolov5_Path, Save_as)


async def Make(sumber, yolov5_Path, Save_as):
    global detect_path
    if system_name == 'nt':
        image_path = 'Target_picture\\'+Save_as + str(sumber) + '.png'
        detect_path = yolov5_Path + '\detect.py'
    elif system_name == 'posix':
        image_path = 'Target_picture/'+Save_as + str(sumber) + '.png'
        detect_path = yolov5_Path + '/detect.py'
    try:
        shell = f'python {detect_path} --source ./{image_path}'
        os.system(shell)
    except Exception as err:
        with open('Imagelabels-err.txt', mode='a+', encoding='utf-8') as err:
            err.write(str(now_time()) + ':' + str(err))
        print('发生错误，可能是由于无法下载yolov5s导致的 错误代码 002 已将错误追加到Imagelabels-err.txt \n An error has occurred, possibly due to failure to download yolov5s Error code 002 The error has been appended to the Imagelabels-err .txt')
        Recover.recover(Pictures_folder, parameter,
                        parameter_json, yolov5_Path, system_name)
        print('已恢复所有配置文件以保证运行 \n All configuration files have been restored to guarantee operation')

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
    await trigger.send(MessageSegment.image('file:///'+Finished_picture_path))

recover = on_command('恢复默认')


@recover.handle()
async def recover_():
    Recover.recover(Pictures_folder, parameter,
                    parameter_json, yolov5_Path, system_name)
    await recover.send('已恢复默认值')


video_ = on_command('标注视频')


@video_.handle()
async def _(event: GroupMessageEvent, bot: Bot, args: Message = CommandArg()):
    global new_list
    with open('parameter.json', mode='r', encoding='UTF-8') as f:
        parameter = json.load(f)
        sumber = parameter['sumber']
        Save_as = parameter['Save_as']
        yolov5_Path = parameter['yolov5_Path']
        file_content = parameter['file_past']

        gropuid = event.group_id
        root = await bot.get_group_root_files(group_id=int(gropuid))
        files = root.get("files")

        new_list = []
        for i in files:
            file_name = i['file_name']
            new_list.append(file_name)
        parameter_json = {
            "sumber": sumber,
            "Save_as": Save_as,
            "yolov5_Path": yolov5_Path,
            "file_past": new_list
        }
        with open('parameter.json', mode='w', encoding='UTF-8') as fa:
            json.dump(parameter_json, fa, ensure_ascii=False)

    plain_text = args.extract_plain_text()
    if plain_text:
        video_.set_arg("city", args)


@video_.got('city', prompt='请发送视频,发送完后回复任意消息')
async def _(event: GroupMessageEvent, bot: Bot):
    with open('parameter.json', mode='r', encoding='UTF-8') as f:
        parameter = json.load(f)
    sumber = parameter['sumber']
    Save_as = parameter['Save_as']
    yolov5_Path = parameter['yolov5_Path']

    gropuid = event.group_id
    root = await bot.get_group_root_files(group_id=int(gropuid))
    files = root.get("files")
    for i in files:
        fid = i["file_id"]
        fbusid = i["busid"]
        file_name = i['file_name']

        if '.mp4' in file_name:

            if file_name in new_list:
                await video_.send('文件名与群文件存在的文件冲突，请改名')

            else:
                finfo = await bot.get_group_file_url(group_id=gropuid, file_id=str(fid), bus_id=int(fbusid))
                url = finfo['url']
                resp_video = httpx.get(url=url).content
                with open('parameter.json', mode='r', encoding='UTF-8') as f:
                    parameter = json.load(f)
                sumber = parameter['sumber']
                video_files_path1 = Get_Video.video_path(
                    system_name, Path, file_name, sumber)

                with open(video_files_path1, mode='wb') as f:
                    f.write(resp_video)
                await video_.send('已获取视频')
        else:
            await video_.send('请发送mp4格式视频')
            break
        new_list.append(file_name)
        break

    parameter_json = {
        "sumber": sumber,
        "Save_as": Save_as,
        "yolov5_Path": yolov5_Path,
        "file_past": new_list
    }
    with open('parameter.json', 'w', encoding='utf-8') as qw:
        json.dump(parameter_json, qw, ensure_ascii=False)

    Gpu_code = gpu_code()
    if Gpu_code == False:
        await video_.send('未识别到显卡，是否继续标注视频，如果继续，可能导致电脑资源不够用或阻塞bot \n 默认将在10s后开始渲染,等待60s左右回复视频发送')
        await asyncsel(10)

        await video_.send('开始渲染')
        threading.Thread(target=Gpu_video, args=(
            video_files_path1, file_name)).start()
    elif Gpu_code == True:

        await video_.send('开始渲染')
        threading.Thread(target=Gpu_video, args=(
            video_files_path1, file_name)).start()


def gpu_code():
    gpu_sumber = torch.cuda.device_count()
    if int(gpu_sumber) == 0:
        return False
    else:
        return True


def Gpu_video(video_path, file_name):
    '''渲染视频'''
    global Finished_picture_path
    with open('parameter.json', mode='r', encoding='UTF-8') as f:
        parameter = json.load(f)
    sumber = parameter['sumber']
    Save_as = parameter['Save_as']
    yolov5_Path = parameter['yolov5_Path']
    if system_name == 'nt':
        yolov5_file = yolov5_Path + '\\detect.py'
        Finished_picture_path = yolov5_Path + \
            f'\\runs\\detect\\exp{sumber}\\' + \
            file_name
    elif system_name == 'posix':
        yolov5_file = yolov5_Path + '/detect.py'
        Finished_picture_path = yolov5_Path + \
            f'/runs/detect/exp{sumber}/' + file_name
    shell = f'python {yolov5_file} --source {video_path}'
    os.system(shell)
    if int(sumber) == 1:
        if system_name == 'nt':
            Finished_picture_path = yolov5_Path + \
                '\\runs\\detect\\exp\\' + file_name
        elif system_name == 'posix':
            Finished_picture_path = yolov5_Path + \
                '/runs/detect/exp/' + file_name
    elif int(sumber) >= 2:
        if system_name == 'nt':
            Finished_picture_path = yolov5_Path + \
                f'\\runs\\detect\\exp{sumber}\\' + \
                file_name
        elif system_name == 'posix':
            Finished_picture_path = yolov5_Path + \
                f'/runs/detect/exp{sumber}/' + file_name
    new_sumber = int(sumber) + 1
    New_json = {
        "sumber": new_sumber,
        "Save_as": Save_as,
        "yolov5_Path": yolov5_Path,
        'file_past': []
    }
    with open('parameter.json', 'w', encoding='utf-8') as fu:
            json.dump(New_json, fu, ensure_ascii=False)
send_video_ = on_command('视频发送')


@send_video_.handle()
async def send_video():
    print(Finished_picture_path)
    try:
        await video_.send(MessageSegment.video(f'file:///{Finished_picture_path}'))
    except Exception as err:
        await video_.send('视频发送失败，可能是渲染视频时出现视频，报错追加至Imagelabels-err.txt')
        with open('Imagelabels-err.txt', mode='a+', encoding='utf-8') as err:
            err.write(str(now_time()) + ':' + str(err))
