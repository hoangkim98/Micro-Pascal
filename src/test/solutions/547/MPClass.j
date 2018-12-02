.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is x I from Label0 to Label1
Label0:
	iconst_1
	istore_1
.var 2 is x I from Label4 to Label5
Label4:
	iconst_2
	istore_2
.var 3 is x I from Label8 to Label9
Label8:
	iconst_3
	istore_3
	iload_3
	invokestatic io/putInt(I)V
Label9:
	iload_2
	invokestatic io/putInt(I)V
Label5:
Label1:
	return
.limit stack 1
.limit locals 4
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
