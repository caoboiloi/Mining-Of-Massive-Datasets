<div align="justify">

# Tổng quan về MapReduce

### MapReduce là gì ?

![MapReduce](https://blog.itnavi.com.vn/wp-content/uploads/2020/06/Mapreduce-l%C3%A0-g%C3%AC-1.jpg)

# Tổng quan về Apache Spark

![Apache Spark](https://scontent.fsgn2-5.fna.fbcdn.net/v/t1.0-9/92210827_2562659827300256_1174788299802279936_n.jpg?_nc_cat=102&ccb=2&_nc_sid=74df0b&_nc_ohc=kifyepT5UTgAX8nyvFX&_nc_ht=scontent.fsgn2-5.fna&oh=0a8e3ce705a1df978f105c6d00ddb978&oe=602D6251)

Ngày nay có rất nhiều hệ thống xử lý dữ liệu thông tin đang sử dụng Hadoop rộng rãi để phân tích dữ liệu lớn. Ưu điểm lớn nhất của Hadoop là được dựa trên một mô hình lập trình song song với xử lý dữ liệu lớn là MapReduce, mô hình này cho phép khả năng tính toán có thể mở rộng, linh hoạt, khả năng chịu lỗi, chi phí rẻ. Điều này cho phép tăng tốc thời gian xử lý các dữ liệu lớn nhằm duy trì tốc độ, giảm thời gian chờ đợi khi dữ liệu ngày càng lớn.

Hadoop đã được nền tảng tính toán cho rất nhiều cho một bài toàn xử lý dữ liệu lớn và các vấn đề về mở rộng tính toán song song trong các bài toàn xếp hạng. Apache Haddop cũng được sử dụng tại rất nhiều công ty lớn như Yahoo, Google. Dù có rất nhiều điểm mạnh về khả năng tính toán song song và khả năng chịu lỗi cao nhưng Apache Haddop có một nhược điểm là tất cả các thao tác đều phải thực hiện trên ổ đĩa cứng điều này đã làm giảm tốc độ tính toán đi gấp nhiều lần.
 
Để khắc phục được nhược điểm này thì Apache Spark được ra đời. Apache Spark có thể chạy nhanh hơn 10 lần so với Haddop ở trên đĩa cứng và 100 lần khi chạy trên bộ nhớ RAM, hình dưới biểu thị thời gian chạy của tính toán hồi quy Logistic trên Haddop và Spark.

### Apache Spark là gì ?

Apache Spark *(gọi tắt là Spark)* là một framework mã nguồn mở tính toán cụm, được phát triển sơ khởi vào năm 2009 bởi AMPLab. Sau này, Spark đã được trao cho Apache Software Foundation vào năm 2013 và được phát triển cho đến nay.

![Apache Spark](https://images.viblo.asia/full/d3be4c1c-8e98-4797-a68c-5862502b121b.png)

Apache Spark là một open source cluster computing framework được phát triển sơ khởi vào năm 2009 bởi AMPLab tại đại học California, Berkeley.

Sau này, Spark đã được trao cho Apache Software Foundation vào năm 2013 và được phát triển cho đến nay. Apache Spark được phát triển nhằm tăng tốc khả năng tính toán xử lý của Haddop.

Spark cho phép xây dựng và phân tích nhanh các mô hình dự đoán. Hơn nữa, nó còn cung cấp khả năng truy xuất toàn bộ dữ liệu cùng lúc, nhờ vậy ta không cần phải lấy mẫu dữ liệu đòi hỏi bởi các ngôn ngữ lập trình như R.

Thêm vào đó, Spark còn cung cấp tính năng streaming, được dùng để xây dựng các mô hình real-time bằng cách nạp toàn bộ dữ liệu vào bộ nhớ. Khi ta có một tác vụ nào đó quá lớn mà không thể xử lý trên một laptop hay một server, Spark cho phép ta phân chia tác vụ này thành những phần dễ quản lý hơn. Sau đó, Spark sẽ chạy các tác vụn ày trong bộ nhớ, trên các cluster của nhiều server khác nhau để khai thác tốc độ truy xuất nhanh từ RAM.
 
Spark sử dụng API Resilient Distributed Dataset (RDD) để xử lý dữ liệu. Spark nhận được nhiều sự hưởng ứng từ cộng đồng Big Data trên thế giới do cung cấp khả năng tính toán nhanh và nhiều thư viện hữu ích đi kèm như Spark SQL (với kiểu dữ liệu DataFrames), Spark Streaming, MLlib (machine learning: classification, regression, clustering, collaborative filtering, và dimensionality reduction) và GraphX (tính toán song song trên dữ liệu đồ thị)

### Thành phần của Spark:

![Spark core](https://techinsight.com.vn/wp-content/uploads/2016/12/stark2.jpg)

Apache Spark gồm có 5 thành phần chính : Spark Core, Spark Streaming, Spark SQL, MLlib và GraphX, trong đó:

* **Spark Core**: là engine thực thi chung làm nền tảng cho Spark. Tất cả các chức năng khác được xây dựng dựa trên base là Spark Core. Nó cung cấp khả năng tính toán trên bộ nhớ RAM và cả bộ dữ liệu tham chiếu trong các hệ thống external storage.

* **Spark SQL**: là một thành phần nằm trên Spark Core, giới thiệu một khái niệm trừu tượng hóa dữ liệu mới gọi là SchemaRDD, cung cấp hỗ trợ cho dữ liệu có cấu trúc và bán cấu trúc.

* **Spark Streaming**: tận dụng khả năng lập lịch memory-base của Spark Core để thực hiện streaming analytics. Nó lấy dữ liệu theo mini-batches và thực hiện các phép biến đổi RDD (Bộ dữ liệu phân tán có khả năng phục hồi) trên các mini-batches dữ liệu đó.

* **MLlib** *(Machine Learning Library)*: là một framework machine learning phân tán trên Spark tận dụng khả năng tính toán tốc độ cao nhờ distributed memory-based của kiến ​​trúc Spark.

* **GrapX**: là một framework xử lý đồ thị phân tán. Nó cung cấp một API để thực hiện tính toán biểu đồ có thể mô hình hóa các biểu đồ do người dùng xác định bằng cách sử dụng API đã được tối ưu sẵn.

### Tính năng, ưu nhược điểm của Spark:

![Apache Spark](https://scontent.fsgn2-4.fna.fbcdn.net/v/t1.0-9/92670619_2562655537300685_174298646274113536_n.jpg?_nc_cat=101&ccb=2&_nc_sid=32a93c&_nc_ohc=SPI9-fWp_PUAX-iq0BD&_nc_ht=scontent.fsgn2-4.fna&oh=ffd2b66a7fec1e8c85ea7e7b503fb57d&oe=602D8444)

*Tính năng và cũng là ưu điểm của Spark:*

* **Advanced Analytics**: Spark không chỉ hỗ trợ "Map" và "Reduce ", nó còn hỗ trợ Spark truy vấn SQL, Streaming data, Machine learning (ML) và các thuật toán xử lý đồ thị đóng vai trò như một bộ công cụ phân tích dữ liệu cực kì mạnh mẽ.

* **Speed**: Spark giúp chạy một ứng dụng với tốc độ rất nhanh. So với Hadoop cluster, Spark Application nến chạy trên bộ nhớ nhanh hơn tới 100 lần và nhanh hơn 10 lần khi chạy trên đĩa. Điều này có được nhờ giảm số lượng các hoạt động đọc / ghi vào ổ đĩa.

* **Supports multiple languages**: Spark cung cấp built-in APIs phổ biến từ Java, Scala đến Python, R. Do đó, có thể code Spark applications với nhiều lựa chọn về ngôn ngữ lập trình. Bên cạnh đó Spark còn cung cấp rất nhiều high-level operators cho việc truy vấn dữ liệu...

*Nhược điểm:*

* Spark không có hệ thống Filesystem riêng, do đó, nó phụ thuộc vào một số nền tảng khác như Hadoop hoặc một nền tảng dựa trên đám mây (S3, Google Cloud Storage,...).

* Apache Spark đòi hỏi rất nhiều RAM để chạy trong bộ nhớ, do đó chi phí của Spark khá cao.

* Spark Streaming không thực sự real-time.

* Việc tối ưu hóa, tinh chỉnh để phù hợp với các bộ dữ liệu cụ thể cần có kinh nghiệm và vẫn cần thực hiện thủ công.

### Mục tiêu sử dụng:

Xử lý dữ liệu nhanh và tương tác

Xử lý đồ thị

Công việc lặp đi lặp lại

Xử lý thời gian thực

joining Dataset

Machine Learning

Apache Spark là Framework thực thi dữ liệu dựa trên Hadoop HDFS. Apache Spark không thay thế cho Hadoop nhưng nó là một framework ứng dụng. Apache Spark tuy ra đời sau nhưng được nhiều người biết đến hơn Apache Hadoop vì khả năng xử lý hàng loạt và thời gian thực.

### Spark tại các công ty công nghệ lớn trên thế giới:

**Ebay**: eBay sử dụng Apache Spark để cung cấp các ưu đãi được nhắm mục tiêu, nâng cao trải nghiệm của khách hàng và để tối ưu hóa hiệu suất tổng thể. Apache Spark được tận dụng tại eBay thông qua Hadoop YARN.

**Alibaba**: Alibaba một trong những nền tảng thương mại điện tử lớn nhất thế giới, sử Apache Spark để phân tích hàng trăm petabyte dữ liệu trên nền tảng thương mại điện tử của mình. Một số công việc Spark thực hiện trích xuất tính năng trên dữ liệu hình ảnh, chạy trong vài tuần. Hàng triệu thương nhân và người dùng tương tác với nền tảng thương mại điện tử Alibaba Taobao. Mỗi tương tác này được biểu diễn dưới dạng một biểu đồ lớn phức tạp và Spark được sử dụng để xử lý nhanh quá trình bằng các thuật toán ML tinh vi trên dữ liệu này.

Những use case tiêu biểu khác có thể liệt kê như các công ty công nghệ như Uber và Netflix sử dụng các công cụ Spark Streaming và MLlib, đến các tổ chức như NASA, CERN và Broad Institute of MIT và Harvard áp dụng Spark vào phân tích dữ liệu khoa học.

### Spark Application

![Apache Spark](https://scontent.fsgn2-5.fna.fbcdn.net/v/t1.0-9/92953707_2568473546718884_2605275033735528448_n.jpg?_nc_cat=104&ccb=2&_nc_sid=32a93c&_nc_ohc=FL4Hd7NjXMsAX-8QhC4&_nc_ht=scontent.fsgn2-5.fna&oh=dc016f6fc5a6084be7533152573d8e76&oe=602D87BB)

Một ứng dụng Spark sẽ gồm 2 thành phần chính:

* **Driver Program**: Là 1 JVM Process, chứa hàm main() như bất kì 1 chương trình JVM nào khác, nó đóng vai trò điều phối code/ logic xử lý trên driver. Driver program chứa Spark Session.

* **Executor**: Là các worker, chịu trách nhiệm thực hiện các tính toán các logic nhận từ Driver. Dữ liệu cần xử lý có thể được load trực tiếp vào memory của Executor.

**Spark session**: Đại diện cho khả năng tương tác với executors trong 1 chương trình. Spark session chính là entry point của mọi chương trình Spark. Từ SparkSession, có thể tạo RDD/ DataFrame/ DataSet, thực thi SQL… từ đó thực thi tính toán phân tán.

Khi chạy, từ logic của chương trình (chính là code xử lý thông qua việc gọi các API), Driver sẽ sinh ra các task tương ứng và lên lịch chạy các task, sau đó gửi xuống Executor để thực thi. Dữ liệu được lưu trên memory của Executor nên việc thực thi tính toán sẽ nhanh hơn rất nhiều.

### RDD (Resilient Distributed Dataset):

![RDD](https://scontent.fsgn2-2.fna.fbcdn.net/v/t1.0-9/93049505_2568474116718827_523214101409693696_n.jpg?_nc_cat=103&ccb=2&_nc_sid=32a93c&_nc_ohc=R-yQ0NKgKpsAX8968KB&_nc_oc=AQmePbQQQgLBF_wFuVRVJQ5znGotCRa8OMC3xNSPpvosJ2sqowUYVzxCvj0oi4OFnkQ&_nc_ht=scontent.fsgn2-2.fna&oh=a937b6407524587cde9f225cc20cd666&oe=602D67D4)

Trong 1 chương trình Spark, RDD là đại diện cho tập dữ liệu phân tán.

Đặc điểm quan trọng của 1 RDD là số partitions. Một RDD bao gồm nhiều partition nhỏ, mỗi partition này đại diện cho 1 phần dữ liệu phân tán. Khái niệm partition là logical, tức là 1 node xử lý có thể chứa nhiều hơn 1 RDD partition. Theo mặc định, dữ liệu các partitions sẽ lưu trên memory. Thử tưởng tượng bạn cần xử lý 1TB dữ liệu, nếu lưu hết trên mem tính ra thì cung khá tốn kém nhỉ. Tất nhiên nếu bạn có 1TB ram để xử lý thì tốt quá nhưng điều đó không cần thiết. Với việc chia nhỏ dữ liệu thành các partition và cơ chế lazy evaluation của Spark bạn có thể chỉ cần vài chục GB ram và 1 chương trình được thiết kế tốt để xử lý 1TB dữ liệu, chỉ là sẽ chậm hơn có nhiều RAM thôi.

</div>

