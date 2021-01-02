from tkinter import *
from tkinter import messagebox as msbox
import random
import time
import os
from PIL import Image,ImageTk

#窗口
root = Tk()
root.geometry("700x450")
root.title("幸运抽抽抽")
root.config(bg="#aaccff")
#标题文字
textLabel = Label(root,text="幸运抽抽抽",font=("微软雅黑",25),fg="#0088ff",
                  bg="#aaccff")
textLabel.pack()
#滚动条
#最小值设置
lowText = Label(root,text="最小值:",font=("微软雅黑",15),fg="#0000ff",
                bg="#aaccff")
lowText.place(x=10,y=60)
lowVar = StringVar()
lowScale = Scale(root,from_=-10,to=100,resolution=1,orient=HORIZONTAL,
                 variable=lowVar,length=300,bg="#aaccff")
lowScale.place(x=85,y=52)
#最大值设置
highText = Label(root,text="最大值:",font=("微软雅黑",15),fg="#0000ff",
                bg="#aaccff")
highText.place(x=10,y=110)
highVar = StringVar()
highScale = Scale(root,from_=-10,to=100,resolution=1,orient=HORIZONTAL,
                 variable=highVar,length=300,bg="#aaccff")
highScale.place(x=85,y=102)
#文字设定
#前缀
frontTextVar = StringVar()
frontLabel = Label(root,text="前缀:",font=("微软雅黑",15),fg="#0000ff",
                  bg="#aaccff")
frontLabel.place(x=10,y=150)
frontEntry = Entry(root,width=43,textvariable=frontTextVar)
frontEntry.place(x=85,y=157)
#后缀
backTextVar = StringVar()
backLabel = Label(root,text="后缀:",font=("微软雅黑",15),fg="#0000ff",
                  bg="#aaccff")
backLabel.place(x=10,y=180)
backEntry = Entry(root,width=43,textvariable=backTextVar)
backEntry.place(x=85,y=187)

#记录功能
memoryLabel = Label(root,text="历史记录:",font=("微软雅黑",15),fg="#0000ff",
                    bg="#aaccff")
memoryLabel.place(x=400,y=47)
memoryVar = StringVar()
memory = Listbox(root,bg="#aaccff",bd=1,width=20,listvariable=memoryVar)
memory.place(x=400,y=75)
#滚动条
memoryScroll=Scrollbar(memory)
memoryScroll.place(x=123,y=0,relheight=1)
memory.config(yscrollcommand=memoryScroll.set)
memoryScroll.config(command=memory.yview)

#结果
okVar = StringVar()
okLabel = Label(root,text="结果:",font=("微软雅黑",15),fg="#0000ff",
                  bg="#aaccff")
okLabel.place(x=10,y=210)
okEntry = Entry(root,width=43,textvariable=okVar,state="disabled")
okEntry.place(x=85,y=217)

#文件管理
#读取目录
readPath = ".\\infoFile"
file = os.listdir(readPath)
#控件
fileLabel = Label(root,text="文件:",font=("微软雅黑",15),fg="#0000ff",
                    bg="#aaccff")
fileLabel.place(x=550,y=47)
fileVar = StringVar()
fileList = Listbox(root,bg="#aaccff",bd=1,width=20,listvariable=fileVar)
fileList.place(x=550,y=75)
fileScroll = Scrollbar(fileList)
fileScroll.place(x=123,y=0,relheight=1)
fileList.config(yscrollcommand=fileScroll.set)
fileScroll.config(command=fileList.yview)

#生成文件列表
for i in file:
      if ".txt" in i:
            fileList.insert("end",i)
#删除文件功能
def delfile():
      delName = str(fileList.get(ACTIVE))
      fileList.delete(fileList.index(ACTIVE))
      os.remove(".\\infoFile\\"+delName)
      msbox.showinfo(title="文件已删除",message="文件 "+delName+" 删除成功!")
#按键
delFile = Button(root,text="删除文件",font=("微软雅黑",10),fg="#0088ff",width=6,
               height=1,command=delfile)
delFile.place(x=560,y=263)

#刷新文件功能
#功能
def updatefile():
      file = os.listdir(readPath)
      fileList.delete(0,"end")
      delCount = 0
      for i in file:
            if ".txt" in i:
                  fileList.insert("end",i)
            else:
                  os.remove(".\\infoFile\\"+i)
                  delCount += 1
      msbox.showinfo(title="刷新完成",
                     message="刷新成功!共删除"+str(delCount)+"个不符合要求的文件")
#按键
update = Button(root,text="刷新列表",font=("微软雅黑",10),fg="#0088ff",width=6,
               height=1,command=updatefile)
update.place(x=630,y=263)

#保存按键
#功能
def savetxt():
      savePath=".\\infoFile"#文档保存路径
      #生成文档名称
      fileTime = time.strftime("%Y-%m-%d",time.localtime(time.time()))
      timePlus = random.randint(1000,9999)
      fileName = fileTime+"-#"+str(timePlus)
      fileSave = savePath+fileName+".txt"#保存文档
      #打开文档并写入信息
      openFile = open(savePath+"\\"+fileName+".txt","w")
      editText = str(memory.get(0,"end"))
      editList=list(editText)
      #去除引号
      while "'" in editList:
            editList.remove("'")
      #去除逗号
      while "," in editList:
            use = editList.index(",")
            editList.pop(use)
            editList.insert(use,"\n")
      #去除括号
      editList.remove("(")
      editList.remove(")")
      result = "".join(editList)
      #print(result)
      openFile.write(result)
      openFile.close()#关闭文档
      fileList.insert("end",fileName+".txt")
      msbox.showinfo(title="保存完毕",message="文本文档"+fileName+".txt保存完成!")
#print(memory.get(0,"end"))
#按键
save = Button(root,text="保存信息",font=("微软雅黑",10),fg="#0088ff",width=6,
              height=1,command=savetxt)
save.place(x=480,y=263)

#清除功能
#功能
def deleteAll():
      memory.delete(0,"end")
      msbox.showinfo(title="清除完毕",message="历史记录清除完毕!")
#按键
clear = Button(root,text="全部清除",font=("微软雅黑",10),fg="#0088ff",width=6,
               height=1,command=deleteAll)
clear.place(x=410,y=263)

#10连抽功能
def tempidRun():
      #窗口
      tempid = Tk()
      tempid.geometry("400x300")
      tempid.title("幸运抽抽抽--10连抽窗口")
      tempid.config(bg="#aaccff")
      #关闭功能
      def unvrbclose():
            msbox.showerror(title="错误:",message="请点击窗口内按键关闭窗口")
      tempid.protocol("WM_DELETE_WINDOW",unvrbclose)
      #标题文字
      txtTitle = Label(tempid,text="幸运抽抽抽--10连抽",font=("微软雅黑",30),
                       fg="#0088ff",bg="#aaccff")
      txtTitle.pack()
      #内容文字
      labelText = Label(tempid,text="信息:恭喜你获得幸运10连抽,请点击下方按键解锁10连抽!",
                        font=("微软雅黑",11),fg="#0088ff",bg="#aaccff",anchor="w")
      labelText.place(x=10,y=50)
      #当前状态
      infoVar = StringVar()
      infoLabel = Label(tempid,text="当前结果:",font=("微软雅黑",15),fg="#0000ff",
                        bg="#aaccff")
      infoLabel.place(x=13,y=240)
      infoEntry = Entry(tempid,width=41,textvariable=infoVar,state="disabled")
      infoEntry.place(x=103,y=247)
      #抽奖列表
      runTimesLabel = Label(tempid,text="结果列表:",font=("微软雅黑",15),fg="#0000ff",
                            bg="#aaccff")
      runTimesLabel.place(x=150,y=77)
      runTimesVar = StringVar()
      runTimes = Listbox(tempid,bg="#aaccff",bd=1,width=34,height=7,
                         listvariable=runTimesVar)
      runTimes.place(x=150,y=112)
      stopButton = Button(tempid,text="关闭窗口",font=("微软雅黑",15),state="disabled")
      stopButton.place(x=15,y=180)
      #滚动条
      runScroll=Scrollbar(runTimes)
      runScroll.place(x=221,y=0,relheight=1)
      runTimes.config(yscrollcommand=runScroll.set)
      runScroll.config(command=runTimes.yview)
      #抽奖功能
      def runFirst():
            listSum = []
            for i in range(10):
                  a = random.randint(lowScale.get(),highScale.get())
                  listSum.append(a)
                  aReturn = frontEntry.get()+str(a)+backEntry.get()
                  infoVar.set(aReturn)
                  runTimes.insert("end",aReturn)
            sumA = sum(listSum)
            runReturn = frontEntry.get()+str(sumA)+backEntry.get()
            okVar.set(runReturn)
            infoVar.set(runReturn)
            memory.insert("end",runReturn)
            stopButton.config(state="normal")
      #重新抽奖功能
      def rerun():
            listSum = []
            runTimes.delete(0,"end")
            for i in range(10):
                  a = random.randint(lowScale.get(),highScale.get())
                  listSum.append(a)
                  aReturn = frontEntry.get()+str(a)+backEntry.get()
                  infoVar.set(aReturn)
                  runTimes.insert("end",aReturn)
            sumA = sum(listSum)
            runReturn = frontEntry.get()+str(sumA)+backEntry.get()
            okVar.set(runReturn)
            memory.insert("end",runReturn)
            stopButton.config(state="normal")
      def quitTempid():
            tempid.destroy()
      #按键
      runButton = Button(tempid,text="解锁10连抽",font=("微软雅黑",15),command=runFirst)
      runButton.place(x=15,y=80)
      rerunButton = Button(tempid,text="重新抽奖",font=("微软雅黑",15),command=rerun)
      rerunButton.place(x=15,y=130)
      stopButton.config(command=quitTempid)
def run():
      if lowScale.get()<=highScale.get():
            tmpid = random.randint(1,15)
            if tmpid == 6:
                  tempidRun()
            else:
                  r = random.randint(lowScale.get(),highScale.get())
                  runReturn = frontEntry.get()+str(r)+backEntry.get()
                  okVar.set(runReturn)
                  memory.insert("end",runReturn)
      else:
            okVar.set("数据错误,请确保最小值<=最大值后重新抽取!")

#重新抽奖功能
def rerun():
      if lowScale.get()<=highScale.get():
            r = random.randint(lowScale.get(),highScale.get())
            runReturn = frontEntry.get()+str(r)+backEntry.get()
            okVar.set(runReturn)
            memory.insert(ACTIVE,runReturn)
            memory.delete(ACTIVE)
      else:
            okVar.set("数据错误,请确保最小值<=最大值后重新抽取!")

#抽奖按键
getButton = Button(root,text="继续抽奖",font=("微软雅黑",15),command=run)
getButton.place(x=65,y=250,width=120,height=40)
regetButton = Button(root,text="重新抽奖",font=("微软雅黑",15),command=rerun)
regetButton.place(x=215,y=250,width=120,height=40)

#下方功能
btm = Canvas(root,bd=1,bg="#0088ff",cursor="arrow",width=694,height=144)
btm.place(x=0,y=300)
#文字
name = btm.create_text(330,130,font=("微软雅黑",13),
                       text="© 2020 857 Software company,All rights reserved.")
#图片
pic = Image.open("logo.png")
img = ImageTk.PhotoImage(pic)
btm.create_image(70,75,image=img)
#图形
#长方形
btm.create_rectangle(550,10,690,140,fill="#00ccff",outline="#aaccff",width=3)
#圆形
btm.create_oval(560,15,680,135,fill="#00aaff",outline="#00ff00",width=3)
#正方形
btm.create_rectangle(580,37,662,113,fill="#ffff00",outline="#eeff00",width=2)
#更多功能
#标题
btm.create_rectangle(140,7,260,117,fill="white",outline="#aaccff",width=2)
btm.create_text(200,60,font=("微软雅黑",15),text="更多功能:",fill="#0000ff")
#功能
btm.create_rectangle(275,7,530,117,fill="#33ccff",outline="#aaccff",width=3)
#清空文件
#功能
def clearall():
      delList = os.listdir(".\\infoFile")
      delFiles = []
      for d in range(len(delList)):
            os.remove(".\\infoFile\\"+delList[d])
            delFiles.append(delList[d])
      fileList.delete(0,"end")
      msbox.showinfo(title="清空完成",
                     message="所有 'infoFile' 目录下的文件已全部清除!共删除"+str(len(delList))+"个文件")
#按键
clearAll = Button(root,text="清空所有文件",font=("微软雅黑",15),fg="#0088ff",
                  command=clearall)
clearAll.place(x=285,y=340)
#特色功能
#功能
def surun():
      os.system(".\\moreApps\\index.html")
#按键
superise = Button(root,text="特色功能",font=("微软雅黑",15),fg="#0088ff",
                  command=surun)
superise.place(x=425,y=340)
#退出功能
#功能
def normalquit():
      msbox.showinfo(title="退出成功",message="退出成功!感谢使用本软件!")
      root.destroy()
#按键
btnquit = Button(root,text="退出软件",font=("微软雅黑",15),fg="#0088ff",
                 command=normalquit)
btnquit.place(x=572,y=351)
#点击窗口上关闭按钮功能
def errorquit():
      msbox.showerror(title="错误",message="请点击右下角按键以退出程序")
root.protocol("WM_DELETE_WINDOW",errorquit)
