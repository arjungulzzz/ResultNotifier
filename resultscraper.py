from bs4 import BeautifulSoup
import openpyxl
import os

student_names=['AANCHAL BANSAL','ABHINAV KUMAR','ADITYA KUMAR','AJAY KUMAR','AKHIL JUNEJA', 'AKSHAY KALIA', 'AMIT KUMAR', 'AMIT YADAV', 'ANJANA KUMARI', 'ANMOL AGNIHOTRI', 'ANMOL GUPTA', 'ANUJ KATIYAR', 'ANUJ KUMAR SAHU', 'ANURAG SHEKHAR', 'ARCHA JAIN', 'ARJUN GULYANI', 'ARPIT KUMAR', 'ARUSH VERMA', 'AYUSH JAIN', 'AYUSHI GUPTA', 'CHESHTA SONI','DEEPAK KUMAR', 'DEEPANSHU', 'DEV SALUJA', 'DEVANSHU TANEJA', 'DIPANSHU SHARMA', 'GANESH PRASAD', 'GAURAV KISHORE', 'GULSHAN KUMAR MEENA', 'HANIL KATHURIA', 'HARISH', 'HIMANI SETHI', 'HIMANSHI', 'KARTIKEY GOYAL', 'KONARK VERMA','KUNAL DARGAN', 'KUNWAR VIKRANT', 'MADHUR VASHISHT', 'MANISH CHANDRA', 'MANJEET YADAV', 'MEHUL SHARMA', 'MOHIT GANGWAR', 'MOHIT KUMAR', 'MUDIT AGGARWAL', 'NARESH KUSHMAKAR', 'NAYAN SHARMA', 'NEEL KUMAR', 'NIDHI SAKARWAL', 'NIDHI SHARMA','NIKHIL GUPTA', 'KUNAL DARGAN']


wb = openpyxl.Workbook()
sheet=wb.get_sheet_by_name('Sheet')
sheet.column_dimensions['A'].width = 23
sheet['A1']='Names'
sheet_columns = ['C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R1','S','T','U','V','W','X','Y','Z']
#number=3
#name_counter=0
#count1=1
#col_count=0
#col_no=3
#while(number<54):
 #   sheet['A'+str(number)]=student_names[name_counter]
  #  soup = BeautifulSoup(open('C:/Users/Arjun/PythonProg/'+student_names[name_counter]+'.txt'),'html5lib')
   # #print(number)
    #table = soup.find('table', id='gvrslt')
    #td_elements = table.find_all('td')
    #print(len(td_elements))
    #while(count1<32):
     #   marks = td_elements[count1].get_text()
      #  sheet[sheet_columns[col_count]+str(col_no)]=marks
        #print(marks)
        
       # out_of = td_elements[count1+1].get_text()
        #sheet[sheet_columns[col_count+1]+str(col_no)]=marks
        #print(out_of)
        
        #count1=count1+4
        #col_no=col_no+1
        #col_count=col_count+2
    #number=number+1
    #name_counter=name_counter+1
    #count1=count1+4
soup0 = BeautifulSoup(open('C:/Users/Arjun/PythonProg/AANCHAL BANSAL.txt'),'html5lib')
td_element=soup0.find('table',id='gvrslt').find_all('td')
count5=0
count6=0
while(count5<24):
    sheet[sheet_columns[count5]+str(1)]=td_element[count6].get_text()
    sheet[sheet_columns[count5+1]+str(1)] = 'Total'
    sheet[sheet_columns[count5+2]+str(1)] = 'Percentage'
    count5=count5+3
    count6=count6+4


def get_td_elements(student,number1):
    sheet['A'+str(number1)]=student
    soup = BeautifulSoup(open('C:/Users/Arjun/PythonProg/'+student+ '.txt'),'html5lib')
    table = soup.find('table', id='gvrslt')
    return(table.find_all('td'))


def populate_csv(td,countt):
    count1=0
    #countt=3
    count3=1
    while(count3<33):
        sheet[sheet_columns[count1]+str(countt)] = int(td[count3].get_text())
        sheet[sheet_columns[count1+1]+str(countt)] = int(td[count3+1].get_text())
        count3=count3+4
        count1=count1+3
    #count2=count2+1
    
#count1=
count2=3
#count3=
number=3
for student in student_names:
    
    td_elements = get_td_elements(student,number)
    number=number+1
    populate_csv(td_elements,count2)
    count2=count2+1




#count1=0
#count2=    
#count3=0
#count4=0
def extract_kv_pairs(s):
    """Extract key value pairs seperated by colons and semi-colons."""
    kvp = []
    for r in s.split(';'):
        k, v = r.split(':')
        # is it an integer?
        try:
            # yes, convert it
            v = int(v)
        except ValueError:
            # no, trim the string
            v = v.strip()

        kvp.append((k.strip(), v))

    return kvp

#s = 'Division : First; Grand Total: 3861; Grand Max Total: 4600'
#kvp = extract_kv_pairs(s)
# [('Division', 'First'), ('Grand Total', 3861), ('Grand Max Total', 4600)]
#numeric_values = [p for p in kvp if isinstance(p[1], int)]
# [('Grand Total', 3861), ('Grand Max Total', 4600)]
sheet['R1']='VI'
sheet['AB1']='Grand Total'
sheet['AC1']='Grand Max Total'
sheet['AD1']='Division'
sheet['AE1']='Total Percentage'
countVI=3
for student in student_names:
    sheet['R'+str(countVI)] = int(BeautifulSoup(open('C:/Users/Arjun/PythonProg/'+student+ '.txt'),'html5lib').find('table',id='gvrslt').find_all('td')[21].get_text())
    s=BeautifulSoup(open('C:/Users/Arjun/PythonProg/' +student+ '.txt'),'html5lib').find('span',id='lbldiv').get_text()
    kvp = extract_kv_pairs(s)
    sheet['AB'+str(countVI)] = kvp[1][1]
    sheet['AC'+str(countVI)] = kvp[2][1]
    sheet['AD'+str(countVI)] = kvp[0][1]
    countVI=countVI+1
    
wb.save('StudentData.xlsx')

#print(td_elements[3].text)

#for td in td_elements:
#	print(td.text)




#count=0
#while(count<150):
 #   count=count+2   
  #  print(td_elements[count].text)
   # print(td_elements[count+1].text)
    #print(td_elements[count+2].text)
    #print(td_elements[count+3].text)
    #print(td_elements[count+4].text)

