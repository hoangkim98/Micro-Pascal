.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is i I from Label0 to Label1
.var 2 is j I from Label0 to Label1
.var 3 is counter I from Label0 to Label1
Label0:
	iconst_0
	istore_3
	iconst_1
	istore_1
Label2:
	iload_1
	sipush 20000
	if_icmpgt Label3
	sipush 20000
	istore_2
Label5:
	iload_2
	iconst_1
	if_icmplt Label6
	iload_3
	iconst_1
	isub
	istore_3
Label7:
	iload_2
	iconst_1
	isub
	istore_2
	goto Label5
Label6:
Label4:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label2
Label3:
	iload_3
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 4
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
