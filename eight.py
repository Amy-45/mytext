import streamlit as st
import pandas as pd
from PIL import Image
import os
from datetime import datetime, time

st.title("python数据采集与预处理实训")

tab1,tab2,tab3,tab4,tab5,tab6= st.tabs(['数据仪表','数字档案','音乐播放器','相册','视频播放网站','个人简历生成器'])

with tab1:
    st.header("📍地图")
    map_data = {
       
        'latitude':[22.853950,22.806988,22.814813,22.832621,22.797759],
        'longitude':[108.222458,108.363594,108.322737,108.289747,108.314627]
     }

    mp_df = pd.DataFrame(map_data)
    st.map(mp_df)

    #定义数据
    re_data = {
        "餐厅":["朴大叔拌饭","重庆小面","蜜雪冰城","三品王汤饭","古茗"],
        "评分":[4.2,4.8,6.0,4.0,5.2],
        "价格":[22,8,10,30,15]
     }
    #创建数据框
    df = pd.DataFrame(re_data)

    st.header("🌟餐厅评分")
    st.bar_chart(df.set_index('餐厅')['评分'])


    # 定义数据,以便创建数据框
    jg_data = {
        '月份': ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'],
        '朴大叔拌饭': [20, 17, 18, 26, 27, 24, 15, 16, 19, 17, 30, 19],
        '蜜雪冰城': [13, 17, 18, 10, 8, 15, 15, 16, 9, 10, 10, 12],
        '古茗': [20, 17, 18, 16, 22, 12, 15, 16, 19, 12, 10, 15],
        '三品王': [20, 17, 18, 30, 24, 24, 22, 16, 19, 17, 25, 19],
        '重庆小面': [10, 14, 18, 13, 14, 14, 15, 10, 12, 14, 10, 13],
    }
    # 根据上面创建的data，创建数据框
    df = pd.DataFrame(jg_data)
    # 定义数据框所用的新索引
    index = pd.Series([1, 2, 3, 4, 5,6,7,8,9,10,11,12], name='序号')
    # 将新索引应用到数据框上
    df.index = index

    # 修改df，用月份列作为df的索引，替换原有的索引
    df.set_index('月份', inplace=True)

    st.subheader("💰不同门店价格")
    # 通过width、height和use_container_width指定折线图的宽度和高度
    st.line_chart(df, width=600, height=300, use_container_width=False)

    data = {
        '月份': ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'],
        '朴大叔拌饭': [20022, 51454, 28685, 22652, 22714, 22454, 21578, 21678, 21945, 21735, 30543, 21945],
        '蜜雪冰城': [12230, 17543, 18356, 16350, 85463, 15545, 154254, 14226, 52559, 531210, 45510, 52312],
        '古茗': [20125, 17454, 54218, 55316, 22332, 15532, 33355, 53316, 75319, 353512, 35310, 3315],
        '三品王': [33320, 33517, 32318, 32330, 23324, 35324, 33522, 53316, 33519, 5317, 57525, 33519],
        '重庆小面': [32510, 3314, 5518, 3513, 35314, 35314, 5315, 35510, 135332, 15444, 54310, 22013],
    }
    # 根据上面创建的data，创建数据框
    df = pd.DataFrame(data)
    # 定义数据框所用的新索引
    index = pd.Series([1, 2, 3, 4, 5,6,7,8,9,10,11,12], name='序号')
    # 将新索引应用到数据框上
    df.index = index

    # 修改df，用月份列作为df的索引，替换原有的索引
    df.set_index('月份', inplace=True)

    st.subheader("🕐用餐高峰时间段")
    # 通过width、height和use_container_width指定面积图的宽度和高度
    st.area_chart(df, width=600, height=300, use_container_width=False)

   
    

with tab2:
     #创建一个为电影的标题，并指定锚点为电影
    st.title("📽  电影 — 疯狂动物城2",anchor='📽  电影 — 疯狂动物城2')
    # 创建一个章节，名为电影介绍
    st.header("🦊  电影介绍",anchor='introduction')
    # 创建一个子章节，名为
    st.subheader("🎬电影详情")

    st.text("上映时间：2025—11—26（美国/中国大陆）")
    st.text("导演：杰拉德·布什 / 拜伦·霍华德")
    st.text("编剧：杰拉德·布什 ")
    st.text("主演： 金妮弗·古德温 / 杰森·贝特曼 / 关继威 / 福琼·费姆斯特 / 安迪·萨姆伯格 ...")

    st.subheader("🤠剧情简介")

    st.text('''一个神秘爬行动物的到来，把温馨的动物城搅动得天翻地覆。面对全新的城市危机，警官兔朱迪（金妮弗·古德温 Ginnifer Goodwin 配音）与狐尼克（杰森·贝特曼 Jason Bateman 配音）将继续携手为保卫动物城而奔波。在追捕行动中，这对老搭档不仅要揭开新角色的神秘面纱，还要前往被迷雾笼罩的新领域，探索未知的地下黑市，一场疯狂动物城的全新冒险即将展开……''')

    st.subheader("🤗 豆瓣评分")
    # 定义列表布局，分成3列
    c1,c2,c3 = st.columns(3)
    c1.metric(label="🌟五星",value="38.5%",delta="11%")
    c2.metric(label="🌟四星",value="44.7%",delta="52%")
    c3.metric(label="🌟三星",value="15.6",delta="-6%%")

    # 创建一个章节，名为电影介绍
    st.header("🦊  角色介绍",anchor='characters')
    data = {
        '职业':['警察', '骗子', '未知', '未知', '未知'],
        '特点':['勇敢、坚持', '聪明、幽默', '神秘、危险', '待补充', '以善意为桥梁'],
        '关系':['尼克的好搭档', '朱迪的好搭档', '制造新危机','待补充','待补充'],
    }  
    index = pd.Series(['朱迪', '尼克', '新反派', '新角色','盖瑞'], name='角色')
    df = pd.DataFrame(data, index=index)

    st.subheader('角色背景🐰')
    st.dataframe(df)

    st.subheader("关键代码")

    python_code = '''# 蛇鳞渲染核心代码
    def render_snake_scale(frame, light_source):
    # 计算鳞片反射和折射
    reflection = calculate_reflection(frame, light_source)
    refraction = calculate_refraction(frame, light_source)
    # 合成最终效果
    return blend(reflection, refraction, alpha=0.8)
    '''
    st.code(python_code, language=None)
    st.markdown('***')
    st.markdown(':red[关键技术总结]')
    st.markdown('''1. 动画渲染：采用游戏引擎技术 
    2. 角色动画：通过AI驱动优化
    3. 场景构建：使用虚拟现实技术构建
     ''')

with tab3:
    # 1. 页面标题
    st.set_page_config(page_title="简易音乐播放器", page_icon="🎵")
    st.title("简易音乐播放器")

    # 2. 歌曲数据
    if 'ind' not in st.session_state:
        st.session_state.ind = 0

    playlist = [
        {
            "url": "https://p2.music.126.net/91GNFB15RhD4G_eRRQKaaQ==/109951172214133834.jpg?param=500y500",
            "song": "fiction",
            "artist": "h3R3",
            "duration": "3:54",
            "mp3": "https://music.163.com/song/media/outer/url?id=3311876765.mp3"
        },
        {
            "url": "http://p1.music.126.net/RYIrCEYzgeAD85DJ0rgOQA==/109951169256300966.jpg?param=500y500",
            "song": "碎碎念",
            "artist": "队长",
            "duration": "2:11",
            "mp3": "https://music.163.com/song/media/outer/url?id=2097443876.mp3"
        },
        {
            "url": "http://p2.music.126.net/JBe7AwcGkYHhleOfQvY2hg==/109951169798343077.jpg?param=500y500",
            "song": "再等冬天(Memories)",
            "artist": "h3R3",
            "duration": "2:48",
            "mp3": "https://music.163.com/song/media/outer/url?id=1927693793.mp3"
        }
    ]

    # 3. 当前歌曲
    idx = st.session_state.ind % len(playlist)   # 把越界风险直接抹掉
    cur = playlist[idx]

    # 4. 左右布局：左图 + 专辑封面字样 | 右信息
    left, right = st.columns([1, 1.2])
    with left:
        st.image(cur["url"], width=250)
        st.caption("专辑封面")   # 图片下方小字

    with right:
        st.markdown(f"**歌名：** {cur['song']}")
        st.markdown(f"**歌手：** {cur['artist']}")
        st.markdown(f"**时长：** {cur['duration']}")
        st.audio(cur["mp3"], format="audio/mpeg")
  
    # 5. 切歌按钮
    def next_song():
        st.session_state.ind = (st.session_state.ind + 1) % len(playlist)

    def prev_song():
        st.session_state.ind = (st.session_state.ind - 1) % len(playlist)

    c1, c2 = st.columns(2)
    with c1:
        st.button("⏮ 上一曲", on_click=prev_song, use_container_width=True)
    with c2:
        st.button("下一曲 ⏭", on_click=next_song, use_container_width=True)



with tab4:
    st.set_page_config(page_title="相册",page_icon="🌏")

    st.title("我的相册")

    if 'ind' not in st.session_state:
        st.session_state['ind']=0

    images = [
        {
          'url':"https://file.moyubuluo.com/d/file/2025-06-03/0176c88a7184c3a883e608a3f2e3b7a4.jpg",
          'text':"疯狂动物城2"
        },{
          'url':"http://img.bbs.duba.net/forum/201111/17/1859436zjpljlnb16snap6.png",
          'text':"倒霉熊"
        },{
          'url':"https://n.sinaimg.cn/sinakd20109/25/w2048h1177/20220714/e154-455b2d43d5de47a621b205ac7a124fbd.jpg",
          'text':"蜡笔小新"
        }]

    idx = st.session_state['ind'] % len(images)
    st.image(images[idx]['url'], caption=images[idx]['text'])
 

    c1,c2=st.columns(2)
 
    def nextImg():
         st.session_state['ind'] = (st.session_state['ind'] + 1) % len(images)

    def backImg():
        st.session_state['ind'] = (st.session_state['ind'] - 1) % len(images)

    with c1:
         st.button("上一张", on_click=backImg, use_container_width=True)
    with c2:
         st.button("下一张", on_click=nextImg, use_container_width=True)


with tab5:
    video_file = [
        {"url": "https://mp-17ef04d6-62a6-4add-9709-6c80be8c52ce.cdn.bspapp.com/1.mp4 ",
         "title": "熊出没第一季第1集", "episode": 1},
        {"url": "https://mp-17ef04d6-62a6-4add-9709-6c80be8c52ce.cdn.bspapp.com/2.mp4 ",
         "title": "熊出没第一季第2集", "episode": 2},
        {"url": "https://mp-17ef04d6-62a6-4add-9709-6c80be8c52ce.cdn.bspapp.com/3.mp4 ",
         "title": "熊出没第一季第3集", "episode": 3},
        {"url": "https://mp-17ef04d6-62a6-4add-9709-6c80be8c52ce.cdn.bspapp.com/4.mp4 ",
         "title": "熊出没第一季第4集", "episode": 4},
        {"url": "https://mp-17ef04d6-62a6-4add-9709-6c80be8c52ce.cdn.bspapp.com/5.mp4 ",
         "title": "熊出没第一季第5集", "episode": 5},
        {"url": "https://mp-17ef04d6-62a6-4add-9709-6c80be8c52ce.cdn.bspapp.com/6.mp4 ",
         "title": "熊出没第一季第6集", "episode": 6},
        ]

    if "ind" not in st.session_state:
        st.session_state.ind = 0  # 默认第 1 集

    def play(i: int):
        if 0 <= i < len(video_file):
            st.session_state.ind = i

    st.set_page_config(page_title="熊出没第一季", layout="centered")

    st.title(f"熊出没第一季 第{st.session_state.ind + 1}集")
    st.video(video_file[st.session_state.ind]["url"], autoplay=True)

    st.markdown(
    """
    **简介：**  
    宁静祥和的东北原始森林，空气清新，万物复苏。熊大和熊二两兄弟在林间追逐奔跑，非常快乐。正在此时，发动机的轰鸣打破了森林的宁静，来者是一个伐木队的小老板，他叫光头强。光头强带着老板的重托，竟来到风景优美的东北原始森林里采伐原木！看着森林被毁，熊兄弟决定要保护森林，保护家园，与光头强斗智斗勇！但是伐木工光头强可没那么容易就离开。于是，一场旷日持久的家园保卫战开始了……
    """
    )

    st.write("**选集：**")
    row1, row2 = st.columns(3), st.columns(3)

    for c, i in enumerate(range(0, 3)):
         with row1[c]:
            st.button(
                f"第{i+1}集",
                use_container_width=True,
                on_click=play,
                args=[i],
             )

    for c, i in enumerate(range(3, 6)):
        with row2[c]:
             st.button(
                 f"第{i+1}集",
                 use_container_width=True,
                 on_click=play,
                 args=[i],
           )


with tab6:
    st.set_page_config(page_title="个人简历生成器",page_icon="😊",layout="wide")

    st.title("🎨个人简历生成器")
    st.text("使用Streamlit创建您的个性化简历")

    c_left, c_right = st.columns([1, 2])

    # 左侧
    with c_left:
        st.subheader("个人信息表单")
        st.divider()

        name = st.text_input('姓名', '')
        work = st.text_input('职位', '')
        phone = st.text_input('电话', '')
        postcode = st.text_input('邮编', '')
        date = st.date_input("出生日期")

        def sex_format_func(gender):
            return f'{gender}'
        sex = st.radio('性别', ['男', '女'], format_func=sex_format_func)

        def my_format_func(option):
            return f'{option}'
        study = st.selectbox('学历', ['小学', '初中', '高中', '大专', '本科', '研究生', '博士'], format_func=my_format_func, index=2)

        option_1 = st.multiselect(
            '选择你最擅长的语言',
            ['英语', '汉语', '日语', '俄语', '阿拉伯语', '泰语', '韩语'],
            format_func=my_format_func,
        )

        options_1 = st.multiselect(
            '技能',
            ['python', 'java', 'C++', 'ppt', 'excel'],
            format_func=my_format_func,
        )

        age = st.slider('工作经验', 0, 60, 3)
    
        values = st.slider('选择薪资范围', 0.0, 100000.0)
    
        intro = st.text_area(label='个人简介：', placeholder='请简要介绍您的专业背景、职业目标和个人特点...')

        st.text("每日最佳联系时间段")
        col1, col2 = st.columns(2)
        with col1:
           t_start = st.time_input("开始时间")
        with col2:
            t_end = st.time_input("结束时间")
   

        st.text("📷 请上传您的个人照片")
        uploaded = st.file_uploader(
            label="选择图片",
            type=["png", "jpg", "jpeg"],
            accept_multiple_files=False
        )

    # 右侧
    with c_right:
        st.subheader('简历实时预览')
        st.divider()
        b_left, b_right = st.columns(2)

        with b_left:
            st.header(name)

            if uploaded is not None:                     
                img = Image.open(uploaded)            
                st.image(img, width=150)
        
            st.write('职位：', work)
            st.write('电话', phone)
            st.write('邮编', postcode)
            st.write('出生日期', date)

        with b_right:
            st.write('性别：', sex)
            st.write('学历：', study)
            st.write("我有 ", age, '年的工作经验')
            st.write('我的期望薪资范围是：', values)
            st.write("你选择的每日最佳联系时间段是：", t_start, " 到 ", t_end)
            st.write('语言能力：', '、'.join(option_1) if option_1 else '未选择')

        st.divider()

        st.subheader('个人简介')
        st.write(intro if intro else '神秘外星人......')

        st.subheader('专业技能')
        st.write('专业技能：', '、'.join(options_1) if options_1 else '未选择')
