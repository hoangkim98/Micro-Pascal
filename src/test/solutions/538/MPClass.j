.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_1
	iconst_2
	if_icmple Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifgt Label4
	bipush 7
	bipush 7
	if_icmpne Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	goto Label2
Label4:
	iconst_1
Label2:
	invokestatic io/putBoolLn(Z)V
	iconst_1
	iconst_0
	if_icmpge Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifgt Label11
	iconst_1
	ineg
	iconst_0
	if_icmple Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	goto Label9
Label11:
	iconst_1
Label9:
	invokestatic io/putBoolLn(Z)V
	iconst_1
	iconst_0
	ineg
	if_icmple Label19
	iconst_1
	goto Label20
Label19:
	iconst_0
Label20:
	ifgt Label18
	iconst_2
	iconst_2
	if_icmplt Label21
	iconst_1
	goto Label22
Label21:
	iconst_0
Label22:
	goto Label16
Label18:
	iconst_1
Label16:
	invokestatic io/putBoolLn(Z)V
	iconst_1
	iconst_1
	iconst_1
	if_icmpne Label26
	iconst_1
	goto Label27
Label26:
	iconst_0
Label27:
	iand
	ifgt Label25
	iconst_2
	iconst_2
	if_icmpge Label28
	iconst_1
	goto Label29
Label28:
	iconst_0
Label29:
	goto Label23
Label25:
	iconst_1
Label23:
	invokestatic io/putBool(Z)V
Label1:
	return
.limit stack 18
.limit locals 1
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
