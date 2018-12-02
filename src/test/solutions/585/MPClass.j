.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static i I
.field static j I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
	iconst_1
	ifle Label3
	ldc "LOOPING..."
	invokestatic io/putStringLn(Ljava/lang/String;)V
	goto Label3
	goto Label2
Label3:
	iconst_1
	putstatic MPClass/i I
Label4:
	getstatic MPClass/i I
	bipush 100
	if_icmpgt Label5
Label7:
	iconst_0
	ifgt Label9
	iconst_1
	goto Label10
Label9:
	iconst_0
Label10:
	ifgt Label11
	iconst_1
	goto Label12
Label11:
	iconst_0
Label12:
	ifgt Label13
	iconst_1
	goto Label14
Label13:
	iconst_0
Label14:
	ifle Label8
	goto Label8
	goto Label7
Label8:
	bipush 9
	ineg
	putstatic MPClass/j I
Label15:
	getstatic MPClass/j I
	iconst_1
	ineg
	if_icmpgt Label16
	getstatic MPClass/j I
	getstatic MPClass/i I
	imul
	ineg
	invokestatic io/putInt(I)V
Label17:
	getstatic MPClass/j I
	iconst_1
	iadd
	putstatic MPClass/j I
	goto Label15
Label16:
	goto Label5
Label6:
	getstatic MPClass/i I
	iconst_1
	iadd
	putstatic MPClass/i I
	goto Label4
Label5:
Label1:
	return
.limit stack 15
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
