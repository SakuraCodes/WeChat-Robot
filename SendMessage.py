from wxauto import WeChat
import schedule
import time


def PushMsg(msg_list, filepath):
    # 获取微信窗口对象
    wx = WeChat()
    for la in listen_atall_list:
        for m in msg_list:
            wx.AtAll(msg=m, who=la)
            wx.SendFiles(filepath=filepath, who=la)
    for l in listen_list:
        for m in msg_list:
            wx.SendMsg(msg=m, who=l)
            wx.SendFiles(filepath=filepath, who=l)


if __name__ == '__main__':
    # 发送对象列表
    listen_atall_list = [
        # '测试群'
        '宁波歪麦霸王餐福利群002',
        '宁波歪麦霸王餐福利群003',
        '宁波歪麦霸王餐福利群004',
        '在宁波0-5元吃霸王餐-A8'
    ]
    listen_list = [
        # '测试群'
        '在宁波0-5元吃霸王餐-A9',
        '宁波福利群-100',
        '宁波福利群-101'
    ]


    def PushBreakfast():
        # 消息列表
        msg_list = [
            # '这是个测试消息'
            '🏆 【霸王餐来袭】 🏆\n🥪 一日之计在于晨，一顿霸王餐让你全天精神百倍！\n\n真味豆浆\n🈵20返14\n懂包帝·包子豆浆\n🈵20返10\n咬不得高祖生煎\n🈵30返15\n绍兴小笼\n🈵20返10\n三米粥铺\n🈵20返11\n------------------\n⬇快来点链接选店啵~👇\n6url.cn/C8XKHh\n\n——————՞•・•՞——————\n🔥每日持续参与，赢取iPad、拍立得等开学礼包\n👉sourl.cn/PGDZa2'
        ]
        # 文件列表
        filepath = [
            # r'F:\!Code\Code_Python\WeChat-Robot\pic\breakfast.jpg'
            r'C:\Users\MM\PycharmProjects\WeChat-Robot\pic\breakfast.jpg'
        ]
        PushMsg(msg_list, filepath)


    def PushLunch():
        wx = WeChat()
        msg_list = [
            '🌈 【午餐不设防】 🌈\n🍔 歪麦霸王餐，让你的午餐时光，美味又自由！\n\n西北阁(炒饭·炒面·炒菜)\n🈵20返14\n兴宁桥烤鸡(邱隘店)\n🈵20返15\n食光解馋坊\n🈵20返15\n尝态·健康创意简餐\n🈵25返15\n来一餐木桶饭第一档口\n🈵20返15\n------------------\n⬇快来点链接选店啵~👇\n6url.cn/C8XKHh\n\n——————՞•・•՞——————\n🔥每日持续参与，赢取iPad、拍立得等开学礼包\n👉sourl.cn/PGDZa2'
        ]
        filepath = [
            r'C:\Users\MM\PycharmProjects\WeChat-Robot\pic\dinner.jpg'
        ]
        PushMsg(msg_list, filepath)


    def PushTea():
        wx = WeChat()
        msg_list = [
            '𝖬𝖾𝖾𝗍𝗂𝗇𝗀▸ ʚ🍰ɞ꙳⋆🍜\n🍹ɞ ⋆慵懒下午茶️时光♡゛ 🍹\n\n蜜雪冰城(宁波通用)\n🈵20返10\n榴小可榴莲饮品\n🈵20返12\n喜茶(宁波海曙龙湖天街店)\n🈵20返10\nF·CAFE\n🈵25返12\n273C(带梦陶然店)\n🈵30返15\n------------------\n⬇快来点链接选店啵~👇\n6url.cn/C8XKHh\n\n——————՞•・•՞——————\n🔥每日持续参与，赢取iPad、拍立得等开学礼包\n👉sourl.cn/PGDZa2'
        ]
        filepath = [
            r'C:\Users\MM\PycharmProjects\WeChat-Robot\pic\tea.jpg'
        ]
        PushMsg(msg_list, filepath)


    def PushSupper():
        wx = WeChat()
        msg_list = [
            '🍲 【晚餐，不花钱的秘密】 🍴\n🥗 今夜，让歪麦的霸王餐成为你餐桌上的主角，享受美食，享受生活，最重要的是——免费！\n\n久久丫·鸭脖(古林店)\n🈵15返12\n食光解馋坊\n🈵20返15\n尝态·健康创意简餐\n🈵25返15\nbigbear韩国炸鸡(海曙店)\n🈵20返13\n毅动轻食·沙拉(镇海新城店)\n🈵25返18\n------------------\n⬇快来点链接选店啵~👇\n6url.cn/C8XKHh\n\n——————՞•・•՞——————\n🔥每日持续参与，赢取iPad、拍立得等开学礼包\n👉sourl.cn/PGDZa2'
        ]
        filepath = [
            r'C:\Users\MM\PycharmProjects\WeChat-Robot\pic\dinner.jpg'
        ]
        PushMsg(msg_list, filepath)


    def PushSnack():
        wx = WeChat()
        msg_list = [
            '🍖 【深夜食堂，美食不打烊】 🍲\n夜宵时间到，啤酒🍺烧烤🍗不能少！\n\n盱眙兄弟龙虾·活龙虾(宁波汽车东站店)\n🈵50返27\n8+1小酒馆\n🈵40返37\n思念酒馆·现调鸡尾酒\n🈵55返18\n永钰烤串·必出精品满\n🈵30返16\n------------------\n⬇快来点链接选店啵~👇\n6url.cn/C8XKHh\n\n——————՞•・•՞——————\n🔔宵夜订单记得要提交哦~~\n🔔别顾着吃忘记啦~'
        ]
        filepath = [
            r'C:\Users\MM\PycharmProjects\WeChat-Robot\pic\snack.png'
        ]
        PushMsg(msg_list, filepath)


    def PushActivity():
        wx = WeChat()
        msg_list = [
            # '🎉活动一览表，🎁福利快速浏览\n\n1️⃣🎉【活动挑战赛】\n• 参与迎中秋限定干饭挑战，赢24元现金🧧\n• 打开app-赚钱-点击活动二，即可参与挑战赛\n\n2️⃣🔥【吃霸王餐抽iPad】\n• 上线参与0元许愿，都能获得1天会员，人人有份，不容错过！\n• 参与吃霸王餐活动即有机会抽取iPad、拍立得、年会员、万元红包等开学礼包！\n🔗 活动详情入口：sourl.cn/PGDZa2 即可查看更多活动详情和参与方式'
            '嘿！到点了别忘了点外卖\n💻工作再多 干饭要紧\n————՞•・•՞————\n📣中秋大促【到店专享】超划算💰\n①、麦当劳大饱口福三件套到手仅19.9元！\n\n②、瑞幸咖啡全网最低价10.49元！\n \n福利尽在歪麦霸王餐，速速囤卷吧❗\n👉6url.cn/C8XKHh'
        ]
        filepath = [
            r'C:\Users\MM\PycharmProjects\WeChat-Robot\pic\activity.jpg'
        ]
        PushMsg(msg_list, filepath)


    # PushBreakfast()
    # PushLunch()
    # PushTea()
    # PushSupper()
    # PushSnack()
    # PushActivity()

    # 定时执行任务
    schedule.every().day.at("08:30:00").do(PushBreakfast)
    schedule.every().day.at("10:00:00").do(PushActivity)
    schedule.every().day.at("10:30:00").do(PushLunch)
    schedule.every().day.at("14:00:00").do(PushTea)
    schedule.every().day.at("16:30:00").do(PushActivity)
    schedule.every().day.at("17:00:00").do(PushSupper)
    schedule.every().day.at("21:00:00").do(PushSnack)

    while True:
        schedule.run_pending()
        time.sleep(1)
