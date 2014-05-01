def main():
	f=open("./outputfilefromapriori.txt","r")
	for line in f:
		words = line.split()
		i=0
		print "[",
		while i<len(words):
		     if '(' not in words[i]:
		        print words[i],
		     else:
		        m=i
		        break
		     i+=1        
		        
		print "] Confidence = %f,Interest = %f "%(float(confidence(words[m+1])),float(Interest(words[m+1],words[0])))
		
def confidence(conf):
    l=conf.split(')')	
    return l[0]
 
def Interest(conf,inter):
    #print inter
    count=0
    total=0
    f=open("./inputfiletoapriori.txt","r")
    for line in f:
       words=line.split()
       total+=1
       if inter in words:
          count+=1          
    #print count,
    #print total
    return (float(confidence(conf))-(count*1.0/total))

main()
