#!/usr/bin/env python
# coding=utf-8
__metaclass__=type
import re
import smtplib
import urllib
import urllib2
import time
import cookielib
from email.mime.text import MIMEText  

class Library:
    def __init__(self,uid,pwd,mail_list):
        self.baseUrl='http://202.38.232.10/opac/servlet/opac.go'
        cookie = cookielib.CookieJar()  
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))  
        self.uid=uid
        self.pwd=pwd
        self.mail_list=mail_list


    def login(self):
        '登录图书馆'
        postdata=urllib.urlencode({
            'cmdACT':'mylibrary.login',
            'libcode':'',
            'method':'mylib',
            'userid':self.uid,
            'passwd':self.pwd,
            'user_login':'登录'
        })
        request=urllib2.Request(data=postdata,url=self.baseUrl)
        self.opener.open(request)

    def getLoanList(self):
        '获取借阅的图书列表'
        self.login()

        url=self.baseUrl+'?cmdACT=loan.list'
        
        response=self.opener.open(url)
        page=response.read()

        pat='<tr>.+?<td>.+?</td><td>(.+?)</td><td><a.+?>(.+?)</a></td><td>.+?</td><td>.+?</td><td>.+?</td><td>.+?</td><td>(.+?)</td><td.+?>(.+?)</td><td.+?</td><td>.+?</a></td>.+?</tr>'
        pattern=re.compile(pat,re.S)
        list=re.findall(pattern,page)
        ''
        return list

    def isOutDate(self,date):
        '检查是否过期'
        endtime=date.split('-')
        curtime=time.localtime()
        year=int(endtime[0])
        month=int(endtime[1])
        day=int(endtime[2])
        if curtime[0] < year:
            return False
        else:
            if curtime[1] < month:
                return False
            else:
                left=day-curtime[2]
                if left > 3:
                    return False
        return True
        
    def checkList(self):
        '对图书列表逐个检查，先进行续借，否则发邮件进行提醒'
        list=self.getLoanList()
        for book in list:
            if(self.isOutDate(book[2])):
                if(book[3]=='2/2'):
                    msg='你借阅的图书'+book[1]+'即将过期，请及时归还'
                    self.sendMail(msg)
                else:
                    self.reLoan(book[0])
         
    
  
    def sendMail(self,content):  #content：邮件内容
        mail_host="smtp.163.com"  #设置服务器
        mail_user="18814122696"    #用户名
        mail_pass="569621285"   #口令 
        mail_postfix="163.com"  #发件箱的后缀
        me="图书馆小助手"+"<"+mail_user+"@"+mail_postfix+">"   #这里的hello可以任意设置，收到信后，将按照设置显示
        msg = MIMEText(content,_subtype='html')    #创建一个实例，这里设置为html格式邮件
        msg['Subject'] = '借阅图书即将过期通知'    #设置主题
        msg['From'] = me  
        msg['To'] = ";".join(self.mail_list)  
        try:  
            s = smtplib.SMTP()  
            s.connect(mail_host)  #连接smtp服务器
            s.login(mail_user,mail_pass)  #登陆服务器
            s.sendmail(me, self.mail_list, msg.as_string())  #发送邮件
            s.close()  
            print 'send sucess'
        except Exception, e:  
            print str(e)  
            print 'send fail' 
    
    
    def reLoan(self,code):
        '进行续借'
        url=self.baseUrl+'?cmdACT=mylibrary.reloan&BARCODE='+code+'&libcode='
        self.opener.open(url)

librarys=[]
librarys.append(Library('D1430842490','842493','lassie1996@qq.com'))
librarys.append(Library('D1330613450','613452','569621285@qq.com'))
librarys[1].sendMail("开始检测图书借阅情况")
t=1
while(True):
    print 'check loan books'+str(t)
    t+=1
    for library in librarys:
        library.checkList()
    time.sleep(3600*24)
