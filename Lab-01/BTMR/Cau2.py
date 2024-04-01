import re

def find_numbers(text):

    so_am = re.findall(r'-\d+', text)
    so = re.findall(r'-?\d+', text)
    so_duong = []
    for num in so:
        num_int = int(num)  
        if num_int > 0:
            so_duong.append(num_int) 
    tong_nguyen_am = sum(int(number) for number in so_am)
    tong_nguyen_duong = sum(int(number) for number in so_duong) + tong_nguyen_am*-1
    return tong_nguyen_duong, tong_nguyen_am

text = "-100#^sdfkj8902w3ir021@swf-20"
tong_duong , tong_am = find_numbers(text)
print("Giá  trị dương: ",tong_duong)
print("Giá  trị âm: ",tong_am)
so_duong = re.findall(r'-?\d+', text)

            