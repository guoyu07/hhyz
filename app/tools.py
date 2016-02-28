# encoding=utf-8
import requests
import hashlib
from qiniu import Auth, put_data
from PIL import Image
from io import BytesIO

q=''#qiniu
baseurl = 'http://7xqubs.com1.z0.glb.clouddn.com'
token = q.upload_token('hhyz')


# 上传图片,并返回图片地址
def get_img_url(img):
    print img
    md5 = hashlib.md5()
    md5.update(img)
    key = md5.hexdigest()
    put_data(token, key,img,mime_type='image/jpeg')
    return baseurl + '/' + key

#进行剪裁图片
def cut_img(path,pos):
    img=Image.open(path)
    cp=img.crop(pos)
    out=BytesIO()
    cp.save(out, format='JPEG')
    out.seek(0)
    return out.getvalue()