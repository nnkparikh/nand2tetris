// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Put your code here.

@R1 	// put R1 in a temp memory location i
D=M
@i
M=D

@R2		// initialize result R2 to zero
M=0


(LOOP)	// summation of R0, R1 times
@i
D=M
@END
D;JEQ
@R0
D=M
@R2
M=M+D
@i
M=M-1
@LOOP
0;JMP

(END)
@END	// infinite loop
0;JMP

