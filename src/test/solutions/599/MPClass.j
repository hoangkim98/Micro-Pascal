.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is i I from Label0 to Label1
.var 2 is j I from Label0 to Label1
.var 3 is k I from Label0 to Label1
.var 4 is counter I from Label0 to Label1
Label0:
	iconst_0
	istore 4
	iload 4
	istore_1
Label2:
	iload_1
	iconst_3
	if_icmpge Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label3
	iconst_0
	istore_2
Label6:
	iload_2
	iconst_4
	if_icmpge Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifle Label7
	iconst_0
	istore_3
Label10:
	iload_3
	iconst_5
	if_icmpge Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifle Label11
	iload_3
	iconst_1
	iadd
	istore_3
	iload 4
	iconst_1
	iadd
	istore 4
	goto Label10
Label11:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label6
Label7:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label2
Label3:
	iload 4
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 8
.limit locals 5
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
