.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static a I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_0
	putstatic MPClass/a I
	iconst_1
	ifle Label2
	getstatic MPClass/a I
	iconst_1
	iadd
	putstatic MPClass/a I
	goto Label3
Label2:
	getstatic MPClass/a I
	iconst_2
	iadd
	putstatic MPClass/a I
Label3:
	getstatic MPClass/a I
	iconst_4
	iadd
	putstatic MPClass/a I
	getstatic MPClass/a I
	invokestatic io/putIntLn(I)V
Label1:
	return
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