#!/usr/bin/env python
# coding: utf-8

# In[78]:


#Import from CSV
import pandas as pd
import sqlite3 as sql
import csv
df = pd.read_csv(r"C:\Users\User\Downloads\Teacher_Data.csv")
print(df)


# In[79]:


#show columns
df.columns


# In[80]:


#remove column
df.drop( 'County (centroid)', inplace=True, axis=1)
df


# In[81]:


df.columns


# In[82]:


df.tail()


# In[83]:


df.head()


# In[84]:


df.describe


# In[85]:


df.columns.tolist()


# In[109]:


import sqlite3
#connecting to sqlite3 and creating database
conn = sqlite3.connect('School.db')
#creating cursor object
mycursor = conn.cursor()
# Creating teacher_Data table
mycursor.execute(''' CREATE TABLE IF NOT EXISTS Teacher_Data 
            (COUNTY TEXT NOT NULL,
             School_Type TEXT NOT NULL,
             Employment_Body TEXT NOT NULL,
             No_of_Teachers INT NOT NULL,
             Year TEXT NOT NULL);''')
conn.commit()
print("School Database Created")


# In[112]:


#remove column
df.drop( 'County (centroid)', inplace=True, axis=1)
df


# In[113]:


df.to_sql('Teacher_Data', conn, if_exists='replace', index = False)


# In[117]:


Teaching = []
#connecting to sqlite3 and creating database
conn = sqlite3.connect('School.db')

#con = lite.connect('/usr/lib/cgi-bin/snmp/sites.db')

Mwalimu = []

with conn:
#creating cursor object
        mycursor = conn.cursor()
        #cur=con.cursor()
        sqlCommand = "SELECT *FROM Teacher_Data;"
        mycursor.execute(sqlCommand)
        while True:
                row = mycursor.fetchone()
                if row is None:
                        break
                Mwalimu.append(str(row[0]))
                Mwalimu.append(str(row[1]))
                Mwalimu.append(str(row[2]))
                Mwalimu.append(str(row[3]))
                Mwalimu.append(str(row[4]))
           
                
                
                
                


# In[131]:


mycursor.execute('SELECT * fROM Teacher_Data')
#tbl="<tr><td>County</td><td>School_Type</td><td>Employment_Body</td><td>Number_of_Teachers</td><td>Year</td></tr>"
#data.append(tbl)

for x in mycursor.fetchall:
    a = "<tr><td>%s</td>"%x['County']
    data.append(a)
    b = "<td>%s</td>"%x['School_Type']
    data.append(b)
    c = "<td>%s</td>"%x['Employment_Body']
    data.append(c)
    d = "<td>%s</td></tr>"%x['Numbers_of_Teachers']
    data.append(d)
    e = "<td>%s</td></tr>"%x['Year']
    data.append(e)
  

 import webbrowser 
f = open('hrec.html', 'w')

H = '''
<html>
<head>
<meta http-equiv="refresh" content="60">

</head>
<body><table><tr><th>County</th><th>School_type</th><th>Employment_Body</th><th>Number_of_Teachers</th><th>Year</th></tr>
'''
f.write (H)

for row in Mwalimu:
    x = '<tr>'
    f.write(x)
    for col in row:
         A_varible='<td>%s</td></tr></table></body></html>'% col
     
f.write (A_varible)
f.close()
         
         
webbrowser.open_new_tab('hrec.html')


# In[129]:


import webbrowser 
f = open('hrec.html', 'w')

H = '''
<html>
<head>
<meta http-equiv="refresh" content="60">

</head>
<body><table><tr><th>County</th><th>School_type</th><th>Employment_Body</th><th>Number_of_Teachers</th><th>Year</th></tr>
'''
f.write (H)

for row in Mwalimu:
    x = '<tr>'
    f.write(x)
    for col in row:
         A_varible='<td>%s</td></tr></table></body></html>'% col
     
f.write (A_varible)
f.close()
         
         
webbrowser.open_new_tab('hrec.html')

    
        

       


# In[ ]:


with con:
               cur = con.cursor()
               sqlCommand = "select * from circuits WHERE area = \'{}\' ORDER BY name".format(area)
               cur.execute(sqlCommand)
               while True:
                       row = cur.fetchone()
                       if row is None:
                               break
                       circuitList.append(row[0])



       for record in circuitList:
               cur = con.cursor()
               sqlCommand = "select * from utilisation where name = \'{}\' order by time DESC LIMIT 1;".format(record)
               cur.execute(sqlCommand)
               print "<tr>"

               while True:
                       inState=' id=\"normal\"'
                       outState=' id=\"normal\"'
                       row = cur.fetchone()
                       if row is None:
                               break
                       else:
                               if float(row[1])+0.5 > alarm:
                                       inState = ' id=\"alarm\"'
                               elif float(row[1])+0.5 > warn:
                                       inState = ' id=\"warn\"'
                               if float(row[2])+0.5 > alarm:
                                       outState = ' id=\"alarm\"'
                               elif float(row[2])+0.5 > warn:
                                       outState = ' id=\"warn\"'
                               print "         <td>{}</td>".format(row[0])
                               print "         <td{}>{}</td>".format(inState ,int(float(row[1])+0.5))
                               print "         <td{}>{}</td>".format(outState ,int(float(row[2])+0.5))
                               print "      </tr>"
       print "</table>"

print "</body></html>"

