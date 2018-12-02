.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static a I
.field static b I
.field static c I

.method public static foo(I)Z
.var 0 is i I from Label0 to Label1
Label0:
	getstatic MPClass/a I
	iload_0
	iadd
	putstatic MPClass/a I
	iload_0
	iconst_5
	if_icmplt Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ireturn
Label1:
.limit stack 3
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is x Z from Label0 to Label1
Label0:
	iconst_0
	putstatic MPClass/a I
	iconst_1
	invokestatic MPClass/foo(I)Z
	iconst_2
	invokestatic MPClass/foo(I)Z
	ior
	iconst_3
	invokestatic MPClass/foo(I)Z
	ior
	bipush 7
	invokestatic MPClass/foo(I)Z
	ior
	invokestatic io/putBoolLn(Z)V
	getstatic MPClass/a I
	invokestatic io/putIntLn(I)V
	iconst_0
	putstatic MPClass/a I
	iconst_1
	invokestatic MPClass/foo(I)Z
	ifgt Label10
	iconst_2
	invokestatic MPClass/foo(I)Z
	goto Label8
Label10:
	iconst_1
Label8:
	ifgt Label7
	iconst_3
	invokestatic MPClass/foo(I)Z
	goto Label5
Label7:
	iconst_1
Label5:
	ifgt Label4
	iconst_4
	invokestatic MPClass/foo(I)Z
	goto Label2
Label4:
	iconst_1
Label2:
	invokestatic io/putBoolLn(Z)V
	getstatic MPClass/a I
	invokestatic io/putIntLn(I)V
	iconst_0
	putstatic MPClass/a I
	iconst_1
	invokestatic MPClass/foo(I)Z
	iconst_2
	invokestatic MPClass/foo(I)Z
	ior
	iconst_3
	invokestatic MPClass/foo(I)Z
	ior
	bipush 7
	invokestatic MPClass/foo(I)Z
	ior
	invokestatic io/putBoolLn(Z)V
	getstatic MPClass/a I
	invokestatic io/putIntLn(I)V
	iconst_0
	putstatic MPClass/a I
	iconst_1
	invokestatic MPClass/foo(I)Z
	iconst_2
	invokestatic MPClass/foo(I)Z
	ior
	ifgt Label16
	iconst_5
	invokestatic MPClass/foo(I)Z
	goto Label14
Label16:
	iconst_1
Label14:
	ifgt Label13
	bipush 7
	invokestatic MPClass/foo(I)Z
	goto Label11
Label13:
	iconst_1
Label11:
	invokestatic io/putBoolLn(Z)V
	getstatic MPClass/a I
	invokestatic io/putInt(I)V
	return
Label1:
	return
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
