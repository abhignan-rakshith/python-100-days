with open("file1.txt", "r") as file1:
  file1_list = file1.readlines()
  file1_list = [int(char_num.strip()) for char_num in file1_list]
  
with open("file2.txt", "r") as file2:
  file2_list = file2.readlines()
  file2_list = [int(char_num.strip()) for char_num in file2_list]

result = [num for num in file1_list if num in file2_list]

print(result)

w = input("Press 'enter' to exit...")