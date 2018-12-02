.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a Z from Label0 to Label1
.var 2 is b Z from Label0 to Label1
Label0:
	iconst_1
	istore_1
	iconst_0
	istore_2
	iload_1
	invokestatic MPClass/test()Z
	ior
	ifgt Label4
	iload_1
	iload_2
	ifgt Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	iand
	invokestatic MPClass/test()Z
	iand
	goto Label2
Label4:
	iconst_1
Label2:
	invokestatic io/putBool(Z)V
Label1:
	return
.limit stack 7
.limit locals 3
.end method

.method public static test()Z
.var 0 is a F from Label0 to Label1
.var 1 is res Z from Label0 to Label1
Label0:
	iconst_0
	istore_1
	ldc 9.5
	fstore_0
	fload_0
	invokestatic io/putFloat(F)V
	iload_1
	ireturn
Label1:
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
