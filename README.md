# Video Classification using SIFT

This program uses the SIFT algorithm to classify videos.

### Prerequisites

Python3 is required.

The required Python packages can be installed with 

```
pip3 install -r requirements.txt
```

OpenCV and ffmpeg are only required if you want to run the program in full (not just doing the demo).


### How to Run
To reproduce the results from the paper.

```
python3 demo.py
```

To regenerate all files and rerun the the whole program
```
python3 init.py -r violentflows -m max

```
-r is the root folder of the dataset.

-m is the method. (max or mean)

## Use on a different dataset
Make sure the structure is as follows.
```
dataset
    movies
        category1
            movie1.avi
            movie2.avi
            ...
        category2
            movie1.avi
            movie2.avi
            ...
```


## Authors

* **Garrett Beatty**

## License

This project is licensed under the Apache License - see the [LICENSE.md](LICENSE.md) file for details
