.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is i1 I from Label0 to Label1
.var 2 is i2 I from Label0 to Label1
Label0:
	iconst_1
	istore_1
Label2:
	iload_1
	bipush 10
	if_icmpgt Label3
	iconst_1
	istore_2
Label5:
	iload_2
	bipush 10
	if_icmpgt Label6
	iload_2
	invokestatic io/putInt(I)V
	iload_2
	iload_1
	iconst_1
	isub
	if_icmpne Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifle Label10
	goto Label7
	goto Label11
Label10:
Label11:
	iload_2
	iload_1
	if_icmpne Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifle Label14
	goto Label6
	goto Label15
Label14:
Label15:
Label7:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label5
Label6:
	iload_1
	iconst_3
	if_icmpne Label16
	iconst_1
	goto Label17
Label16:
	iconst_0
Label17:
	ifle Label18
	goto Label4
	goto Label19
Label18:
Label19:
	iload_1
	iconst_5
	if_icmpne Label20
	iconst_1
	goto Label21
Label20:
	iconst_0
Label21:
	ifle Label22
	goto Label3
	goto Label23
Label22:
Label23:
Label4:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label2
Label3:
	return
Label1:
	return
.limit stack 11
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
