.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	bipush 9
	bipush 6
	iadd
	invokestatic io/putIntLn(I)V
	bipush 9
	bipush 6
	isub
	invokestatic io/putIntLn(I)V
	bipush 9
	bipush 6
	imul
	invokestatic io/putIntLn(I)V
	bipush 9
	bipush 6
	idiv
	invokestatic io/putIntLn(I)V
	bipush 9
	bipush 6
	irem
	invokestatic io/putIntLn(I)V
	bipush 9
	bipush 6
	if_icmpne Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	invokestatic io/putBoolLn(Z)V
	bipush 9
	bipush 6
	if_icmpgt Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	invokestatic io/putBoolLn(Z)V
	bipush 9
	bipush 6
	if_icmpge Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	invokestatic io/putBoolLn(Z)V
	bipush 9
	bipush 6
	if_icmple Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	invokestatic io/putBoolLn(Z)V
	bipush 9
	bipush 6
	if_icmplt Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	invokestatic io/putBoolLn(Z)V
	bipush 9
	bipush 6
	if_icmpeq Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	invokestatic io/putBoolLn(Z)V
	bipush 9
	i2f
	bipush 6
	i2f
	fdiv
	invokestatic io/putFloatLn(F)V
	ldc 3.14159
	ldc 2.51
	fadd
	invokestatic io/putFloatLn(F)V
	ldc 3.14159
	ldc 2.51
	fsub
	invokestatic io/putFloatLn(F)V
	ldc 3.14159
	ldc 2.51
	fmul
	invokestatic io/putFloatLn(F)V
	ldc 3.14159
	ldc 2.51
	fdiv
	invokestatic io/putFloatLn(F)V
	ldc 3.14159
	ldc 2.51
	fcmpl
	ifne Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	invokestatic io/putBoolLn(Z)V
	ldc 3.14159
	ldc 2.51
	fcmpl
	ifgt Label16
	iconst_1
	goto Label17
Label16:
	iconst_0
Label17:
	invokestatic io/putBoolLn(Z)V
	ldc 3.14159
	ldc 2.51
	fcmpl
	ifge Label18
	iconst_1
	goto Label19
Label18:
	iconst_0
Label19:
	invokestatic io/putBoolLn(Z)V
	ldc 3.14159
	ldc 2.51
	fcmpl
	ifle Label20
	iconst_1
	goto Label21
Label20:
	iconst_0
Label21:
	invokestatic io/putBoolLn(Z)V
	ldc 3.14159
	ldc 2.51
	fcmpl
	iflt Label22
	iconst_1
	goto Label23
Label22:
	iconst_0
Label23:
	invokestatic io/putBoolLn(Z)V
	ldc 3.14159
	ldc 2.51
	fcmpl
	ifeq Label24
	iconst_1
	goto Label25
Label24:
	iconst_0
Label25:
	invokestatic io/putBoolLn(Z)V
	ldc 3.14159
	ldc 2.51
	fdiv
	invokestatic io/putFloatLn(F)V
	iconst_1
	ldc 1.3
	iconst_4
	i2f
	fcmpl
	ifle Label26
	iconst_1
	goto Label27
Label26:
	iconst_0
Label27:
	iand
	invokestatic io/putBoolLn(Z)V
	iconst_1
	ldc 1.3
	iconst_4
	i2f
	fcmpl
	ifle Label28
	iconst_1
	goto Label29
Label28:
	iconst_0
Label29:
	ior
	invokestatic io/putBoolLn(Z)V
	iconst_1
	ifle Label31
	ldc 1.3
	iconst_4
	i2f
	fcmpl
	ifle Label33
	iconst_1
	goto Label34
Label33:
	iconst_0
Label34:
	goto Label30
Label31:
	iconst_0
Label30:
	invokestatic io/putBoolLn(Z)V
	iconst_1
	ifgt Label37
	ldc 1.3
	iconst_4
	i2f
	fcmpl
	ifle Label38
	iconst_1
	goto Label39
Label38:
	iconst_0
Label39:
	goto Label35
Label37:
	iconst_1
Label35:
	invokestatic io/putBoolLn(Z)V
	ldc 3.14159
	iconst_2
	i2f
	fadd
	invokestatic io/putFloatLn(F)V
	iconst_3
	i2f
	ldc 2.51
	fadd
	invokestatic io/putFloat(F)V
Label1:
	return
.limit stack 28
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
