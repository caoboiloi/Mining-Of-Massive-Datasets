# TỔNG QUAN VỀ SPARK RDD *(RESILIENT DISTRIBUTED DATASETS)*

Tập dữ liệu phân tán phục hồi (RDD - Resilient Distributed Datasets) một cấu trúc dữ liệu cơ bản của Spark. Nó là một tập hợp bất biến phân tán của một đối tượng. Mỗi dataset trong RDD được chia ra thành nhiều phần vùng logical. Có thể được tính toán trên các node khác nhau của một cụm máy chủ (cluster).

RDDs có thể chứa bất kỳ kiểu dữ liệu nào của Python, Java, hoặc đối tượng Scala, bao gồm các kiểu dữ liệu do người dùng định nghĩa. Thông thường, RDD chỉ cho phép đọc, phân mục tập hợp của các bản ghi. RDDs có thể được tạo ra qua điều khiển xác định trên dữ liệu trong bộ nhớ hoặc RDDs, RDD là một tập hợp có khả năng chịu lỗi mỗi thành phần có thể được tính toán song song.

Có hai cách để tạo RDDs:
 
Tạo từ một tập hợp dữ liệu có sẵn trong ngôn ngữ sử dụng như Java, Python, Scala.
Lấy từ dataset hệ thống lưu trữ bên ngoài như HDFS, Hbase hoặc các cơ sở dữ liệu quan hệ.

# RDD CREATION

Để tạo RDD, trước tiên cần tạo **SparkSession**, đây là một điểm vào ứng dụng PySpark. SparkSession có thể được tạo bằng cách sử dụng một *builder()* hoặc *newSession()* là các phương thức của **SparkSession**.

**SparkSession** tạo ra một biến sparkContext. Có thể tạo nhiều đối tượng SparkSession nhưng chỉ một SparkContext cho mỗi JVM (Java virtual machine). Trong trường hợp nếu bạn muốn tạo một SparkContext mới khác, bạn nên dừng Sparkcontext hiện có (sử dụng  *stop()*) trước khi tạo một cái mới.

Ví dụ:

```python
spark = SparkSession.builder()
      .master("local[2]")
      .appName("WordCount")
      .getOrCreate()  
```

# TÀI LIỆU THAM KHẢO

* https://laptrinh.vn/books/apache-spark/page/apache-spark-rdd
* https://helpex.vn/article/rdd-trong-spark-la-gi-va-tai-sao-chung-ta-can-no-5c6afe5bae03f628d053a84c
* https://sparkbyexamples.com/pyspark-tutorial/
* https://www.tutorialspoint.com/apache_spark/apache_spark_rdd.htm
* https://data-flair.training/blogs/spark-rdd-tutorial/
* https://spark.apache.org/docs/latest/rdd-programming-guide.html
* https://ichi.pro/vi/vi-du-ve-viec-su-dung-apache-spark-voi-pyspark-bang-python-267611095265298
* https://laptrinh.vn/link/93#bkmrk-t%E1%BA%A1o-t%E1%BB%AB-m%E1%BB%99t-t%E1%BA%ADp-h%E1%BB%A3p-d