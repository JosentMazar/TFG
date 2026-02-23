import olefile
import oletools
from oletools import oleform
import re
import sys

inputfile = olefile.OleFileIO(sys.argv[1])

streams = inputfile.listdir(streams=True, storages=False)

fStreams = []

for stream in streams:
	if stream[0] == 'Macros' and stream[-1] == 'f' and re.search("^i[0-9]{2,}",stream[-2]) == None:
		fStreams.append(stream[:-1])

streamDict = {}

for fStream in fStreams:
	vars = oletools.oleform.extract_OleFormVariables(inputfile,['/'.join(fStream)])
	if(vars):
		outfilename = '_'.join(fStream[1:])
		outFile = open(outfilename, "w")
		for var in vars:
			outFile.write("%s\n" % var)
		outFile.close()

inputfile.close()
