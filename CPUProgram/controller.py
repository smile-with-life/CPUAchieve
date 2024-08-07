import os
import pin
import assembly as ASM 

dirname =os.path.dirname(__file__)
filename=os.path.join(dirname,'micro.bin')

#将微指令控制器填充关机微指令
micro =[pin.HLT for _ in range(0x10000)]
CJMPS={ASM.JO,ASM.JNO,ASM.JZ,ASM.JNZ,ASM.JP,ASM.JNP}

def complite_addr2(addr,ir,psw,index):
    global micro
    op = ir & 0xf0 #取出操作指令
    amd = (ir >> 2) & 3 #取出目标操作数的寻址方式
    ams = ir & 3#取出源操作数的寻址方式
    INST =ASM.INSTRUCTIONS[2]#取出二操作数的所有指令作为一个列表
    if op not in INST:#遍历二操作数的所有指令看存不存在
        micro[addr] = pin.CYC
        return
    am =(amd,ams) # 目的操作数和源操作数合起来
    if am not in INST[op]:#遍历该指令下的所有寻址方式
        micro[addr] = pin.CYC
        return 
    EXEC = INST[op][am]#拷贝出对应的微指令
    if index < len(EXEC):#把指令补到后面
        micro[addr] = EXEC[index]
    else:
        micro[addr] = pin.CYC
def get_condition_jump(exec,op,psw):
    overflow =psw & 1
    zero =psw&2
    parity =psw&4
    if op == ASM.JO and overflow:
        return exec
    if op == ASM.JNO and not overflow:
        return exec
    if op == ASM.JZ and zero:
        return exec
    if op == ASM.JNZ and not zero:
        return exec
    if op == ASM.JP and parity:
        return exec
    if op == ASM.JNP and not parity:
        return exec
    return [pin.CYC]
def get_interrupt(exec,op,psw):
    interrupt = psw & 8
    if interrupt:
        return exec
    return [pin.CYC]
def complite_addr1(addr,ir,psw,index):
    global micro
    global CJMPS
    op = ir & 0xfc #取出操作指令
    amd = ir & 3 #取出目标操作数的寻址方式

    INST =ASM.INSTRUCTIONS[1]#取出一操作数的所有指令作为一个列表
    if op not in INST:#遍历一操作数的所有指令看存不存在
        micro[addr] = pin.CYC
        return
    if amd not in INST[op]:
        micro[addr] = pin.CYC
        return
    EXEC = INST[op][amd]#拷贝出对应的微指令
    if op in CJMPS:
        EXEC = get_condition_jump(EXEC,op,psw)
    if op == ASM.INT:
        EXEC = get_interrupt(EXEC,op,psw)
    if index < len(EXEC):#把指令补到后面
        micro[addr] = EXEC[index]
    else:
        micro[addr] = pin.CYC
def complite_addr0(addr,ir,psw,index):
    global micro
    op = ir # 取出操作指令

    INST = ASM.INSTRUCTIONS[0] #取出零操作数的所有指令的列表
    if op not in INST: #遍历零操作数的所有指令
        micro[addr] = pin.CYC #跳过该指令
        return

    EXEC = INST[op] #拷贝出对应的微指令
    if index < len(EXEC): # 把指令补到后面
        micro[addr] = EXEC[index]
    else:
        micro[addr] = pin.CYC

for addr in range(0x10000):#对整个指令集依次处理
    ir = addr >> 8 #取出表示指令的一段
    psw = (addr >> 4)& 0xf #取出表示指令的一段
    cyc = addr & 0xf #取出微指令周期的一段
    if cyc < len(ASM.FETCH):#将一段取值微程序放到所有指令中
        micro[addr] =ASM.FETCH[cyc]
        continue
    
    addr2 = ir &(1 << 7)#取出表示二操作数指令的位
    addr1 = ir &(1 << 6)#取出表示一操作数指令的位
    index = cyc -len(ASM.FETCH)#ASM.FETCH已经有6个指令
    # 对操作数不同的指令分情况处理
    if addr2:
        complite_addr2(addr,ir,psw,index)
    elif addr1:
        complite_addr1(addr,ir,psw,index)
    else:
        complite_addr0(addr,ir,psw,index)
        
#写入文件
with open(filename,'wb') as file:
    for value in micro:
        result = value.to_bytes(4,byteorder='little')
        file.write(result)
        #print(result)
