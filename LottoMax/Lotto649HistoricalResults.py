from bs4 import BeautifulSoup
import requests
import pandas as pd
import datetime

today = datetime.date.today()
this_year = today.year

data1 = pd.DataFrame(columns=['Draw_Date','DrawNo_1','DrawNo_2','DrawNo_3','DrawNo_4','DrawNo_5','DrawNo_6','Draw_Bonus'])
   
for year in range(2000,this_year + 1):
    url = 'https://www.lottomaxnumbers.com/lotto-649/numbers/' + str(year)
    print(url)
    html_data = requests.get(url).text
    soup = BeautifulSoup(html_data, 'html.parser')
    tables=soup.find('table',{'class':'archiveResults mobFormat'})
         
    for row in tables.tbody.find_all('tr'):
        col = row.find_all('td')
       
        if col != [] and len(col)>1:
            ddate = col[0].text.strip()        
            resd = ddate.split(',')
            
            if len(ddate) > 16:
                r = resd[0].rpartition('\n')
                drawdate = r[0]
            else:
                drawdate = resd[0]
            
            dresults = col[1].text.strip()
            res = dresults.split('\n')
            print(res)
            draw1 = res[0]
            draw2 = res[1]
            draw3 = res[2]
            draw4 = res[3]
            draw5 = res[4]
            draw6 = res[5]
            drawbonus = res[6]
               
            data1 = data1._append({'Draw_Date':drawdate,'DrawNo_1':draw1,'DrawNo_2':draw2,'DrawNo_3':draw3,'DrawNo_4':draw4,'DrawNo_5':draw5,'DrawNo_6':draw6,'Draw_Bonus':drawbonus}, ignore_index = True)

data1.to_excel('./Lotto649HistoricalResults_new.xlsx', 'Results')