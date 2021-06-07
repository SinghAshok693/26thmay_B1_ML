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

#####################################################
#### for average age
l=list(d['Age'])

sum=0
for i in l:
    sum=int(i)+sum
    
avg_age=sum/len(l)

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

