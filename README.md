# Write in front
This repository is created to store some source file and instruction about getting point cloud in `Unreal Engine 5` and sequential operations.

# Workflow
### Remove the coordinate indicator
After getting the point cloud file of `.txt`, use the python script `remove_Cor.py` to remove the coordinate indicator of data.

**original.txt**:
```txt
X=13887.905 Y=20843.490 Z=135.916
X=13887.905 Y=20843.490 Z=109.581
X=13887.905 Y=20843.490 Z=90.309
```
**new.txt**:
```txt
13887.905 20843.490 135.916
13887.905 20843.490 109.581
13887.905 20843.490 90.309
```
### Remove the invalid value 
There are some lines recording **invalid** data of position of points, which may cause error when using datafile `.txt`. It's sensible to remove them by using the script `remove_Ind.py`.
```txt
13868.196 20941.620 52.236
-nan(ind) -nan(ind) -nan(ind)
13867.102 20915.477 47.973
```

