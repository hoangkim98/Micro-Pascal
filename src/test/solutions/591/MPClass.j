.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static foo(I)V
.var 0 is i I from Label0 to Label1
Label0:
	iload_0
	iconst_0
	if_icmplt Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label4
	ldc "POSITIVE"
	invokestatic io/putStringLn(Ljava/lang/String;)V
	return
Label4:
Label5:
	ldc "NEGATIVE"
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label1:
	return
.limit stack 3
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_1
	invokestatic MPClass/foo(I)V
	iconst_2
	invokestatic MPClass/foo(I)V
	iconst_3
	invokestatic MPClass/foo(I)V
	iconst_3
	ineg
	invokestatic MPClass/foo(I)V
	iconst_2
	ineg
	invokestatic MPClass/foo(I)V
	iconst_0
	invokestatic MPClass/foo(I)V
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
