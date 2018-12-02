.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is i I from Label0 to Label1
Label0:
	iconst_0
	istore_1
	iload_1
	invokestatic io/putIntLn(I)V
.var 2 is i F from Label4 to Label5
Label4:
	bipush 8
	i2f
	fstore_2
	fload_2
	invokestatic io/putFloatLn(F)V
Label5:
	iload_1
	invokestatic io/putIntLn(I)V
Label1:
	return
.limit stack 1
.limit locals 3
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
