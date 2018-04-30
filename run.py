#***************************************************************************
#    *********First we transform xml files to csv ************8
#***************************************************************************
#import org.apache.spark.{SparkConf, SparkContext}
from pyspark import SparkContext, SparkConf
import matplotlib.pyplot as plt
import csv
import os, os.path
import pandas as pd
import numpy as np

#// 1. Create Spark configuration
#val conf = new SparkConf()
#  .setAppName("SparkMe Application")
#  .setMaster("local[*]")  // local mode

#// 2. Create Spark context
#val sc = new SparkContext(conf)

conf = SparkConf().setAppName('appName').setMaster('local')
sc = SparkContext(conf=conf)

#funtion for CSV conversion
def line22csv(line,tags_list):
    offset=0
    result=""
    for i in tags_list:
        val=""
        patt=i+"="
        ind=line.find(patt,offset)
        if(ind==-1):
            result+=','
            continue
        ind+=(len(i)+2)
        val+='\"'
        while(line[ind]!='\"'):
            val+=line[ind]
            ind+=1
        val+='\"'
        result+=val+','
        offset=ind
    return result[:-1]

fileName = 'Users.xml'

raw = (sc.textFile(fileName, 4))



#Removing top 2 lines form XML file,they didn't contain useful data
headers = raw.take(2)
UsersRDD = raw.filter(lambda x: x != headers)



#FieldNames for Users
tags_list=['Id','Reputation','CreationDate','DisplayName','LastAccessDate',
           'WebsiteUrl','Location','AboutMe','Views','UpVotes','DownVotes',
           'EmailHash','Age', 'AccountId']

Users_csvRDD=UsersRDD.map(lambda x:line22csv(x,tags_list))



#Folder path to save processed files
targetFile = './users_csv'

Users_csvRDD.saveAsTextFile(targetFile)

#FieldNames for Posts
tags_list=['Id','PostTypeId','AcceptedAnswerId','ParentId','CreationDate',
           'DeletionDte','Score','ViewCount','Body','OwnerUserId','OwnerDisplayName',
           'LastEditorUserId','LastEditorDisplayName','LastEditDate','LastActivityDate',
           'Title','Tags','AnswerCount','CommentCount','FavoriteCount','ClosedDate',
           'CommunityOwnedDate']

fileName = 'Posts.xml'

raw = (sc.textFile(fileName, 4))

#Removing top 2 lines form XML file,they didn't contain useful data
headers = raw.take(2)
PostsRDD = raw.filter(lambda x: x != headers)

Posts_csvRDD=PostsRDD.map(lambda x:line22csv(x,tags_list))

targetFile = './posts_csv'

Posts_csvRDD.saveAsTextFile(targetFile)
sc.stop()
#***************************************************************************
#    *********Now we merge posts and users csv files into a single csv ************8
#***************************************************************************
os.chdir('./posts_csv')	
current=os.getcwd()
print(current)
# here we merge the files into a single outposts
fout=open("outposts.csv","w")
# first file:
for line in open("part-00000"):
    fout.write(line)
# now the rest:    
for num in range(1,4):
    f = open("part-0000"+str(num))
    for line in f:
         fout.write(line)
    f.close() # not really needed
fout.close()

os.chdir('..')
os.chdir('./users_csv')	
current=os.getcwd()
print(current)
# here we merge the files into a single outusers
fout=open("outusers.csv","w")
# first file:
for line in open("part-00000"):
    fout.write(line)
# now the rest:    
for num in range(1,4):
    f = open("part-0000"+str(num))
    for line in f:
         fout.write(line)
    f.close() # not really needed
fout.close()
#***************************************************************************
#************in this part we find top 10 (questions/answers) posts according to score
#********* we find the corresponding questions of the top 10 answers
#******  finally we find the accepted (is they exists) answers of the top 10 questions
#******* we dsiplay the top 3 of each questions/answers of each cathegory
#***************************************************************************
os.chdir('..')
os.chdir('./posts_csv')	
def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False


df = pd.read_csv('outposts.csv', skiprows=2,names=['Id','PostTypeId','AcceptedAnswerId','ParentId','CreationDate','DeletionDte','Score','ViewCount','Body','OwnerUserId','OwnerDisplayName','LastEditorUserId','LastEditorDisplayName','LastEditDate','LastActivityDate','Title','Tags','AnswerCount','CommentCount','FavoriteCount','ClosedDate','CommunityOwnedDate'])
dfQ=df.loc[df['PostTypeId'] == 1]
dfA=df.loc[df['PostTypeId'] == 2]


Qbyscore=dfQ.sort_values(by=['Score']).iloc[-10:]
Abyscore=dfA.sort_values(by=['Score']).iloc[-10:]
# find id questions of the answers
TopParent=[]

for index, row in Abyscore.iterrows():
	TopParent.append(int(row['ParentId']))

Accepteda=[]
for index, row in Qbyscore.iterrows():
	if str(row['AcceptedAnswerId'])!='nan':
		Accepteda.append([int(row['AcceptedAnswerId']),int(row['Id'])])
	else:
		Accepteda.append(['No answer accepted',0])

print('acepted list',Accepteda)

#find the actual questions of the top 10 answers (they must exist)
Q=[]
pd.set_option('display.max_colwidth', -1)
for i in range(0,10):
	Q.append(dfQ.loc[dfQ['Id'] == TopParent[i]]['Body'])

pd.set_option('display.max_colwidth', -1)

# now we look for accepted answers of the top 10 questions
Aa=[]
n=len(Accepteda)
for i in range(0,3):
	if RepresentsInt(str(Accepteda[i][0])):
		Aa.append(dfA.loc[dfA['Id'] == Accepteda[i][0]]['Body'])
	else:
		Aa.append('Naa') 

print('*************top 3 questions*******************888')
print(Qbyscore.iloc[0:3,[7,8]])
print('*******************top 3 accepted answers***************8')
print(Aa[0])
print(Aa[1])
print(Aa[2])
print('***************top 3 answers****************************88')
print(Abyscore.iloc[0:3,[7,8]])
#***************************************************************************
#************* here we display the flow of questions and answers over time*********
#***************************************************************************
flowq=[[]]

for index, row in dfQ.iterrows():
	y=int(row['CreationDate'][0:4])
	m=int(row['CreationDate'][5:7])
	i=0
	looksession=0
	while (i < len(flowq)) & (looksession==0):#look if session already exists to update
		if not flowq[i]:
			flowq[0]=[y,m,1]
			looksession=1
		else:
			item=flowq[i]
			if item[0]==y and item[1]==m:#the year and month already exist
				looksession=1#update session
				flowq[i]=[y,m,item[2]+1]
			elif (i==len(flowq)-1):#open new session
				flowq.append([y,m,1])
				looksession=1
			else:#keep looking
				i+=1

flowqsorted=sorted(flowq)
vecq=[]
n=len(flowq)
for i in range(0,n):
	vecq.append(flowqsorted[i][2])


flowqsorted=sorted(flowq)
m=len(flowqsorted)
timeq=np.linspace(flowqsorted[0][0], flowqsorted[m-1][0], m)
vecq=[]
for i in range(0,m):
	vecq.append(flowqsorted[i][2])


with open('flowq.txt', 'w') as Out_file:
	for i in range(0,m):
		oline=str(flowqsorted[i][0])+','+str(flowqsorted[i][1])+','+str(flowqsorted[i][2])+'\n'
		Out_file.write(oline)
	Out_file.close()

flowa=[[]]

for index, row in dfA.iterrows():
	y=int(row['CreationDate'][0:4])
	m=int(row['CreationDate'][5:7])
	i=0
	looksession=0
	while (i < len(flowa)) & (looksession==0):#look if session already exists to update
		if not flowa[i]:
			flowa[0]=[y,m,1]
			looksession=1
		else:
			item=flowa[i]
			if item[0]==y and item[1]==m:#the year and month already exist
				looksession=1#update session
				flowa[i]=[y,m,item[2]+1]
			elif (i==len(flowa)-1):#open new session
				flowa.append([y,m,1])
				looksession=1
			else:#keep looking
				i+=1
flowasorted=sorted(flowa)

m=len(flowasorted)
timea=np.linspace(flowasorted[0][0], flowasorted[m-1][0], m)
veca=[]

for i in range(0,m):
	veca.append(flowasorted[i][2])
plt.hold(True)
plt.plot(timeq, vecq, 'bs')
plt.plot(timea, veca, 'r-')

plt.title("Blue = Questions, Red=Answers")
plt.ylabel('Number of posts')
plt.xlabel('Time')
plt.show()
with open('flowa.txt', 'w') as Out_file:
	for i in range(0,m):
		oline=str(flowasorted[i][0])+','+str(flowasorted[i][1])+','+str(flowasorted[i][2])+'\n'
		Out_file.write(oline)
	Out_file.close()
#***************************************************************************
## now we read users and identity top responders according to our own metric
# we print relevant information of top reponders: age, location, about me, we save their users Id
#***************************************************************************
os.chdir('..')
os.chdir('./users_csv')

df = pd.read_csv('outusers.csv', skiprows=2,names=['Id','Reputation', 'CreationDate','DisplayName','LastAccessDate','WebsiteUrl','Location','AboutMe','Views','UpVotes','DownVotes','EmailHash','Age','AccountId'])

df['MyPunctuation']=0

rep=0
up=0
down=0

for index, row in df.iterrows():
	rep=0
	up=0
	down=0
	if str(row['Reputation'])!='nan':
		rep=int(row['Reputation'])
	if str(row['UpVotes'])!='nan':
		up=int(row['UpVotes'])
	if str(row['DownVotes'])!='nan':
		down=int(row['DownVotes'])
	df.iloc[index, df.columns.get_loc('MyPunctuation')] = rep+up-down


Ubyscore=df.sort_values(by=['MyPunctuation']).iloc[-10:]
print(Ubyscore[['Id','Location','Age','AboutMe']])

# now we save the user id of those top responders
users=[]
for index, row in Ubyscore.iterrows():
	users.append(int(row['Id']))

print('Id of top users: ',users)
#***************************************************************************
#####*** finally we track the post history of questions/answer of the top 3 users
#***************************************************************************
os.chdir('..')
os.chdir('./posts_csv')
df = pd.read_csv('outposts.csv', skiprows=2,names=['Id','PostTypeId','AcceptedAnswerId','ParentId','CreationDate','DeletionDte','Score','ViewCount','Body','OwnerUserId','OwnerDisplayName','LastEditorUserId','LastEditorDisplayName','LastEditDate','LastActivityDate','Title','Tags','AnswerCount','CommentCount','FavoriteCount','ClosedDate','CommunityOwnedDate'])
dfQ=df.loc[df['PostTypeId'] == 1]
dfA=df.loc[df['PostTypeId'] == 2]

timeq=[[],[],[]]
vecq=[[],[],[]]
timea=[[],[],[]]
veca=[[],[],[]]
for i in range(0,3):
	dfuQ=dfQ.loc[df['OwnerUserId'] == users[i]]	
	dfuA=dfA.loc[df['OwnerUserId'] == users[i]]
	print('Questions',dfuQ)
	print('Answers',dfuA)
	flowq=[[]]
	for index, row in dfuQ.iterrows():
		y=int(row['CreationDate'][0:4])
		m=int(row['CreationDate'][5:7])
		k=0
		looksession=0
		while (k < len(flowq)) & (looksession==0):#look if session already exists to update
			if not flowq[k]:
				flowq[0]=[y,m,1]
				looksession=1
			else:
				item=flowq[k]
				if item[0]==y and item[1]==m:#the year and month already exist
					looksession=1#update session
					flowq[k]=[y,m,item[2]+1]
				elif (k==len(flowq)-1):#open new session
					flowq.append([y,m,1])
					looksession=1
				else:#keep looking
					k+=1

	flowqsorted=sorted(flowq)
	m=len(flowqsorted)
	timeq[i]=np.linspace(flowqsorted[0][0], flowqsorted[m-1][0], m)
	#vecq[i]=[]
	n=len(flowq)
	for j in range(0,n):
		vecq[i].append(flowqsorted[j][2])

	flowa=[[]]

	for index, row in dfuA.iterrows():
		y=int(row['CreationDate'][0:4])
		m=int(row['CreationDate'][5:7])
		k=0
		looksession=0
		while (k < len(flowa)) & (looksession==0):#look if session already exists to update
			if not flowa[k]:
				flowa[0]=[y,m,1]
				looksession=1
			else:
				item=flowa[k]
				if item[0]==y and item[1]==m:#the year and month already exist
					looksession=1#update session
					flowa[k]=[y,m,item[2]+1]
				elif (k==len(flowa)-1):#open new session
					flowa.append([y,m,1])
					looksession=1
				else:#keep looking
					k+=1
	flowasorted=sorted(flowa)

	m=len(flowasorted)
	timea[i]=np.linspace(flowasorted[0][0], flowasorted[m-1][0], m)
	#veca[i]=[]
	n=len(flowa)
	for j in range(0,n):
		veca[i].append(flowasorted[j][2])



fig, ax = plt.subplots()
ax.plot(timeq[0], vecq[0], 'rs-.',label='Questions user #1')
ax.plot(timeq[1], vecq[1], 'gs-.',label='Questions user #2')
ax.plot(timeq[2], vecq[2], 'bs-.',label='Questions user #3')

ax.plot(timea[0], veca[0], 'r-',label='Answers user #1')
ax.plot(timea[1], veca[1], 'g-',label='Answers user #2')
ax.plot(timea[2], veca[2], 'b-',label='Answers user #2')
legend = ax.legend(loc='upper center', shadow=True)
frame = legend.get_frame()
frame.set_facecolor('0.90')

# Set the fontsize
for label in legend.get_texts():
    label.set_fontsize('large')

for label in legend.get_lines():
    label.set_linewidth(2.5)  # the legend line width

plt.ylabel('Number of posts')
plt.xlabel('Time')
plt.show()



