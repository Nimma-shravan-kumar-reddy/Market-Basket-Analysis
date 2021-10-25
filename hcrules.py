#!/usr/bin/env python
# coding: utf-8

# In[210]:


import sys
import time
import pandas as pd
min_sup = int(sys.argv[1])
min_conf = float(sys.argv[2])
file_name = sys.argv[3]
out_file = sys.argv[4]
file = open(file_name,'r')
lines = file.readlines()


# In[132]:


col=[]
for i in lines:
    k=i.split(" ")
    if(k[1].strip()) not in col:
        col.append(k[1].strip())
import pandas as pd
df = pd.DataFrame(columns=col)


# In[133]:


r=[]
for i in lines:
    c=i.split(" ")
    if(int(c[0].strip()) not in r):
        r.append(int(c[0].strip()))
    
q=[]
for i in range(len(r)):
    p=[]
    for j in range(len(col)):
        p.append(0)
    q.append(p)


# In[134]:


df=pd.DataFrame(q,columns=col)


# In[135]:


for i in lines:
    k=i.split(" ")
    df[k[1].strip()][int(k[0].strip())]=1
#df.head()


# In[136]:


#df.drop(0, axis=1, inplace=True)
#df.drop(8755,axis=1,inplace=True)


# In[137]:


#df.shape


# In[138]:


#df = pd.read_csv('final_transactions.csv',index_col=0)
#df.head()


# In[205]:


from time import time
start = time()
l=[]
for i in lines:
    l.append(i.strip())
p=[]
for i in l:
    k=i.split(' ')
    p.append(k[1])
from collections import Counter
c1=Counter(p)
print("C1")
for i in c1:
    print(str([i])+": "+str(c1[i]))
print("L1")
support = min_sup
final=[]
l = Counter()
for i in c1:
    if(c1[i]>=support):
        l[frozenset([i])]+=c1[i]
for i in l:
    print(str(list(i))+": "+str(l[i]))
freq1=len(l)
def cal_support(a,b):
    p=list(a)
    q=list(b)
    return (len(df[(df[p[0]]==1) & (df[q[0]]==1)]))

c2=dict()
k=list(l)
for i in range(0,len(l)):
    for j in range(i+1,len(l)):
            c2[(k[i].union(k[j]))]=cal_support(k[i],k[j])
print("C2 :")
print()
print(c2)
l2=dict()
for i,j in c2.items():
    if(j>=support):
        l2[i]=j
print("L2 :")
print()
print(l2)
final.append(l2)
def calc_support(q):
    m=list(q)
    result=df[m].sum(axis=1)
    return sum(result==len(m))

import itertools
def pruning_check(sub,mm,n):
    l=list(itertools.combinations(mm,n))
    l1=list(sub)
    l2=[set(i) for i in l1]
    t=[set(i) for i in l]
    if all(item in l2 for item in t):
        return True
    else:
        return False


#generating candidate itemsets
p=list(l2)
cand=3
for count in range(3,84):
    temp=dict()
    sub=p
    r=dict()
    for i in range(0,len(p)-1):
        for j in range(i+1,len(p)):
            #checking immediate subset for pruning as well
            mm=p[i].union(p[j])
            if(len(p[i].union(p[j]))==count):
                r[(p[i].union(p[j]))]=calc_support(p[i].union(p[j]))
                if(pruning_check(sub,mm,count-1)):
                    temp[(p[i].union(p[j]))]= calc_support(p[i].union(p[j]))
    print("C"+str(cand))
    print()
    print(r)
    print()
    print("After Pruning :")
    print()
    print(temp)
    print()
    check=dict()
    for i,j in temp.items():
        if(j>=support):
            check[i]=j
    print("L"+str(cand))
    print(check)
    if(len(check)==0):
        print("No more Frequent Items .....")
        break;
    else:
        temp=check;
        final.append(temp)
        p=list(check)
        cand=cand+1    

#print(final)

end = time()

print()
print(end-start)


# In[206]:


final_list=[]
for i in final:
    for j in i:
        final_list.append(set(j))
final_list


# In[207]:


# Association Rules generation
import itertools
with open(out_file, "w") as external_file:
    time_rules_start=time()
    num_freq = len(final_list)+freq1
    count=0
    if(min_conf!=-1):
        #print("  LHS",end="       |      ",file=external_file)
        #print("  RHS",end="       |      ",file=external_file)
        #print("  Support",end="     |      ",file=external_file)
        #print("    confidence",file=external_file)
        for i in final_list:
            for j in range(1,len(i)):
                a =list(itertools.combinations(i,j))
                for k in a:
                    lhs=set(k)
                    rhs=i-lhs
                    usup=calc_support(i)
                    lsup=calc_support(lhs)
                    conf = usup/lsup
                    if(conf>=min_conf):
                        print()
                        print(lhs,end="|",file=external_file)
                        print(rhs,end="|",file=external_file)
                        print(round(usup/len(df),4),end="|",file=external_file)
                        print(round(conf,4),file=external_file)
                        count+=1
    else:
        #print("    LHS    |",end=" ",file=external_file)
        #print("      RHS    |",end=" ",file=external_file)
        #print("     Support   |",end=" ",file=external_file)
        #print(" Confidence ",file=external_file)
        for i in final_list:
            print(i,end="|",file=external_file)
            print({},end="|",file=external_file)
            print(round(calc_support(i)/len(df),4),end="|",file=external_file)
            print(-1,file=external_file)
            count+=1
    time_rules_end=time()
external_file.close()


# In[208]:


cand_time=end-start
rules_time=time_rules_end-time_rules_start
#print(cand_time)
#print(rules_time)


# In[209]:


import matplotlib.pyplot as plt
plt.title("min_confidence : "+str(min_conf)+" min_support : "+str(support))
plt.ylabel("Execution Time (Seconds)")
plt.bar(['Frequent Itemsets'],[cand_time])
plt.bar(['Rules'],[rules_time])
plt.legend([cand_time,rules_time])
plt.show()


import matplotlib.pyplot as plt
plt.title("min_confidence : "+str(min_conf)+" min_support : "+str(support))
plt.bar(['Number of Frequent Itemsets'],[num_freq],color='r')
plt.bar(['Number of High confidence rules'],[count],color='g')
plt.ylabel("Count")
plt.legend([num_freq,count])
plt.show()


# In[ ]:




