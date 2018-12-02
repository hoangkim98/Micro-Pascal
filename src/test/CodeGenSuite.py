import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_int(self):
        input = """procedure main(); begin putInt(100); end"""
        expect = "100"
        self.assertTrue(TestCodeGen.test(input, expect, 500))

    def test_float(self):
        input = """procedure main(); begin putFloat(10.5); end"""
        expect = "10.5"
        self.assertTrue(TestCodeGen.test(input, expect, 501))

    def test_add(self):
        input = """procedure main();
            begin putInt(10 + 5); end"""
        expect = "15"
        self.assertTrue(TestCodeGen.test(input, expect, 502))

    def test_div(self):
        input = """procedure main();
            begin putFloat(8.5 / 5); end"""
        expect = "1.7"
        self.assertTrue(TestCodeGen.test(input, expect, 503))

    def test_var_decl(self):
        input = """var a:real;
            procedure main();
            begin putFloat(10-5.5); end"""
        expect = "4.5"
        self.assertTrue(TestCodeGen.test(input, expect, 504))

    def test_var_decl_real(self):
        input = """var a:real;
            procedure main();
            begin
                a:=1.5;
                //putint(9 div 6);
                putFloat(a);
            end"""
        expect = "1.5"
        self.assertTrue(TestCodeGen.test(input, expect, 505))

    def test_var_decl_bool(self):
        input = """var a:boolean;
            procedure main();
            begin
                a:=tRue;
                putbool(A);
            end"""
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 506))

    def test_print_fucntion_return_int(self):
        input = """var a:boolean;
            procedure main();
            begin
                putinT(foo());
            end
            function foo():integer;
            begin
                return 5;
            end
            """
        expect = "5"
        self.assertTrue(TestCodeGen.test(input, expect, 507))

    def test_print_fucntion_return_coer(self):
        input = """var a:boolean;
            procedure main();
            begin
                putfloat(foo());
            end
            function foo():real;
            begin
                return 5;
            end
            """
        expect = "5.0"
        self.assertTrue(TestCodeGen.test(input, expect, 508))

    def test_assign_coer(self):
        input = """var a:real;
            procedure main();
            begin
                a:=10;
                putfloat(a);
            end
            """
        expect = "10.0"
        self.assertTrue(TestCodeGen.test(input, expect, 509))

    def test_print_fucntion_return_bool(self):
        input = """var a:boolean;
            procedure main();
            begin
                putbool(foo());
            end
            function foo():boolean;
            begin
                return trUE;
            end
            """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 510))

    def test_return_string(self):
        input = """//var a:string;

            procedure main();
            begin
                putstRing(foo());
                //PUtString("abc");
            end
            function foo():string;
            begin
                return "abc";
            end
            """
        expect = "abc"
        self.assertTrue(TestCodeGen.test(input, expect, 511))

    def test_local_decl(self):
        input = """var c:real;
            procedure main();
            var a,b,c:boolean; d,e:real; x,y,z:string;
            begin
                c := true;
                putbool(c);
            end
            function foo(N:string):real;
            var g,h:real;
            begin
                putInt(1);
                return 1.5;
            end
            """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 512))

    def test_assign_func(self):
        input = """var c:real;
            procedure main();
            begin
                c:= foo(1,1.5);
                putInt(3);
            end
            function foo(N:integer;z:real):real;
            begin
                return 1.5;
            end
            """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input, expect, 513))

    def test_if(self):
        input = """var c:integer;
            procedure main();
            begin
                c := 3;
                if c<1 then putintln(c);
                else putintln(1);
                putintln(10);
            end
            """
        expect = "1\n10\n"
        self.assertTrue(TestCodeGen.test(input, expect, 514))

    def test_if_complex(self):
        input = """var a:integer;
            procedure main();
            begin
                a := 0;
                if true then a:=a+1;
                else a:=a+2;
                a:=a+4;
                putintln(a);
            end
            """
        expect = "5\n"
        self.assertTrue(TestCodeGen.test(input, expect, 515))

    def test_if_local(self):
        input = """//var a:real;
            procedure main();
            var a:integer;d:boolean;
            begin
                a := 0;
                if true then a:=a+1;
                else a:=a+2;
                a:=a+4;
                putintln(a);
            end
            """
        expect = "5\n"
        self.assertTrue(TestCodeGen.test(input, expect, 516))

    def test_while(self):
        input = """var a:integer;
            procedure main();
            begin
                a := 4;
                while a>1 do
                begin
                    a:=a-1;
                    putIntln(a);
                end
                putintln(a);
            end
            """
        expect = "3\n2\n1\n1\n"
        self.assertTrue(TestCodeGen.test(input, expect, 517))

    def test_while_local(self):
        input = """
            procedure main();
            var a:integer;
            begin
                a := 4;
                while a>1 do
                begin
                    a:=a-1;
                    putIntln(a);
                end
                putintln(a);
            end
            """
        expect = "3\n2\n1\n1\n"
        self.assertTrue(TestCodeGen.test(input, expect, 518))

    def test_for11(self):
        input = """var a:integer;
            procedure main();
            begin
                a := 0;
                for a:=1 to 5 do
                    putintln(a);
            end
            """
        expect = "1\n2\n3\n4\n5\n"
        self.assertTrue(TestCodeGen.test(input, expect, 519))

    def test_bin_and(self):
        input = """var c:boolean;
            procedure main();
            begin
                c := true and false;
                putbool(c);
            end
            """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input, expect, 520))

    def test_bin_or(self):
        input = """var c:boolean;
            procedure main();
            begin
                c := true or faLse;
                putbool(c);
            end
            """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 521))

    def test_bin_cuc_manh(self):
        input = """
            procedure main(); 
            begin
                putintln(9 + 6);
                putintln(9 - 6);
                putintln(9 * 6);
                putintln(9 div 6);
                putintln(9 mod 6);
                putboolln(9 = 6);
                putboolln(9 <= 6);
                putboolln(9 < 6);
                putboolln(9 > 6);
                putboolln(9 >= 6);
                putboolln(9 <> 6);
                putfloatln(9 / 6);
                putfloatln(3.14159 + 2.51);
                putfloatln(3.14159 - 2.51);
                putfloatln(3.14159 * 2.51);
                putfloatln(3.14159 / 2.51);
                putboolln(3.14159 = 2.51);
                putboolln(3.14159 <= 2.51);
                putboolln(3.14159 < 2.51);
                putboolln(3.14159 > 2.51);
                putboolln(3.14159 >= 2.51);
                putboolln(3.14159 <> 2.51);
                putfloatln(3.14159 / 2.51);
                putBooLlN(trUe aNd (1.3>4));
                putBooLlN(trUe oR (1.3>4));
                putBooLlN(true  aNd tHen (1.3>4));
                putBooLlN(trUe or eLse (1.3>4));
                putfloatln(3.14159 + 2);
                putfloat(3 + 2.51);
            end
        """
        expect = "15\n3\n54\n1\n3\nfalse\nfalse\nfalse\ntrue\ntrue\ntrue\n1.5\n5.6515903\n0.6315901\n7.885391\n1.2516296\nfalse\nfalse\nfalse\ntrue\ntrue\ntrue\n1.2516296\nfalse\ntrue\nfalse\ntrue\n5.14159\n5.51"
        self.assertTrue(TestCodeGen.test(input, expect, 522))

    def test_if_return(self):
        input = """
            procedure main();
            var a:integer;
            begin
                a:=1;
               putint(foo());
                if a>1 then return ;
                else return ;
                //a:=4;
            end
            function foo():integer;
            var a:integer;
            begin
                a:=1;
                if a>1 then return 1;
                else return 3;
                a:=3;
            end
        """
        expect ="3"
        self.assertTrue(TestCodeGen.test(input,expect,523))

    def test_if_break(self):
        input = """
            procedure main();
            var a:integer;
            begin
                for a:=1 to 3 do 
                begin
                    putint(1);
                    if a>1 then break;
                    else putint(3);
                    a:=6;
                end
            end
        """
        expect ="13"
        self.assertTrue(TestCodeGen.test(input,expect,524))

    def test_1(self):
        input ="""
            function isPrime(n:integer):boolean;
            var flag:boolean;i:integer;
            begin
            	if (n=1) or (n=0) then return false;
            	if (n=2) or (n=3) then return true;
            	flag :=true;
            	for i:=2 to (n div 2) do
            		if n - ((n div i) * i) = 0 then
            		begin
            			flag := false;
            			break;
            		end
            	return flag;
            end

            procedure main();
            begin
            	putBoolln(isPrime(1));
            	putBoolln(isPrime(2));
            	putBoolln(isPrime(7));
            	putBool(isPrime(14));
            end
        """
        expect ="false\ntrue\ntrue\nfalse"
        self.assertTrue(TestCodeGen.test(input,expect,525))

    def test_10(self):
        input = Program([VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType()),VarDecl(Id("c"),IntType()),
                        FuncDecl(Id("foo"),[VarDecl(Id("i"),IntType())],[],[Assign(Id("a"),BinaryOp("+",Id("a"),Id("i"))),Return(BinaryOp(">=",Id("i"),IntLiteral(5)))], BoolType()),
                        FuncDecl(Id("main"),[],[VarDecl(Id("x"),BoolType())],[Assign(Id("a"),IntLiteral(0)),CallStmt(Id("putBoolLn"),[BinaryOp("or",BinaryOp("or",BinaryOp("or",CallExpr(Id("foo"),[IntLiteral(1)]),CallExpr(Id("foo"),[IntLiteral(2)])),CallExpr(Id("foo"),[IntLiteral(3)])),CallExpr(Id("foo"),[IntLiteral(7)]))]),CallStmt(Id("putIntLn"),[Id("a")]),Assign(Id("a"),IntLiteral(0)),CallStmt(Id("putBoolLn"),[BinaryOp("orelse",BinaryOp("orelse",BinaryOp("orelse",CallExpr(Id("foo"),[IntLiteral(1)]),CallExpr(Id("foo"),[IntLiteral(2)])),CallExpr(Id("foo"),[IntLiteral(3)])),CallExpr(Id("foo"),[IntLiteral(4)]))]),CallStmt(Id("putIntLn"),[Id("a")]),Assign(Id("a"),IntLiteral(0)),CallStmt(Id("putBoolLn"),[BinaryOp("or",BinaryOp("or",BinaryOp("or",CallExpr(Id("foo"),[IntLiteral(1)]),CallExpr(Id("foo"),[IntLiteral(2)])),CallExpr(Id("foo"),[IntLiteral(3)])),CallExpr(Id("foo"),[IntLiteral(7)]))]),CallStmt(Id("putIntLn"),[Id("a")]),Assign(Id("a"),IntLiteral(0)),CallStmt(Id("putBoolLn"),[BinaryOp("orelse",BinaryOp("orelse",BinaryOp("or",CallExpr(Id("foo"),[IntLiteral(1)]),CallExpr(Id("foo"),[IntLiteral(2)])),CallExpr(Id("foo"),[IntLiteral(5)])),CallExpr(Id("foo"),[IntLiteral(7)]))]),CallStmt(Id("putInt"),[Id("a")]),Return(None)])])
        expect ="true\n13\nfalse\n10\ntrue\n13\ntrue\n8"
        self.assertTrue(TestCodeGen.test(input,expect,526))

    def test_with3(self):
        input = """
            procedure main();
            var a:integer;
            begin
                a:=5;
                putint(a);
                with a:real;do
                    begin
                        a:=6;
                        putfloAt(a);
                    end
            end
            var a:integer;
        """
        expect = "56.0"
        self.assertTrue(TestCodeGen.test(input,expect,527))

    def test_9(self):
        input = Program([FuncDecl(Id("main"),[],[VarDecl(Id("i1"),IntType()),VarDecl(Id("i2"),IntType())],[For(Id("i1"),IntLiteral(1),IntLiteral(10),True,[For(Id("i2"),IntLiteral(1),IntLiteral(10),True,[CallStmt(Id("putInt"),[Id("i2")]),If(BinaryOp('=',Id("i2"),BinaryOp('-',Id("i1"),IntLiteral(1))),[Continue()],[]),If(BinaryOp('=',Id("i2"),Id("i1")),[Break()],[])]),If(BinaryOp('=',Id("i1"),IntLiteral(3)),[Continue()],[]),If(BinaryOp('=',Id("i1"),IntLiteral(5)),[Break()],[])]),Return(None)],VoidType())])
        expect = "112123123412345"
        self.assertTrue(TestCodeGen.test(input,expect,528))
    
    def test_bin_and_then(self):
        input = """var c:boolean;a:integer;
            procedure main();
            begin
                a:=10;
                if (false and then foo()) then putint(a);
                else putintln(5);
                putint(a);
            end
            function foo():boolean;
            begin
                a := a-1;
                return false;
            end
            """
        expect = "5\n10"
        self.assertTrue(TestCodeGen.test(input, expect, 529))

    def test_bin_or_else(self):
        input = """var c:boolean;a:integer;
            procedure main();
            begin
                a:=10;
                if (false or else foo()) then putintln(a);
                else putintln(5);
                putint(a);
            end
            function foo():boolean;
            begin
                a := a-1;
                return true;
            end
            """
        expect = "9\n9"
        self.assertTrue(TestCodeGen.test(input, expect, 530))

    def test_while_1(self):
        input = """
        procedure main();
        begin
            while not true do
                while not false do
                    while true do
                        WHILE TRUE and TRUE do
                            putInt(-999);
        end
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 531))

    def test_exp(self):
        input = """
        var INTMAX, INTMIN:integer;
        procedure main();
        //var a,b,c,d,e,g:integer;
        begin
            INTMAX := 2147483647;
            INTMIN := INTMAX*-1-1;
            putIntLn(INTMAX);
            putIntLn(INTMIN);
            putIntLn(INTMAX + INTMIN);
        end
        """
        expect = "2147483647\n-2147483648\n-1\n"
        self.assertTrue(TestCodeGen.test(input, expect, 532))

    def test_call_591(self):
        input = """
        procedure printSum(a,b,c:integer);
        begin
            putIntLn(a+b+c);
            a := 0;
            b := 0;
            c := 0;
        end

        procedure main();
        var a : integer;
        begin
            a := 1;
            printSum(a, 6, 7);
            putIntLn(a);
        end
        """
        expect = "14\n1\n"
        self.assertTrue(TestCodeGen.test(input, expect, 533))

    def test_call_595(self):
        input = """
        function sum(a,b:integer):integer;
        begin
            return a + b;
        end

        procedure main();
        begin
            putInt(sum(1,10) - sum(10,1));
        end
        """
        expect = "0"
        self.assertTrue(TestCodeGen.test(input, expect, 534))

    def test_break_continue_1(self):
        input = """
        var i : integer;
        procedure main();
        begin
            for i:=90 downto 0 do
                if i mod 10 <> 0 then continue;
                else
                    putFloatLn(i / 10);
        end
        """
        expect = "9.0\n8.0\n7.0\n6.0\n5.0\n4.0\n3.0\n2.0\n1.0\n0.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 535))

    def test_for12(self):
        input = """
        var i:integer;
        procedure main();
        begin
            for i:=9 downto 5 do
                if i mod 3 = 0 then
                    putfloatln(i div 3);
        end
        """
        expect = "3.0\n2.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 536))

    def test_if1(self):
        input = """
        function absFloat(i:integer):real;
        begin
            if i >= 0 then
                return i*1.;
            else
                return -i*1.;
        end

        procedure main();
        begin
            putFloatLn(absFloat(167));
            putFloatLn(absFloat(-167));
            putFloatLn(absFloat(167)-absFloat(-167));
        end
        """
        expect = "167.0\n167.0\n0.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 537))

    def test_bin_or_else1(self):
        input = """
            procedure main();
            begin
                putBoolLn(1 > 2 or else 7 = 7);
                putBoolLn(1 < 0 or else -1 > 0);
                putBoolLn(1 > -0 or else 2 >= 2);
                putBool(true and (1 = 1) or else 2 < 2);
            end
        """
        expect = "true\nfalse\ntrue\ntrue"
        self.assertTrue(TestCodeGen.test(input,expect,538))

    def test_call_stmt_float_pass_int(self):
        input = """ 
            var x: real;
            procedure foo(a: real; b: integer);
            begin
                putFloatLn(a);
                putIntLn(b);
            end

            procedure main();
            var a : integer;
            begin
                foo(12,4);
            end
        """
        expect = "12.0\n4\n"
        self.assertTrue(TestCodeGen.test(input,expect,539))

    def test_random1(self):
        input = """
        function foo(): boolean;
        begin
            putStringLn("hello");
            return true;
        end

        procedure main();
        var x : integer;
        begin
            x := 123;
            if (x > 100) then
                putStringLn("100 < x < 200");
            else if (x > 200) then
                putStringLn("200 < x < 300");
            else if (x > 300) then
                putStringLn("x > 300");
            else 
            begin
                if (x > 100) then
                 x := x + 100;
            end
            putIntLn(x);
        end
"""
        expect = """100 < x < 200
123
"""
        self.assertTrue(TestCodeGen.test(input, expect, 540))

    def test_random2(self):
        input = """
        function foo(): boolean;
        begin
            putStringLn("hello");
            return true;
        end

        procedure main();
        var x : integer;
        begin
            x := 123;
            if (true and false) then
                x := x - 100;
            putIntLn(x);
        end
        """
        expect = """123\n"""
        self.assertTrue(TestCodeGen.test(input, expect, 541))

    def test_random3(self):
        input = """
        function foo(): boolean;
        begin
            putStringLn("hello");
            return true;
        end

        procedure main();
        var x : integer;
        begin
            x := 1;
            while x <= 10 do
            begin
 putIntLn(x);
                if x = 10 then putStringLn("lmao");

                x := x + 1;
            end
        end
        """
        expect = """1
2
3
4
5
6
7
8
9
10
lmao
"""
        self.assertTrue(TestCodeGen.test(input, expect, 542))

    def test_random4(self):
        input = """
function isPrime(x: integer): boolean;
var i : integer;
begin
    for i := 2 to x div 2 do
    begin
        if x mod i = 0 then return false;
    end

    return true;
end

procedure main();
var x, i : integer;
begin
    i := 0;
    x := 100;

    while i <= x do
    begin
        if isPrime(i) then putIntLn(i);
        i := i + 1;
    end

end
        """
        expect = """0
1
2
3
5
7
11
13
17
19
23
29
31
37
41
43
47
53
59
61
67
71
73
79
83
89
97
"""
        self.assertTrue(TestCodeGen.test(input, expect, 543))

    def test_random5(self):
        input = """
function fact(x: integer): integer;
var i, f : integer;
begin
    f := 1;
    for i := 1 to x do f := f * i;
    return f;
end

procedure main();
var s, i : integer;
begin
    i := 1;
    s := 0;

    while i <= 10 do 
    begin
        putIntLn(fact(i));
        i := i + 1;
    end

end
        """
        expect = """1
2
6
24
120
720
5040
40320
362880
3628800
"""
        self.assertTrue(TestCodeGen.test(input, expect, 544))

    def test_random6(self):
        input = """
procedure main();
var s, i, j : integer;
begin
    i := 1;

    while i <= 10 do 
    begin
        if (i > 4) and (i < 7) then 
        begin
            i := i + 1;
            continue;
        end

        s := 0;
        for j := i * 10 to (i + 1)*10 do
        begin
            if (j mod 2 = 0) then continue;
            s := s + j;
        end
        putInt(i);
        putString(", ");
        putInt(s);
        putLn();
        i := i + 1;
    end

end

function fact(x: integer): integer;
var i, f : integer;
begin
    f := 1;
    for i := 1 to x do f := f * i;
    return f;
end
        """
        expect = """1, 75
2, 125
3, 175
4, 225
7, 375
8, 425
9, 475
10, 525
"""
        self.assertTrue(TestCodeGen.test(input, expect, 545))

    def test_random7(self):
        input = """
procedure main();
var s, i, j : integer;
begin
    i := 1;
    putIntLn(fact(7));
end

function fact(x: integer): integer;
begin
    if x < 2 then
        return 1;
    else
    return x * fact(x - 1);
end
        """
        expect = """5040\n"""
        self.assertTrue(TestCodeGen.test(input, expect, 546))

    

    def test_random8(self):
        input = """
       procedure main();
       var x: integer;
       begin
            x := 1;
            with x : integer; do 
            begin
                x := 2;
                with x : integer; do
                begin
                    x := 3;
                    putInt(x);
                end
                putInt(x);
            end
       end
        """
        expect = """32"""
        self.assertTrue(TestCodeGen.test(input, expect, 547))

    def test_random9(self):
        input = """

    var x: integer;
    
    function foo(): boolean;
    begin
        putString("in foo");
        return false;
    end

    procedure main();
    begin
        x := 10;
        if (x > 100 and then foo()) then
            putStringLn("in then");
        else
            putStringLn("in else");
    end
        """
        expect = """in else\n"""
        self.assertTrue(TestCodeGen.test(input, expect, 548))

    def test_random10(self):
        input = """
    var x: integer;
    
    function foo(): boolean;
    begin
        putString("in foo ");
        x := 1000;
        return true;
    end

    procedure main();
    begin
        x := 10;

        if (x < 100 and then foo()) then
            putStringLn("in then");
        else
            putStringLn("in else");
    end        """
        expect = """in foo in then\n"""
        self.assertTrue(TestCodeGen.test(input, expect, 549))

    def test_random11(self):
        input = """
    var x: integer;
    
    function foo(): boolean;
    begin
        putString("in foo ");
        return false;
    end

    procedure main();
    begin
        x := 10;

        if (x < 100 and then foo()) then
            putStringLn("in then");
        else
            putStringLn("in else");
    end        """
        expect = """in foo in else\n"""
        self.assertTrue(TestCodeGen.test(input, expect, 550))

    def test_random12(self):
        input = """
    var x: integer;
    
    function foo(): boolean;
    begin
        putString("in foo ");
        x := 1000;
        return true;
    end

    procedure main();
    begin
        x := 10;

        if (x > 100 and then foo()) then
            putStringLn("in then");
        else
            putStringLn("in else");

        putIntLn(x);
    end        """
        expect = """in else\n10\n"""
        self.assertTrue(TestCodeGen.test(input, expect, 551))

    def test_random13(self):
        input = """
       function foo(): real;
       begin
            return 1;
        end

        procedure main();
        begin
            putFloat(foo());
        end
        """
        expect = """1.0"""
        self.assertTrue(TestCodeGen.test(input, expect, 552))

    def test_random14(self):
        input = """
        procedure main();
        var x, y: integer;
        begin
            x := 10;
            y := 12;
            putInt(gcd(x + y, x));
        end

        function gcd(a,b : integer): integer;
        begin
            if b = 0 then
                return a;
            else
                return gcd(b, a mod b);
        end        """
        expect = """2"""
        self.assertTrue(TestCodeGen.test(input, expect, 553))

    

    def test_random15(self):
        input = """
		procedure main();
		var x: integer;
		begin
			x := 10;
			foo(x);
			putFloat(x);
		end

		procedure foo(x: real);
		begin
			putFloat(x);
		end        """
        expect = """10.010.0"""
        self.assertTrue(TestCodeGen.test(input, expect, 554))




    

    def test_random16(self):
        input = """
        var i: integer;
        procedure main();
        begin
            foo();
            putInt(i);
        end

        procedure foo();
        begin
            i := 100;
        end
        """
        expect = """100"""
        self.assertTrue(TestCodeGen.test(input, expect, 555))

    def test_random17(self):
        input = """
        var x: integer;

        procedure main();
        var n, i, j : integer;
        begin
            n := 10;
            for i := 1 to n do
            begin
                for j := 1 to i do
                    putString("*");
                putLn();
            end
        end

        """
        expect = """*
**
***
****
*****
******
*******
********
*********
**********
"""
        self.assertTrue(TestCodeGen.test(input, expect, 556))

    

    def test_random18(self):
        input = """
        var x: integer;
        procedure main();

        begin
            for x := 0 to 0 do
                continue;
            putInt(x);

        end
        """
        expect = """1"""
        self.assertTrue(TestCodeGen.test(input, expect, 557))

    def test_random19(self):
        input = """
        function fib(x : integer):integer;
        begin
            if (x < 2) then return 1;
            return fib(x-1) + fib(x-2);
        end

        procedure main();
        var x : integer;

        begin
            putInt(fib(5));
        end
        """
        expect = """8"""
        self.assertTrue(TestCodeGen.test(input, expect, 558))

    


    def test_random20(self):
        input = """
        procedure main();
        var i, sum: integer; 
        begin

            i := 0;
            sum := 0;

            while i < 100 do begin
                sum := sum +i;
                i := i + 1;
            end

            putInt(sum);

            sum := sum + 100;

            putInt(sum);

        end
        """
        expect = """49505050"""
        self.assertTrue(TestCodeGen.test(input, expect, 559))

    def test_random21(self):
        input = """
        procedure main();
        var i, j: integer;
        begin
            i := 0;
            while i < 10 do begin
                for j := 0 to 10 do begin
                    if j mod 2 = 0 then continue;
                    putIntLn(foo(i, j));
                end
                if i > 2 then break; 
                i := i + 1;
            end
        end

        function foo(i, j: integer): integer;
        begin
            return i*10 + j;
        end
        """
        expect = """1
3
5
7
9
11
13
15
17
19
21
23
25
27
29
31
33
35
37
39
"""
        self.assertTrue(TestCodeGen.test(input, expect, 560))

    

    def test_random22(self):
        input = """
            var i : integer ;
             function f (): integer ;
             begin
             return 200;
             end
             procedure main ();
             var main : integer ;
             begin
                 main := f ();
                 putIntLn (main );
                 with
                 i : integer ;
                 main : integer ;
                 f : integer ;
                 do begin
                 main := f := i := 100;
                 putIntLn(i);
                 putIntLn(main);
                 putIntLn(f);
                 end
                 putIntLn (main);
             end
             var g : real ;
             """
        expect = "200\n100\n100\n100\n200\n"
        self.assertTrue(TestCodeGen.test(input, expect, 561))

    def test_random23(self):
        input = """
        procedure main();
        var X: integer;
        begin
            x := 12;
            putint(X);
            Foo();
        end

        procedure foo();
        begin
            putString("Hello world");
        end
        """
        expect = """12Hello world"""
        self.assertTrue(TestCodeGen.test(input, expect, 562))

    def test_random24(self):
        input = """
            var d: integer;
            procedure main();
            var a,b: boolean;
                c: String;
            begin
                a := True;
                b := False;
                c := "ahihi";
                d := 1 + 2;
                putBool(a or b and not b or False);
                putString(c);
                putInt(d);
            end
        """
        expect = "trueahihi3"
        self.assertTrue(TestCodeGen.test(input, expect, 563))

    

    def test_random25(self):
        input = """
            procedure main();
            var a: integer;
                b: real;
            begin
                a := 1;
                putInt(a);
                with a: real; b: integer; do begin
                    a := 1.5;
                    b := 1;
                    putFloat(a+b+0.15);
                end
                with a: boolean ; b: boolean; do begin
                    b := true;
                    a := b;
                    putBool(a);
                end
                a := a + 2;
                putInt(3);
            end
        """
        expect = "12.65true3"
        self.assertTrue(TestCodeGen.test(input, expect, 564))

    def test_random26(self):
        input = """
            procedure main();
            var a,i: integer;
                b: real;
            begin
                i := 8 ;
                a := 1 ;
                while (i>0) do begin
                    a := a * i;
                    i := i - 1;
                    if i = 4 then break;
                end
                putInt(a);
            end
            """
        expect = "1680"
        self.assertTrue(TestCodeGen.test(input, expect, 565))

    def test_random27(self):
        input = """
            procedure main();
            var a,b: boolean;
            begin
                a := True;
                b := False;
                putbool(a and b and then a and not b and test());
            end
            function test(): boolean;
            var a: real;
                res: boolean;
            begin
                res := false;
                a := 9.5;
                putFloat(a);
                return res;
            end
            """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input, expect, 566))

    def test_random28(self):
        input = """
            procedure main();
            var a,b: boolean;
            begin
                a := True;
                b := False;
                putBool((a or test()) or else a and not b and test());
            end
            function test(): boolean;
            var a: real;
                res: boolean;
            begin
                res := false;
                a := 9.5;
                putFloat(a);
                return res;
            end
            """
        expect = "9.5true"
        self.assertTrue(TestCodeGen.test(input, expect, 567))

    def test_random29(self):
        input = """
            procedure main();
            var a,i: integer;
                b: real;

            begin
                up := 10;
                a := 0;
                for i:=up downto 1 do begin
                    if a > 40 then continue;
                    a := a + i;
                end
                putInt(a);
            end
            var up:integer;
            """
        expect = "45"
        self.assertTrue(TestCodeGen.test(input, expect, 568))

    def test_random30(self):
        input = """
            procedure main();
            var a,b: integer;
            begin
                b := 6;
                a := factor(b);
                putInt(a);
            end
            function factor(a: integer): integer;
            begin
                if a <= 1 then
                    return 1;
                else
                    return a * factor(a-1);
            end
        """
        expect = "720"
        self.assertTrue(TestCodeGen.test(input, expect, 569))


    def test_random(self):
        input = """
            procedure main();
            var a,b: integer;
            begin
                b := 6;
                a := factor(b);
                putInt(a);
            end
            function factor(a: integer): integer;
            begin
                if a <= 1 then
                    return 1;
                else
                    return a * factor(a-1);
            end
        """
        expect = """720"""
        self.assertTrue(TestCodeGen.test(input, expect, 570))

    def test_if_empty_then(self):
        input = """
        procedure main();
        begin
            if (10 > 1) then
            begin end
            else
                putString("ABC");
        end
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 571))

    def test_for_empty_do(self):
        input = """
        procedure main();
        var i:integer;
        begin
            for i:=1 to 5 do
                begin end
            //putint(3);
        end
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 572))
    
    def test_for(self):
        input = """
        procedure main();
        var i : integer;
        begin
            for i := -5 to -1 do
                putInt(i);
        end
        """
        expect = "-5-4-3-2-1"
        self.assertTrue(TestCodeGen.test(input, expect, 573))

    def test_for1(self):
        input = """
        procedure main();
        var i : integer;
        begin
            for i := 1 to 3 do
            begin end
            putInt(i);
        end
        """
        expect = "4"
        self.assertTrue(TestCodeGen.test(input, expect, 574))

    def test_for2(self):
        input = """
        procedure main();
        var i : integer;
        begin
            for i := 9 downto 1 do
            begin
                putInt(i);
            end
        end
        """
        expect = "987654321"
        self.assertTrue(TestCodeGen.test(input, expect, 575))

    def test_for3(self):
        input = """
        procedure main();
        var i : integer;
        begin
            for i := -1 downto -4 do
            begin
                putInt(i);
            end
            putInt(i);
        end
        """
        expect = "-1-2-3-4-5"
        self.assertTrue(TestCodeGen.test(input, expect, 576))

    def test_for4(self):
        input = """
        procedure main();
        var i : integer;
        begin
            for i := 0 to 10 do
            begin
                if i mod 2 = 0 then
                    putInt(i);
            end
        end
        """
        expect = "0246810"
        self.assertTrue(TestCodeGen.test(input, expect, 577))

    def test_for5(self):
        input = """
        procedure main();
        var i,j,counter : integer;
        begin
            counter := 0;
            for i := 0 to 10 do
                for j := 0 to 10 do
                    counter := counter + 1;
            putInt(counter);
        end
        """
        expect = "121"
        self.assertTrue(TestCodeGen.test(input, expect, 578))

    def test_for6(self):
        input = """
        procedure main();
        var i,j,k,counter : integer;
        begin
            counter := 0;
            for i := 9 downto 1 do
                for j := 8 downto 1 do
                    for k:= 7 downto 1 do
                        counter := counter + 1;
            putBool(counter = 7*8*9);
        end
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 579))

    def test_for7(self):
        input = """
        procedure main();
        var i : integer;
        begin
            for i:= 10 div 10 to 9 * 19 div 10 do
                while 5 > i do
                begin
                    putInt(i);
                    i := i + 1;
                end
            putStringLn("");
            putInt(i);
        end
        """
        expect = "1234\n18"
        self.assertTrue(TestCodeGen.test(input, expect, 580))

    def test_for8(self):
        input = """
        procedure main();
        var i,j,counter : integer;
        begin
            counter := 0;
            for i:= 1 to 20000 do
                for j := 20000 downto 1 do
                    counter := counter - 1;
            putInt(counter);
        end
        """
        expect = "-400000000"
        self.assertTrue(TestCodeGen.test(input, expect, 581))

    

    def test_for9(self):
        input = """
        var i:integer;
        procedure main();
        begin
            for i:=9 downto 5 do
                if i mod 3 = 0 then
                    putfloatln(i div 3);
        end
        """
        expect = "3.0\n2.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 582))

    def test_for10(self):
        input = """
        var i:integer;
        procedure main();
        begin
            for i:=-100 to 100 do
                for i:= 0 to 100 do begin end
            putInt(i);
        end
        """
        expect = "102"
        self.assertTrue(TestCodeGen.test(input, expect, 583))

    def test_break_continue(self):
        input = """
        var i:integer;
        procedure main();
        begin
            for i:= 0 to 10 do
                if i > 5 then break;
            putIntLn(i);

            for i:= 0 to 100 do
            begin
                if i >= 10 then continue;
                else putInt(i);
            end
        end
        """
        expect = "6\n0123456789"
        self.assertTrue(TestCodeGen.test(input, expect, 584))

    def test_break_continue1(self):
        input = """
        var i,j:integer;
        procedure main();
        begin
            while TRUE do
            begin
                putStringLn("LOOPING...");
                break;
            end
            for i:= 1 to 100 do
            begin
                while not not not false do
                    break;
                for j := -9 to -1 do
                begin
                    putInt(-(j*i));
                end
                break;
            end
        end
        """
        expect = "LOOPING...\n987654321"
        self.assertTrue(TestCodeGen.test(input, expect, 585))

    def test_break_continue2(self):
        input = """
        procedure main();
        var i : integer;
        begin
            for i := -10000 to 10000 do
            begin
                if i*i > 9 then continue;
                PUTINTln(i);
            end
        end
        """
        expect = "-3\n-2\n-1\n0\n1\n2\n3\n"
        self.assertTrue(TestCodeGen.test(input, expect, 586))

    def test_break_continue3(self):
        input = """
        procedure main();
        var i: integer;
        begin
            while True do
            begin
                while true do
                begin
                    while not false do
                        break;
                    break;
                end
                break;
            end
            for i := -10000 to 10000 do
            begin
                if i*i > 9 then continue;
                PUTINTln(i);
            end
        end
        """
        expect = "-3\n-2\n-1\n0\n1\n2\n3\n"
        self.assertTrue(TestCodeGen.test(input, expect, 587))

    def test_break_continue4(self):
        input = """
        var i : integer;
        procedure main();
        begin
            for i:=90 downto 0 do
                if i mod 10 <> 0 then continue;
                else
                    putFloatLn(i / 10);
        end
        """
        expect = "9.0\n8.0\n7.0\n6.0\n5.0\n4.0\n3.0\n2.0\n1.0\n0.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 588))

    def test_return(self):
        input = """
        procedure main();
        begin
            if true then return;
            else putString("HUYTC");
        end
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 589))

    def test_return1(self):
        input = """
        function fib(n:integer):integer; //calculate the nth Fibonacci number
        begin
            if n < 0 then return -1;
            else if n = 0 then return 0;
            else if n = 1 then return 1;
            else return fib(n - 1) + fib(n - 2);
        end

        procedure main();
        var i : integer;
        begin
            putIntLn(fib(-100));
            for i := 0 to 10 do
                putIntLn(fib(i));
        end
        """
        expect = "-1\n0\n1\n1\n2\n3\n5\n8\n13\n21\n34\n55\n"
        self.assertTrue(TestCodeGen.test(input, expect, 590))

    def test_return2(self):
        input = """
        procedure foo(i:integer);
        begin
            if i >= 0 then
            begin
                putStringLn("POSITIVE");
                return;
            end
            putStringLn("NEGATIVE");
        end

        procedure main();
        begin
            foo(1);
            foo(2);
            foo(3);
            foo(-3);
            foo(-2);
            foo(0);
        end
        """
        expect = "POSITIVE\nPOSITIVE\nPOSITIVE\nNEGATIVE\nNEGATIVE\nPOSITIVE\n"
        self.assertTrue(TestCodeGen.test(input, expect, 591))

    def test_with(self):
        input = """
        procedure main();
        var i : integer;
        begin
            i := 0;
            putIntLn(i);
            with i:integer; do
            begin
                i := 8;
                putIntLn(i);
            end
            putIntLn(i);
        end
        """
        expect = "0\n8\n0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 592))

    def test_with1(self):
        input = """
        procedure main();
        var i : integer;
        begin
            i := 0;
            putIntLn(i);
            with i:real; do
            begin
                i := 8;
                putFloatLn(i);
            end
            putIntLn(i);
        end
        """
        expect = "0\n8.0\n0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 593))

    def test_with2(self):
        input = """
        var i : integer;
        procedure foo();
        begin
            i := 0;
            putint(i);
            with i:integer; do
                with f,i:real; do
                    with i:boolean; do
                    begin
                        i := 1 > -5;
                        putBool(i);
                    end
        end

        procedure main();
        var i : integer;
        begin
            i := -1;
            putint(i);
            foo();
            putint(i);
        end
        """
        expect = "-10true-1"
        self.assertTrue(TestCodeGen.test(input, expect, 594))

    def test_call(self):
        input = """
        procedure printSum(a,b,c:integer);
        begin
            putIntLn(a+b+c);
            a := 0;
            b := 0;
            c := 0;
        end

        procedure main();
        var a : integer;
        begin
            a := 1;
            printSum(a, 6, 7);
            putIntLn(a);
        end
        """
        expect = "14\n1\n"
        self.assertTrue(TestCodeGen.test(input, expect, 595))

    

    def test_call1(self):
        input = """
        function sum(a,b:integer):integer;
        begin
            return a + b;
        end

        procedure main();
        begin
            putInt(sum(1,10) - sum(10,1));
        end
        """
        expect = "0"
        self.assertTrue(TestCodeGen.test(input, expect, 596))

    

    def test_call2(self):
        input = """
        procedure print(s:string);
        begin
            putStringLn(s);
        end

        function helloWorld():String;
        begin
            return "HELLO WORLD";
        end

        procedure main();
        begin
            print("TEST");
            print(helloWorld());
        end
        """
        expect = "TEST\nHELLO WORLD\n"
        self.assertTrue(TestCodeGen.test(input, expect, 597))

    def test_call3(self):
        input = """
        function finalTest():real;
        begin
            return 420/420;
        end

        procedure main();
        begin
            putFloatLn(100*finalTest()*100 - 1e4);
        end
        """
        expect = "0.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 598))

    def test_final(self):
        input = """
        procedure main();
        var i,j,k,counter : integer;
        begin
            i := counter := 0;
            while i < 3 do
            begin
                j := 0;
                while j < 4 do
                begin
                    k := 0;
                    while k < 5 do
                    begin
                        k := k + 1;
                        counter := counter + 1;
                    end
                    j := j + 1;
                end
                i := i + 1;
            end
            putInt(counter);
        end
        """
        expect = "60"
        self.assertTrue(TestCodeGen.test(input, expect, 599))