.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static foo()Z
Label0:
	ldc "hello"
	invokestatic io/putStringLn(Ljava/lang/String;)V
	iconst_1
	ireturn
Label1:
.limit stack 2
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is x I from Label0 to Label1
Label0:
	bipush 123
	istore_1
	iconst_1
	iconst_0
	iand
	ifle Label2
	iload_1
	bipush 100
	isub
	istore_1
	goto Label3
Label2:
Label3:
	iload_1
	invokestatic io/putIntLn(I)V
Label1:
	return
.limit stack 4
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
