.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static c F

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a Z from Label0 to Label1
.var 2 is b Z from Label0 to Label1
.var 3 is c Z from Label0 to Label1
.var 4 is d F from Label0 to Label1
.var 5 is e F from Label0 to Label1
.var 6 is x Ljava/lang/String; from Label0 to Label1
.var 7 is y Ljava/lang/String; from Label0 to Label1
.var 8 is z Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_1
	istore_3
	iload_3
	invokestatic io/putBool(Z)V
Label1:
	return
.limit stack 2
.limit locals 9
.end method

.method public static foo(Ljava/lang/String;)F
.var 0 is N Ljava/lang/String; from Label0 to Label1
.var 1 is g F from Label0 to Label1
.var 2 is h F from Label0 to Label1
Label0:
	iconst_1
	invokestatic io/putInt(I)V
	ldc 1.5
	freturn
Label1:
.limit stack 1
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
