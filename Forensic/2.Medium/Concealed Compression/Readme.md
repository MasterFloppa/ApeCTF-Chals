# Concealed Compression

### Overview
```

Score : 200 points
Author : FateGraphite

```
### Description

Master ape (King of ape) has concealed his secrets in an image and challeged his minions to find it
Help the minions in their mission..!

### Solution

```

Use binwalk -M <file> (or) hexeditor to identify the hidden zip file 

binwalk -e image.png
cd _image.png.extracted (extracted folder)

here we can find the secret folder
check out the might_be_flag.txt

ls -la reveals hidden jpg image
might_be_flag.txt has a hash value 

use your favorite password cracking tools to find out the passphrase (kingofmonkeyking)
steghide extract -sf <hidden jpg image>
enter the pass phrase 
flag.txt is found

```
