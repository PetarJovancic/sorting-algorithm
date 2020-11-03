import gender_lastname_sort
import datebirth_sort
import lastname_sort
import read_data
from datetime import datetime

"""
Variables
"""
text1="gender then lastname ascending\n--------------------------\n"
text2="\ndateofbirth ascending\n--------------------------\n"
text3="\nlastname descending\n--------------------------\n"

"""
Execution of first sorting
"""
final_list1=read_data.main()
GenderLastname=gender_lastname_sort.gender_lastname_sort(final_list1)

"""
Execution of second sorting
"""
final_list2=read_data.main()
for i in final_list2:
    i[3]=datetime.strptime(i[3], '%m/%d/%Y')
Datebirth=datebirth_sort.datebirth_sort(final_list2)
for i in Datebirth:
    i[3]=datetime.strftime(i[3],'%m/%d/%Y')

"""
Execution of third sorting
"""
final_list3 = read_data.main()
Lastname=lastname_sort.lastname_sort(final_list3)


"""
Writing output to .txt
"""
def output(text,x):
    with open("output.txt", "a+") as f:
        f.write(text)
        for i in range(0,len(x)):
            for j in range(0,5):
                f.write("{:<15}".format(x[i][j]))
            f.write("\n")
        f.close()

output(text1,GenderLastname)
output(text2,Datebirth)
output(text3,Lastname)