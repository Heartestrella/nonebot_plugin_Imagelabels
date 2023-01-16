import os 
class Get_Video(object):
    def video_path(system_name,Path,file_name,sumber):
        if system_name == 'nt':
            
            video_files_path = Path + '\\Target_picture\\viode' 
            video_files = os.path.exists(video_files_path)
            video_files_path1 = video_files_path + f'\\{file_name}'
        elif system_name == 'posix':
            
            video_files_path = Path + '/Target_picture/viode' 
            video_files = os.path.exists(video_files_path)
            video_files_path1 = video_files_path + f'/{file_name}'
        if video_files == True:
            pass
        elif video_files == False:
            os.mkdir(video_files_path)

        return video_files_path1
        
