import time
import os
title = input('请输入作品标题：')
dynasty = input('请输入作者所属朝代：')
author = input('请输入作者：')
categories = input('请输入类别[1(诗)/0(词)]：')
t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
file = open('./source/_posts/draft.md',mode='a')

if categories == "1":
    categories = "诗"
elif categories == "0":
    categories = "词"
	
file.write('---\n'
                    f"title: {title}——【{dynasty}】{author}  \n"
                    f"date: {t}  \n"
                    f"tags:  \n"
                    f"- {author}  \n"
                    f"categories:  \n"
                    f"- {categories}  \n"
                    f"---\n"
                    f"{title}  \n"
)

title_pronun = input("请输入标题的发音：")
file.write( f"`{title_pronun}`  \n"
            f"【{dynasty}】{author}  \n"
)
author_pronun = input("请输入朝代和作者名字的发音：")
file.write(f"`{author_pronun}`  \n\n")
p = 1
while p == 1:
    sentence = input("请输入句子[0(无句)/1(换片)]：")
    if sentence == "0":
        p = 0
    elif sentence == "1":
        file.write("  \n")
    else:
        file.write(f"{sentence}  \n")
        sen_pronun = input("请输入该句的发音：")
        file.write(f"`{sen_pronun}`  \n")
newname = input("请输入文件名：")+".md"
os.rename("./source/_posts/draft.md","./source/_posts/"+newname)
