    mov ss,1;
    mov sp,0x20;
    jmp start;

show:
    mov d,255;
    iret;
start:
    mov c,0;
increase:
    inc c;
    mov d,c;
    cli;
    int show;
    jmp increase;
    hlt;