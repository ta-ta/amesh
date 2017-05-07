#アメッシュの画像の一部分を拡大し, クイックルックで一度だけ表示する
#背景画像は前もって取得しておく

#coding:utf-8

from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import urllib.request

#####
center_x = 1000
center_y = 1000
width = 200
height = 200

magnification = 3

path = '保存先パス'
#####

#画像URLのための取得可能なurlリスト取得
url = "http://tokyo-ame.jwa.or.jp/scripts/mesh_index.js"
response = urllib.request.urlopen(url)
html = response.read()
response.close()
date_query = str(html).split('"')[1]

#画像取得
url = "http://tokyo-ame.jwa.or.jp/mesh/100/" + date_query + ".gif"
response = urllib.request.urlopen(url)
src = response.read()

#保存先
rain_gif = open(path + 'rain.gif', 'wb');

#取得した画像を書き込み
rain_gif.write(src)
rain_gif.close()

#画像合成
background = Image.open(path + 'back.png')#背景画像
background = background.convert('RGBA')
rain = Image.open(path + 'rain.gif')
rain = rain.convert('RGBA')
whole = Image.alpha_composite(background, rain)
whole.save(path + 'whole.png')

#画像トリミング
part = whole.crop((center_x - width//2, center_y - height//2, center_x + width//2, center_y + height//2))
part = part.resize((part.width * magnification, part.height * magnification))

part.save(path + 'part.png')

