#Alternative File Reading Methods:
'''

1.  write
filevar.write(astring)
Add a string to the end of the file.
filevar must refer to a file that has been opened for writing.

2.  read(n)
filevar.read()
Read and return a string of n characters,
or the entire file as a single string if n is not provided.

3.  readline(n)
filevar.readline()
Read and return the next line of the file with all text up to 
and including the newline character. If n is provided as a parameter,
then only n characters will be returned if the line is longer than n.
!! Note the parameter n is not supported in the browser version of Python,
 and in fact is rarely used in practice, you can safely ignore it.

4.  readlines(n)
filevar.readlines()
Returns a list of strings, each representing a single line of the file.
 If n is not provided then all lines of the file are returned. 
 If n is provided then n characters are read but n is rounded up so that
 an entire line is returned. Note Like readline readlines ignores the parameter n in the browser.


'''
