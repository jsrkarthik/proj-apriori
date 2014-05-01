import csv
from googlemaps import GoogleMaps
import os
def main():	
	gmaps = GoogleMaps()
	cr = csv.reader(open("mark.csv","rb"))
	dic=dict()
	i=0
	for row in cr:
	    if not row[0]:
	      break
	    if i==0:
		i+=1
		continue
	    print row[2]
	    #address=row[2]
	    state=lookup(row[2])
	    text=row[14]
	    a=text.split('/')
	    if int(a[0])>6:
			date='winter'
	    else:
			date='summer'
	    if state not in dic:
			dic[state]=dict()	
	    if date not in dic[state]:	
			dic[state][date]=dict()             
	    if row[5] not in dic[state][date]:
			dic[state][date][row[5]]=list()
	    if row[6] not in dic[state][date][row[5]]:
	        dic[state][date][row[5]].append(row[6])
	
	for state in dic:
	   print state,
	   for date in dic[state]:
	    print date
	    for order in dic[state][date]:
	          print dic[state][date][order]
	         

	for state in dic:
	   for date in dic[state]:
	      if not state:
	         state1='statenotfoun'
	      else:
	         state1=state
	      if not date:
	         date1='datenotfound'
	      else:
	         date1=date
	      if not os.path.exists('./ir'):
               os.makedirs('./ir')   
	      f=open('./ir/'+state1+date1+'.txt','a')
	      for order in dic[state][date]:
	          i=0
	          while i<len(dic[state][date][order]):
	             f.write(dic[state][date][order][i])
	             f.write(' ')
	             i+=1
	          f.write('\n')
	
def lookup(zipcode):
    cr = csv.reader(open("zipcode.csv","rb"))
    for row in cr:
       #print "lookup",
       #print row[0]
       if row[0]==zipcode:
          #print "print",
          #print row[2]
          return row[2]
       else:
          continue

main()
