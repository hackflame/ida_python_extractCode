#coding=utf-8
try:
    import idaapi
except ImportError:
    print "Could not import idc. Running in 'pydoc mode'."

try:
    import idc
except ImportError:
    print "Could not import idc. Running in 'pydoc mode'."



def printAvd():
	print 25*"==="
	info ='''
	特征码生成工具 Ver1.0 By:火哥 QQ:471194425 QQ群:1026716399
	道破红尘优化版
	1.优化匹配模式 
	2.增加鼠标选中代码生成特征码 extractCode()
	3.增加 Alt-Z 快捷键
	'''
	print info
	print 25*"==="

def formatByte(ea):
    return "{:02X}".format(idc.Byte(ea))

def calcStr(ea,endcount):
    hstr = ""
    firstByte = formatByte(ea)
    hstr += formatByte(ea)
    hstr = hstr + formatByte(ea+1) if(firstByte == "FF" or firstByte == "66" or firstByte == "67") else hstr
    hstr = hstr + (endcount-len(hstr)/2) * "*" if endcount >= 2 else hstr
    return hstr

def extractCode():
	printAvd()
	
	start = idc.SelStart()
	end = idc.SelEnd()
	codeSize = end - start
	ea = start
	#print hex(ea)
	result=""

	for i in range(codeSize):
		op1 = idc.GetOpType(ea,0)
		op2 = idc.GetOpType(ea,1)
		instructionSize=idc.ItemSize(ea) 
	
		if op1 == idc.o_reg and (op2 ==idc.o_reg or op2 == idc.o_void or op2 == idc.o_phrase):
			for b in range(0,instructionSize):
				result += formatByte(ea+b)
		elif (op1 == idc.o_reg and op2 == idc.o_displ) or (op1 == idc.o_displ and op2 == idc.o_reg) or (op1 == idc.o_displ and op2 == idc.o_imm):
			result += formatByte(ea) + formatByte(ea+1)
			for b in range(2,instructionSize):
				result=result+"*"
		elif op1 == idc.o_phrase and op2 == idc.o_reg:
			for b in range(0,instructionSize):
				result+=formatByte(ea+b)
		else:
			result+=calcStr(ea,instructionSize)

		ea = ea + instructionSize
		if ea >= (start + codeSize):
			break
	print ("%s  Offset:%s") % (idc.GetFunctionName(start),hex(start - idc.GetFunctionAttr(start,0)))
	print result
	return result
	
	
def registerHotkey(shortcut):
    idaapi.CompileLine(r'static extractCode() { RunPythonStatement("tq.extractCode()"); }')
    idc.AddHotkey(shortcut, "extractCode")	
	
printAvd()

keyname ="Alt-Z"
registerHotkey(keyname)