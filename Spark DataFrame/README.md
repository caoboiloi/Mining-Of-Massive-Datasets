<div align="justify">

# TỔNG QUAN VỀ SPARK DATAFRAME

Theo Databricks, DataFrame là một tập hợp dữ liệu phân tán được tổ chức thành các cột được đặt tên. Về mặt khái niệm, nó tương đương với một bảng trong cơ sở dữ liệu quan hệ hoặc một khung dữ liệu trong R / Python, nhưng với các tối ưu hóa phong phú hơn. DataFrames có thể được xây dựng từ nhiều nguồn như tệp dữ liệu có cấu trúc, Hive table, cơ sở dữ liệu bên ngoài hoặc RDD hiện có.

Dataframe thường đề cập đến một cấu trúc dữ liệu, có bản chất là dạng bảng. Nó đại diện cho các Hàng, mỗi hàng bao gồm một số quan sát. Các hàng có thể có nhiều định dạng dữ liệu khác nhau (Không đồng nhất), trong khi một cột có thể có dữ liệu có cùng kiểu dữ liệu (Đồng nhất). Khung dữ liệu thường chứa một số siêu dữ liệu ngoài dữ liệu; ví dụ, tên cột và hàng.

![Spark_DataFrame_Define](../Image/Spark_dataframe_define.jpg)

![spark_dataframes_define_2](../Image/spark_dataframes_define_2.png)

# DATAFRAME CREATION

## sử dụng *createDataFrame()*

Bằng cách sử dụng createDataFrame()chức năng của SparkSession, bạn có thể tạo một DataFrame:

```python
import pyspark
from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession
import collections
spark = SparkSession.builder.master("local[2]").appName("dataframetest").getOrCreate()
data = [('51800574','Loi','Tan','Huynh','2000-02-26','M',3320),
  ('51800544','Minh','Nhat','Pham','2000-05-19','M',1000),
  ('51800302','Linh','Nhat','Nguyen','2000-09-05','M',4000),
  ('51800112','Nam','Van','Ho','2000-04-01','M',2200),
  ('51800115','Thong','Huy','Luu','2000-07-17','M',3480)
]

columns = ["id","firstname","middlename","lastname","birth","gender","salary"]
df = spark.createDataFrame(data=data, schema = columns)
# df.show() hiển thị 20 phần tử đầu
df.show()
```

```note
+--------+---------+----------+--------+----------+------+------+
|      id|firstname|middlename|lastname|     birth|gender|salary|
+--------+---------+----------+--------+----------+------+------+
|51800574|      Loi|       Tan|   Huynh|2000-02-26|     M|  3320|
|51800544|     Minh|      Nhat|    Pham|2000-05-19|     M|  1000|
|51800302|     Linh|      Nhat|  Nguyen|2000-09-05|     M|  4000|
|51800112|      Nam|       Van|      Ho|2000-04-01|     M|  2200|
|51800115|    Thong|       Huy|     Luu|2000-07-17|     M|  3480|
+--------+---------+----------+--------+----------+------+------+
```

## DataFrame Operations

Giống như RDD, DataFrame cũng có các hoạt động như Biến đổi (DataFrame Transformations) và Hành động (DataFrame Actions).

## DataFrame từ nguồn dữ liệu bên ngoài

Ví dụ:

```python
import pyspark
from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession
from google.colab import drive
drive.mount('/content/drive', force_remount=True)
import collections
spark = SparkSession.builder.master("local[2]").appName("dataframetest").getOrCreate()
df = spark.read.csv("drive/MyDrive/BIGDATA/Week2/DataFrame/DataAnalyst.csv")
df.printSchema()
```

## Các định dạng tệp được hỗ trợ

DataFrame có một bộ API phong phú hỗ trợ đọc và ghi một số định dạng tệp như:

* csv
* text
* Avro
* Parquet
* tsv
* xml và nhiều hơn nữa,...

# TÀI LIỆU THAM KHẢO

* https://codetudau.com/xu-ly-du-lieu-voi-spark-dataframe/index.html
* https://helpex.vn/article/huong-dan-pyspark-dataframe-gioi-thieu-ve-dataframes-5c6b21e6ae03f628d053c29e
* https://www.edureka.co/blog/pyspark-dataframe-tutorial/#what
* https://sparkbyexamples.com/pyspark-tutorial/
</div>