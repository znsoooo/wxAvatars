# parameter = None, 在保证输出有结果时有用，不会存在未定义的变量
# 后来有关None的代码删掉了(见另一个文档)

import os
import math
import random
from PIL import Image
from operator import itemgetter, attrgetter

# 转载请注明出处
# 原文标题：微信好友头像拼接
# 原文地址：https://github.com/znsoooo/wxAvatars
# 原文作者：硫酸锌01/流水线

IMAGE_WIDTH = 1500
IMAGE_RATIO = 8

def gen_pic(avatars, width, count_x, count_y):
    x = 0
    y = 0
    img_new = Image.new('RGB', (width * count_x, width * count_y))
    for avatar in avatars:
        img = Image.open(user + "/" + avatar[3])
        img = img.resize((width, width), Image.ANTIALIAS)
        img_new.paste(img, (x * width, y * width))
        x += 1
        if x == count_x:
            x = 0
            y += 1
    return img_new

user = 'avatars'
avatars = os.listdir(user)

colors = []
for avatar in avatars:
    try:
        image = Image.open(user + "/" + avatar)
        image.thumbnail((1, 1))
        image = image.convert('RGB') # 没有这一句纯灰度像素会转换失败(H未知)
        image = image.convert('HSV')
        hsv = image.getcolors(1)[0][1] #(图片总像素数)[图片包含的第一种颜色][0:像素个数,1:像素色值]
        colors.append([hsv[0],hsv[1],hsv[2],avatar])
    except IOError:
        print("Error:", avatar)

Count = len(colors)

if IMAGE_RATIO == 1:
    colors_1 = colors[:] # 切片拷贝数组
    Width = int(IMAGE_WIDTH / math.ceil(math.sqrt(Count / IMAGE_RATIO)))
    Count_x = int(IMAGE_WIDTH / Width) # 可选 + 20
    random.seed(0) # 初始化种子，每次随机得到的值一样
    for i in range(Count_x * Count_x - Count): # 在随机位置随机填充以前用过的图片
        colors_1.insert(random.randint(1,Count + i), colors[random.randint(1,Count-1)]) # 从1开始排除第一张的自己的头像
    gen_pic(colors_1, Width, Count_x, Count_x).save(user + '_random.jpg')
    print('生成图片0完毕')

    Width = int(IMAGE_WIDTH / math.floor(math.sqrt(Count / IMAGE_RATIO))) # 优先满足'填充'的宽度计算方法
    Count_x = int(IMAGE_WIDTH / Width)
    Count_y = Count_x
else: # 实际得到高宽比例不大于IMAGE_RATIO
    Width = int(IMAGE_WIDTH / math.ceil(math.sqrt(Count / IMAGE_RATIO))) # 优先满足'放下'的宽度计算方法
    Count_x = int(IMAGE_WIDTH / Width)
    Count_y = int(Count / Count_x) # 改为math.ceil为容纳下所有图片

print('像素宽度:', IMAGE_WIDTH)
print('高宽比例:', IMAGE_RATIO)
print('图片总数:', Count)
print('拼图宽度:', Width)
print('总共列数:', Count_x)
print('总共行数:', Count_y)
print('遗漏数目:', Count - Count_x * Count_y)

avatars = sorted(colors, key=itemgetter(0))
gen_pic(avatars, Width, Count_x, Count_y).save(user + '_ratio' + str(IMAGE_RATIO) + "_0.jpg")
print('生成图片1完毕')
avatars = sorted(colors, key=itemgetter(1))
gen_pic(avatars, Width, Count_x, Count_y).save(user + '_ratio' + str(IMAGE_RATIO) + "_1.jpg")
print('生成图片2完毕')
avatars = sorted(colors, key=itemgetter(2), reverse=True) # 可选 itemgetter=排序主键 reverse=True 
gen_pic(avatars, Width, Count_x, Count_y).save(user + '_ratio' + str(IMAGE_RATIO) + "_2.jpg")
print('生成图片3完毕')
