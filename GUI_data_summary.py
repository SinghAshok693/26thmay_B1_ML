import tkinter as tk
data_analysis=tk.Tk()
data_analysis.title('Summary')
data_analysis.geometry('400x280')
#

users=tk.Variable(data_analysis)
av_age=tk.Variable(data_analysis)
google=tk.Variable(data_analysis)
yahoo=tk.Variable(data_analysis)


tk.Label(data_analysis, text='Total Users').place(x=20,y=30)
tk.Label(data_analysis, text='Average Age').place(x=20,y=60)
tk.Label(data_analysis, text='Commonly Used Mail Domain:').place(x=20,y=90)
tk.Label(data_analysis, text='Google').place(x=20,y=120)
tk.Label(data_analysis, text='Yahoo').place(x=20,y=150)


tk.Label(data_analysis,width=30,bg='#ffffff',textvariable=users).place(x=150,y=30)
tk.Label(data_analysis,width=30,bg='#ffffff',textvariable=av_age).place(x=150,y=60)
tk.Label(data_analysis,width=30,bg='#ffffff',textvariable=google).place(x=150,y=120)
tk.Label(data_analysis,width=30,bg='#ffffff',textvariable=yahoo).place(x=150,y=150)



def fetch():
    f=open('data.csv','r')
    r=f.read()
    f.close
    ####################################################
    ########### making dictionary from data
    r1=r.split('\n')[:-1]
    r2=list(map(lambda x:x.split(','),r1[::]))
    cols=['Full Name','Email ID','User Name','Password','Age','Mobile Number']
    d=dict(zip(cols,zip(*r2)))
    ######################################################
    ##total users
    total_users=len(d['Full Name'])
    users.set(total_users)
    #####################################################
    #### for average age
    l=list(d['Age'])

    sum=0
    for i in l:
        sum=int(i)+sum
        
    avg_age=sum/len(l)
    av_age.set(avg_age)
    #####################################################
    ####Counting number of mail id's
    ##
    a=list(d['Email ID'])
    b=list(map(lambda x:x.split(','),a[::]))
    c=[]
    v=[]
    for i in b:
        str(i)
        x=(str(i)).split('@')
        if 'gmail' in x[1]:
            c.append('1')
        elif 'yahoo' in x[1]:
            v.append('2')

    gmail_ids=len(c)
    yahoo_ids=len(v)
    google.set(gmail_ids)
    yahoo.set(yahoo_ids)
    
tk.Button(data_analysis,text='Get Data', command=fetch).place(x=150,y=210)

#
data_analysis.mainloop()
