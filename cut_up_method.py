import math             #for factorial purpose
import itertools        #for permutations of list elements
from readability import Readability

"""
This Script performs Cut Up Method on Text.  
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
Details of modules used in this program can be found from links below
https://github.com/cdimascio/py-readability-metrics
https://pypi.org/project/py-readability-metrics/
pip install py-readability-metrics
python -m nltk.downloader punkt
"""

num_columns=3           #Total Number of Partitions
filename="new.txt"
cutup_pieces_list=[]    #Contains Partitioned/Cut Up pieces of string in a list
text_string=""          #Containing total text in string form
start=0
step=30                 #Step means number of words in a sentence/phrase of cut up piece
end=step

# Here we read the text from file and store it in text_string.
fhandle=open(filename)
for line in fhandle:
    text_string=text_string+line

#print(text_string)

#Cutup pieces list= list of list elements equal to number of partitions
for i in range(num_columns):
    cutup_pieces_list.append([])

#Reading sentences from text_string and placing in different partitions
i=0
while(end<len(text_string)):
    if i<num_columns:
        cutup_pieces_list[i].append(text_string[start:end])
        start=end
        end=end+step
        i+=1
    else:
        i = 0

#Here we convert list of lists to list of strings to simplify cutpieces. Our strings will be different cut pieces
cutup_pieces_list=[''.join(x) for x in cutup_pieces_list]
print((cutup_pieces_list))

#to see number of possible Permutations(different combinations of list enteries without any repetitions)
#e.g in case of A,B,C . Permutations ABC, ACB, BAC,BCA, CAB, CBA  i.e. 6 combinations for 3 columns/list enteries
num_combinations=math.factorial(num_columns)

"""Finding All Cut Up Permutations and Storage in a list """
permutations_object = itertools.permutations(cutup_pieces_list) #Find permutations of a_list.
permutations_list = list(permutations_object)        #Create list from permutations.
permuted_strings_list=["".join(tup) for tup in permutations_list]
#print(permuted_strings_list)

readability_index_list=[]

for i in range(num_combinations):
    r = Readability(permuted_strings_list[i])
    dc = r.dale_chall()
    readability_index_list.append(dc.score)
    #print(dc.grade_levels)

#Finding index of list with highest readability score to extract text which is most readable
index=readability_index_list.index(max(readability_index_list))
print(permuted_strings_list[index])
#    print(permuted_strings_list[i])
"""Dale Chall Readability
The Dale-Chall Formula is an accurate readability formula for the simple reason that it is based on the use of
familiar words, rather than syllable or letter counts. Reading tests show that readers usually find it easier 
to read, process and recall a passage if they find the words familiar."""



