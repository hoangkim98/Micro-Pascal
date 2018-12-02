.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static d I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a Z from Label0 to Label1
.var 2 is b Z from Label0 to Label1
.var 3 is c Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_1
	istore_1
	iconst_0
	istore_2
	ldc "ahihi"
	astore_3
	iconst_1
	iconst_2
	iadd
	putstatic MPClass/d I
	iload_1
	iload_2
	iload_2
	ifgt Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	iand
	ior
	iconst_0
	ior
	invokestatic io/putBool(Z)V
	aload_3
	invokestatic io/putString(Ljava/lang/String;)V
	getstatic MPClass/d I
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 8
.limit locals 4
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
