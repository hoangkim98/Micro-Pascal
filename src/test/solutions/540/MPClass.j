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
	iload_1
	bipush 100
	if_icmple Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label4
	ldc "100 < x < 200"
	invokestatic io/putStringLn(Ljava/lang/String;)V
	goto Label5
Label4:
	iload_1
	sipush 200
	if_icmple Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label8
	ldc "200 < x < 300"
	invokestatic io/putStringLn(Ljava/lang/String;)V
	goto Label9
Label8:
	iload_1
	sipush 300
	if_icmple Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ifle Label12
	ldc "x > 300"
	invokestatic io/putStringLn(Ljava/lang/String;)V
	goto Label13
Label12:
	iload_1
	bipush 100
	if_icmple Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	ifle Label16
	iload_1
	bipush 100
	iadd
	istore_1
	goto Label17
Label16:
Label17:
Label13:
Label9:
Label5:
	iload_1
	invokestatic io/putIntLn(I)V
Label1:
	return
.limit stack 10
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
