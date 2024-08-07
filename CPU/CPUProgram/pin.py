# coding=utf-8

#微指令为32位,可以分别控制不同的单元器件
#控制寄存器的位数(5位二进制数组合控制)
MSR = 1
MAR = 2
MDR = 3
RAM = 4
IR = 5 
DST = 6
SRC = 7
A = 8
B = 9
C = 10
D = 11
DI = 12
SI = 13
SP = 14
BP = 15
CS = 16
DS = 17
SS = 18
ES = 19
VEC = 20
T1 = 21
T2 = 22

#控制读写不同寄存器的位数
SRC_R = 2 ** 10#从源操作数寄存器中表示的寄存器读
SRC_W = 2 ** 11#向源操作数寄存器中表示的寄存器写
DST_R= 2 ** 12#从目的操作数寄存器中表示的寄存器读
DST_W = 2 ** 13#向目的操作数寄存器中表示的寄存器写

#控制程序计数器的位数
PC_WE = 2 ** 14
PC_CS = 2 ** 15
PC_EN = 2 ** 16

OP_SHEFT = 17
OP_ADD  = 0 << OP_SHEFT
OP_SUB = 1 << OP_SHEFT
OP_INC = 2 << OP_SHEFT
OP_DEC = 3 << OP_SHEFT
OP_AND = 4 << OP_SHEFT
OP_OR = 5 << OP_SHEFT
OP_XOR = 6 << OP_SHEFT
OP_NOT = 7 << OP_SHEFT

ALU_OUT = 1 << 20
ALU_PSW = 1 << 21
ALU_INT_W = 1 << 22
ALU_INT = 1 << 23


CYC = 2 ** 30
#控制关机的位数
HLT = 2 ** 31 



#定义寄存器写入总线的微操作
MSR_OUT = MSR
MAR_OUT = MAR
MDR_OUT = MDR
RAM_OUT = RAM
IR_OUT = IR
DST_OUT = DST
SRC_OUT = SRC
A_OUT = A
B_OUT = B
C_OUT = C
D_OUT = D
DI_OUT = DI
SI_OUT = SI
SP_OUT = SP
BP_OUT = BP
CS_OUT = CS
DS_OUT = DS
SS_OUT = SS
ES_OUT = ES
VEC_OUT = VEC
T1_OUT = T1
T2_OUT = T2

#读写相差位数
_DST_SHIFT = 5
#定义寄存器从总线读的微操作
MSR_IN = MSR << _DST_SHIFT
MAR_IN = MAR << _DST_SHIFT
MDR_IN = MDR << _DST_SHIFT
RAM_IN = RAM << _DST_SHIFT
IR_IN = IR << _DST_SHIFT
DST_IN = DST << _DST_SHIFT
SRC_IN = SRC << _DST_SHIFT
A_IN = A << _DST_SHIFT
B_IN = B << _DST_SHIFT
C_IN = C << _DST_SHIFT
D_IN = D << _DST_SHIFT
DI_IN = DI << _DST_SHIFT
SI_IN = SI << _DST_SHIFT
SP_IN = SP << _DST_SHIFT
BP_IN = BP << _DST_SHIFT
CS_IN = CS << _DST_SHIFT
DS_IN = DS << _DST_SHIFT
SS_IN = SS << _DST_SHIFT
ES_IN = ES << _DST_SHIFT
VEC_IN = VEC << _DST_SHIFT
T1_IN = T1 << _DST_SHIFT
T2_IN = T2 << _DST_SHIFT

ALU_STI = ALU_INT_W
ALU_CLI = ALU_INT_W | ALU_INT

#程序计数器微操作
PC_OUT = PC_CS
PC_IN = PC_CS | PC_WE
PC_INC = PC_CS | PC_WE | PC_EN

ADDR2 = 1 << 7 #二操作数指令标志1xxx[aa][bb]
ADDR1 = 1 << 6 #一操作数指令标志01xxxx[aa]
ADDR0 = 0 << 6 #一操作数指令标志00xxxxxx

ADDR2_SHIFT = 4#二操作数指令寻址特征位数
ADDR1_SHIFT = 2#一操作数指令寻址特征位数

#寻址特征
AM_INS = 0 #立即数
AM_REG = 1 #寄存器寻址
AM_DIR = 2 #直接寻址
AM_RAM = 3 #寄存器间接寻址
