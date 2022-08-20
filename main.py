import lxml.html.clean as clean
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from getpass import getpass
import time
import random
import os
from bs4 import BeautifulSoup
import requests
import re
import base64
import json
import datetime
import subprocess
from date_detector import Parser
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def filter2(str):
    str=str.replace('More items…','')
    str=str.replace('<a>More items...</a>','')
    return str
def replace_flt(str):
    pattern="\d{2}-(?:[A-Za-z].*){3}-\d{4}"
    pattern2="\d{2} More items…"
    pattern3="\d{1} More items…"
    pattern4="\d{1} more row"
    pattern5="\d{2} more row"
    pattern6="More items…"


    str=(re.sub('More items…', '',str))
    str=(re.sub(pattern, '',str))
    str=(re.sub(pattern2, '',str))
    str=(re.sub(pattern3, '',str))
    str=(re.sub(pattern4, '',str))
    str=(re.sub(pattern5, '',str))
    str=(re.sub(pattern6, '',str))
    str=str.replace("•","")
    return (str)

def refilter(str):
    parser = Parser()
    for match in parser.parse(str):
        str=re.sub(match[2],'',str)
    return(str)
def remtf(str):
    pattern="(?:[A-Za-z].*){4} (?:[A-Za-z].*){5}…"
    str=(re.sub(pattern, '',str))
    return str

def attrclean(code):
    safe_attrs = clean.defs.safe_attrs
    cleaner = clean.Cleaner(safe_attrs_only=True, safe_attrs=frozenset())
    cleansed = cleaner.clean_html(code)
    return replace_flt(cleansed)

def wp_post(title,content,w1,c1):
    catt=get_catid(w1,c1,title)
    Previous_Date = datetime.datetime.today() - datetime.timedelta(days=1)
    createdAt = Previous_Date.strftime("%Y-%m-%dT%H:%M:%S")
    currentTime = datetime.datetime.today().strftime("%d-%h-%Y at %I:%M %p")
    user = "admin"
    password = "B6qS 4bEi 9ypO G2EP jeoB RFYU"
    url = "https://allbusinesshoursnow.com/wp-json/wp/v2/posts"
    credentials = user + ':' + password
    token = base64.b64encode(credentials.encode())
    header = {'Authorization': 'Basic ' + token.decode('utf-8')}
    post = {
    'title'    : title,
    'status'   : 'publish', 
    'content'  : content,
    'categories': catt, 
    'date'   : createdAt
    }
    responce = requests.post(url , headers=header, json=post)
    print(responce)

def wc(string):
    wl=string.split()
    rtt=len(wl)
    return int(rtt)

def check_question(long_string):
    search_list = ['how', 'what', 'where','of','is','when','where','to','are','does',]
    
    if re.compile('|'.join(search_list),re.IGNORECASE).search(long_string):
        return long_string
    else:
        stt=('what is '+str(long_string))
        return stt

def arty(code):

    safe_attrs = clean.defs.safe_attrs
    cleaner = clean.Cleaner(style=True)
    cleansed = cleaner.clean_html(code)

    return (cleansed)
def get_qu():
    filename = 'query.txt'
    line_to_delete = 0
    initial_line = 0
    file_lines = {}
    try:
        with open(filename) as f:
            content = f.readlines()
            
        for line in content:
            file_lines[initial_line] = line.strip()
            initial_line += 1
            ss=file_lines[0]
        f = open(filename, "w")
        for line_number, line_content in file_lines.items():
            if line_number != line_to_delete:
                f.write('{}\n'.format(line_content))
        f.close()
        return ss
    except:
        return 0
    

def vgetId(videourl):
    vidid=videourl.find('watch?v=')
    Id = videourl[vidid+8:vidid+19]
    if vidid==-1:
        vidid=videourl.find('be/')
        Id=videourl[vidid+3:]
    return Id        

def get_catid(catt,cattid,string):
    string=string.lower()
    all_words = string.split()
    first_word= all_words[0]
    for animal in catt:
        if animal == first_word:
            ct=catt.index(first_word)
            return cattid[ct]
def countdown(t):
	
	while t:
		mins, secs = divmod(t, 60)
		timer = '{:02d}:{:02d}'.format(mins, secs)
		print(timer, end="\r")
		time.sleep(1)
		t -= 1
	
	print("Loading")
def scrape_html(asx,s):
    open('sss.html','w',encoding='utf-8').write(str(' '))
    open('ttt2.html','w',encoding='utf-8').write(str(' '))
    expr = re.compile('\d{2}-(?:[A-Za-z].*){3}-\d{4}')
    soup = BeautifulSoup(s, 'html.parser')
    pas='People also ask'
    aas=(soup.findAll('div',{ "class" : "Wt5Tfe" }))
    
    #open('sss.html','a',encoding='utf-8').write(str(qaa))
    for aa in aas:
        
    #	if  aa.find(pas):
        open('sss.html','a',encoding='utf-8').write(str(aa))

        #print(aa)
    ss=open('sss.html','r',encoding='utf-8').read()
    soups = BeautifulSoup(ss, 'html.parser')
        
    aass=(soups.findAll('div',{ "class" : "related-question-pair" }))
    
    cont=0
    for aaw in aass:
        axx=(aaw.find('div',{ "jsname" : "jIA8B" }))
        title_temp=(axx.find('span'))
        span_temp=aaw.findAll('span')
        axx2=(aaw.find('div',{ "class" : "t0bRye" }))

        axx3=(axx2.findAll('div',{ "class" : "wDYxhc" }))
        snn=(aaw.find('span',{ "class" : "CTkDab" }))
	
  
        
        for a3 in axx3:
            if 'YouTube' in str(a3):
                ahref=a3.find('a')
                yt_link=''
                try:
                    yt_link=ahref['href']
                  
                # yt_link=(ahref['href'])
                    frame='<iframe height="300" width="500"src="https://www.youtube.com/embed/{}"></iframe>'.format(vgetId(yt_link))
                    axs=' <div class="boxrel"><div class="answers"><h2>'+str((title_temp.text))+'</h2></div><div class="questions"><br><center>'+str((frame))+"<br><p>"+str(refilter(snn.text))+'</p><center></div></div>'
                    open('ttt2.html','a',encoding='utf-8').write(str(axs))
                    cont=cont+1
                except:
                    pass  


            else:
                if(wc(a3.text)>5):
                    try:
                        for a in a3.findAll('a'):
                            del a['href']
                    except:
                        pass
                            
                    line = re.sub(expr, '', str(a3))

                    axs=' <div class="boxrel"><div class="answers"><h2>'+str(attrclean(title_temp.text))+'</h2></div><div class="questions">'+str(filter2(refilter(attrclean(line))))+'</div></div>'
                    cont=cont+1
                    open('ttt2.html','a',encoding='utf-8').write(str(axs))
                else:
                    pass
    return cont

def ask_click(browser,irng,endingclick):
    ispost=True
    for i in range(endingclick,irng):
        xpathclicK=('/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[3]/div/div/div[2]/div[{}]/div[2]/div/div/div[1]/div[3]').format(str(i))
                 
                    #<div jsname="Q8Kwad" class="YsGUOb"></div>
                    #

       
        cx=browser.find_element_by_class_name("Q8Kwad")
        for c in cx:
            browser.execute_script("arguments[0].click();", c[i])    
        

            #browser.execute_script("arguments["+str(i)+"].click();", elx)
#        browser.execute_script("arguments[0].click();", l)
            #elx.click()
        # try:
            
            # l =browser.find_elements_by_class_name(xpathclicK)

            # 
            
            # l1 =browser.find_element_by_xpath(xpathclicK)
            # browser.execute_script("arguments[0].click();", l1)

#            if(click1):
#                print('Click Ok')
                # ispost=True
# 
            # elif(click2):
                # print('click ok')
                # ispost=True
            # else:
                # print('No click Found')
                # ispost=False
                        
        # except:
            # pass
        time.sleep(3)
        return ispost     
def write_file(txtt):
	with open("ttt2.html", 'r+',encoding='utf-8') as fp:
		lines = fp.readlines()
		lines.insert(0, txtt) 
		fp.seek(0)            
		fp.writelines(lines)
	
def mainfs(asx,irng,custum_key,w1,c1):
    
    try:
        os.remove("sss.html")
        os.remove("ttt2.html")
    except:
        pass
    req1=asx.replace(' ','+')	
    req=check_question(req1)
    browser = webdriver.Chrome()
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    lent=random.randint(900,999)
    wlent=random.randint(999,1100)
    browser.set_window_size(lent,wlent)
    
    video = ('https://www.google.com/search?q='+str(req))

    browser.get(video)
    time.sleep(5)
    click=1
    cont=0
    cont_scrape=0
    isspost=True
    while True:
        if cont_scrape<=irng :
            try:

                ispost= True#ask_click(browser,click,click-1)
                cx=browser.find_elements_by_class_name("YsGUOb")
                for c in cx:
                    browser.execute_script("arguments[0].click();", c)    
                #cx.click()

            except:
                pass
            time.sleep(5)
            s=browser.page_source
            cont_scrape2=scrape_html(asx,s)
        else:
            break

        cont_scrape=cont_scrape+cont_scrape2
        if cont_scrape==0:
            isspost=False
            break
        print(cont_scrape)
        click=click+1        
    custum_key1=custum_key.format(asx)
    stts='''
        <style>
        .boxrel {
     
        top: 0;
        bottom: 0;
        left: 0;
        right: 0;
        margin:20px auto;
        padding: 20px;
        background: #fff;
        border-radius: 5px;
        transition: all 5s ease-in-out;
        border: 2px solid #eee;
        }
        .answers{
        margin-top: 0;
        font-family: Tahoma, Arial, sans-serif;
        font-size: 24px;
        font-color: #000!important;
        }
        .questions{
        margin-top: -15px;
        font-color: #000!important;
        font-size: 18px;
        }
        </style>
        '''
            
    write_file(custum_key1)
    write_file(stts)        
    content=open('ttt2.html','r',encoding='utf-8').read()
    #ispost=ask_click(browser,irng)
    if isspost:
        try:
            wp_post(asx,content,w1,c1)
        except:
            print('Posting Error')    
    else:
        print('Asked Not Found')    
    browser.close()
    return ispost

ic=1
time_to_upload=10 #Minutes
Number_of_Content=30
Categories=['what','how','why']
categoryIDs=[43,42,44]
custum_key="""
If you are searching for the {} then must check out reference guide below. 
"""
while True:
    if ic<=99999:
        #try:
            
        kk=get_qu()
            
        if(kk==0):
            print('Add Query')
            break
        else:
            k2=kk.capitalize()
        
            print("Working on "+str(kk))
                            
            sf=mainfs(k2,Number_of_Content,custum_key,Categories,categoryIDs)
            if sf:
                print('loading')
            else:
                pass    
            print("Next Query loading in "+str(countdown(60*time_to_upload)))
            ic=ic+1
    else:
        time.sleep(82400)           