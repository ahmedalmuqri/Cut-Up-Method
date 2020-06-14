# Cut-Up-Method
Performs Cut Up technique on text files to divide text into different arrangements to form an innovative text. Maybe Poetry or any meaningful text.

Details of Cut up method can be found in link below:
Burroughs explains how he does Cut-Ups: 
http://www.languageisavirus.com/creative-writing-techniques/william-s-burroughs-cut-ups.php#.XnQJ_YgzaUk

Details of this program functioning is as under:
Read text in a string from some txt file. Currently Text file is named as 'new.txt'
Set some sentence limit for each cut piece. This can be changed by variable 'step' below. Default is 30
Set some Number of Columns(number of lists) or No. of partitions into which which we want to divide text.
This can be set by variable 'num_columns' below. Default is 30.
From String captured before, Write 1st sentence in 1st column and then in 2nd column until last column
then write sentences in same way from start again until end in each column until end of string is reached.
Merge these columns in all possible Permutations. Itertools is used for this
then use readability index to see which one is more readable and then output that one.
Dale Chall Readability is used for readability index.
Details of modules used in this program can be found from link below
https://pypi.org/project/py-readability-metrics/

To Use, Simply write name of your file in variable 'filename'
Set Number of Divisions or Partitions into which you want to divide the text in variable 'num_columns'
Set Line length of paritioned texts in variable 'step'
