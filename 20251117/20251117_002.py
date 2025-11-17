# book 디셔너리 데이터에서, value값을 변경하려고 한다.
# value가 15000원을 초과하는 책은 5%인상하여 수정하고,
# value가 15000원 이하인 책은 10% 인상하여 수정한다.

book = {'역사대모험' : 19999, '영단어' : 9000, '파이썬' : 17000, '여행에세이' : 22000,'삼국지' : 33000}
print(f"인상전 book : {book}")
for k, v in book.items():
    if v>14999:
        book[k] = v*0.05
    else:
        book[k] = v*0.1
print(f"인상후 book : {book}")