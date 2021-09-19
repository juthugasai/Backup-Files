import time, os, shutil

path = ''
days = 30
seconds = time.time() - (days * 24 * 60 * 60)

if os.path.extsts(path):
    ctime = os.stat(path).st_ctime
    for root_folder, folders, files in os.walk(path):
        if seconds >= ctime:
            os.remove(path)
            break
else:
    print('Path Not Exist')