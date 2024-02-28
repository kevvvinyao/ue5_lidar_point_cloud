# Write in front
This repository is created to store some source file and instruction about getting point cloud in `Unreal Engine 5` and subsequent operations.

# Workflow
### Remove the Unneeded 
The function `cleanUnneeded` in the file `formater.py` can be called to remove coordinate like `X= Y= Z=` and remove the invalid value `-nan(ind)` in the data file.


**original**:
```txt
X=13868.196 Y=20941.620 Z=52.236
X=-nan(ind) Y=-nan(ind) Z=-nan(ind)
X=13867.102 Y=20915.477 Z=47.973
```
**derived**:
```txt
13868.196 20941.620 52.236
13867.102 20915.477 47.973
```

