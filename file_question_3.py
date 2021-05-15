bank_list=["Kotak","HDF","RBL","SBI","Bank of Baroda"]
file=open("file_question_3.txt","r+")
# i=0
# while i<len(bank_list):
#     file.write(bank_list[i])
#     file.write("\n")
#     i+=1



for i in bank_list:
    file.write(i)
    file.write("\n")
