import bs4 as bs
import urllib.request as ur
import re

def url_int(url):
    response=ur.urlopen(url).read()
    html=(bs.BeautifulSoup(response,'lxml'))
    body_int_today=html.body
    list_teams=[]
    list_odds=[]

    matches_int={}

    #match[0]/odd[0] Home team
    #match[1]/odd[1] X
    #match[2]/odd[2] Away team

    for url in body_int_today.find_all("tr",class_="b n3x"):
        match=url.find_all("span")
        
        list_teams.append(((((match[0].text+"-"+ match[2].text).replace(" FC","")).replace(" ","")).replace("(","")).replace(")",""))
        odd=url.find_all("strong")
    
        matches_int.update({(((((match[0].text+"-"+ match[2].text).replace(" FC","")).replace(" ","")).replace("(","")).replace(")",""))+" HOME WIN":float((odd[0].string).replace(",","."))})
        matches_int.update({((((match[0].text+"-"+ match[2].text).replace(" FC","")).replace(" ","").replace("(","")).replace(")",""))+" X":float((odd[1].string).replace(",","."))})
        matches_int.update({((((match[0].text+"-"+ match[2].text).replace(" FC","")).replace(" ","").replace("(","")).replace(")",""))+" AWAY WIN":float((odd[2].string).replace(",","."))})

    return (matches_int,list_teams)


def url_st(url):
    response=ur.urlopen(url).read()
    html=(bs.BeautifulSoup(response,'lxml'))
    body=html.body
    list_teams=[]
    list_odds=[]

    matches={}
    p=0
    j=0

    for url in body.find_all("a",class_="js-event-click a26"):
        url=url.text.replace("\n","")
        list_teams.append((((url.replace(" FC","")).replace(" ","").replace("(","")).replace(")","")))

    for url1 in body.find_all("a",class_="a1e js-selection qs"):
        url1 = re.findall(r"[-+]?\d*\.\d+|\d+", url1.string)
        list_odds.append(float(url1[0]))


    for i in list_teams:  
        matches.update({(((list_teams[j].replace(" FC","")).replace(" ","").replace("(","")).replace(")",""))+" HOME WIN" :list_odds[p]})
        matches.update({(((list_teams[j].replace(" FC","")).replace(" ","").replace("(","")).replace(")",""))+" X":list_odds[p+1]})
        matches.update({(((list_teams[j].replace(" FC","")).replace(" ","").replace("(","")).replace(")",""))+" AWAY WIN":list_odds[p+2]})
        p+=3
        j+=1
    return(matches,list_teams)
    

    
matches_st={}    
matches_int={}
#list_t teams interwetten

url_in="https://www.interwetten.gr/en/sportsbook/today"
matches_int,list_tin=(url_int(url_in))

url_stoix="https://en.stoiximan.gr/Upcoming24H/Soccer-FOOT"
matches_st,list_tst=(url_st(url_stoix))

sum=0

#matches_int[list_t(match)]  HOME WIN
#matches_int[list_t(match+1)]  X
#matches_int[list_t(match+2)]  AWAY WIN
for list_t in list_tin:
    if(list_t in list_tst):
        sum+=1 
        if(matches_int[list_t+" HOME WIN"]!=matches_st[list_t+" HOME WIN"]):
            if((1/matches_int[list_t+" HOME WIN"] + 1/matches_int[list_t+" X"] + 1/matches_st[list_t+" AWAY WIN"])<1 ):
                print(matches_int[list_t+" HOME WIN"]+matches_int[list_t+" X"]+matches_st[list_t+" AWAY WIN"])
            elif((1/matches_int[list_t+" HOME WIN"] + 1/matches_st[list_t+" X"] + 1/matches_st[list_t+" AWAY WIN"])<1):
                print( matches_int[list_t+" HOME WIN"]+matches_st[list_t+" X"] +matches_st[list_t(match+2)])
            elif((1/matches_int[list_t+" HOME WIN"] + 1/matches_st[list_t+" X"] + 1/matches_int[list_t+" AWAY WIN"])<1):
                print(matches_int[list_t+" HOME WIN"]+matches_st[list_t+" X"] +matches_int[list_t+" AWAY WIN"])
            elif((1/matches_st[list_t+" HOME WIN"] + 1/matches_st[list_t+" X"] + 1/matches_int[list_t+" AWAY WIN"])<1):
                print(matches_st[list_t+" HOME WIN"] +matches_st[list_t+" X"] +matches_int[list_t+" AWAY WIN"] )
            elif((1/matches_st[list_t+" HOME WIN"] + 1/matches_int[list_t+" X"] + 1/matches_int[list_t+" AWAY WIN"])<1):
                print(matches_st[list_t+" HOME WIN"] +matches_int[list_t+" X"] + matches_int[list_t+" AWAY WIN"])
            elif((1/matches_st[list_t+" HOME WIN"] + 1/matches_int[list_t+" X"] + 1/matches_st[list_t+" AWAY WIN"])<1):
                print(matches_st[list_t+" HOME WIN"] +matches_int[list_t+" X"] +matches_st[list_t+" AWAY WIN"]) 

print(sum)
