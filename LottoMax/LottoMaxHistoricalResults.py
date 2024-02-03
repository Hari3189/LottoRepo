from bs4 import BeautifulSoup
import requests
import pandas as pd
import datetime

today = datetime.date.today()
this_year = today.year

data1 = pd.DataFrame(columns=['Draw_Date','DrawNo_1','DrawNo_2','DrawNo_3','DrawNo_4','DrawNo_5','DrawNo_6','DrawNo_7','Draw_Bonus','Jackpot'])
   
for year in range(2009,this_year + 1):
    url = 'https://www.lottomaxnumbers.com/numbers/' + str(year)
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
            draw1 = res[0]
            draw2 = res[1]
            draw3 = res[2]
            draw4 = res[3]
            draw5 = res[4]
            draw6 = res[5]
            draw7 = res[6]
            drawbonus = res[7]
               
            jackpot = col[2].text.strip()
                
            data1 = data1._append({'Draw_Date':drawdate,'DrawNo_1':draw1,'DrawNo_2':draw2,'DrawNo_3':draw3,'DrawNo_4':draw4,'DrawNo_5':draw5,'DrawNo_6':draw6,'DrawNo_7':draw7,'Draw_Bonus':drawbonus, 'Jackpot':jackpot}, ignore_index = True)

data1.to_excel('./LottoMaxHistoricalResults2024.xlsx', 'Results')