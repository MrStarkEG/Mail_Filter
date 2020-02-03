import re
import sys
import os

mail_list = sys.argv[1]
domains_list = []

pattern = re.compile(r'(\w*)(@)(\w*\.)(\w*)(:*)(\w*)')
mail_pattern = re.compile(r'(\w*)(@)(\w*\.)(\w*)')

try:
    with open (mail_list, 'r') as mail: 
        for i in mail.readlines():
            Searching = pattern.findall(i) ##
            Domain = Searching[0][2] + Searching[0][3]

            Mail_Finder = mail_pattern.findall(i)
            i = Mail_Finder[0][0] + Mail_Finder[0][1] + Mail_Finder[0][2] + Mail_Finder[0][3]

            if Domain not in domains_list:
                domains_list.append(Domain)
                with open('%s.txt'%Domain, 'a') as writer:

                    writer.write(i+'\n') ##
                    writer.close()

            else:
                with open('%s.txt'%Domain, 'a') as writer2:
                    writer2.write(i+'\n')

        writer2.close()
except Exception as e:
    print(e)



def Counter(filer):
    try: 
        i = 0
        with open('%s.txt'%filer, 'r') as hh:
            for _ in hh:
                i +=1
        return str(i)
    except Exception as e:
        print(e)


try:
    for one in domains_list:
        print('%s : %s'%(one, Counter(one)))
except Exception as e:
    print(e)

sys.exit()