# GIỚI THIỆU VỀ THUẬT TOÁN APRIORI

Bài toán khai thác tập phổ biến (frequent itemset) là bài toán rất quan trọng trong lĩnh vực data mining. Bài toán khai thác tập phổ biến là bài toán tìm tất cả tập các hạng mục (itemset) S có độ phổ biến (support) thỏa mãn độ phổ biến tối thiểu minsupp.

Dựa trên tính chất của tập phổ biến, ta có phương pháp tìm kiếm theo chiều rộng (thuật toán Apriori (1994)) hay phương pháp phát triển mẫu (thuật toán FP-Growth (2000)). Trong bài viết này, ta sẽ nói về Apriori cùng với một ví dụ được triển khai trên 1 tập dataset [Store data](https://github.com/caoboiloi/Mining-Of-Massive-Datasets/blob/main/Spark%20-%20Apriori%20Algorithm/store_data.csv) khi chạy thuật toán này.