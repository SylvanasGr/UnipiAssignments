import requests

r = requests.get('https://drand.cloudflare.com/public/latest', headers={ 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
data = r.json()

# this is the latest id
id = data['round']
print(id)
# print(id)
id_100= id - 100;
# print(id_100)
count=0
all_data_for_randomness_100=''
for i in range(id_100,id+1):
    r = requests.get('https://drand.cloudflare.com/public/'+str(i), headers={ 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
    data = r.json()
    all_data_for_randomness_100+=data['randomness']
# print(all_data_for_randomness_100)
binary = ''.join(format(x,'b') for x in bytearray(all_data_for_randomness_100,'utf-8'))
# initiliaze max and temp variables for finding the max 0 and the max 1 in a row
max_0_temp=0
max_1_temp=0
max_0_final=0
max_1_final=0
# make a list of  each binary's element
y=list(binary)
# for breaking the inside loop
end =len(y)
count=0
done=0
# while 0 < len of list size 
while done<len(y):
    # loop for every element in y list and using temp and max variables
    for i in y:
        if(i=='0'):
            max_0_temp+=1
            if(max_0_temp>max_0_final):
                max_0_final += 1
        else:
            max_0_temp=0
        if(i=='1'):
            max_1_temp+=1
            if(max_1_temp>max_1_final):
                max_1_final += 1
        else:
            max_1_temp=0
        count+=1    
    if(count>end):
        break
    max_0_temp=0
    max_1_temp=0
        
print('Biggest row sequence for 0 was :',max_0_final,'times -->',max_0_final*'0')     
print('Biggest row sequence for 1 was :',max_1_final,'times -->',max_1_final*'1')     


