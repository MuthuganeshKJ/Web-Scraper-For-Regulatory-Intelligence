from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import nltk
from nltk.corpus import gutenberg
from nltk.text import Text
import time

def compDate(date1, date2):
    if(date1[-1]>date2[-1]):
        return True
    elif(date1[-1] == date2[-1]):
        m1 = date1[0];
        m2 = date2[0];
        
        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        a = months.index(m1)
        b = months.index(m2)
        if(a>b):
            return True
        elif(months.index(m1)==months.index(m2)):
            d1 = int(date1[1].strip().strip(","))
            d2 = int(date2[1].strip().strip(","))
            if(d1>d2):
                return True;
    return False
        
        

PATH = "C:\Program Files (x86)\chromedriver.exe"

opt=Options()
opt.add_argument("start-maximized")
opt.add_argument("--disable-extensions")


opt.add_experimental_option("prefs", { \
"profile.default_content_setting_values.media_stream_mic": 1,
"profile.default_content_setting_values.media_stream_camera": 1,
"profile.default_content_setting_values.geolocation": 1,
"profile.default_content_setting_values.notifications": 1
})

search_string = input("Input the Medicine you want to search for:")

driver  = webdriver.Chrome(chrome_options=opt, executable_path='C:\Program Files (x86)\chromedriver.exe')

for i in range(1):
    matched_elements = driver.get("https://www.drugs.com/comments/"+search_string+"/?sort_reviews=most_recent")

reviews = driver.find_elements_by_xpath('//*[@class="ddc-comment ddc-box ddc-mgb-2"]');
#print(reviews);
storage = open("SearchResults.txt", "a")
reviewlst = []
cpm=[]
rvw=[]
latestRun = "December 1, 2021".split() #The last updated date is hard coded here this can the made dynamic during the real time application
temp=''
sideEffects = ["stomach upset", "head ache", "weight loss", "Inflamation", "diaheria", "rash", "anemic"]
sel = []
for review in reviews:
    #print(review.text.split("\n"))
    rvw = review.text.split("\n")
    l = len(rvw);
    
    if(l == 7):
        
        temp = rvw[2].split();
        
        if(compDate(temp, latestRun)):
            storage.write(rvw[2]+","+rvw[3]+"\n")
            print(rvw[2]);
            print(rvw[3], "\n___________________\n");
            for se in rvw[3]:
                if(se in sideEffects):
                    sel.append(se)
        reviewlst.append(review.text.split("\n"))
    else:
        
        temp = rvw[4].split();
        if(compDate(temp, latestRun)):
            storage.write(rvw[4]+","+rvw[5]+"\n")
            print(rvw[4]);
            print(rvw[5], "\n___________________\n");
            for se in rvw[3]:
                if(se in sideEffects):
                    sel.append(se)
            courpus = rvw[5]
           
       

print("FILTERED SIDE EFFECTS")
print(sideEffects)

storage.close()
