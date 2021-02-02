A = [5, 1, 2, 3, 4, 0, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 11, 21]
k = 0
max_len_increase_arr = 0 # Kích thước lớn nhất của mảng liên tục tăng hiện đang tìm thấy
result = []
while k < len(A):
 if k == 0 or (k > 0 and A[k-1] > A[k]): # Nếu có dấu hiệu bắt đầu tăng
    i = k # Đánh dấu biến i ban đầu bằng k
    while i + 1 < len(A) and A[i] <= A[i+1]: # Nếu mảng tăng
        i += 1 # Tăng dần biến
    if i > k:
        i += 1
        if i - k > max_len_increase_arr: # Xoá result cũ đi
            result = [(k, i)]
            print(A[k: i])
            max_len_increase_arr = i - k
            print(f"max_len_increase_arr = {max_len_increase_arr}")
        elif i - k == max_len_increase_arr: # Thêm vào result cũ
            result.append((k, i))
            print(A[k: i])
            max_len_increase_arr = i - k
            print(f"max_len_increase_arr = {max_len_increase_arr}")
        k = i
    else:
        k += 1
 else:
    k += 1
print(result)