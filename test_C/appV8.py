#https://github.com/miguelluiz/vanhack-quiz-C.git

from flask import Flask,  jsonify, request, render_template
from googlesearch import search
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/<url>',methods= ['POST', 'GET'])
def getFive(url=None): 
    def getTopUrls(url, n):
        '''
        Returns google search after reaching 'n' urls
        '''
        _urls=[]
        for url in search(url, stop=n):
            _urls.append(url)
        return _urls
    def getDataSoup(url):
        response = requests.get(url)
        data = response.text
        soup = BeautifulSoup(data, 'html.parser')
        return (soup)
    def getData(soup):
        lparagraphs=len(soup.find_all("p"))
        textContent = []
        for i in range(0, lparagraphs): #1 #10 #20
            paragraphs = soup.find_all("p")[i].text
            textContent.append(paragraphs)
        return (textContent)
    def getLinks(soup):
        link_list = [a['href'] for a in soup.find_all('a', href=True)]
        return link_list
    def cleanLinksAndDuplicates(raw, string):
        '''
        this function will filter under the following conditions:
        a row must be greater or equal to 15 chars long
        a row must not be the same for the first 20 chars
        and it must start with http or https
        '''
        def valid(string, raw):
            '''
            NOT IMPLEMENTED YET - TBD
            this function will filter under the following conditions:
            at least one world (len>3) from 'search' string (split) 
            must be found in the row extracted from the page
            '''
            newString=[i for i in string if len(i)>3]
            for i in newString:
                if i in raw:
                    return True
            return False
    
        lists=[]
        shortList=[]
        string=string.split()
        for i in raw:
            i=i.strip()
            if len(i)<15:
                continue     
            
            #only http and https
            if not i.startswith('http'):
                continue
            
            if i not in lists:
               lists.append(i)
            '''
            TO BE IMPLEMENTED
            #just record up to 20 position 
            if i[:20] not in shortList:  ## must be 'unique' for the first 20 chars
                if valid(string, i):   #in this case, we will check against the whole row - not only with the first 20 char
                    #just add if any the data matches any part of the string
                    shortList.append(i[:20])
                    lists.append(i)
            '''
        shortList=[]
        return lists
    if url is None:
        print ('url is None!')
        return  render_template('empty.html') 
    else:
        _urls=getTopUrls(url, 5)
        v={} #hold all url and their data
        for target_url in _urls:
            soup=getDataSoup(target_url)
            data = getData(soup)
            #data = basicClean(data)
            if len(data)==0:
                data=['No relevant data has been founded']
            link = getLinks(soup)
            if len(link)>0:
                links = cleanLinksAndDuplicates(link, target_url)
            else:
                links = ['No link has been founded']  
            v[target_url]=data,links
        '''
        ##Debug only 
        for url in v:
            print ('URL:', url)
            print ('================ general data ====================')
            #print (v[url][0])
            #for k in v[url][0]:
            #     print (k)
            #print ('================== links ====================')
            #print (v[url][1])
            #for k in v[url][1]:
            #     print (k)
            #print()
        '''
       
        return render_template('urls.html', title='searching URLs..', data=v)


if __name__ == '__main__':
    app.run(debug=True)