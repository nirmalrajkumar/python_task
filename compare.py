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
		#dict_fail1={'fail':[]}
		#dict_ok2={'ok':[]}
		#dict_fail2={'fail':[]}
		dict1={}
		dict2={}
		list1=[]
		list2=[]
		
		

                with open(a,'r')as file1, open(b,'r')as file2:
                        source = file1.readlines()
                        
                    	for i in source:
                                word1 = re.match('tempest', i)
				if word1:
					
					words = i.split()
					if words[1] =='...':
						count1 += 1
					#if words[2]=='ok':
						#dict_ok1['ok'].append(i)
					#if words[2]=='FAIL':
						#dict_fail1['fail'].append(i)
						dkey1 = words[0]
						dval1 = words[2]
						dict1[dkey1] = dval1
						a = str(dkey1) + str(dval1)
						
						list1.append(a)
						
						
						
			print 'Total number of lines starting with tempest in first  file '						
		        print count1
			#for n in dict_ok1['ok']:
				#print n	
			#for r in dict_fail1['fail']:
				#print r
			
			des = file2.readlines()

                        for j in des:
                                word2 = re.match('tempest', j)
				if word2:
					words = j.split()
					if words[1] =='...':	
                				count2 += 1
					#if words[2]=='ok':
						#dict_ok2['ok'].append(j)
					#if words[2]=='fail':
						#dict_fail2['fail'].append(j)
						dkey2 = words[0]
						dval2 = words[2]
						dict2[dkey2] = dval2
						a = str(dkey2) + str(dval2)
						
						list2.append(a)
						

						
			print 'Total number of lines starting with tempest in second  file ' 						                               
                        print count2
			#for n in dict_ok2['ok']:
			#	print n
			#for r in dict_fail2['fail']:
			#	print r

		
			for i in list1:
				for j in list2:
					if i==j:
						count3 +=1
			print 'Total number of lines tempest to ... matching status same '
			print count3
			
			for i in dict1:
				for j in dict2:
					if i==j:
						count4 +=1
			print 'Total number of lines tempest to ... matching status differs '
			print count4

					
			for i in dict1:
				for j in dict2:
					if i==j:
						if dict1[i] != dict2[j]:
							#print i
							count5 +=1
			print 'Total number of lines tempest to ... matching status may be anything '
			print count5

			for i in dict1:
				if i in dict2:
					continue
				else:
					count6+=1
			print 'Total number of lines tempest to ... available in first not in second '
			print count6
			
			for i in dict2:
				if i in dict1:
					continue
				else:
					count7+=1
			print'Total number of lines tempest to ... available in second not in first '
			print count7
			
			
			
			#compar=set(dict_ok1['ok'])-set(dict_ok2['ok'])

			#compar1=set(dict_fail1['fail'])-set(dict_fail2['fail'])

			#compar2=set(dict_ok1['ok'])-set(dict_fail2['fail'])

			#compar3=set(dict_fail1['fail'])-set(dict_ok2['ok'])

				
					
			
			#print len(compar)+len(compar1)
			#print len(compar1)
			#print len(compar2)
			#print len(compar3)
				#break

dd = Mycls()


