# Clustering Assignment Analysis

### My Output
Custom KMeans - k=2, SSE: 2478059388299320.0

Custom KMeans - k=3, SSE: 637716608492624.0

Custom KMeans - k=4, SSE: 385013093896074.0

Custom KMeans - k=5, SSE: 272027647776499.0


Sklearn KMeans - k=2, SSE: 475585783363368.4
Cluster Centers (k=2):
 [[3.34303691e+01 3.81956414e+04 1.72525971e+04 1.71259114e+04]
 [2.48202114e+01 1.30599315e+05 6.18098878e+03 5.98992219e+03]]

Sklearn KMeans - k=3, SSE: 292008115188059.0
Cluster Centers (k=3):
 [[2.81200740e+01 9.40193639e+04 8.94408051e+03 8.79142348e+03]
 [2.17733538e+01 1.70161850e+05 3.94257497e+03 3.77208483e+03]
 [3.39402302e+01 3.19185997e+04 1.83138862e+04 1.81752821e+04]]

Sklearn KMeans - k=4, SSE: 215836165625000.75
Cluster Centers (k=4):
 [[3.10980792e+01 6.79191062e+04 1.20655078e+04 1.19919748e+04]
 [2.52203237e+01 1.20542550e+05 6.34200348e+03 6.09324607e+03]
 [3.42866409e+01 2.63341438e+04 1.94242157e+04 1.92701585e+04]
 [2.05770073e+01 1.94624111e+05 3.23460196e+03 3.15734876e+03]]

Sklearn KMeans - k=5, SSE: 173599077566984.12
Cluster Centers (k=5):
 [[3.29512041e+01 5.24107033e+04 1.40518175e+04 1.39845654e+04]
 [2.32406758e+01 1.43495218e+05 4.81522715e+03 4.56849813e+03]
 [3.42508370e+01 2.20943794e+04 2.05525770e+04 2.03743785e+04]
 [1.95349894e+01 2.17814208e+05 2.82458224e+03 2.81853672e+03]
 [2.79287445e+01 9.54810209e+04 8.65806989e+03 8.49866694e+03]]

 ### Analysis

It seems that the Sklearns implementation of the clustering process achieved better SSE values than the customKmeans implementation. The lower SSE values that the Sklearns clustering achieved means that the data was clustered more accurately and tightly. As K increases, the average values for the columns we clustered over, odometer, condition, mmr, and selling price, became more refined. We also get better SSE values when K increases, especially after seeing the difference between k=3 and k=4. K=3 provides us a good balance between finding the best SSE value and not overfitting.

After looking at the clusters, we can see that there are three particular variations. New vehicles, slightly used vehicles, and older or heavily used vehicles. However, there are some anomalies we need to look at, which could be a result of wrong data, or incorrect implementation. It seems that vehicles with lower mileage have a lower MMR, which is quite odd. There is also the possiblity that some luxury, rare vehicles are outliers and throwing the clustering off because of their low mileage, but also low MMR because of their resale value. This is something we intend to look at. 