.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
	iconst_1
	ifgt Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label3
Label6:
	iconst_0
	ifgt Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifle Label7
Label10:
	iconst_1
	ifle Label11
Label12:
	iconst_1
	iconst_1
	iand
	ifle Label13
	sipush 999
	ineg
	invokestatic io/putInt(I)V
	goto Label12
Label13:
	goto Label10
Label11:
	goto Label6
Label7:
	goto Label2
Label3:
Label1:
	return
.limit stack 13
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
