.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static isPrime(I)Z
.var 0 is n I from Label0 to Label1
.var 1 is flag Z from Label0 to Label1
.var 2 is i I from Label0 to Label1
Label0:
	iload_0
	iconst_1
	if_icmpne Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	iload_0
	iconst_0
	if_icmpne Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ior
	ifle Label6
	iconst_0
	ireturn
Label6:
Label7:
	iload_0
	iconst_2
	if_icmpne Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	iload_0
	iconst_3
	if_icmpne Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ior
	ifle Label12
	iconst_1
	ireturn
Label12:
Label13:
	iconst_1
	istore_1
	iconst_2
	istore_2
Label14:
	iload_2
	iload_0
	iconst_2
	idiv
	if_icmpgt Label15
	iload_0
	iload_0
	iload_2
	idiv
	iload_2
	imul
	isub
	iconst_0
	if_icmpne Label17
	iconst_1
	goto Label18
Label17:
	iconst_0
Label18:
	ifle Label19
	iconst_0
	istore_1
	goto Label15
	goto Label20
Label19:
Label20:
Label16:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label14
Label15:
	iload_1
	ireturn
Label1:
.limit stack 16
.limit locals 3
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_1
	invokestatic MPClass/isPrime(I)Z
	invokestatic io/putBoolLn(Z)V
	iconst_2
	invokestatic MPClass/isPrime(I)Z
	invokestatic io/putBoolLn(Z)V
	bipush 7
	invokestatic MPClass/isPrime(I)Z
	invokestatic io/putBoolLn(Z)V
	bipush 14
	invokestatic MPClass/isPrime(I)Z
	invokestatic io/putBool(Z)V
Label1:
	return
.limit stack 1
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
