# SPARK VỚI HỌC MÁY (MACHINE LEARNING)

## BÀI TOÁN: DỰ ĐOÁN NGƯỜI DÙNG CÓ GỬI MỘT KHOẢNG TIỀN GỬI CÓ KỲ HẠN CHO NGÂN HÀNG HAY KHÔNG - [BANK DATASET](https://github.com/caoboiloi/Mining-Of-Massive-Datasets/blob/main/Spark%20With%20Machine%20Learning/bank.csv)

Dùng model Logistic Regression để training data

## THỰC THI CODE

#### Bước 1: Thêm các thư viện cần thiết

```python
import pyspark
import pandas as pd
import numpy as np
from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession
from google.colab import drive
import time
from pyspark.sql import SQLContext
drive.mount('/content/drive')
import collections
from pyspark.mllib.linalg import *
from pyspark.ml.feature import HashingTF, IDF, Tokenizer, StopWordsRemover
from pyspark.mllib.linalg import SparseVector
from scipy.spatial import distance
from pyspark.ml import Pipeline
from pyspark.ml.feature import StringIndexer
import json
conf = SparkConf().setMaster("local[8]").setAppName("Exercise")
sc = SparkContext.getOrCreate(conf=conf)
spark = SparkSession(sc)
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType, StringType, FloatType
from pyspark.sql.functions import concat, lit
from pyspark.sql.functions import monotonically_increasing_id 
```

#### Bước 2: Đọc data từ file
```python
df = spark.read.csv('/content/drive/MyDrive/BIGDATA/Week5/bank.csv', header = True, inferSchema=True)
df.printSchema()
```

```note
root
 |-- age: integer (nullable = true)
 |-- job: string (nullable = true)
 |-- marital: string (nullable = true)
 |-- education: string (nullable = true)
 |-- default: string (nullable = true)
 |-- balance: integer (nullable = true)
 |-- housing: string (nullable = true)
 |-- loan: string (nullable = true)
 |-- contact: string (nullable = true)
 |-- day: integer (nullable = true)
 |-- month: string (nullable = true)
 |-- duration: integer (nullable = true)
 |-- campaign: integer (nullable = true)
 |-- pdays: integer (nullable = true)
 |-- previous: integer (nullable = true)
 |-- poutcome: string (nullable = true)
 |-- deposit: string (nullable = true)
```
#### Bước 3: Preprocessing data

```python
df = df.toPandas()
df.deposit = df.deposit.apply(lambda x: 1 if x == 'yes' else 0)
```

Chuyển các features thành các vector thông qua StringIndexer có trong PySpark (***from pyspark.ml.feature import StringIndexer***)
```python
class_name = 'deposit'
df.groupby(class_name).count()
df = spark.createDataFrame(df)
indexers = [StringIndexer(inputCol=column, outputCol=column+"_index").fit(df) for column in list(set(df.columns)-set(['date'])) ]
pipeline = Pipeline(stages=indexers)
df_r = pipeline.fit(df).transform(df)
df_r.show()
```
Kết quả nhận được
```note
+---+-----------+--------+---------+-------+-------+-------+----+-------+---+-----+--------+--------+-----+--------+--------+-------+-----------+-------------+---------+-------------+--------------+--------------+--------------+-----------+-------------+-------------+--------------+---------+-------------+---------------+----------+-------------+---------+
|age|        job| marital|education|default|balance|housing|loan|contact|day|month|duration|campaign|pdays|previous|poutcome|deposit|month_index|default_index|job_index|contact_index|duration_index|campaign_index|poutcome_index|pdays_index|housing_index|marital_index|previous_index|day_index|deposit_index|education_index|loan_index|balance_index|age_index|
+---+-----------+--------+---------+-------+-------+-------+----+-------+---+-----+--------+--------+-----+--------+--------+-------+-----------+-------------+---------+-------------+--------------+--------------+--------------+-----------+-------------+-------------+--------------+---------+-------------+---------------+----------+-------------+---------+
| 59|     admin.| married|secondary|     no|   2343|    yes|  no|unknown|  5|  may|    1042|       1|   -1|       0| unknown|      1|        0.0|          0.0|      3.0|          1.0|         788.0|           0.0|           0.0|        0.0|          1.0|          0.0|           0.0|      3.0|          1.0|            0.0|       0.0|       2746.0|     31.0|
| 56|     admin.| married|secondary|     no|     45|     no|  no|unknown|  5|  may|    1467|       1|   -1|       0| unknown|      1|        0.0|          0.0|      3.0|          1.0|        1004.0|           0.0|           0.0|        0.0|          0.0|          0.0|           0.0|      3.0|          1.0|            0.0|       0.0|        436.0|     32.0|
| 41| technician| married|secondary|     no|   1270|    yes|  no|unknown|  5|  may|    1389|       1|   -1|       0| unknown|      1|        0.0|          0.0|      2.0|          1.0|         999.0|           0.0|           0.0|        0.0|          1.0|          0.0|           0.0|      3.0|          1.0|            0.0|       0.0|        680.0|     12.0|
| 55|   services| married|secondary|     no|   2476|    yes|  no|unknown|  5|  may|     579|       1|   -1|       0| unknown|      1|        0.0|          0.0|      4.0|          1.0|         563.0|           0.0|           0.0|        0.0|          1.0|          0.0|           0.0|      3.0|          1.0|            0.0|       0.0|       2787.0|     26.0|
| 54|     admin.| married| tertiary|     no|    184|     no|  no|unknown|  5|  may|     673|       2|   -1|       0| unknown|      1|        0.0|          0.0|      3.0|          1.0|         643.0|           1.0|           0.0|        0.0|          0.0|          0.0|           0.0|      3.0|          1.0|            1.0|       0.0|        285.0|     29.0|
| 42| management|  single| tertiary|     no|      0|    yes| yes|unknown|  5|  may|     562|       2|   -1|       0| unknown|      1|        0.0|          0.0|      0.0|          1.0|         393.0|           1.0|           0.0|        0.0|          1.0|          1.0|           0.0|      3.0|          1.0|            1.0|       1.0|          0.0|     13.0|
| 56| management| married| tertiary|     no|    830|    yes| yes|unknown|  6|  may|    1201|       1|   -1|       0| unknown|      1|        0.0|          0.0|      0.0|          1.0|         971.0|           0.0|           0.0|        0.0|          1.0|          0.0|           0.0|      8.0|          1.0|            1.0|       1.0|        848.0|     32.0|
| 60|    retired|divorced|secondary|     no|    545|    yes|  no|unknown|  6|  may|    1030|       1|   -1|       0| unknown|      1|        0.0|          0.0|      5.0|          1.0|         688.0|           0.0|           0.0|        0.0|          1.0|          2.0|           0.0|      8.0|          1.0|            0.0|       0.0|       1152.0|     33.0|
| 37| technician| married|secondary|     no|      1|    yes|  no|unknown|  6|  may|     608|       1|   -1|       0| unknown|      1|        0.0|          0.0|      2.0|          1.0|         395.0|           0.0|           0.0|        0.0|          1.0|          0.0|           0.0|      8.0|          1.0|            0.0|       0.0|          1.0|      7.0|
| 28|   services|  single|secondary|     no|   5090|    yes|  no|unknown|  6|  may|    1297|       3|   -1|       0| unknown|      1|        0.0|          0.0|      4.0|          1.0|         985.0|           2.0|           0.0|        0.0|          1.0|          1.0|           0.0|      8.0|          1.0|            0.0|       0.0|       3388.0|     14.0|
| 38|     admin.|  single|secondary|     no|    100|    yes|  no|unknown|  7|  may|     786|       1|   -1|       0| unknown|      1|        0.0|          0.0|      3.0|          1.0|         866.0|           0.0|           0.0|        0.0|          1.0|          1.0|           0.0|     16.0|          1.0|            0.0|       0.0|         78.0|      8.0|
| 30|blue-collar| married|secondary|     no|    309|    yes|  no|unknown|  7|  may|    1574|       2|   -1|       0| unknown|      1|        0.0|          0.0|      1.0|          1.0|        1013.0|           1.0|           0.0|        0.0|          1.0|          0.0|           0.0|     16.0|          1.0|            0.0|       0.0|         91.0|      5.0|
| 29| management| married| tertiary|     no|    199|    yes| yes|unknown|  7|  may|    1689|       4|   -1|       0| unknown|      1|        0.0|          0.0|      0.0|          1.0|        1309.0|           3.0|           0.0|        0.0|          1.0|          0.0|           0.0|     16.0|          1.0|            1.0|       1.0|        151.0|     10.0|
| 46|blue-collar|  single| tertiary|     no|    460|    yes|  no|unknown|  7|  may|    1102|       2|   -1|       0| unknown|      1|        0.0|          0.0|      1.0|          1.0|         949.0|           1.0|           0.0|        0.0|          1.0|          1.0|           0.0|     16.0|          1.0|            1.0|       0.0|       1131.0|     15.0|
| 31| technician|  single| tertiary|     no|    703|    yes|  no|unknown|  8|  may|     943|       2|   -1|       0| unknown|      1|        0.0|          0.0|      2.0|          1.0|         903.0|           1.0|           0.0|        0.0|          1.0|          1.0|           0.0|     10.0|          1.0|            1.0|       0.0|        184.0|      0.0|
| 35| management|divorced| tertiary|     no|   3837|    yes|  no|unknown|  8|  may|    1084|       1|   -1|       0| unknown|      1|        0.0|          0.0|      0.0|          1.0|         941.0|           0.0|           0.0|        0.0|          1.0|          2.0|           0.0|     10.0|          1.0|            1.0|       0.0|       3154.0|      4.0|
| 32|blue-collar|  single|  primary|     no|    611|    yes|  no|unknown|  8|  may|     541|       3|   -1|       0| unknown|      1|        0.0|          0.0|      1.0|          1.0|         619.0|           2.0|           0.0|        0.0|          1.0|          1.0|           0.0|     10.0|          1.0|            2.0|       0.0|        812.0|      1.0|
| 49|   services| married|secondary|     no|     -8|    yes|  no|unknown|  8|  may|    1119|       1|   -1|       0| unknown|      1|        0.0|          0.0|      4.0|          1.0|         951.0|           0.0|           0.0|        0.0|          1.0|          0.0|           0.0|     10.0|          1.0|            0.0|       0.0|        915.0|     20.0|
| 41|     admin.| married|secondary|     no|     55|    yes|  no|unknown|  8|  may|    1120|       2|   -1|       0| unknown|      1|        0.0|          0.0|      3.0|          1.0|         693.0|           1.0|           0.0|        0.0|          1.0|          0.0|           0.0|     10.0|          1.0|            0.0|       0.0|        449.0|     12.0|
| 49|     admin.|divorced|secondary|     no|    168|    yes| yes|unknown|  8|  may|     513|       1|   -1|       0| unknown|      1|        0.0|          0.0|      3.0|          1.0|         459.0|           0.0|           0.0|        0.0|          1.0|          2.0|           0.0|     10.0|          1.0|            0.0|       1.0|         82.0|     20.0|
+---+-----------+--------+---------+-------+-------+-------+----+-------+---+-----+--------+--------+-----+--------+--------+-------+-----------+-------------+---------+-------------+--------------+--------------+--------------+-----------+-------------+-------------+--------------+---------+-------------+---------------+----------+-------------+---------+
only showing top 20 rows
```

Sau khi chuyển các features thành các number, gom chúng lại thành 1 Array vào cột ***features***

```python
# Bỏ cột label đi vì không tính chung vào
df_r = df_r.drop(df_r.deposit_index)
```

Dùng VectorAssembler trong PySpark dể gom các features thành 1 array (***from pyspark.ml.feature import VectorAssembler***)
```python
from pyspark.ml.feature import VectorAssembler

feature_names = df_r.columns[17:]
print(feature_names)
assembler = VectorAssembler()
assembler.setInputCols(feature_names).setOutputCol('features')
transformed_data = assembler.transform(df_r)

transformed_data.show()
```
```note
['month_index', 'default_index', 'job_index', 'contact_index', 'duration_index', 'campaign_index', 'poutcome_index', 'pdays_index', 'housing_index', 'marital_index', 'previous_index', 'day_index', 'education_index', 'loan_index', 'balance_index', 'age_index']
+---+-----------+--------+---------+-------+-------+-------+----+-------+---+-----+--------+--------+-----+--------+--------+-------+-----------+-------------+---------+-------------+--------------+--------------+--------------+-----------+-------------+-------------+--------------+---------+---------------+----------+-------------+---------+--------------------+
|age|        job| marital|education|default|balance|housing|loan|contact|day|month|duration|campaign|pdays|previous|poutcome|deposit|month_index|default_index|job_index|contact_index|duration_index|campaign_index|poutcome_index|pdays_index|housing_index|marital_index|previous_index|day_index|education_index|loan_index|balance_index|age_index|            features|
+---+-----------+--------+---------+-------+-------+-------+----+-------+---+-----+--------+--------+-----+--------+--------+-------+-----------+-------------+---------+-------------+--------------+--------------+--------------+-----------+-------------+-------------+--------------+---------+---------------+----------+-------------+---------+--------------------+
| 59|     admin.| married|secondary|     no|   2343|    yes|  no|unknown|  5|  may|    1042|       1|   -1|       0| unknown|      1|        0.0|          0.0|      3.0|          1.0|         788.0|           0.0|           0.0|        0.0|          1.0|          0.0|           0.0|      3.0|            0.0|       0.0|       2746.0|     31.0|(16,[2,3,4,8,11,1...|
| 56|     admin.| married|secondary|     no|     45|     no|  no|unknown|  5|  may|    1467|       1|   -1|       0| unknown|      1|        0.0|          0.0|      3.0|          1.0|        1004.0|           0.0|           0.0|        0.0|          0.0|          0.0|           0.0|      3.0|            0.0|       0.0|        436.0|     32.0|(16,[2,3,4,11,14,...|
| 41| technician| married|secondary|     no|   1270|    yes|  no|unknown|  5|  may|    1389|       1|   -1|       0| unknown|      1|        0.0|          0.0|      2.0|          1.0|         999.0|           0.0|           0.0|        0.0|          1.0|          0.0|           0.0|      3.0|            0.0|       0.0|        680.0|     12.0|(16,[2,3,4,8,11,1...|
| 55|   services| married|secondary|     no|   2476|    yes|  no|unknown|  5|  may|     579|       1|   -1|       0| unknown|      1|        0.0|          0.0|      4.0|          1.0|         563.0|           0.0|           0.0|        0.0|          1.0|          0.0|           0.0|      3.0|            0.0|       0.0|       2787.0|     26.0|(16,[2,3,4,8,11,1...|
| 54|     admin.| married| tertiary|     no|    184|     no|  no|unknown|  5|  may|     673|       2|   -1|       0| unknown|      1|        0.0|          0.0|      3.0|          1.0|         643.0|           1.0|           0.0|        0.0|          0.0|          0.0|           0.0|      3.0|            1.0|       0.0|        285.0|     29.0|(16,[2,3,4,5,11,1...|
| 42| management|  single| tertiary|     no|      0|    yes| yes|unknown|  5|  may|     562|       2|   -1|       0| unknown|      1|        0.0|          0.0|      0.0|          1.0|         393.0|           1.0|           0.0|        0.0|          1.0|          1.0|           0.0|      3.0|            1.0|       1.0|          0.0|     13.0|(16,[3,4,5,8,9,11...|
| 56| management| married| tertiary|     no|    830|    yes| yes|unknown|  6|  may|    1201|       1|   -1|       0| unknown|      1|        0.0|          0.0|      0.0|          1.0|         971.0|           0.0|           0.0|        0.0|          1.0|          0.0|           0.0|      8.0|            1.0|       1.0|        848.0|     32.0|(16,[3,4,8,11,12,...|
| 60|    retired|divorced|secondary|     no|    545|    yes|  no|unknown|  6|  may|    1030|       1|   -1|       0| unknown|      1|        0.0|          0.0|      5.0|          1.0|         688.0|           0.0|           0.0|        0.0|          1.0|          2.0|           0.0|      8.0|            0.0|       0.0|       1152.0|     33.0|(16,[2,3,4,8,9,11...|
| 37| technician| married|secondary|     no|      1|    yes|  no|unknown|  6|  may|     608|       1|   -1|       0| unknown|      1|        0.0|          0.0|      2.0|          1.0|         395.0|           0.0|           0.0|        0.0|          1.0|          0.0|           0.0|      8.0|            0.0|       0.0|          1.0|      7.0|(16,[2,3,4,8,11,1...|
| 28|   services|  single|secondary|     no|   5090|    yes|  no|unknown|  6|  may|    1297|       3|   -1|       0| unknown|      1|        0.0|          0.0|      4.0|          1.0|         985.0|           2.0|           0.0|        0.0|          1.0|          1.0|           0.0|      8.0|            0.0|       0.0|       3388.0|     14.0|(16,[2,3,4,5,8,9,...|
| 38|     admin.|  single|secondary|     no|    100|    yes|  no|unknown|  7|  may|     786|       1|   -1|       0| unknown|      1|        0.0|          0.0|      3.0|          1.0|         866.0|           0.0|           0.0|        0.0|          1.0|          1.0|           0.0|     16.0|            0.0|       0.0|         78.0|      8.0|(16,[2,3,4,8,9,11...|
| 30|blue-collar| married|secondary|     no|    309|    yes|  no|unknown|  7|  may|    1574|       2|   -1|       0| unknown|      1|        0.0|          0.0|      1.0|          1.0|        1013.0|           1.0|           0.0|        0.0|          1.0|          0.0|           0.0|     16.0|            0.0|       0.0|         91.0|      5.0|(16,[2,3,4,5,8,11...|
| 29| management| married| tertiary|     no|    199|    yes| yes|unknown|  7|  may|    1689|       4|   -1|       0| unknown|      1|        0.0|          0.0|      0.0|          1.0|        1309.0|           3.0|           0.0|        0.0|          1.0|          0.0|           0.0|     16.0|            1.0|       1.0|        151.0|     10.0|(16,[3,4,5,8,11,1...|
| 46|blue-collar|  single| tertiary|     no|    460|    yes|  no|unknown|  7|  may|    1102|       2|   -1|       0| unknown|      1|        0.0|          0.0|      1.0|          1.0|         949.0|           1.0|           0.0|        0.0|          1.0|          1.0|           0.0|     16.0|            1.0|       0.0|       1131.0|     15.0|[0.0,0.0,1.0,1.0,...|
| 31| technician|  single| tertiary|     no|    703|    yes|  no|unknown|  8|  may|     943|       2|   -1|       0| unknown|      1|        0.0|          0.0|      2.0|          1.0|         903.0|           1.0|           0.0|        0.0|          1.0|          1.0|           0.0|     10.0|            1.0|       0.0|        184.0|      0.0|(16,[2,3,4,5,8,9,...|
| 35| management|divorced| tertiary|     no|   3837|    yes|  no|unknown|  8|  may|    1084|       1|   -1|       0| unknown|      1|        0.0|          0.0|      0.0|          1.0|         941.0|           0.0|           0.0|        0.0|          1.0|          2.0|           0.0|     10.0|            1.0|       0.0|       3154.0|      4.0|(16,[3,4,8,9,11,1...|
| 32|blue-collar|  single|  primary|     no|    611|    yes|  no|unknown|  8|  may|     541|       3|   -1|       0| unknown|      1|        0.0|          0.0|      1.0|          1.0|         619.0|           2.0|           0.0|        0.0|          1.0|          1.0|           0.0|     10.0|            2.0|       0.0|        812.0|      1.0|[0.0,0.0,1.0,1.0,...|
| 49|   services| married|secondary|     no|     -8|    yes|  no|unknown|  8|  may|    1119|       1|   -1|       0| unknown|      1|        0.0|          0.0|      4.0|          1.0|         951.0|           0.0|           0.0|        0.0|          1.0|          0.0|           0.0|     10.0|            0.0|       0.0|        915.0|     20.0|(16,[2,3,4,8,11,1...|
| 41|     admin.| married|secondary|     no|     55|    yes|  no|unknown|  8|  may|    1120|       2|   -1|       0| unknown|      1|        0.0|          0.0|      3.0|          1.0|         693.0|           1.0|           0.0|        0.0|          1.0|          0.0|           0.0|     10.0|            0.0|       0.0|        449.0|     12.0|(16,[2,3,4,5,8,11...|
| 49|     admin.|divorced|secondary|     no|    168|    yes| yes|unknown|  8|  may|     513|       1|   -1|       0| unknown|      1|        0.0|          0.0|      3.0|          1.0|         459.0|           0.0|           0.0|        0.0|          1.0|          2.0|           0.0|     10.0|            0.0|       1.0|         82.0|     20.0|(16,[2,3,4,8,9,11...|
+---+-----------+--------+---------+-------+-------+-------+----+-------+---+-----+--------+--------+-----+--------+--------+-------+-----------+-------------+---------+-------------+--------------+--------------+--------------+-----------+-------------+-------------+--------------+---------+---------------+----------+-------------+---------+--------------------+
only showing top 20 rows
```

#### Bước 4: Áp dụng model training data

Phân data thành 2 tập Train & Test với tỉ lệ 8:2
```python
[training_data, test_data] = transformed_data.randomSplit([0.8,0.2])
training_data.toPandas()
```
Lấy cột label
```python
class_name = 'deposit'
```

Tạo model Logistic Regression
```python
from pyspark.ml.classification import LogisticRegression
model = LogisticRegression(featuresCol = 'features',labelCol=class_name, maxIter=30)
```
Bỏ tập data training vào model để model học tập
```python
M = model.fit(training_data)
```

Kết quả Prediction với tập data testing
```python
predictions = M.transform(test_data)
from pyspark.ml.evaluation import MulticlassClassificationEvaluator

multi_evaluator = MulticlassClassificationEvaluator(labelCol = 'deposit', metricName = 'accuracy')
print('Logistic Regression Accuracy:', multi_evaluator.evaluate(predictions))
```

Kết quả
```note
Logistic Regression Accuracy: 0.781408191440405
```

Độ chính xác sau khi Training và Testing ~~ 78%