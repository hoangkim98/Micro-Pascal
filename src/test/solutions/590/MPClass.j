.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static fib(I)I
.var 0 is n I from Label0 to Label1
Label0:
	iload_0
	iconst_0
	if_icmpge Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label4
	iconst_1
	ineg
	ireturn
Label4:
	iload_0
	iconst_0
	if_icmpne Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label8
	iconst_0
	ireturn
Label8:
	iload_0
	iconst_1
	if_icmpne Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ifle Label12
	iconst_1
	ireturn
Label12:
	iload_0
	iconst_1
	isub
	invokestatic MPClass/fib(I)I
	iload_0
	iconst_2
	isub
	invokestatic MPClass/fib(I)I
	iadd
	ireturn
Label13:
Label9:
Label5:
Label1:
.limit stack 9
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is i I from Label0 to Label1
Label0:
	bipush 100
	ineg
	invokestatic MPClass/fib(I)I
	invokestatic io/putIntLn(I)V
	iconst_0
	istore_1
Label2:
	iload_1
	bipush 10
	if_icmpgt Label3
	iload_1
	invokestatic MPClass/fib(I)I
	invokestatic io/putIntLn(I)V
Label4:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label2
Label3:
Label1:
	return
.limit stack 2
.limit locals 2
.end method

.method public <init>()V
.var 0 is this LMPClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method
