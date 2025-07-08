# PanoCycle360: A Cyclist-Centric $360^{\circ}$ Panoramic Dataset for Safety-Critical Object Detection in Real-World Cycling Scenarios

## 1.PanoCycle360 Download Link
 ​​Coming soon! The dataset is currently under compilation and will be uploaded before July 15.​


## 2.PanoCycle360 introduction
•	The first large-scale 360° panoramic dataset captured from a cyclist’s perspective.

•	PanoCycle360 annotated various safety-critical objects in complex road environments.

•	The novel annotation method effectively suppresses fisheye distortion.

•	PanoCycle360’s performance has been validated with the most popular detection models.


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

 ## 3.Details of the dataset

 ### The proportion of annotation boxes of each class in PanoCycle360.
 
 <img src="https://github.com/Feng-LChen/image/blob/main/images/bing.png" width="500px">
 
 <img src="https://github.com/Feng-LChen/image/blob/main/images/tongji.png" width="800px">

### The number distribution of annotation boxes under different modalities.
 <img src="https://github.com/Feng-LChen/image/blob/main/images/f1.png" width="300px"> <img src="https://github.com/Feng-LChen/image/blob/main/images/f2.png" width="300px"> <img src="https://github.com/Feng-LChen/image/blob/main/images/f3.png" width="300px"> 

### The distribution of the size of annotation boxes under different modalities.
 <img src="https://github.com/Feng-LChen/image/blob/main/images/Figure.10(a).png" width="300px"> <img src="https://github.com/Feng-LChen/image/blob/main/images/Figure.10(b).png" width="300px"> <img src="https://github.com/Feng-LChen/image/blob/main/images/Figure.10(c).png" width="300px"> 

 ### The distribution of center point coordinates of annotation boxes under different modalities.
  <img src="https://github.com/Feng-LChen/image/blob/main/images/Figure.9(a).png" width="300px"> <img src="https://github.com/Feng-LChen/image/blob/main/images/Figure.9(b).png" width="300px"> <img src="https://github.com/Feng-LChen/image/blob/main/images/Figure.9(c).png" width="300px"> 

  ## 4.Experimental results
   <img src="https://github.com/Feng-LChen/image/blob/main/images/result1.png" width="800px">
   <img src="https://github.com/Feng-LChen/image/blob/main/images/result2.png" width="800px">

   ## 5.Visualization of experimental results
   <img src="https://github.com/Feng-LChen/image/blob/main/images/result3.png" width="800px">
   The detection results of partial test images with different parameter quantities in the algorithms during the day.

   <img src="https://github.com/Feng-LChen/image/blob/main/images/result4.png" width="800px">
   The detection results of partial test images with different parameter quantities in the algorithms at night.
