# SỬ DỤNG PHƯƠNG PHÁP LOCALITY SENSITIVE HASHING VÀ MÔI TRƯỜNG PYSPARK ĐỂ TÌM KIẾM CÁC VĂN BẢN TƯƠNG TỰ TRONG TẬP VĂN BẢN

## GIỚI THIỆU

Phương pháp Locality Sensitive Hashing (LSH) là một tập hợp các kỹ thuật sử dụng hàm băm giúp tăng tốc quá trình tìm kiếm lân cận hoặc phát hiện sự trùng lặp gần trên dữ liệu một cách đáng kể. Cách tiếp cận chung đối với LSH là “băm” (hash) các mục nhiều lần.

LSH sẽ sử dụng các hàm băm (LSH Families) để hash các dữ liệu vào từng bucket sao cho các dữ liệu gần nhau nhất sẽ có xác suất cao vào cùng một bucket được phân, ngược lại thì chúng sẽ bị băm vào hai bucket khác nhau.

LSH là một loại phương pháp dựa trên lân cận giống như k-nearest neighbors (KNN) nhưng lại có quy mô ưu việt hơn vì có thể mở rộng bằng cách sử dụng kỹ thuật Forest khi số lượng item tăng lên

## CÁC BƯỚC XỬ LÝ

Bài toán tìm kiếm văn bản tương tự trong tập dữ liệu bằng phương pháp LSH nhìn chung sẽ trải qua ba quá trình chính để có thể đưa ra một kết quả:

* Shingling
* Min-Hashing
* Locality sensitive Hashing

## DATASET

Dữ liệu là các bài báo được Crawl từ trang các Báo điện tử lớn ở Việt Nam:
* [Vn Express](https://vnexpress.net/)
* [Vietnam.net](https://vietnamnet.vn/)
* [Thanh niên](https://thanhnien.vn/)

## LÝ THUYẾT - [REPORT.DOCX](https://github.com/caoboiloi/Mining-Of-Massive-Datasets/blob/main/Spark%20-%20LSH%20(Locality-Sensitive%20Hashing)/report.docx)
## THỰC THI THUẬT TOÁN

Bài toán trên được thực thi trên Spark và Thường để có thể so sánh tốc độ giữa 2 cách làm với nhau:
* Spark: [LSH Spark](https://github.com/caoboiloi/Mining-Of-Massive-Datasets/blob/main/Spark%20-%20LSH%20(Locality-Sensitive%20Hashing)/GK_MINING_MASSIVE_DATASET_PYSPARK.ipynb)
* Thường: [LSH Original](https://github.com/caoboiloi/Mining-Of-Massive-Datasets/blob/main/Spark%20-%20LSH%20(Locality-Sensitive%20Hashing)/GK_MINING_MASSIVE_DATASET_ORIGINAL.ipynb)


# TÀI LIỆU THAM KHẢO

* http://infolab.stanford.edu/~ullman/mmds/ch3.pdf
* https://towardsdatascience.com/understanding-locality-sensitive-hashing-49f6d1f6134
* https://www.learndatasci.com/tutorials/building-recommendation-engine-locality-sensitive-hashing-lsh-python/
