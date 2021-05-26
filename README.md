# midSort
An efficient sorting algorithm
---
For array with n elements and m range of numbers

Algorithm

Step 1) Find max and min from the array [2n]

Step 2) Find mid value [1]

Step 3) Split into two array, one array with less than mid value, another with more than mid value [n]

Step 4) Repeat Step 1 to 3 for splitted array if array length is >1 [log m]
---
Overall average time complexity = n log(m)

Best case time complexity = n (Range = 1, every element is same)
---
Test Benchmark (0-1000 random ints)

| No. of elements | Mode | Seconds |
| --------------- | ---- | ------- |
| 2 |mid| 0.0 |
| 2 |quick| 0.0 |
| 4 |mid| 0.0 |
| 4 |quick| 0.0 |
| 8 |mid| 0.0 |
| 8 |quick| 0.0 |
| 16 |mid| 0.0 |
| 16 |quick| 0.0 |
| 32 |mid| 0.0 |
| 32 |quick| 0.0 |
| 64 |mid| 0.0 |
| 64 |quick| 0.0 |
| 128 |mid| 0.0 |
| 128 |quick| 0.0 |
| 256 |mid| 0.0009961128234863281 |
| 256 |quick| 0.000997781753540039 |
| 512 |mid| 0.001995563507080078 |
| 512 |quick| 0.0009963512420654297 |
| 1024 |mid| 0.003989458084106445 |
| 1024 |quick| 0.0030181407928466797 |
| 2048 |mid| 0.011969566345214844 |
| 2048 |quick| 0.006986141204833984 |
| 4096 |mid| 0.06682085990905762 |
| 4096 |quick| 0.013962507247924805 |
| 8192 |mid| 0.0359041690826416 |
| 8192 |quick| 0.048874616622924805 |
| 16384 |mid| 0.05784726142883301 |
| 16384 |quick| 0.1077117919921875 |
| 32768 |mid| 0.15857577323913574 |
| 32768 |quick| 0.351060152053833 |
| 65536 |mid| 0.26429319381713867 |
| 65536 |quick| 0.8991029262542725 |
| 131072 |mid| 0.520606279373169 |
| 131072 |quick| 2.634948492050171 |
| 262144 |mid| 0.9823253154754639 |
| 262144 |quick| 7.673469305038452 |
| 524288 |mid| 2.0823981761932373 |
| 524288 |quick| 34.21467041969299 |
