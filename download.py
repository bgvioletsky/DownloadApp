import requests
from tqdm import tqdm
import zipfile
import os
import shutil

folder_path = "path"
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

urllist = [{'name': "MetaCubeX/ClashX.Meta", 'path': 0},
           {'name': "Molunerfinn/PicGo", 'path': 5}]

for x in urllist:
    url = "https://api.github.com/repos/" + x['name'] + "/releases/latest"
    response = requests.get(url)
    assets = response.json()['assets']
    if len(assets) > x['path']:
        asset = assets[x['path']]
        a = "https://gh.ddlc.top/" + asset['browser_download_url']
        b = asset['name']
        output_path = os.path.join(folder_path, b)  # 文件保存路径
        response = requests.get(a, stream=True)
        total_size = int(response.headers.get("content-length", 0))
        with open(output_path, "wb") as f:
            with tqdm(total=total_size, unit="B", unit_scale=True, desc=b + "下载中", ncols=80) as pbar:
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
                        pbar.update(len(chunk))


def zip_folder(folder_path, output_path):
    with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, os.path.relpath(file_path, folder_path))
    shutil.rmtree(folder_path)


# 要压缩的文件夹路径
folder_path = 'path'

# 压缩后的输出文件路径
output_path = 'ruanjian.zip'

# 调用函数进行压缩
zip_folder(folder_path, output_path)
