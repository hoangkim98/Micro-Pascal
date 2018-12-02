.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static fact(I)I
.var 0 is x I from Label0 to Label1
.var 1 is i I from Label0 to Label1
.var 2 is f I from Label0 to Label1
Label0:
	iconst_1
	istore_2
	iconst_1
	istore_1
Label2:
	iload_1
	iload_0
	if_icmpgt Label3
	iload_2
	iload_1
	imul
	istore_2
Label4:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label2
Label3:
	iload_2
	ireturn
Label1:
.limit stack 3
.limit locals 3
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is s I from Label0 to Label1
.var 2 is i I from Label0 to Label1
Label0:
	iconst_1
	istore_2
	iconst_0
	istore_1
Label2:
	iload_2
	bipush 10
	if_icmpgt Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label3
	iload_2
	invokestatic MPClass/fact(I)I
	invokestatic io/putIntLn(I)V
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label2
Label3:
Label1:
	return
.limit stack 4
.limit locals 3
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
