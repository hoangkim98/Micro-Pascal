.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is i I from Label0 to Label1
Label0:
	bipush 10
	bipush 10
	idiv
	istore_1
Label2:
	iload_1
	bipush 9
	bipush 19
	imul
	bipush 10
	idiv
	if_icmpgt Label3
Label5:
	iconst_5
	iload_1
	if_icmple Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifle Label6
	iload_1
	invokestatic io/putInt(I)V
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label5
Label6:
Label4:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label2
Label3:
	ldc ""
	invokestatic io/putStringLn(Ljava/lang/String;)V
	iload_1
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 5
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
