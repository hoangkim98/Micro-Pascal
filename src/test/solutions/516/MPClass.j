.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a I from Label0 to Label1
.var 2 is d Z from Label0 to Label1
Label0:
	iconst_0
	istore_1
	iconst_1
	ifle Label2
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label3
Label2:
	iload_1
	iconst_2
	iadd
	istore_1
Label3:
	iload_1
	iconst_4
	iadd
	istore_1
	iload_1
	invokestatic io/putIntLn(I)V
Label1:
	return
.limit stack 3
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