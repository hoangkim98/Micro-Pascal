.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a I from Label0 to Label1
Label0:
	iconst_1
	istore_1
	invokestatic MPClass/foo()I
	invokestatic io/putInt(I)V
	iload_1
	iconst_1
	if_icmple Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label4
	return
Label4:
	return
Label5:
Label1:
	return
.limit stack 3
.limit locals 2
.end method

.method public static foo()I
.var 0 is a I from Label0 to Label1
Label0:
	iconst_1
	istore_0
	iload_0
	iconst_1
	if_icmple Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label4
	iconst_1
	ireturn
Label4:
	iconst_3
	ireturn
Label5:
	iconst_3
	istore_0
Label1:
.limit stack 3
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
