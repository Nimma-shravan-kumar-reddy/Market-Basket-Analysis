Requirements

- Anaconda 4.10.1
- Python 3.8.8
- Jupyter notebbok 6.3.0


Steps for Running:


1. open Anaconda Prompt and type "jupyter notebook" and press enter.



2. Extracted zip file consists of the following files
   
   a. hcrules.py
   b. final report
   c. output1.txt (min_sup =  120, min_conf = -1)
   d. output2.txt (min_sup =  70, min_conf = 0.9)
   e. output3.txt (min_sup =  100, min_conf = 0.85)
   f. transactions.txt(input file)



3. In the jupyter notebook upload the following files one by one

   a. hcrules.py
   b. an empty text file (sample.txt) (for storing the output or you can give your own file but must be uploaded into jupyter notebook).
   c. transactions.txt(input file)

All the above files need to be uploaded in jupyter notebook.



4. Now open a new Anaconda Prompt and run the following code.

     "python hcrules.py <minsupport> <minconfidence> <inputfile(transactions.txt)> <outputfile(output.txt)>" 

     This the format for running the code below is the sample command to run with minsupport=100 and minconfidence=0.8. 
   
                            python hcrules.py 100 0.8 transactions.txt output.txt 



5. The results can be found in the output.txt file in jupyter notebook.