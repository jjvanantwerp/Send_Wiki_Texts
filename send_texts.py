from py_imessage import imessage
import bs4
import sys
import requests
import os

os.chdir('') #replace this with the path to your directory of choice.
wiki_page = 'Special:Random'
res = requests.get(f'https://en.wikipedia.org/wiki/{wiki_page}' )
res.raise_for_status()
wiki = bs4.BeautifulSoup(res.text,"html.parser")

# open a file named as your wiki page in write mode
with open(wiki_page+".txt", "w+", encoding="utf-8") as f:
    for i in wiki.select('p'):
        # write each paragraph to the file
        f.write(i.getText())

phone=''#put your phonenumber here.

if not imessage.check_compatibility(phone):
    print ("Not an iPhone. Sadly this script won't work.")

with open(wiki_page+".txt",'r') as fin:
    article=fin.readlines()

for paragraph in article: #[i for i in script if (i.strip() !='')]:
    paragraph = paragraph.replace('...','')
    temp = paragraph.split('\n')
    line = [x for x in temp if not (x =='.' or x=='' or x==' ' or x=='\n')]
    for sentence in line:
        #These lines were supoused to remove footnotes, but I haven't yet gotten them to work.
        '''
        while (sentence.find('[') != -1) and (sentence.find(']'))!=-1 and (sentence.find(']')>sentence.find('[')):
            begin = sentence.find('[')
            end = sentence.find(']')
            sentence = (sentence[0:begin]+sentence[end])
        '''
        sentence = sentence.strip()
        if ((not sentence.isspace()) and (sentence!='[' and sentence!=']')) and len(sentence)>9: #If the sentence is reasonable
            guid = imessage.send(phone, sentence.strip()+'.')
            #print(sentence.strip())

