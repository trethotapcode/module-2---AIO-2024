import pandas as pd
import numpy as np
# lấy dữ liệu
data = pd.read_csv('advertising.csv')

# chuyển sang numpy
data = data.to_numpy()


# Lấy giá trị lớn nhất và chỉ mục tương ứng của nó trên cột Sales
max_value = data[:, 3].max()
index = np.nonzero(max_value == data)[0]
print(max_value, index)


# trung bình cột TV
print(data[:, 0].mean())


# Số lượng bản ghi có giá trị tại cột Sales lớn hơn hoặc bằng 20 là:
sales = data[:, 3]
print(len(sales[sales >= 20]))


# Tính giá trị trung bình của cột Radio thoả mãn điều kiện giá trị tương ứng
# trên cột Sales lớn hơn hoặc bằng 15

# lấy cột sales ở trên.
# vector reduces sales về > 15. lấy được index vector.
sales_reduce = np.nonzero(sales >= 15)[0]

# lấy cột radio gốc.
radio = data[:, 1]

# lấy các phần tử radio tương ứng sales>15 bằng index list.
radio_reduce = radio[sales_reduce]
print(radio_reduce.mean())


# Tính tổng các hàng của cột Sales với điều kiện giá trị Newspaper lớn hơn
# giá trị trung bình của cột Newspaper:
news = data[:, 2]
news_mean = news.mean()
# nonzero get index
news_condition = np.nonzero(news >= news_mean)[0]
sales_condition = sales[news_condition]
print(sales_condition.sum())


# Gọi giá trị trung bình của cột Sales là A. Tạo ra mảng mới scores chứa các
# giá trị Good, Average và Bad sao cho: nếu giá trị hiện tại > A => giá trị trong mảng mới
# là Good, < A thì sẽ là Bad và = A sẽ là Average. Sau đó in ra kết quả scores[7:10]

a = sales.mean()
# nhúng where trong where
score = np.where(sales >= a, np.where(
    sales > a, 'Good', 'Average'), 'Bad')
print(score[7:10])

# Gọi giá trị trên cột Sales gần nhất với giá trị trung bình cũng chính cột
# Sales là A. Tạo ra mảng mới scores chứa các giá trị Good, Average và Bad sao cho: nếu
# giá trị hiện tại > A => giá trị trong mảng mới là Good, < A thì sẽ là Bad và = A sẽ là
# Average. Sau đó in ra kết quả scores[7:10]

new_scores = abs(sales-a)
idx = np.nonzero(new_scores == new_scores.min())[0]
aver_value = sales[idx]

score = np.where(sales >= aver_value, np.where(
    sales > aver_value, 'Good', 'Average'), 'Bad')
print(score[7:10])
