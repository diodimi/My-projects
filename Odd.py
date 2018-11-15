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

url_in="https://www.interwetten.gr/en/sportsbook/betting/bettingoffer.aspx?type=0&leagueid=1061,408903,408904,408905,408906,10410,105379,405632,406208,10428,405410,405679,407164,10659,105120,1019,1020,10268,10347,105325,405432,1021,1022,10467,10468,1091,10427,10691,405369,405368,1029,405298,407902,405355,407636,1030,105034,10523,1024,10416,1081,1025,1023,406244,405464,1026,10605,405266,10607,10269,405658,10172,1027,10448,1079,1028,10265,10412,405677,10287,1035,105225,405273,406007,405447,10306,1059,406254,405357,10909,405485,10750,105121,406888,405525,405526,406106,407689,406594,406548,405736,406573,406569,405394,406817,409352,406317,406076,10405,406638,10406,408639"
matches_int,list_tin=(url_int(url_in))

url_stoix="https://en.stoiximan.gr/Upcoming24H/Soccer-FOOT"
matches_st,list_tst=(url_st(url_stoix))

sum=0


for list_t in list_tin:
    if(list_t in list_tst):
        sum+=1 
        home_win=max((matches_int[list_t+" HOME WIN"],matches_st[list_t+" HOME WIN"]))
        x=max((matches_int[list_t+" X"],matches_st[list_t+" X"]))
        away_win=max((matches_int[list_t+" AWAY WIN"],matches_st[list_t+" AWAY WIN"]))
        result=1/home_win+1/x+1/away_win
        if(result<1):
            print(list_t,home_win,x,away_win)
            print("Profit: ",(1-result)*100,"%")
            
            print("HOME WIN: ", format(100/home_win, '.2f'),"%")
            print("X: ",format(100/x, '.2f'),"%")
            print("AWAY WIN: ",format(100/away_win,'.2f'),"%")


print(sum)
print(len(list_tst))

