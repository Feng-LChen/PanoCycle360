# PanoCycle360: A Cyclist-Centric $360^{\circ}$ Panoramic Dataset for Safety-Critical Object Detection in Real-World Cycling Scenarios

## PanoCycle360 Download Link
 ​​Coming soon! The dataset is currently under compilation and will be uploaded before July 15.​


## PanoCycle360 introduction
Cycling safety is becoming an increasingly significant challenge for urban transportation, and vision-based object detection technology for cycling scenes has been widely studied. Datasets are an essential component of studying object detection in cycling scenes; however, existing datasets often have limitations, including limited scene diversity and incomplete coverage of safety-critical objects. What is particularly critical is that the data acquisition perspective is not from the perspective of real cyclists, and the limited field of view cannot cover blind spot risks. Such limitations limit the ability of datasets to capture the complexity and potential dangers of real-world cycling environments, hindering their suitability for training deep learning based risk assessment and object detection models. To address these limitations, we introduce PanoCycle360, a novel 360° panoramic dataset designed for complex cycling scenarios, aiming to train deep learning based object detection models for cycling scenarios. All data are collected using a 360° panoramic camera mounted on the cyclist’s helmet, providing full 360° coverage to eliminate blind spots in cycling and encompassing all common safety-critical objects and real-world cycling scenarios. To enhance the accuracy and reliability of the dataset for object detection, 10,055 panoramic images underwent pixel-level manual annotation, encompassing nine high-frequency cycling risk object classes, such as E-Bike Rider, Person, Car, Bus, Truck, Cyclist, Cargo Tricycle, and Auto Rickshaw, resulting in 102,171 bounding boxes. This paper provides a comprehensive analysis of the distributional features of safety-critical objects in panoramic images, characterized by their alignment along the central axis and aggregation within undistorted regions, which helps mitigate the effects of inherent fisheye distortion. It suppresses its influence without complex correction calculations, providing a novel method for annotating panoramic image object detection bounding boxes from a cyclist’s natural perspective. Finally, we evaluated the applicability of the PanoCycle360 dataset in single-stage, two-stage, and Transformer-based object detection frameworks by testing it across various algorithms with different parameter scales. In combination with the experimental results, it can be concluded that PanoCycle360 exhibits excellent performance in multiple scenarios. The development of the PanoCycle360 dataset holds significant implications for advancing cyclist-centric safety research and developing safety-critical object detection systems for real-world cycling scenarios worldwide.

The following table shows the details of the raw data.
| Number  | Size | Duration | Time | Weather | Objects | Scenario |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
| 1  | 15.3GB  | 00:29:59  | Day  | Cloudy  | o1,o2,o3,o4,o5,o6,o7,o8,o9  | s1  |
| 2  | 3.06GB  | 00:06:02  | Day  | Cloudy  | o1,o2,o3,o4,o5,o7,o8  |  s1,s4  |
| 3  | 15.8GB  | 00:29:59  | Day  | Sunny  | o1,o2,o3,o4,o5,o6,o7,o8,o9  |  s1  |
| 4  | 0.81GB  | 00:01:32  | Day  | Sunny  | o1,o2,o3,o4,o5,o6,o7,o8  |  s1  |
| 5  | 16.4GB  | 00:29:59  | Day  | Sunny  | o1,o2,o3,o4,o5,o6,o7,o8,o9  |  s1  |
| 6  | 1.86GB  | 00:03:25  | Day  | Sunny  | o1,o2,o3,o4,o5, o7,o8  |  s1,s4  |
| 7  | 4.12GB  | 00:09:23  | Night  | Cloudy  | o1,o2,o3,o4,o5,o6,o7,o8,o9  |  s2,s8  |
| 8  | 2.29GB  | 00:05:22  | Night  | Cloudy  | o1,o2,o3,o4,o5,o7,o8,o9  |  s1,s2,s8  |
| 9  | 3.57GB  | 00:08:08  | Night  | Cloudy  | o1,o2,o3,o4,o5,o6,o7,o8,o9  |  s1,s2,s8  |
| 10  | 5.02GB  | 00:10:09  | Night  | Cloudy  | o1,o2,o3,o4,o5,o7,o8,o9  |  s1  |
| 11  | 9.49GB  | 00:20:59  | Night  | Cloudy  | o1,o2,o3,o4,o5,o6,o7,o8,o9  |  s1,s2  |
| 12  | 9.58GB  | 00:17:13  | Day  | Sunny  | o1,o2,o3,o4,o5,o6,o7,o8,o9  |  s1,s7  |
| 13  | 2.04GB  | 00:04:29  | Day  | Sunny  | o1,o2,o3,o4,o5,o7,o8  |  s1,s5  |
| 14  | 3.16GB  | 00:06:50  | Day  | Cloudy  | o1,o3,o4,o5,o6,o7,o9  |  s3,s6  |
| 15  | 14.8GB  | 00:29:59  | Day  | Cloudy  | o1,o2,o3,o4,o5,o6,o7,o8,o9  |  s1,s2,s5,s9  |
| 16  | 0.97GB  | 00:01:53  | Day  | Cloudy  | o1,o3,o4,o5,o7  |  s2,s6  |
| 17  | 4.72GB  | 00:10:04  | Night  | Cloudy  | o1,o4  |  s2,s3  |
| 18  | 2.87GB  | 00:05:34  | Night  | Cloudy  | o1,o2,o3,o4,o5,o7,o8  |  s1,s3  |
| 19  | 40.24GB  | 01:11:32  | Day  | Sunny  | o1,o2,o3,o4,o5,o6,o7,o8,o9  |  s1,s2  |
| 20  | 27.91GB  | 01:04:37  | Night  | Cloudy  | o1,o2,o3,o4,o5,o6,o7,o8,o9  |  s1,s2  |

*o1. Person, o2. Bus, o3. Car, o4. Cyclist, o5. E-Bike Rider, o6. Cargo Tricycle, o7. Van, o8. Truck, o9. Auto Rickshaw,
 s1. Urban Roads, s2. Suburban Roads, s3. Cycling Greenways，s4. Bridge, s5. Viaduct, s6.Park, s7. Avenue, s8. Ferry, s9. Rail

The following pictures show the classes of the dataset.
 ![image](https://github.com/Feng-LChen/image/blob/main/images/9.png)

 ## Details of the dataset

 ### The proportion of annotation boxes of each class in PanoCycle360.
 
 <img src="https://github.com/Feng-LChen/image/blob/main/images/bing.png" width="500px">
 
 <img src="https://github.com/Feng-LChen/image/blob/main/images/tongji.png" width="800px">

### The number distribution of annotation boxes under different modalities.
 <img src="https://github.com/Feng-LChen/image/blob/main/images/f1.png" width="300px"> <img src="https://github.com/Feng-LChen/image/blob/main/images/f2.png" width="300px"> <img src="https://github.com/Feng-LChen/image/blob/main/images/f3.png" width="300px"> 

### The distribution of the size of annotation boxes under different modalities.
 <img src="https://github.com/Feng-LChen/image/blob/main/images/Figure.10(a).png" width="300px"> <img src="https://github.com/Feng-LChen/image/blob/main/images/Figure.10(b).png" width="300px"> <img src="https://github.com/Feng-LChen/image/blob/main/images/Figure.10(c).png" width="300px"> 

 ### The distribution of center point coordinates of annotation boxes under different modalities.
  <img src="https://github.com/Feng-LChen/image/blob/main/images/Figure.9(a).png" width="300px"> <img src="https://github.com/Feng-LChen/image/blob/main/images/Figure.9(b).png" width="300px"> <img src="https://github.com/Feng-LChen/image/blob/main/images/Figure.9(c).png" width="300px"> 

  ## Experimental results
   <img src="https://github.com/Feng-LChen/image/blob/main/images/result1.png" width="800px">
   <img src="https://github.com/Feng-LChen/image/blob/main/images/result2.png" width="800px">

   ## Visualization of experimental results
   <img src="https://github.com/Feng-LChen/image/blob/main/images/result3.png" width="800px">
   The detection results of partial test images with different parameter quantities in the algorithms during the day.

   
    <img src="https://github.com/Feng-LChen/image/blob/main/images/result4.png" width="800px">
   The detection results of partial test images with different parameter quantities in the algorithms at night.
