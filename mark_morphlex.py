import sys

# largely one time thing, converting ${morphvals}. comments --> ${morphvals}.comments ɸmorphvals

INP_S_M_DELIM = ','  # symbol map delimiter for input language character strings mapped to phone(t/m)ic values
OUTFILE_DELIM = ','  # column delimiter for output file columns
MORPHCLAUSE_START = '{'
MORPHCLAUSE_END = '}'
CMT_FLAG = '$'
FORM_ID_FLAG = "ɸ"


inp = open(sys.argv[1], encoding="utf-8")
inplines = inp.readlines()
inp.close()

for i in range(0,len(inplines)):
	mcstart = inplines[i].find(MORPHCLAUSE_START)
	mcclause = ""
	if mcstart != -1:
		mclength = inplines[i][mcstart+1:].find(MORPHCLAUSE_END)
		if mclength != -1:
			mcclause = inplines[i][mcstart+1:mcstart+1+mclength]

	if len(mcclause) != 0:
		inplines[i] = inplines[i][:inplines[i].find("\n")] + FORM_ID_FLAG + mcclause + "\n"

outp =  open(sys.argv[1], mode="w",encoding="utf-8")
outp.writelines(inplines)
outp.close()

