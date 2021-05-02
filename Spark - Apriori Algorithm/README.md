<div align="justify">

# GIỚI THIỆU VỀ THUẬT TOÁN APRIORI

Bài toán khai thác tập phổ biến (frequent itemset) là bài toán rất quan trọng trong lĩnh vực data mining. Bài toán khai thác tập phổ biến là bài toán tìm tất cả tập các hạng mục (itemset) S có độ phổ biến (support) thỏa mãn độ phổ biến tối thiểu minsupp.

Dựa trên tính chất của tập phổ biến, ta có phương pháp tìm kiếm theo chiều rộng (thuật toán Apriori (1994)) hay phương pháp phát triển mẫu (thuật toán FP-Growth (2000)). Trong bài viết này, ta sẽ nói về Apriori cùng với một ví dụ được triển khai trên 1 tập dataset - [Store data](https://github.com/caoboiloi/Mining-Of-Massive-Datasets/blob/main/Spark%20-%20Apriori%20Algorithm/store_data.csv) khi chạy thuật toán này.

### Thuật toán Apriori

Thuật toán Apriori được công bố bởi R. Agrawal và R. Srikant vào năm 1994 vì để tìm các tập phổ biến trong một bộ dữ liệu lớn. Tên của thuật toán là Apriori vì nó sử dụng kiến thức đã có từ trước (prior) về các thuộc tính, vật phẩm thường xuyên xuất hiện trong cơ sở dữ liệu. Để cải thiện hiệu quả của việc lọc các mục thường xuyên theo cấp độ, một thuộc tính quan trọng được sử dụng gọi là thuộc tính Apriori giúp giảm phạm vi tìm kiếm của thuật toán.

### Các khái niệm cơ bản

Để minh họa cho các khái niệm, ta lấy ví dụ CSDL với các giao dịch sau. 
```note
| TID (mã giao dịch) | Itemset (tập các hạng mục) |
| 1 | A, B, E |
| 2 | B, D |
| 3 | B, C |
| 4 | A, B, D |
| 5 | A, C |
| 6 | B, C |
| 7 | A, C |
| 8 | A, B, C, E |
| 9 | A, B, C |
```
* Hạng mục (item): mặt hàng A = apple, B = bread, C = cereal, D = donuts, E = eggs.

* Tập các hạng mục (itemset): danh sách các hạng mục trong giỏ hàng như {A, B, C, D, E}.

* Giao dịch (transaction): tập các hạng mục được mua trong một giỏ hàng, lưu kèm với mã giao dịch (TID).

* Mẫu phổ biến (frequent item): là mẫu xuất hiện thường xuyên trong tập dữ liệu như {A, C} xuất hiện khá nhiều trong các giao dịch.

* Tập k-hạng mục (k-itemset): ví dụ danh sách sản phẩm (1-itemset) như {A, B, C}, danh sách cặp sản phẩm đi kèm (2-itemset) như {{A, B}, {A, C}}, danh sách 3 sản phẩm đi kèm (3-itemset) như {{A, B, C}, {B, C, E}}.

* Độ phổ biến (support): được tính bằng supp(X) = count(X)/D. Với X = {B, C} là tập các hạng mục (B giao với C), D là cơ sở dữ liệu (CSDL) giao dịch.

* Tập phổ biến (frequent itemset): là tập các hạng mục S (itemset) thỏa mãn độ phổ biến tối thiểu (minsupp – do người dùng xác định như 40% hoặc xuất hiện 5 lần). Nếu supp(S) >= minsupp thì S là tập phổ biến.

* Tập phổ biến tối đại (max pattern) thỏa supp(X)  >= minsupp không tồn tại |X’| > |X|, với X’ cũng phổ biến.

* Tập phổ biến đóng (closed pattern) thỏa supp(S)  >= minsupp không tồn tại |X’| > |X| mà supp(X’) = supp(X).

* Luật kết hợp (association rule): kí hiệu X => Y, nghĩa là khi X có mặt thì Y cũng có mặt (với xác suất nào đó). Ví dụ, A => B; A,B => C; B,D => E.

* Độ tin cậy (confidence): được tính bằng conf(X) = supp(X,Y)/supp(X).

![SparkApriori](../Image/Spark_Apriori_2.png)

</div>