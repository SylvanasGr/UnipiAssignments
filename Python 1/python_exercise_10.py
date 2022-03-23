file_path = "./two_cities_ascii.txt"
# open the file and store the read file to a variable
with open(file_path,"r") as text_file:
 text = text_file.read()

# ascii to bit
text_to_bit = ' '.join(format(x, 'b') for x in bytearray(text, 'utf-8'))

# seperate by " "
x_split_by_space =list(text_to_bit.split(" "))

# hold the first and last two into a list
y=[]
for i in range(0,len(x_split_by_space)):
 y.insert(i,(x_split_by_space[i][:2] + x_split_by_space[i][-2:]))

# join all together
all_without = ''.join(y)

# separete by 16
separete_per_16 =[
 all_without[i : i + 16 ] for i in range(0,len(all_without),16)
 ]

#calculatios with 2 parameter , 1st the list, 2st the divided number
def calculations(list,x):
 count=0;
 for i in list:
  if(int(i,2)) % x == 0 :
   count+=1
 result = (count / len(list) * 100)
 return result


even_numbers = calculations(separete_per_16,2)
divided_exactly_by_3 = calculations(separete_per_16,3)
divided_exactly_by_5 = calculations(separete_per_16,5)
divided_exactly_by_7 = calculations(separete_per_16,7)
print('Even number percentage:',even_numbers,'%')
print('Divided by 3 percentage:',divided_exactly_by_3,'%')
print('Divided by 5 percentage:',divided_exactly_by_5,'%')
print('Divided by 7 percentage:',divided_exactly_by_7,'%')

