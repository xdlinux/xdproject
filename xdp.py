#!/usr/bin/python
# -*- coding: utf-8 -*- 
import urllib                   #get the web  获得网页
from BeautifulSoup import BeautifulSoup      #analysis the xml   分析xml语言          
import re                       #regular 包括正则表达处理的部分
import sys                      #import this for debug sys中包括文件处理的部分
#################################################
####get the web of xdlinux in github 获得网页####
#################################################
url="http://github.com/xdlinux" #set url 设置url 
web=urllib.urlopen(url)         #get the url 获得网页
content=web.read()              #get the content 获得网页内容
#

#print for debug this is not real part of this code 
#print content                  #test the content 测试网页内容
file=open('cache/xdgithub.html','w')                     #open the file  打开文件准备写入
print >> file,content           #save the content to the file 存储网页内容到文件
file.close()                    #close the file 写入结束关闭文件
#
###########################################
####analysis the content 开始处理文件了####
###########################################
f_src=open('cache/xdgithub.html','r')                     #open the source file 以只读的形式打开文件
f_tar=open('data/xdgithub.txt','w+')                      #open the target file  

####load the data into soup 送到soup#######

f_src.seek(0)                    #go back to the head of file 回到文件头部
soup=BeautifulSoup(f_src.read()) #put the file into the soup  将文件放到soup中处理

pschar=re.compile("public source$")                        #set fix points 用正则表达设立定位点的特征
project=soup.findAll('li',attrs={'class':pschar})          #get the fix point 取得定位点
#print project[0].h3.a
##########################################
#####find the key data 找到关键数据#######
n=0
pro=[]
for i in project:
    pro.append([])
    pro[n].append(i.h3.a)
    pro[n].append(i.div.p)
    pro[n].append(i.canvas)
    n=n+1

#print pro
#print n
########################################
####clear and fix the data清理并修正数据########





################################################
####save data into file 输出到文件#####
for row in pro:
    for i in [0,1,2]:
        print >> f_tar,row[i]
#print >> f_tar,pro

###############

print >> f_tar,"</br> powered by lvzongting@gmail.com"

##debug#########
#print "####cache/xdgithub.html####"
#f_src.seek(0)                      #go back to the head of file 回到文件开始
#print f_src.read(200)              #print the 200 litter in head of file_src  输出开始的200个字
#print "####data/xdgithub.txt####"
#f_tar.seek(0)
#print f_tar.read(200)              #print the content of file_src  
#################

f_src.close()
f_tar.close()                    #close the files关闭文件

########################################################
####build the project.html 构建新的xdgithub.html文件####
########################################################
f_src=open('data/xdgithub.txt','r')                       #open the data file 
f_tar=open('project.html','w')

print >> f_tar,"<html>"
print >> f_tar,"<meta charset=\"utf8\"/>"
#######





########

##debug## 
#print "data/xdgithub.txt:"
#f_tar.seek(0)
#print f_src.read(200)               #print the files   
#########


print >> f_tar,f_src.read()
print >> f_tar,"</html>"
f_src.close()
f_tar.close()

