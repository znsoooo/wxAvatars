# 微信好友头像拼接
* 获取好友/群聊成员头像并按照定义的图片比例和排序模式拼图
* 运行脚本输出色调正序/饱和度正序/亮度倒序的三个拼图
# 作者
* 转载请注明出处
* 原文标题：微信好友头像拼接
* 原文地址：https://github.com/znsoooo/wxAvatars
* 原文作者：硫酸锌01/流水线
# 用法
* IMAGE_WIDTH = 拼图横向宽度最大值
* IMAGE_RATIO = 画面高宽比例，数值约大画面纵向越长
* user = 保存路径文件夹和输出拼图文件名
* name_chatrooms = 需要获取的群聊列表
* log.txt = 输出保存用户昵称/保存头像文件名/所在群名的日志文件名
## 1.0 & 2.0
* 由于微信头像爬下来之后也许还可以用作别的用途，所以将微信头像的获取和处理写在了两段程序里，先1.0/1.1再运行2.0
## 1.0 & 1.1
* 1.1相比1.0新增加了获取微信群成员头像的功能，但是群需要先保存到通讯录中，不然会获取不到群聊成员信息
# 注释
* non_bmp_map = 将用户昵称中的emoji转化为print可以输出的字符，但是在输出到日志中没有此限制
* 实际输出图片像素宽度为单个头像像素宽度的整数倍且横向宽度不超过IMAGE_WIDTH设定值的最大值，不然会出现黑边
* 当IMAGE_RATIO == 1时，因为当高宽比例为1时，通常可以用做头像<del>（或者强迫症）</del>，所以输出图像为满足高宽比为1，且能容纳最多头像的的拼图
* 并额外输出一张在能满足容纳下所有好友头像的正方形图片，空白的地方通过在随机位置插入随机的头像以满足总头像数为平方数
* <del>阅读脚本可以通过添加代码生成更多大于好友头像数的图片，通过在随机位置随机添加随机的已有头像，可以生成复杂效果的拼图</del>
* 当IMAGE_RATIO != 1时，输出图片为满足最后一行填满的前提下不超过IMAGE_RATIO的最大值，不然拼图下方会出现黑边
* 之所以不严格满足设定比例，因为本来当比例值不为1时能满足设定比例的画面长宽比例就非常有限，如果设定了严格画面比例，将会有可能有太多的头像无法容纳到输出的图像中
* 之所以选用“删除最后一行”而不是“补全最后一行”而满足“容纳了所有的好友头像”的<del>强迫症</del>需求，是因为好友头像在排序状态下，不好随机插入，插入了之后很容易看出来头像重复，但是在头像乱序排序时就没有了这个限制
# TODO and NEVER DO
* 由于有部分用户没有设置头像，所以返回的是一张空图，然后程序会转化为一张纯黑图，所以在某些（除亮度排序以外的）排序方式中，会出现一些纯黑色的头像稀疏地插在拼图里，影响观感，可以通过程序方法将这些特殊头像剔除出去，<del>但是我懒得改了</del>
* 当选择头像亮度排序时，会由于某些颜色的HSV色值中的亮度值很高，但是实际上“看起来”的亮度并不高，所以会出现一些颜色明明好像没有那么亮，但是依旧排在了前面
* <del>也有可能就是算法有问题，现在是通过生成1x1的缩略图来计算画面平均HSV值，也许这样算会不准，但是不设置成1x1，设置成几乘几呢？</del>
* 当选择头像色调排序时，当颜色是纯黑色时，颜色的色值是红色（只不过饱和度为0），所以会出现一些红色的头像和黑色的头像插在了一起，这个可以通过综合排序来改变这个现象，<del>但是我懒得改了</del>
* 但是综合排序会带来饱和度或亮度的周期性变化，影响观感
