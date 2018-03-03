import os
import sys # non_bmp_map 用到
import itchat
import PIL.Image as Image

# 转载请注明出处
# 原文标题：微信好友头像拼接
# 原文地址：https://github.com/znsoooo/wxAvatars
# 原文作者：硫酸锌01/流水线

non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

user = 'avatars'
num_all = 0
all_friends = []

if not os.path.exists(user):
    os.makedirs(user)

itchat.auto_login(hotReload=True)

def log(text):
    f=open('log.txt','w',encoding = 'utf-8')
    f.write(str(text))
    f.close()

text = '\nfriends:\n\n'

friends = itchat.get_friends()[0:]
num_all = 0
for friend in friends:
    all_friends.append(friend["UserName"])
    ''''''
    #当只是需要输出好友列表而不需要下载头像时可以注释掉此段
    img = itchat.get_head_img(userName=friend["UserName"])
    fileImage = open(user + "/" + str(num_all) + ".jpg",'wb')
    fileImage.write(img)
    fileImage.close()
    ''''''
    text = text + str(num_all) + ".jpg " + friend["NickName"] + '\n'
    num_all += 1
print('friends finished:', len(all_friends))

log(text)

