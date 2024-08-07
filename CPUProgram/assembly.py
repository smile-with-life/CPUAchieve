# coding=utf-8

import pin

#取值周期微命令
FETCH = [
    pin.PC_OUT | pin.MAR_IN,
    pin.RAM_OUT | pin.IR_IN | pin.PC_INC,
    pin.PC_OUT | pin.MAR_IN,
    pin.RAM_OUT | pin.DST_IN | pin.PC_INC,
    pin.PC_OUT | pin.MAR_IN,
    pin.RAM_OUT | pin.SRC_IN | pin.PC_INC
]
#间址周期
#执行周期
#中断周期
MOV = (0 << pin.ADDR2_SHIFT) | pin.ADDR2 #0b1000
ADD = (1 << pin.ADDR2_SHIFT) | pin.ADDR2 #0b1001
SUB = (2 << pin.ADDR2_SHIFT) | pin.ADDR2 #0b1010
CMP = (3 << pin.ADDR2_SHIFT) | pin.ADDR2 #0b1011
AND = (4 << pin.ADDR2_SHIFT) | pin.ADDR2 #0b1100
OR = (5 << pin.ADDR2_SHIFT) | pin.ADDR2 #0b1101
XOR = (6 << pin.ADDR2_SHIFT) | pin.ADDR2 #0b1110
#0b1111

INC = (0 << pin.ADDR1_SHIFT) | pin.ADDR1 #0b010000
DEC = (1 << pin.ADDR1_SHIFT) | pin.ADDR1 #0b010001
NOT = (2 << pin.ADDR1_SHIFT) | pin.ADDR1 #0b010010
JMP = (3 << pin.ADDR1_SHIFT) | pin.ADDR1 #0b010011
JO = (4 << pin.ADDR1_SHIFT) | pin.ADDR1 #0b010100
JNO = (5 << pin.ADDR1_SHIFT) | pin.ADDR1 #0b010101
JZ = (6 << pin.ADDR1_SHIFT) | pin.ADDR1 #0b010110
JNZ = (7 << pin.ADDR1_SHIFT) | pin.ADDR1 #0b010111
JP = (8 << pin.ADDR1_SHIFT) | pin.ADDR1 #0b011000
JNP = (9 << pin.ADDR1_SHIFT) | pin.ADDR1 #0b011001
PUSH = (10 << pin.ADDR1_SHIFT) | pin.ADDR1 #0b011010
POP = (11 << pin.ADDR1_SHIFT) | pin.ADDR1 #0b011011
CALL =(12 << pin.ADDR1_SHIFT) | pin.ADDR1 #0b011100
INT =(13 << pin.ADDR1_SHIFT) | pin.ADDR1 #0b011100


NOP = pin.ADDR0 | 0  #0b00000000
RET = pin.ADDR0 | 1  #0b00000001
IRET = pin.ADDR0 | 2  #0b00000010
STI = pin.ADDR0 | 3  #0b00000011
CLI =pin.ADDR0 | 4  #0b00000100
HLT = pin.ADDR0 | 0x3f#0b00111111

#指令集
INSTRUCTIONS={
    2: 
    {
        MOV: #指令 0b1000
        {
            #寻址方式:寄存器寻址,立即数寻址 0b1000 01 00
            (pin.AM_REG,pin.AM_INS):
            [
                pin.DST_W | pin.SRC_OUT#将SRC中的值写入DST中指定的寄存器中
            ],
            #寻址方式:寄存器寻址,寄存器寻址 0b1000 01 01
            (pin.AM_REG,pin.AM_REG):
            [
                pin.DST_W | pin.SRC_R#将SRC中指定的寄存器中的值,写入DST中指定的寄存器中
            ],
            #寻址方式:寄存器寻址,直接寻址 0b1000 01 10
            (pin.AM_REG,pin.AM_DIR):
            [
                pin.SRC_OUT | pin.MAR_IN,#将SRC中的值写入MAR
                pin.DST_W | pin.RAM_OUT#将RAM中的值写入DST中指定的寄存器中
            ],
            #寻址方式:寄存器寻址,寄存器间接寻址 0b1000 01 11
            (pin.AM_REG,pin.AM_RAM):
            [
                pin.SRC_R | pin.MAR_IN,#将SRC中指定的寄存器中的值写入MAR
                pin.DST_W | pin.RAM_OUT#将RAM的值写入DST中指定的寄存器
            ],
            #寻址方式:直接寻址,立即数寻址 0b1000 10 00
            (pin.AM_DIR, pin.AM_INS): [ 
                pin.DST_OUT | pin.MAR_IN,#将DST中的值写入MAR
                pin.RAM_IN | pin.SRC_OUT#将SRC中的值写入RAM
            ],
            #寻址方式:直接寻址,寄存器寻址 0b1000 10 01
            (pin.AM_DIR, pin.AM_REG): 
            [ 
                pin.DST_OUT | pin.MAR_IN,#将DST中的值送到MAR
                pin.RAM_IN | pin.SRC_R,#将SRC中指定的寄存器中的值写入RAM
            ],
            #寻址方式:直接寻址,直接寻址 0b1000 10 10
            (pin.AM_DIR, pin.AM_DIR): 
            [ 
                pin.SRC_OUT | pin.MAR_IN,#将SRC中的值写入MAR
                pin.RAM_OUT | pin.T1_IN,#将RAM中的值写入T1寄存器
                pin.DST_OUT | pin.MAR_IN,#将DST中的值写入MAR
                pin.RAM_IN | pin.T1_OUT,#将T1寄存器中的值写入RAM
            ],
            #寻址方式:直接寻址,寄存器间接寻址 0b1000 10 11
            (pin.AM_DIR, pin.AM_RAM):
            [ 
                pin.SRC_R | pin.MAR_IN,#将SRC中指定的寄存器中的值写入MAR
                pin.RAM_OUT | pin.T1_IN,#将RAM中的值写入T1寄存器
                pin.DST_OUT | pin.MAR_IN,#将DST中的值写入MAR
                pin.RAM_IN | pin.T1_OUT,#将T1寄存器中的值写入RAM
            ],
            #寻址方式:寄存器间接寻址,立即数寻址 0b1000 11 00
            (pin.AM_RAM, pin.AM_INS): 
            [
                pin.DST_R | pin.MAR_IN,#将DST中指定的寄存器中的值写入MAR
                pin.RAM_IN | pin.SRC_OUT#将SRC中的值写如RAM
            ],
            #寻址方式:寄存器间接寻址,寄存器寻址 0b1000 11 01
            (pin.AM_RAM, pin.AM_REG): 
            [ 
                pin.DST_R | pin.MAR_IN,#将DST中指定的寄存器中的值写入MAR
                pin.RAM_IN | pin.SRC_R,#将SRC中的指定的的寄存器中的值写入RAM
            ],
            #寻址方式:寄存器间接寻址,直接寻址 0b1000 11 10
            (pin.AM_RAM, pin.AM_DIR): 
            [
                pin.SRC_OUT | pin.MAR_IN,#将SRC寄中的值写入MAR
                pin.RAM_OUT | pin.T1_IN,#将RAM中的值写入T1寄存器
                pin.DST_R | pin.MAR_IN,#DST读寄存器到MAR
                pin.RAM_IN | pin.T1_OUT,#把T1读到RAM里
            ],
            #寻址方式:寄存器间接寻址,寄存器间接寻址 0b1000 11 11
            (pin.AM_RAM, pin.AM_RAM): 
            [
                pin.SRC_R | pin.MAR_IN,#将SRC中的寄存器中的值写入MAR
                pin.RAM_OUT | pin.T1_IN,#将RAM的值写入T1寄存器
                pin.DST_R | pin.MAR_IN,#将DST中的寄存器中的值写入MAR
                pin.RAM_IN | pin.T1_OUT,#将T1寄存器中的值写入RAM
            ]
        },
        ADD:
        {
            #寻址方式:寄存器寻址,立即数寻址
            (pin.AM_REG, pin.AM_INS): 
            [
                pin.DST_R | pin.A_IN,#将DST中指定的寄存器中的值写入A寄存器中
                pin.SRC_OUT | pin.B_IN,#将SRC中的值写入B寄存器中
                pin.OP_ADD | pin.ALU_OUT | pin.DST_W | pin.ALU_PSW#选择加法,将ALU输出写入DST中指定的寄存器中，更新ALU状态字
            ],
            #寻址方式:寄存器寻址,寄存器寻址
            (pin.AM_REG, pin.AM_REG): 
            [ 
                pin.DST_R | pin.A_IN,#将DST中指定的寄存器中的值写入A寄存器
                pin.SRC_R | pin.B_IN,#将SRC中指定的寄存器中的值写入B寄存器
                pin.OP_ADD | pin.ALU_OUT | pin.DST_W | pin.ALU_PSW#选择加法,将ALU输出写入DST中指定的寄存器中，更新ALU状态字
            ],

        },
        SUB:
        {
            #寻址方式:寄存器寻址,立即数寻址
            (pin.AM_REG, pin.AM_INS): 
            [
                pin.DST_R | pin.A_IN,#将DST中指定的寄存器中的值写入A寄存器中
                pin.SRC_OUT | pin.B_IN,#将SRC中的值写入B寄存器中
                pin.OP_SUB | pin.ALU_OUT | pin.DST_W | pin.ALU_PSW#选择减法,将ALU输出写入DST中指定的寄存器中,更新ALU状态字
            ],
            #寻址方式:寄存器寻址,寄存器寻址
            (pin.AM_REG, pin.AM_REG): 
            [ 
                pin.DST_R | pin.A_IN,#将DST中指定的寄存器中的值写入A寄存器
                pin.SRC_R | pin.B_IN,#将SRC中指定的寄存器中的值写入B寄存器
                pin.OP_SUB | pin.ALU_OUT | pin.DST_W | pin.ALU_PSW#选择减法,将ALU输出写入DST中指定的寄存器中,更新ALU状态字
            ],
        },
        CMP:
        {
            #寻址方式:寄存器寻址,立即数寻址
            (pin.AM_REG, pin.AM_INS): 
            [
                pin.DST_R | pin.A_IN,#将DST中指定的寄存器中的值写入A寄存器中
                pin.SRC_OUT | pin.B_IN,#将SRC中的值写入B寄存器中
                pin.OP_SUB | pin.ALU_PSW#选择减法,更新ALU状态字

            ],
            #寻址方式:寄存器寻址,寄存器寻址
            (pin.AM_REG, pin.AM_REG): 
            [ 
                pin.DST_R | pin.A_IN,#将DST中指定的寄存器中的值写入A寄存器
                pin.SRC_R | pin.B_IN,#将SRC中指定的寄存器中的值写入B寄存器
                pin.OP_SUB | pin.ALU_PSW#选择减法,更新ALU状态字
            ],
        },
        AND:
        {
            #寻址方式:寄存器寻址,立即数寻址
            (pin.AM_REG, pin.AM_INS): 
            [
                pin.DST_R | pin.A_IN,#将DST中指定的寄存器中的值写入A寄存器中
                pin.SRC_OUT | pin.B_IN,#将SRC中的值写入B寄存器中
                pin.OP_AND | pin.ALU_OUT | pin.DST_W | pin.ALU_PSW#选择AND,将ALU输出写入DST中指定的寄存器中,更新ALU状态字
            ],
            #寻址方式:寄存器寻址,寄存器寻址
            (pin.AM_REG, pin.AM_REG): 
            [ 
                pin.DST_R | pin.A_IN,#将DST中指定的寄存器中的值写入A寄存器
                pin.SRC_R | pin.B_IN,#将SRC中指定的寄存器中的值写入B寄存器
                pin.OP_AND | pin.ALU_OUT | pin.DST_W | pin.ALU_PSW#选择AND,将ALU输出写入DST中指定的寄存器中,更新ALU状态字
            ],
        },
        OR:
        {
            #寻址方式:寄存器寻址,立即数寻址
            (pin.AM_REG, pin.AM_INS): 
            [
                pin.DST_R | pin.A_IN,#将DST中指定的寄存器中的值写入A寄存器中
                pin.SRC_OUT | pin.B_IN,#将SRC中的值写入B寄存器中
                pin.OP_OR | pin.ALU_OUT | pin.DST_W | pin.ALU_PSW#选择OR,将ALU输出写入DST中指定的寄存器中,更新ALU状态字
            ],
            #寻址方式:寄存器寻址,寄存器寻址
            (pin.AM_REG, pin.AM_REG): 
            [ 
                pin.DST_R | pin.A_IN,#将DST中指定的寄存器中的值写入A寄存器
                pin.SRC_R | pin.B_IN,#将SRC中指定的寄存器中的值写入B寄存器
                pin.OP_OR | pin.ALU_OUT | pin.DST_W | pin.ALU_PSW#选择OR,将ALU输出写入DST中指定的寄存器中,更新ALU状态字
            ],
        },
        XOR:
        {
            #寻址方式:寄存器寻址,立即数寻址
            (pin.AM_REG, pin.AM_INS): 
            [
                pin.DST_R | pin.A_IN,#将DST中指定的寄存器中的值写入A寄存器中
                pin.SRC_OUT | pin.B_IN,#将SRC中的值写入B寄存器中
                pin.OP_XOR | pin.ALU_OUT | pin.DST_W | pin.ALU_PSW#选择XOR,将ALU输出写入DST中指定的寄存器中,更新ALU状态字
            ],
            #寻址方式:寄存器寻址,寄存器寻址
            (pin.AM_REG, pin.AM_REG): 
            [ 
                pin.DST_R | pin.A_IN,#将DST中指定的寄存器中的值写入A寄存器
                pin.SRC_R | pin.B_IN,#将SRC中指定的寄存器中的值写入B寄存器
                pin.OP_XOR | pin.ALU_OUT | pin.DST_W | pin.ALU_PSW#选择XOR,将ALU输出写入DST中指定的寄存器中,更新ALU状态字
            ],
        },
    },
    1:
    {
        INC: 
        {
            pin.AM_REG: 
            [
                pin.DST_R | pin.A_IN,#将DST中指定的寄存器中的值写入A寄存器
                pin.OP_INC | pin.ALU_OUT | pin.DST_W | pin.ALU_PSW#选择+1,将ALU输出写入DST中指定的寄存器中,更新ALU状态字
            ],
        },
        DEC: 
        {
            pin.AM_REG: 
            [
                pin.DST_R | pin.A_IN,#将DST中指定的寄存器中的值写入A寄存器
                pin.OP_DEC | pin.ALU_OUT | pin.DST_W | pin.ALU_PSW#选择-1,将ALU输出写入DST中指定的寄存器中,更新ALU状态字
            ],
        },
        NOT: 
        {
            pin.AM_REG: 
            [
                pin.DST_R | pin.A_IN,#将DST中指定的寄存器中的值写入A寄存器
                pin.OP_NOT | pin.ALU_OUT | pin.DST_W | pin.ALU_PSW#选择NOT,将ALU输出写入DST中指定的寄存器中,更新ALU状态字
            ],
        },
        JMP:
        {
            pin.AM_INS: 
            [
                pin.DST_OUT | pin.PC_IN,#将DST中的值写入PC
            ],
        },
        JO:
        {
            pin.AM_INS: 
            [
                pin.DST_OUT | pin.PC_IN,#将DST中的值写入PC
            ],
        },
        JNO:
        {
            pin.AM_INS: 
            [
                pin.DST_OUT | pin.PC_IN,#将DST中的值写入PC
            ],
        },
        JZ:
        {
            pin.AM_INS: 
            [
                pin.DST_OUT | pin.PC_IN,#将DST中的值写入PC
            ],
        },
        JNZ:
        {
            pin.AM_INS: 
            [
                pin.DST_OUT | pin.PC_IN,#将DST中的值写入PC
            ],
        },
        JP:
        {
            pin.AM_INS: 
            [
                pin.DST_OUT | pin.PC_IN,#将DST中的值写入PC
            ],
        },
        JNP:
        {
            pin.AM_INS: 
            [
                pin.DST_OUT | pin.PC_IN,#将DST中的值写入PC
            ],
        },
        PUSH:
        {
            pin.AM_INS: 
            [
                pin.SP_OUT | pin.A_IN,
                pin.OP_DEC | pin.SP_IN | pin.ALU_OUT,
                pin.SP_OUT| pin.MAR_IN,
                pin.SS_OUT | pin.MSR_IN,
                pin.DST_OUT| pin.RAM_IN,
                pin.CS_OUT |pin.MSR_IN,
            ],
            pin.AM_REG: 
            [
                pin.SP_OUT | pin.A_IN,
                pin.OP_DEC | pin.SP_IN | pin.ALU_OUT,
                pin.SP_OUT| pin.MAR_IN,
                pin.SS_OUT | pin.MSR_IN,
                pin.DST_R| pin.RAM_IN,
                pin.CS_OUT |pin.MSR_IN,
            ],
        },
        POP:
        {
            pin.AM_REG: 
            [
                pin.SP_OUT | pin.MAR_IN,
                pin.SS_OUT | pin.MSR_IN,
                pin.DST_W | pin.RAM_OUT,#问题:目标位A寄存器会有问题
                pin.SP_OUT | pin.A_IN,
                pin.OP_INC | pin.SP_IN | pin.ALU_OUT,
                pin.CS_OUT | pin.MSR_IN

            ],
        },
        CALL:
        {
            pin.AM_INS: 
            [
                pin.SP_OUT | pin.A_IN,
                pin.OP_DEC | pin.SP_IN | pin.ALU_OUT,
                pin.SP_OUT| pin.MAR_IN,
                pin.SS_OUT | pin.MSR_IN,
                pin.PC_OUT| pin.RAM_IN,
                pin.DST_OUT| pin.PC_IN,
                pin.CS_OUT |pin.MSR_IN,
            ],
            pin.AM_REG: 
            [
                pin.SP_OUT | pin.A_IN,
                pin.OP_DEC | pin.SP_IN | pin.ALU_OUT,
                pin.SP_OUT| pin.MAR_IN,
                pin.SS_OUT | pin.MSR_IN,
                pin.PC_OUT| pin.RAM_IN,
                pin.DST_R| pin.PC_IN,
                pin.CS_OUT |pin.MSR_IN,
            ],
        },
        INT:
        {
            pin.AM_INS: 
            [
                pin.SP_OUT | pin.A_IN,
                pin.OP_DEC | pin.SP_IN | pin.ALU_OUT,
                pin.SP_OUT | pin.MAR_IN,
                pin.SS_OUT | pin.MSR_IN,
                pin.PC_OUT | pin.RAM_IN,
                pin.DST_OUT| pin.PC_IN,
                pin.CS_OUT | pin.MSR_IN | pin.ALU_PSW | pin.ALU_CLI
            ],
            pin.AM_REG: 
            [
                pin.SP_OUT | pin.A_IN,
                pin.OP_DEC | pin.SP_IN | pin.ALU_OUT,
                pin.SP_OUT| pin.MAR_IN,
                pin.SS_OUT | pin.MSR_IN,
                pin.PC_OUT| pin.RAM_IN,
                pin.DST_R| pin.PC_IN,
                pin.CS_OUT |pin.MSR_IN | pin.ALU_PSW | pin.ALU_CLI
            ],
        },
        
    },
    0:
    {
        NOP:
        [
            pin.CYC
        ],
        RET:
        [
            pin.SP_OUT | pin.MAR_IN,
            pin.SS_OUT | pin.MSR_IN,
            pin.PC_IN | pin.RAM_OUT,#问题:目标位A寄存器会有问题
            pin.SP_OUT | pin.A_IN,
            pin.OP_INC | pin.SP_IN | pin.ALU_OUT,
            pin.CS_OUT | pin.MSR_IN
        ],
        IRET:
        [
            pin.SP_OUT | pin.MAR_IN,
            pin.SS_OUT | pin.MSR_IN,
            pin.PC_IN | pin.RAM_OUT,#问题:目标位A寄存器会有问题
            pin.SP_OUT | pin.A_IN,
            pin.OP_INC | pin.SP_IN | pin.ALU_OUT,
            pin.CS_OUT | pin.MSR_IN |pin.ALU_PSW |pin.ALU_STI
        ],
        STI:
        [
            pin.ALU_PSW | pin.ALU_STI
        ],
        CLI:
        [
           pin.ALU_PSW | pin.ALU_CLI
        ],
        HLT:
        [
            pin.HLT
        ]
    }
}