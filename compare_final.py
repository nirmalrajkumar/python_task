import sys
import re


class Mycls:
        def __init__(self):
                count1 = 0
                count2 = 0
		count3 = 0
		count4 = 0
		count5=0
		count6=0
		count7=0
                a = sys.argv[1]
                b = sys.argv[2]
		dict1={}
		dict2={}
		list1=[]
		list2=[]
		
		
      
                with open(a,'r')as file1, open(b,'r')as file2:
                        source = file1.readlines()
                        f=open("newfile.txt",'w+')
                    	for i in source:
                                word1 = re.match('tempest', i)
				if word1:
					
					words = i.split()
					if words[1] =='...':
						f.writelines(i+'\n')
						count1 += 1
					
						dkey1 = words[0]
						dval1 = words[2]
						dict1[dkey1] = dval1
						a = str(dkey1) + str(dval1)
						
						list1.append(a)
						
						
						
			print 'Total number of lines starting with tempest in first  file '						
		        print count1
			f=0
			
			des = file2.readlines()
			f=open("newfile.txt",'w+')
                        for j in des:
                                word2 = re.match('tempest', j)
				if word2:
					words = j.split()
					if words[1] =='...':
						f.writelines(j+'\n')	
                				count2 += 1
					
						dkey2 = words[0]
						dval2 = words[2]
						dict2[dkey2] = dval2
						a = str(dkey2) + str(dval2)
						
						list2.append(a)
						

						
			print 'Total number of lines starting with tempest in second  file ' 						                               
                        print count2
			f=0
			

			f=open("newfile.txt",'w+')
			for i in list1:
				for j in list2:
					if i==j:
						f.writelines(i+'\n')
						count3 +=1
			print 'Total number of lines tempest to ... matching status newfile '
			print count3
			f=0
			
			f=open("newfile.txt",'w+')
			for i in dict1:
				for j in dict2:
					if i==j:
						f.writelines(i+'\n')
						count4 +=1
			print 'Total number of lines tempest to ... matching status differs '
			print count4
			f=0
			
			f=open("newfile.txt",'w+')		
			for i in dict1:
				for j in dict2:
					if i==j:
						if dict1[i] != dict2[j]:
							#print i
							f.writelines(i+'\n')
							count5 +=1
			print 'Total number of lines tempest to ... matching status may be anything '
			print count5
			f=0
			
			f=open("newfile.txt",'w+')	
			for i in dict1:
				if i in dict2:
					continue
				else:
					f.writelines(i+'\n')
					count6+=1
			print 'Total number of lines tempest to ... available in first not in second '
			print count6
			f=0
			
			f=open("newfile.txt",'w+')			
			for i in dict2:
				if i in dict1:
					continue
				else:
					f.writelines(i+'\n')
					count7+=1
			print'Total number of lines tempest to ... available in second not in first '
			print count7
			f=0
			
			
			

dd = Mycls()


