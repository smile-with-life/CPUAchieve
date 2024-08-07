

# 1. 寄存器

- **`PC` 程序计数器**
- **`ALU`**
- **`PSW/FLAG` 程序状态字**
- **`A` 寄存器**
- **`B` 寄存器**
- **`C` 寄存器**
- **`D` 寄存器**
- **`IR` 指令寄存器**
- **`DST` 目的操作数寄存器**
- **`SRC` 源操作数寄存器**
- **`MSR` 存储器段寄存器**
- **`MAR` 存储器地址寄存器**
- **`MDR` 存储器数据寄存器**
- **`MC` 内存寄存器**
- **`SP` 堆栈指针寄存器**
- **`BP` 基址寄存器**
- **`SI` 源变址寄存器**
- **`DI` 目的变址寄存器**
- **`CS` 代码段寄存器**
- **`DS` 数据段寄存器**
- **`SS` 堆栈段寄存器**
- **`ES` 附加段寄存器**
- **`TMP` 临时寄存器若干**

# 2. 指令系统

### 指令种类

- **二操作数:**
  - **`mov dst,src`**
  - **`add dst,src`**
  - **`sub dst,src`**
  - **`cmp dst,src`**
  - **`and dst,src`**
  - **`or dst,src`**
  - **`xor dst,src`**
- **一操作数:**
  - **`inc src`**
  - **`dec src`** 
  - **`not src`**
  - **`call src`**
  - **`jmp dst`**
  - **`jo dst`**
  - **`jno dst`**
  - **`jz dst`**
  - **`jnz dst`**
  - **`push src`**
  - **`pop src`**
  - **`int dst`**
- **零操作数:**
  - **`nop`**
  - **`hlt`**
  - **`ret`**
  - **`iret`**

### 指令格式

**8位CPU指令操作码字段长度为8位**

- **二操作数指令:4位操作码 4位寻址特征,最高位为1**

![cpu-image-46.png](CPU-image\cpu-image-46.png)

- **一操作数指令:6位操作码 2位寻址特征,最高两位为01**

![cpu-image-47.png](CPU-image\cpu-image-47.png)

- **二操作数指令:8位操作码 0位寻址特征,最高两位为00**

![cpu-image-48.png](CPU-image\cpu-image-48.png)

### 寻址方式 

- **立即寻址 `MOV A,5`寻址特征表示为00**
- **寄存器寻址 `MOV A,B`寻址特征表示为01**
- **直接寻址 `MOV A,[5]`寻址特征表示为10**
- **寄存器间接寻址 `MOV A,[B]`寻址特征表示为11**

### 指令编码

| 二操作数指令 |  编码  |
| :----------: | :----: |
|     MOV      | 0b1000 |
|     ADD      | 0b1001 |
|     SUB      | 0b1010 |
|     CMP      | 0b1011 |
|     AND      | 0b1100 |
|      OR      | 0b1101 |
|     XOR      | 0b1110 |

| 一操作数指令 |   编码   |
| :----------: | :------: |
|     INC      | 0b010000 |
|     DEC      | 0b010001 |
|     NOT      | 0b010010 |
|     JMP      | 0b010011 |
|      JO      | 0b010100 |
|     JNO      | 0b010101 |
|      JZ      | 0b010110 |
|     JNZ      | 0b010111 |
|      JP      | 0b011000 |
|     JNP      | 0b011001 |
|     PUSH     | 0b011010 |
|     POP      | 0b011011 |
|     CALL     | 0b011100 |
|     INT      | 0b011101 |

| 零操作数指令 |    编码    |
| :----------: | :--------: |
|     NOP      | 0b00000000 |
|     RET      | 0b00000001 |
|     IRET     | 0b00000010 |
|     STI      | 0b00000011 |
|     CLI      | 0b00000100 |
|     HLT      | 0b00111111 |



### 程序状态字 

- **`OF` 溢出标志**
- **`ZF` 零标志**
- **`PF` 奇偶标志**
- **`IF` 中断标志**



# 3. 取指周期微程序

### 取指令步骤

- **PC->MAR**
- **RAM->IR ,PC+1**
- **PC->MAR**
- **RAM->DST ,PC+1**
- **PC->MAR**
- **RAM->SRC ,PC+1**

**取一条指令需要6个时钟周期**

### 程序设计

```python
FETCH = [
    pin.PC_OUT | pin.MAR_IN,
    pin.RAM_OUT | pin.IR_IN | pin.PC_INC,
    pin.PC_OUT | pin.MAR_IN,
    pin.RAM_OUT | pin.DST_IN | pin.PC_INC,
    pin.PC_OUT | pin.MAR_IN,
    pin.RAM_OUT | pin.SRC_IN | pin.PC_INC
]
```


