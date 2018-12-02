.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static c F

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_1
	ldc 1.5
	invokestatic MPClass/foo(IF)F
	putstatic MPClass/c F
	iconst_3
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 2
.limit locals 1
.end method

.method public static foo(IF)F
.var 0 is N I from Label0 to Label1
.var 1 is z F from Label0 to Label1
Label0:
	ldc 1.5
	freturn
Label1:
.limit stack 1
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
