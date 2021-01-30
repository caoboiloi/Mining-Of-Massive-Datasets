<div align="justify">

# THUỘC TÍNH SPARK *(SPARK PROPERTIES)*

Thuộc tính Spark kiểm soát hầu hết các cài đặt ứng dụng và được cấu hình riêng cho từng ứng dụng. Các thuộc tính này có thể được đặt trực tiếp trên SparkConf được chuyển đến của bạn SparkContext. SparkConf cho phép bạn định cấu hình một số thuộc tính chung (ví dụ: URL chính và tên ứng dụng), cũng như các cặp key-value tùy ý thông qua phương thức set().

Ví dụ: chúng ta có thể khởi tạo một ứng dụng với hai luồng như sau:

```python
val conf = new SparkConf()
             .setMaster("local[2]")
             .setAppName("countingWord")
val sc = new SparkContext(conf)
```

Lưu ý: với **local[2]**, nghĩa là hai luồng - thể hiện được việc tối thiểu có 2 luồng đang chạy song song, có thể giúp phát hiện lỗi chỉ tồn tại khi ta chạy trong bối cảnh phân tán.

Các thuộc tính chỉ định một số khoảng thời gian với một đơn vị thời gian. Các định dạng sau được chấp nhận trong Spark:

```note
25ms (milliseconds)
5s (seconds)
10m or 10min (minutes)
3h (hours)
5d (days)
1y (years)
```

Các thuộc tính chỉ định kích thước byte so với một đơn vị kích thước. Các định dạng sau được chấp nhận trong Spark:

```note
1b (bytes)
1k or 1kb (kibibytes = 1024 bytes)
1m or 1mb (mebibytes = 1024 kibibytes)
1g or 1gb (gibibytes = 1024 mebibytes)
1t or 1tb (tebibytes = 1024 gibibytes)
1p or 1pb (pebibytes = 1024 tebibytes)
```

# TẢI ĐỘNG ĐỐI VỚI CÁC THUỘC TÍNH SPARK *(DYNAMICALLY LOADING SPARK PROPERTIES)*

Trong một số trường hợp, ta có thể tránh việc thiết lập cứng cho các cấu hình mặc định trong một SparkConf. 

Ví dụ: nếu bạn muốn chạy cùng một ứng dụng với các bản gốc khác nhau hoặc số lượng bộ nhớ khác nhau. Spark cho phép bạn chỉ cần tạo một SparkConf() trống:

```python
val sc = new SparkContext(new SparkConf())
```

Sau đó, bạn có thể cung cấp các giá trị cấu hình trong lúc chạy Spark:

```
./bin/spark-submit --name "My app" --master local[4] --conf spark.eventLog.enabled=false --conf "spark.executor.extraJavaOptions=-XX:+PrintGCDetails -XX:+PrintGCTimeStamps" myApp.jar
```

**Spark shell** và công cụ **spark-submit** hỗ trợ hai cách để tải cấu hình động cho các thuộc tính trong Spark. Đầu tiên là các tùy chọn dòng lệnh, chẳng hạn như **--master**, như được hiển thị ở trên. **spark-submit** có thể chấp nhận bất kỳ thuộc tính Spark nào bằng cách sử dụng flag **--conf/-c**, việc sử dụng flag đặc biệt cho các thuộc tính đóng một phần trong việc khởi chạy ứng dụng Spark. Lệnh chạy **./bin/spark-submit --help** sẽ hiển thị toàn bộ danh sách các tùy chọn này.

**bin/spark-submit** cũng sẽ đọc các tùy chọn cấu hình từ **conf/spark-defaults.conf**, trong đó mỗi dòng bao gồm một khóa và một giá trị được phân tách bằng khoảng trắng.

Ví dụ:

```note
spark.master            spark://5.6.7.8:7077
spark.executor.memory   4g
spark.eventLog.enabled  true
spark.serializer        org.apache.spark.serializer.KryoSerializer
```

Mọi giá trị được chỉ định dưới dạng flag hoặc trong file thuộc tính sẽ được chuyển đến ứng dụng và được hợp nhất với những giá trị được chỉ định thông qua **SparkConf**. Các thuộc tính được đặt trực tiếp trên **SparkConf** được ưu tiên cao nhất, sau đó các flag được chuyển đến **spark-submit** hoặc **spark-shell**, sau đó là các tùy chọn trong file **spark-defaults.conf**. Một vài khóa cấu hình đã được đổi tên kể từ các phiên bản Spark trước đó; trong những trường hợp như vậy, các tên khóa cũ hơn vẫn được chấp nhận, nhưng được ưu tiên thấp hơn bất kỳ trường hợp nào của khóa mới hơn.

Các thuộc tính của Spark chủ yếu có thể được chia thành hai loại:

* một là liên quan đến triển khai, như **spark.driver.memory**, **spark.executor.instances**, loại thuộc tính này có thể không bị ảnh hưởng khi thiết lập theo chương trình **SparkConf** trong thời gian chạy, hoặc hành vi tùy thuộc vào trình quản lý cụm và chế độ triển khai mà bạn chọn, vì vậy bạn nên đặt thông qua file cấu hình hoặc tùy chọn dòng lệnh trên **spark-submit**.

* một cái khác chủ yếu liên quan đến kiểm soát thời gian chạy Spark, như **spark.task.maxFailures**, loại thuộc tính này có thể được đặt theo một trong hai cách.

# XEM THUỘC TÍNH CỦA SPARK *(VIEWING SPARK PROPERTIES)*

Apache spark cung cấp một bộ giao diện người dùng web tại địa chỉ http://localhost:4040 (Jobs, Stages, Tasks, Storage, Environment, Executors, and SQL). Vào thẻ Environment để xem danh sách các thuộc tính của Spark:


![Spark properties](../Image/Spark_properties.png)

Ngoài ra có thể xác định giá trị mặc định thông qua spark-defaults.conf, SparkConf. Đối với các thuộc tính cấu hình khác, giá trị mặc định sẽ được áp dụng.

## Thuộc tính mặc định có sẳn

Hầu hết các thuộc tính đều có giá trị mặc định hợp lý. Một số thuộc tính như:

### Thuộc tính ứng dụng *(Application Properties)*

Ví dụ:

spark.app.name - Tên ứng dụng của bạn, được hiển thị trong giao diện người dùng và trong dữ liệu nhật ký.

![Spark app name](../Image/Spark_app_name.png)

Ngoài ra còn nhiều thuộc tính khác như:

* spark.driver.cores: Số lõi để sử dụng cho quy trình trình điều khiển, chỉ ở chế độ cụm.
* spark.logConf: Ghi lại SparkConf hiệu quả dưới dạng thông tin khi một SparkContext được khởi động.
* spark.driver.memoryOverhead: Số lượng bộ nhớ không phải bộ nhớ heap sẽ được phân bổ cho mỗi quá trình điều khiển ở chế độ cụm.
* spark.resources.discoveryPlugin, ...

### Thuộc tính xáo trộn *(Shuffle Behavior)*

Một vài thuộc tính như:

* spark.shuffle.compress: Có nén các map output file hay không.
* spark.shuffle.io.retryWait: (Chỉ mạng) Thời gian chờ giữa các lần tìm nạp lại. Theo mặc định, Độ trễ tối đa do thử lại là 15 giây.
* spark.shuffle.service.port: Cổng mà dịch vụ shuffle ngoài sẽ chạy, mặc định port 7337.
* spark.shuffle.compress, ...

### Giao diện người dùng Spark *(Spark UI)*

Ví dụ:

spark.eventLog.enabled - Có ghi lại các sự kiện Spark hay không, hữu ích trong việc tạo lại giao diện người dùng Web sau khi ứng dụng hoàn tất.

![spark.eventLog.enabled](../Image/Spark_eventLog_enabled.png)

Một vài thuộc tính khác:

* spark.eventLog.logBlockUpdates.enabled: Có ghi lại các sự kiện cho mỗi lần cập nhật khối hay không, nếu spark.eventLog.enabled là true => *Cảnh báo*: Điều này sẽ làm tăng đáng kể kích thước của nhật ký sự kiện.
* spark.eventLog.compress: Có nén các sự kiện đã ghi nếu spark.eventLog.enabled = true.
* spark.eventLog.overwrite: Có ghi đè lên bất kỳ tệp hiện có nào không.
* spark.ui.enabled: Có chạy giao diện người dùng web (User interface) cho ứng dụng Spark hay không.

### Nén và tuần tự hoá *(Compression and Serialization)*

spark.rdd.compress - Có nén các phân vùng tuần tự

Ví dụ:
StorageLevel.MEMORY_ONLY_SERtrong Java và Scala hoặc StorageLevel.MEMORY_ONLY trong Python). Có thể tiết kiệm không gian đáng kể với chi phí tăng thêm thời gian CPU. Nén sẽ sử dụng tới thuộc tính spark.io.compression.codec.

Các thuộc tính khác:

* spark.serializer
* spark.serializer.objectStreamReset
* spark.kryoserializer.buffer
* spark.kryo.registrator
* spark.kryo.referenceTracking, ...

### Các loại thuộc tính khác

Ngoài các loại thuộc tính trên, Spark còn hỗ trợ nhiều loại thuộc tính khác nhau:

* Môi trường thực thi (Runtime Environment)
* Quản lý bộ nhớ (Memory Management)
* Hành vi thực thi (Execution Behavior)
* Chỉ số thực thi (Executor Metrics)
* Kết nối mạng (Networking)
* Lập lịch (Scheduling)
* Chế độ thực thi rào cản (Barrier Execution Mode)
* Phân bố động (Dynamic Allocation)
* Cấu hình Thread (Thread Configurations)
* Bảo mật (Security)

</div>