# 1. 半加器

### 功能

**半加器是实现两个一位二进制数加法运算的器件**

### 真值表

| A(输入1) | B(输入2) | S(输出) | C(进位) |
| :------: | :------: | :-----: | :-----: |
|    0     |    0     |    0    |    0    |
|    0     |    1     |    1    |    0    |
|    1     |    0     |    1    |    0    |
|    1     |    1     |    0    |    1    |

### 逻辑表达式

$$
S=\overline{A}B+ A \overline{B} \quad 或 \quad S=A \bigoplus B
$$

$$
C=AB
$$

### 电路实现

![cpu-image-1](CPU-image\cpu-image-1.png)

# 2. 全加器

### 功能

**全加器是实现两位二进制数加法运算的器件**

### 真值表

| A(输入1) | B(输入2) | CI(进位输入) | S(输出) | CO(进位输出) |
| -------- | -------- | ------------ | ------- | ------------ |
| 0        | 0        | 0            | 0       | 0            |
| 0        | 0        | 1            | 1       | 0            |
| 0        | 1        | 0            | 1       | 0            |
| 0        | 1        | 1            | 0       | 1            |
| 1        | 0        | 0            | 1       | 0            |
| 1        | 0        | 1            | 0       | 1            |
| 1        | 1        | 0            | 0       | 1            |
| 1        | 1        | 1            | 1       | 1            |

### 逻辑表达式

$$
S=A\bigoplus B \bigoplus C
$$

$$
CO=AB+CI(A \bigoplus B)
$$

### 电路实现

![cpu-image-2](CPU-image\cpu-image-2.png)

# 3. 8位串行加法器

### 电路实现

![cpu-image-3](CPU-image\cpu-image-3.png)

# 4. 8位取反器

### 真值表

| E    | I    | O    |
| ---- | ---- | ---- |
| 0    | 0    | 0    |
| 0    | 1    | 1    |
| 1    | 0    | 1    |
| 1    | 1    | 0    |

### 逻辑表达式

$$
O=E \bigoplus I
$$

### 电路实现

![cpu-image-4](CPU-image\cpu-image-4.png)

# 5. 8位加法和减法实现

### 电路实现

![cpu-image-5](CPU-image\cpu-image-5.png)

### 加法测试

![cpu-image-6](CPU-image\cpu-image-6.png)

### 减法测试（使用补码进行计算）

![cpu-image-7](CPU-image\cpu-image-7.png)

# 6. 2-1选择器

### 真值表

|  EN  |  A   |  B   |  S   |
| :--: | :--: | :--: | :--: |
|  1   |  0   |  0   |  0   |
|  1   |  0   |  1   |  0   |
|  1   |  1   |  0   |  1   |
|  1   |  1   |  1   |  1   |
|  0   |  0   |  0   |  0   |
|  0   |  0   |  1   |  1   |
|  0   |  1   |  0   |  0   |
|  0   |  1   |  1   |  1   |

### 逻辑表达式

$$
S=EN \cdot A + \overline{EN} \cdot B
$$

### 电路实现

![cpu-image-8](CPU-image\cpu-image-8.png)

# 7. 8位2-1选择器

### 电路实现

![cpu-image-9.png](CPU-image\cpu-image-9.png)

# 8. 十六进制数码管

### 电路实现

![cpu-image-10.png](CPU-image\cpu-image-10.png)

### 数码管显示

**EN有效时，不显示**

| 十进制 | 十六进制 | 数码管输入(十六进制) |                        显示                         |
| :----: | :------: | :------------------: | :-------------------------------------------------: |
|   0    |    0     |          3F          |  ![light-image-0.png](CPU-image\light-image-0.png)  |
|   1    |    1     |          06          |  ![light-image-1.png](CPU-image\light-image-1.png)  |
|   2    |    2     |          5B          |  ![light-image-2.png](CPU-image\light-image-2.png)  |
|   3    |    3     |          4F          |  ![light-image-3.png](CPU-image\light-image-3.png)  |
|   4    |    4     |          66          |  ![light-image-4.png](CPU-image\light-image-4.png)  |
|   5    |    5     |          6D          |  ![light-image-5.png](CPU-image\light-image-5.png)  |
|   6    |    6     |          7D          |  ![light-image-6.png](CPU-image\light-image-6.png)  |
|   7    |    7     |          07          |  ![light-image-7.png](CPU-image\light-image-7.png)  |
|   8    |    8     |          7F          |  ![light-image-8.png](CPU-image\light-image-8.png)  |
|   9    |    9     |          6F          |  ![light-image-9.png](CPU-image\light-image-9.png)  |
|   10   |    A     |          77          | ![light-image-10.png](CPU-image\light-image-10.png) |
|   11   |    B     |          7C          | ![light-image-11.png](CPU-image\light-image-11.png) |
|   12   |    C     |          39          | ![light-image-12.png](CPU-image\light-image-12.png) |
|   13   |    D     |          5E          | ![light-image-13.png](CPU-image\light-image-13.png) |
|   14   |    E     |          79          | ![light-image-14.png](CPU-image\light-image-14.png) |
|   15   |    F     |          71          | ![light-image-15.png](CPU-image\light-image-15.png) |

# 9. 十六进制显示

### 电路实现

![cpu-image-11.png](CPU-image\cpu-image-11.png)

# 10. 十进制显示

### 电路实现

![cpu-image-12.png](CPU-image\cpu-image-12.png)

# 11. R-S触发器

### 功能

**存储一位数据,依赖于两个门电路正反馈**

### 真值表

**当R,S端都为0时,输出不确定**

|  R   |  S   |  Q   |  Q'  |
| :--: | :--: | :--: | :--: |
|  0   |  0   |  ?   |  ?   |
|  0   |  1   |  1   |  0   |
|  1   |  0   |  0   |  1   |
|  1   |  1   |  0   |  0   |

### 电路实现

![cpu-image-13.png](CPU-image\cpu-image-13.png)

**该电路有以下特点：**

- **刚上电时，输出的状态是不确定的，只确定两个输出是相反的。**
- **当其中一个输出为1时，输出状态立刻确定，见上面真值表。**
- **当两个输出都为0时，输出状态保持不变。**
- **当两个输出都为1时，输出都为0，则无法通过单个输出判断状态，此时触发器状态不确定(应避免此情况)。**

**该电路主要作用在于：如果R和S都为0时，电路状态可以得到保存，这个功能也叫作锁存器。**

# 12. D触发器

### 功能

**存储一位数据,输出与激励有关**

## 真值表

|  EN  |  D   |  Q   |
| :--: | :--: | :--: |
|  0   |  0   |  ?   |
|  0   |  1   |  ?   |
|  1   |  0   |  0   |
|  1   |  1   |  1   |

### 电路实现

![cpu-image-14.png](CPU-image\cpu-image-14.png)

# 13. D边沿触发器

### 电路实现

![cpu-image-15.png](CPU-image\cpu-image-15.png)

**上升沿触发,即CP端由0变为1时,将D>端数据存储进去**

# 14. 可以预设和清零的R-S触发器,D触发器,D边沿触发器

### 电路实现

![cpu-image-16.png](CPU-image\cpu-image-16.png)

![cpu-image-17.png](CPU-image\cpu-image-17.png)

![cpu-image-18.png](CPU-image\cpu-image-18.png)

# 15. T触发器

### 电路实现

![cpu-image-19.png](CPU-image\cpu-image-19.png)

**上升沿触发,使状态反转,一个周期翻转一次状态**

# 16. 行波计数器

### 电路实现

![cpu-image-20.png](CPU-image\cpu-image-20.png)

**第一个T触发器的两个周期构成第二个T触发器的一个周期，第二个T触发器的两个周期构成第三个T触发器的一个周期，依次类推。即构成了一个8位计数器，从0到255**

### 8位计数器

![cpu-image-30.png](CPU-image\cpu-image-30.png)

### 3位计数器

![cpu-image-31.png](CPU-image\cpu-image-31.png)

# 17. 1字节存储单元

### 电路实现

![cpu-image-21.png](CPU-image\cpu-image-21.png)

**D边沿触发器可以在上升沿中将输入写入，利用这样的功能我们可以实现一个1字节存储器**

# 18. 8位三态门

### 电路实现

![cpu-image-22.png](CPU-image\cpu-image-22.png)

**EN为0时断开**

# 19. 8位寄存器

### 电路实现

![cpu-image-23.png](CPU-image\cpu-image-23.png)

- **WE为写允许信号,*
- **CS为片选有效信号**

# 20. 3-8译码器

### 真值表

|  A2  |  A1  |  A0  |  O7  |  O6  |  O5  |  O4  |  O3  |  O2  |  O1  |  O0  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  0   |  0   |  0   |      |      |      |      |      |      |      |  1   |
|  0   |  0   |  1   |      |      |      |      |      |      |  1   |      |
|  0   |  1   |  0   |      |      |      |      |      |  1   |      |      |
|  0   |  1   |  1   |      |      |      |      |  1   |      |      |      |
|  1   |  0   |  0   |      |      |      |  1   |      |      |      |      |
|  1   |  0   |  1   |      |      |  1   |      |      |      |      |      |
|  1   |  1   |  0   |      |  1   |      |      |      |      |      |      |
|  1   |  1   |  1   |  1   |      |      |      |      |      |      |      |

### 电路实现

![cpu-image-24.png](CPU-image\cpu-image-24.png)

# 21. 8x1B存储器

### 电路实现

![cpu-image-25.png](CPU-image\cpu-image-25.png)

# 22. 存储器扩展

### 电路实现

**位扩展**

![cpu-image-26.png](CPU-image\cpu-image-26.png)

**字扩展**

**低位交叉编址**

![cpu-image-27.png](CPU-image\cpu-image-27.png)

**高位交叉编址**

![cpu-image-28.png](CPU-image\cpu-image-28.png)

# 23. 逻辑运算

### 8位AND电路实现

![cpu-image-38.png](CPU-image\cpu-image-38.png)

### 8位OR电路实现

![cpu-image-39.png](CPU-image\cpu-image-39.png)

### 8位XOR电路实现

![cpu-image-40.png](CPU-image\cpu-image-40.png)

### 8位NIV电路实现

![cpu-image-41.png](CPU-image\cpu-image-41.png)

