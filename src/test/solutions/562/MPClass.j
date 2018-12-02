.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is X I from Label0 to Label1
Label0:
	bipush 12
	istore_1
	iload_1
	invokestatic io/putInt(I)V
	invokestatic MPClass/foo()V
Label1:
	return
.limit stack 1
.limit locals 2
.end method

.method public static foo()V
Label0:
	ldc "Hello world"
	invokestatic io/putString(Ljava/lang/String;)V
Label1:
	return
.limit stack 1
.limit locals 0
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
