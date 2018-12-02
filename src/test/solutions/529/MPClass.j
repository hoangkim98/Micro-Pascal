.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static c Z
.field static a I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	bipush 10
	putstatic MPClass/a I
	iconst_0
	ifle Label3
	invokestatic MPClass/foo()Z
	goto Label2
Label3:
	iconst_0
Label2:
	ifle Label5
	getstatic MPClass/a I
	invokestatic io/putInt(I)V
	goto Label6
Label5:
	iconst_5
	invokestatic io/putIntLn(I)V
Label6:
	getstatic MPClass/a I
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 2
.limit locals 1
.end method

.method public static foo()Z
Label0:
	getstatic MPClass/a I
	iconst_1
	isub
	putstatic MPClass/a I
	iconst_0
	ireturn
Label1:
.limit stack 2
.limit locals 0
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
