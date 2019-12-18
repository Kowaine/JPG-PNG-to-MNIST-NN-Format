# JPG-and-PNG-to-MNIST

Super simple method for converting a set of jpg and/or png images (or a mix) into mnist binary format for training  
On Windows!

# Dependencies:

Pillow
7z(Path variable is necessary)

```Pillow
pip install pillow
```

# Transform your images into an MNIST NN Ready Binary:


1\. Copy-pasta your jpg and/or png images(28x28) into one of the class folders, as seen in  (e.g. dogs -> 0, cats -> 1, ... giraffes->9)

2\. Change the appropriate labels in `batches.meta.txt`

3\. lastly, run the following python script to fold all the pics and categories into a single ble binary -- binary will appear as `ubyte` files ready to tar

`python convert-images-to-mnist-format.py`


# Victory!

You now have the files, and can replace the the conventional data in any standard mnist tutorial with your own data :D

Enjoy!

# Tree

example of where files will appear/where-to put png's (ignore placeholder.txt, this is only there so that git could check in their parent folders -- since empty folders can't be committed):
```

.
├── batches.meta.txt
├── convert-images-to-mnist-format.py
├── LICENSE
├── README.md
├── resize-script.sh
├── t10k-images(according to setting in 'convert-images-to-mnist-format.py')  
│   ├── 0
│   │   ├── home-cat.png
│   │   └── placeholder.txt
│   ├── 1
│   │   ├── dog-07.png
│   │   └── placeholder.txt
│   ├── 2
│   │   └── placeholder.txt
│   ├── 3
│   │   └── placeholder.txt
│   ├── 4
│   │   └── placeholder.txt
│   ├── 5
│   │   └── placeholder.txt
│   ├── 6
│   │   └── placeholder.txt
│   ├── 7
│   │   └── placeholder.txt
│   ├── 8
│   │   └── placeholder.txt
│   └── 9
│       └── placeholder.txt
└── training-images(according to setting in 'convert-images-to-mnist-format.py')  
    ├── 0
    │   ├── home-cat.png
    │   └── placeholder.txt
    ├── 1
    │   ├── dog-07.png
    │   └── placeholder.txt
    ├── 2
    │   └── placeholder.txt
    ├── 3
    │   └── placeholder.txt
    ├── 4
    │   └── placeholder.txt
    ├── 5
    │   └── placeholder.txt
    ├── 6
    │   └── placeholder.txt
    ├── 7
    │   └── placeholder.txt
    ├── 8
    │   └── placeholder.txt
    └── 9
        └── placeholder.txt
```
