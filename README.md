EditDistance-py
===============

Calculate the Levenshtein edit distance, which is the minimum number of single-character edits (insertions, deletions or substitutions) required to change one word into another. Also print the required edits.

This has applications in typo correction and correction systems for optical character recognition.

This uses a dynamic programming approach.

Getting started 
----------------

### Command Line 
Run this in the command line:
```
python -m editDistance word1 word2
```

Example output
```
zzzzHEllooWurlld -> HelloWorld
edit distance: 8
rm ̲zzzzHEllooWurlld -> _zzzHEllooWurlld
rm ̲zzzHEllooWurlld -> _zzHEllooWurlld
rm ̲zzHEllooWurlld -> _zHEllooWurlld
rm ̲zHEllooWurlld -> _HEllooWurlld
   H̲EllooWurlld -> H̲EllooWurlld
rp HE̲llooWurlld -> He̲llooWurlld
   Hel̲looWurlld -> Hel̲looWurlld
   Hell̲ooWurlld -> Hell̲ooWurlld
rm Hell̲ooWurlld -> Hell_oWurlld
   Hello̲Wurlld -> Hello̲Wurlld
   HelloW̲urlld -> HelloW̲urlld
rp HelloWu̲rlld -> HelloWo̲rlld
   HelloWor̲lld -> HelloWor̲lld
rm HelloWor̲lld -> HelloWor_ld
   HelloWorl̲d -> HelloWorl̲d
   HelloWorld̲ -> HelloWorld̲
```

### Importing
Available methods for importing with Python are:
* ```editDistance```
* ```editPath```
* ```printEdits```

e.g. in Python: ``` from editDistance import editDistance, editPath, printEdits ```

```_editDistanceDP``` is not meant to be used directly. It returns the matrix made with the dynamic programming algorithm.

Sources
----------------

* [Wikipedia: Edit Distance](https://en.wikipedia.org/wiki/Edit_distance)
* [Wikipedia: Edit Distance](https://en.wikipedia.org/wiki/Wagner%E2%80%93Fischer_algorithm), 
* Original code edited [GeeksForGeeks](https://www.geeksforgeeks.org/edit-distance-dp-5/)


