import sys

#INP_S_M_DELIM = ','  # symbol map delimiter for input language character strings mapped to phone(t/m)ic values
#OUTFILE_DELIM = ','  # column delimiter for output file columns
#MORPH_CLAUSE_FLAG = '%'
#CMT_FLAG = '$'
FORM_ID_FLAG = "ɸ"
MORPHVAL_DELIM = "."

inp = open(sys.argv[1], encoding="utf-8")
inplines = [line.strip() for line in inp.readlines() if len(line.strip()) > 0]
inp.close()

if inplines[0][0] in "~=": #header
	inplines = inplines[1:]

suffixbound = sys.argv[1].rfind(".")


morphvals = {}

for ili in inplines:
	if FORM_ID_FLAG in ili:
		vals_here = ili[ili.find(FORM_ID_FLAG)+1:].split(MORPHVAL_DELIM)
		for val in vals_here:
			if val in morphvals:
				morphvals[val] += 1
			else:
				morphvals[val] = 1
	else:
		print("no morphval flag in line : "+ili)

outp = open(sys.argv[1][:suffixbound] + "-morphvalcount.txt", encoding="utf-8")

for mvi in morphvals:
	outp.writeline(mvi+" : "+morphvals[mvi])

outp.close()


