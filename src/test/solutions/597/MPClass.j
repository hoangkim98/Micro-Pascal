.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static print(Ljava/lang/String;)V
.var 0 is s Ljava/lang/String; from Label0 to Label1
Label0:
	aload_0
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static helloWorld()Ljava/lang/String;
Label0:
	ldc "HELLO WORLD"
	areturn
Label1:
.limit stack 1
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	ldc "TEST"
	invokestatic MPClass/print(Ljava/lang/String;)V
	invokestatic MPClass/helloWorld()Ljava/lang/String;
	invokestatic MPClass/print(Ljava/lang/String;)V
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
