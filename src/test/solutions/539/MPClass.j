.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static x F

.method public static foo(FI)V
.var 0 is a F from Label0 to Label1
.var 1 is b I from Label0 to Label1
Label0:
	fload_0
	invokestatic io/putFloatLn(F)V
	iload_1
	invokestatic io/putIntLn(I)V
Label1:
	return
.limit stack 1
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a I from Label0 to Label1
Label0:
	bipush 12
	i2f
	iconst_4
	invokestatic MPClass/foo(FI)V
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
