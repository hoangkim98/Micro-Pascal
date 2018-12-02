
import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_simple_proc(self):
        input ="""procedure foo(); begin print(); end"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[CallStmt(Id(r'print'),[])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,300))

    def test_simple_var(self):
        input = """var a,b:integer; c,d:real; e:array[-1 .. 2] of boolean;
        """
        expect = str(Program([VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'c'),FloatType()),VarDecl(Id(r'd'),FloatType()),VarDecl(Id(r'e'),ArrayType(-1,2,BoolType()))]))
        self.assertTrue(TestAST.test(input,expect,301))

    def test_simple_func(self):
        input = """function foo():integer;
        begin print(); end"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[CallStmt(Id(r'print'),[])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,302))

    def test_func_with_proc(self):
        input = """function foo():integer;
        begin end
        procedure main();
        begin end"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[],IntType()),FuncDecl(Id(r'main'),[],[],[],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,303))

    def test_simple_proc_with_param(self):
        input = """procedure foo(a:integer); begin print(); end"""
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'a'),IntType())],[],[CallStmt(Id(r'print'),[])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,304))

    def test_andthen_stmt(self):
        input = """procedure foo(); begin a:= 1 and then 2 or else 3 and then 4; end"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[Assign(Id(r'a'),BinaryOp(r'andthen',BinaryOp(r'orelse',BinaryOp(r'andthen',IntLiteral(1),IntLiteral(2)),IntLiteral(3)),IntLiteral(4)))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,305))

    def test_andthen_stmt_with_compound(self):
        input = """procedure foo(); begin begin a:= 1 and then 2 or else 3 and then 4; end  end"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[Assign(Id(r'a'),BinaryOp(r'andthen',BinaryOp(r'orelse',BinaryOp(r'andthen',IntLiteral(1),IntLiteral(2)),IntLiteral(3)),IntLiteral(4)))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,306))

    def test_return_stmt(self):
        input = """procedure foo(); begin return 1; end"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[Return(IntLiteral(1))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,307))

    def test_return_stmt_with_compound(self):
        input = """procedure foo(); begin return 1; begin return; end end"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[Return(IntLiteral(1)),Return(None)],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,308))

    def test_compound_stmt(self):
        input = """procedure foo(); begin return a; end"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[Return(Id(r'a'))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,309))

    def test_with_stmt_(self):
        input = """procedure foo(); begin with a:integer;c:array[1 .. 2] of string; do print(); return a; end"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[With([VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'c'),ArrayType(1,2,StringType()))],[CallStmt(Id(r'print'),[])]),Return(Id(r'a'))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,310))

    def test_with_stmt_with_compound(self):
        input = """procedure foo(); begin with a:integer;c:array[1 .. 2] of string; do begin print(); end return a; end"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[With([VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'c'),ArrayType(1,2,StringType()))],[CallStmt(Id(r'print'),[])]),Return(Id(r'a'))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,311))

    def test_arraycell(self):
        input = """procedure foo(); begin return a[1]; a[i]:= a[i]+b[i]; end"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[Return(ArrayCell(Id(r'a'),IntLiteral(1))),Assign(ArrayCell(Id(r'a'),Id(r'i')),BinaryOp(r'+',ArrayCell(Id(r'a'),Id(r'i')),ArrayCell(Id(r'b'),Id(r'i'))))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,312))

    def test_assign_stmt(self):
        input = """procedure foo(); begin a:=b:=a[1]:=1; end"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[Assign(ArrayCell(Id(r'a'),IntLiteral(1)),IntLiteral(1)),Assign(Id(r'b'),ArrayCell(Id(r'a'),IntLiteral(1))),Assign(Id(r'a'),Id(r'b'))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,313))

    def test_assign_stmt_with_compound(self):
        input = """procedure foo(); begin begin a:=b:=a[1]:=1; end return a; end"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[Assign(ArrayCell(Id(r'a'),IntLiteral(1)),IntLiteral(1)),Assign(Id(r'b'),ArrayCell(Id(r'a'),IntLiteral(1))),Assign(Id(r'a'),Id(r'b')),Return(Id(r'a'))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,314))

    def test_call_stmt(self):
        input = """procedure foo(); begin foo(); print(1+1,2); end"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[CallStmt(Id(r'foo'),[]),CallStmt(Id(r'print'),[BinaryOp(r'+',IntLiteral(1),IntLiteral(1)),IntLiteral(2)])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,315))

    def test_call_stmt_with_compound(self):
        input = """procedure foo(); begin foo(); begin print(1+1,2);end end"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[CallStmt(Id(r'foo'),[]),CallStmt(Id(r'print'),[BinaryOp(r'+',IntLiteral(1),IntLiteral(1)),IntLiteral(2)])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,316))

    def test_funcall(self):
        input = """procedure foo(); begin return foo(1+1,2); end"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[Return(CallExpr(Id(r'foo'),[BinaryOp(r'+',IntLiteral(1),IntLiteral(1)),IntLiteral(2)]))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,317))

    def test_if_with_compound(self):
        input = """procedure foo(); begin if a>b then begin b:=1; end else begin a:=2; end end"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[If(BinaryOp(r'>',Id(r'a'),Id(r'b')),[Assign(Id(r'b'),IntLiteral(1))],[Assign(Id(r'a'),IntLiteral(2))])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,318))

    def test_if(self):
        input = """procedure foo(); begin if a>b then b:=1; else  a:=2;  end"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[If(BinaryOp(r'>',Id(r'a'),Id(r'b')),[Assign(Id(r'b'),IntLiteral(1))],[Assign(Id(r'a'),IntLiteral(2))])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,319))

    def test_while_with_compound(self):
        input = """procedure foo(); begin while a>1 do begin print(); begin return a;end end  end"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[While(BinaryOp(r'>',Id(r'a'),IntLiteral(1)),[CallStmt(Id(r'print'),[]),Return(Id(r'a'))])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,320))

    def test_while(self):
        input = """procedure foo(); begin while a>1 do print(); return a;  end"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[While(BinaryOp(r'>',Id(r'a'),IntLiteral(1)),[CallStmt(Id(r'print'),[])]),Return(Id(r'a'))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,321))

    def test_for(self):
        input = """procedure foo(); begin for a:=1 to 10 do return a;end"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[For(Id(r'a'),IntLiteral(1),IntLiteral(10),True,[Return(Id(r'a'))])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,322))

    def test_for_with_compound(self):
        input = """procedure foo(); begin for a:=1 to 10 do begin return a;end end"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[For(Id(r'a'),IntLiteral(1),IntLiteral(10),True,[Return(Id(r'a'))])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,323))

    def test_complete_func(self):
        input = """function foo(a:integer):array[1 .. 2] of real;
        var x,y:array[1 .. 2] of real;
        begin print(a,b); end"""
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'a'),IntType())],[VarDecl(Id(r'x'),ArrayType(1,2,FloatType())),VarDecl(Id(r'y'),ArrayType(1,2,FloatType()))],[CallStmt(Id(r'print'),[Id(r'a'),Id(r'b')])],ArrayType(1,2,FloatType()))]))
        self.assertTrue(TestAST.test(input,expect,324))

    def test_complete_proc(self):
        input = """
        procedure foo(a:integer);
        var x,y:array[1 .. 2] of real;
        begin print(a,b);return a; end"""
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'a'),IntType())],[VarDecl(Id(r'x'),ArrayType(1,2,FloatType())),VarDecl(Id(r'y'),ArrayType(1,2,FloatType()))],[CallStmt(Id(r'print'),[Id(r'a'),Id(r'b')]),Return(Id(r'a'))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,325))

    def test_break(self):
        input = """function foo():real;
        var x,y:real;
        begin break; end"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[VarDecl(Id(r'x'),FloatType()),VarDecl(Id(r'y'),FloatType())],[Break()],FloatType())]))
        self.assertTrue(TestAST.test(input,expect,326))

    def test_continue(self):
        input = """function foo():real;
        var x,y:real;
        begin continue; end"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[VarDecl(Id(r'x'),FloatType()),VarDecl(Id(r'y'),FloatType())],[Continue()],FloatType())]))
        self.assertTrue(TestAST.test(input,expect,327))

    def test_assign_stm_with_expression_andthen(self):
        input = """
        function foo(): integer;
        var a: array [1 .. 10] of integer;
        begin
            x := a[1] and then a[2];
        end
        """
        expect = str(Program([FuncDecl(Id(r'foo'),[],[VarDecl(Id(r'a'),ArrayType(1,10,IntType()))],[Assign(Id(r'x'),BinaryOp(r'andthen',ArrayCell(Id(r'a'),IntLiteral(1)),ArrayCell(Id(r'a'),IntLiteral(2))))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,328))

    def test_assign_stm_with_expression_orelse(self):
        input = """
        function foo(): integer;
        var a: array [1 .. 10] of integer;
        begin
            a[1] := 1;
            a[5] := 0 OR ELSE a[1];
        end
        """
        expect = str(Program([FuncDecl(Id(r'foo'),[],[VarDecl(Id(r'a'),ArrayType(1,10,IntType()))],[Assign(ArrayCell(Id(r'a'),IntLiteral(1)),IntLiteral(1)),Assign(ArrayCell(Id(r'a'),IntLiteral(5)),BinaryOp(r'orelse',IntLiteral(0),ArrayCell(Id(r'a'),IntLiteral(1))))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,329))

    def test_assign_stm_with_expression_EQ(self):
        input = """
        function foo(): integer;
        begin
            x := (9 = 5);
        end
        """
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[Assign(Id(r'x'),BinaryOp(r'=',IntLiteral(9),IntLiteral(5)))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,330))

    def test_assign_stm_with_expression_NEQ(self):
        input = """
        function foo(): integer;
        begin
            x := (TRUE <> false);
        end
        """
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[Assign(Id(r'x'),BinaryOp(r'<>',BooleanLiteral(True),BooleanLiteral(False)))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,331))

    def test_assign_stm_with_expression_LESS(self):
        input = """
        function foo(): integer;
        begin
            x := (9 < 5);
        end
        """
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[Assign(Id(r'x'),BinaryOp(r'<',IntLiteral(9),IntLiteral(5)))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,332))

    def test_assign_stm_with_expression_GREATER(self):
        input = """
        function foo(): integer;
        begin
            x := (9 > 5);
        end
        """
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[Assign(Id(r'x'),BinaryOp(r'>',IntLiteral(9),IntLiteral(5)))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,333))

    def test_assign_stm_with_expression_LESS_or_EQ(self):
        input = """
        function foo(): integer;
        begin
            x := (y <= z);
        end
        """
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[Assign(Id(r'x'),BinaryOp(r'<=',Id(r'y'),Id(r'z')))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,334))

    def test_assign_stm_with_expression_GREATER_or_EQ(self):
        input = """
        function foo(): integer;
        begin
            x := (x >= arr[2]);
        end
        """
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[Assign(Id(r'x'),BinaryOp(r'>=',Id(r'x'),ArrayCell(Id(r'arr'),IntLiteral(2))))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,335))

    def test_assign_stm_with_expression_ADD(self):
        input = """
        function foo(): integer;
        begin
            x := (1+1)+1;
        end
        """
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[Assign(Id(r'x'),BinaryOp(r'+',BinaryOp(r'+',IntLiteral(1),IntLiteral(1)),IntLiteral(1)))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,336))

    def test_assign_stm_with_expression_SUB(self):
        input = """
        function foo(): integer;
        begin
            x := 2.5-0.5;
        end
        """
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[Assign(Id(r'x'),BinaryOp(r'-',FloatLiteral(2.5),FloatLiteral(0.5)))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,337))

    def test_assign_stm_with_expression_minus_number(self):
        input = """
        function foo(): integer;
        begin
            x := -1;
            y := -x;
        end
        """
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[Assign(Id(r'x'),UnaryOp(r'-',IntLiteral(1))),Assign(Id(r'y'),UnaryOp(r'-',Id(r'x')))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,338))

    def test_assign_stm_with_expression_NOT(self):
        input = """
        function foo(): integer;
        begin
            x := not y and z;
        end
        """
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[Assign(Id(r'x'),BinaryOp(r'and',UnaryOp(r'not',Id(r'y')),Id(r'z')))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,339))

    def test_assign_stm_with_functioncall_without_param(self):
        input = """
        function foo(): integer;
        begin
            x := foo() + 1;
        end
        """
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[Assign(Id(r'x'),BinaryOp(r'+',CallExpr(Id(r'foo'),[]),IntLiteral(1)))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,340))

    def test_assign_stm_with_functioncall_with_one_param(self):
        input = """
        function foo(): integer;
        begin
            x := foo(123) + 1;
        end
        """
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[Assign(Id(r'x'),BinaryOp(r'+',CallExpr(Id(r'foo'),[IntLiteral(123)]),IntLiteral(1)))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,341))

    def test_assign_stm_with_functioncall_with_many_param(self):
        input = """
        function foo(): integer;
        begin
            x := range(10,0,-2) + 1;
        end
        """
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[Assign(Id(r'x'),BinaryOp(r'+',CallExpr(Id(r'range'),[IntLiteral(10),IntLiteral(0),UnaryOp(r'-',IntLiteral(2))]),IntLiteral(1)))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,342))

    def test_assign_stm_MP_document_example(self):
        input = """
        function foo(): integer;
        begin
            a := b[10] := foo()[3] := x := 1+1;
        end
        """
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[Assign(Id(r'x'),BinaryOp(r'+',IntLiteral(1),IntLiteral(1))),Assign(ArrayCell(CallExpr(Id(r'foo'),[]),IntLiteral(3)),Id(r'x')),Assign(ArrayCell(Id(r'b'),IntLiteral(10)),ArrayCell(CallExpr(Id(r'foo'),[]),IntLiteral(3))),Assign(Id(r'a'),ArrayCell(Id(r'b'),IntLiteral(10)))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,343))

    def test_assign_stm_with_expression_OR(self):
        input = """
        function foo(): integer;
        begin
            x := y1 OR z2;
        end
        """
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[Assign(Id(r'x'),BinaryOp(r'OR',Id(r'y1'),Id(r'z2')))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,344))

    def test_assign_stm_with_expression_DIV_and_ADD(self):
        input = """
        function foo(): integer;
        begin
            y := x/2 + 1;
        end
        """
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[Assign(Id(r'y'),BinaryOp(r'+',BinaryOp(r'/',Id(r'x'),IntLiteral(2)),IntLiteral(1)))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,345))

    def test_assign_stm_with_expression_MUL_and_SUB(self):
        input = """
        function foo(): integer;
        begin
            y := x*x - 1;
        end
        """
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[Assign(Id(r'y'),BinaryOp(r'-',BinaryOp(r'*',Id(r'x'),Id(r'x')),IntLiteral(1)))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,346))

    def test_assign_stm_with_expression_INT_DIV_and_MOD(self):
        input = """
        function foo(): integer;
        begin
            x := 4 div 3;
            y := 4 mOd 3;
        end
        """
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[Assign(Id(r'x'),BinaryOp(r'div',IntLiteral(4),IntLiteral(3))),Assign(Id(r'y'),BinaryOp(r'mOd',IntLiteral(4),IntLiteral(3)))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,347))

    def test_assign_stm_with_expression_many_and_or(self):
        input = """
        function foo(): integer;
        begin
            x := true and false or false or true;
        end
        """
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[Assign(Id(r'x'),BinaryOp(r'or',BinaryOp(r'or',BinaryOp(r'and',BooleanLiteral(True),BooleanLiteral(False)),BooleanLiteral(False)),BooleanLiteral(True)))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,348))

    def test_many_function_and_procedure_decls(self):
        input = """
        var a,b: integer;
        procedure foo(a:integer);
        begin
            if(goo(a,b) = TRUE) then
                return;
            else a := a - b;
        end
        function goo(a,b:integer): BOOLEAN;
        begin
            return a >  0;
        END
        """
        expect = str(Program([VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType()),FuncDecl(Id(r'foo'),[VarDecl(Id(r'a'),IntType())],[],[If(BinaryOp(r'=',CallExpr(Id(r'goo'),[Id(r'a'),Id(r'b')]),BooleanLiteral(True)),[Return(None)],[Assign(Id(r'a'),BinaryOp(r'-',Id(r'a'),Id(r'b')))])],VoidType()),FuncDecl(Id(r'goo'),[VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType())],[],[Return(BinaryOp(r'>',Id(r'a'),IntLiteral(0)))],BoolType())]))
        self.assertTrue(TestAST.test(input,expect,349))

    def test_test_complex_program(self):
        input = """
        var i:integer;
            j,k:real;
        procedure main();
        begin
        end
        """
        expect = str(Program([VarDecl(Id(r'i'),IntType()),VarDecl(Id(r'j'),FloatType()),VarDecl(Id(r'k'),FloatType()),FuncDecl(Id(r'main'),[],[],[],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,350))

    def test_test_complex_program_minus_index_array(self):
        input = """
        var i:array [-3 .. -2] of integer;
        procedure main();
        begin
        end
        var j,x:array [-1 .. -2] of string;
        """
        expect = str(Program([VarDecl(Id(r'i'),ArrayType(-3,-2,IntType())),FuncDecl(Id(r'main'),[],[],[],VoidType()),VarDecl(Id(r'j'),ArrayType(-1,-2,StringType())),VarDecl(Id(r'x'),ArrayType(-1,-2,StringType()))]))
        self.assertTrue(TestAST.test(input,expect,351))

    def test_test_complex_program_many_variables_declares(self):
        input = """
        procedure main(a:INTEGER;b:real;c:real;d:boolean;e:boolean;f:boolean);
        var b:rEAL;c:boolean;d:boolean;
            e,f,h:array[1 .. 2] of real;
        begin
        end
        """
        expect = str(Program([FuncDecl(Id(r'main'),[VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),FloatType()),VarDecl(Id(r'c'),FloatType()),VarDecl(Id(r'd'),BoolType()),VarDecl(Id(r'e'),BoolType()),VarDecl(Id(r'f'),BoolType())],[VarDecl(Id(r'b'),FloatType()),VarDecl(Id(r'c'),BoolType()),VarDecl(Id(r'd'),BoolType()),VarDecl(Id(r'e'),ArrayType(1,2,FloatType())),VarDecl(Id(r'f'),ArrayType(1,2,FloatType())),VarDecl(Id(r'h'),ArrayType(1,2,FloatType()))],[],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,352))

    def test_test_complex_program_with_in_compound_stmt(self):
        input = """
        procedure main();
        begin
        	with a:real;b,c:boolean;d:INTEGER; do begin
        		with a:integer; do begin end
        		with b:real;c,d:integer; do begin end
        	end
        end
        """
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[With([VarDecl(Id(r'a'),FloatType()),VarDecl(Id(r'b'),BoolType()),VarDecl(Id(r'c'),BoolType()),VarDecl(Id(r'd'),IntType())],[With([VarDecl(Id(r'a'),IntType())],[]),With([VarDecl(Id(r'b'),FloatType()),VarDecl(Id(r'c'),IntType()),VarDecl(Id(r'd'),IntType())],[])])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,353))

    def test_if_stm_with_expression_andthen(self):
        input = """
        function foo(): integer;
        var a: array [1 .. 10] of integer;
        begin
            if a[1] and then a[2] then print();
        end
        """
        expect = str(Program([FuncDecl(Id(r'foo'),[],[VarDecl(Id(r'a'),ArrayType(1,10,IntType()))],[If(BinaryOp(r'andthen',ArrayCell(Id(r'a'),IntLiteral(1)),ArrayCell(Id(r'a'),IntLiteral(2))),[CallStmt(Id(r'print'),[])],[])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,354))

    def test_if_stm_with_expression_orelse(self):
        input = """
        function foo(): integer;
        var a: array [1 .. 10] of integer;
        begin
            a[1] := 1;
            if 0 OR ELSE a[1] then foo();
        end
        """
        expect = str(Program([FuncDecl(Id(r'foo'),[],[VarDecl(Id(r'a'),ArrayType(1,10,IntType()))],[Assign(ArrayCell(Id(r'a'),IntLiteral(1)),IntLiteral(1)),If(BinaryOp(r'orelse',IntLiteral(0),ArrayCell(Id(r'a'),IntLiteral(1))),[CallStmt(Id(r'foo'),[])],[])],IntType())])) 
        self.assertTrue(TestAST.test(input,expect,355))

    def test_if_stm_with_expression_EQ(self):
        input = """
        function foo(): integer;
        begin
            if (9 = 5) then foo();
        end
        """
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[If(BinaryOp(r'=',IntLiteral(9),IntLiteral(5)),[CallStmt(Id(r'foo'),[])],[])],IntType())])) 
        self.assertTrue(TestAST.test(input,expect,356))

    def test_if_stm_with_expression_NEQ(self):
        input = """
        function foo(): integer;
        begin
            if (TRUE <> false) then foo();
        end
        """
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[If(BinaryOp(r'<>',BooleanLiteral(True),BooleanLiteral(False)),[CallStmt(Id(r'foo'),[])],[])],IntType())])) 
        self.assertTrue(TestAST.test(input,expect,357))

    def test_if_stm_with_expression_LESS(self):
        input = """
        function foo(): integer;
        begin
            if (9 < 5) then foo();
        end
        """
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[If(BinaryOp(r'<',IntLiteral(9),IntLiteral(5)),[CallStmt(Id(r'foo'),[])],[])],IntType())])) 
        self.assertTrue(TestAST.test(input,expect,358))

    def test_if_stm_with_expression_GREATER(self):
        input = """
        function foo(): integer;
        begin
            if (9 > 5) then foo();
        end
        """
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[If(BinaryOp(r'>',IntLiteral(9),IntLiteral(5)),[CallStmt(Id(r'foo'),[])],[])],IntType())])) 
        self.assertTrue(TestAST.test(input,expect,359))

    def test_if_stm_with_expression_LESS_or_EQ(self):
        input = """
        function foo(): integer;
        begin
            if (y <= z) then foo();
        end
        """
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[If(BinaryOp(r'<=',Id(r'y'),Id(r'z')),[CallStmt(Id(r'foo'),[])],[])],IntType())])) 
        self.assertTrue(TestAST.test(input,expect,360))

    def test_if_stm_with_expression_GREATER_or_EQ(self):
        input = """
        function foo(): integer;
        begin
            if (x >= arr[2]) then foo();
        end
        """
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[If(BinaryOp(r'>=',Id(r'x'),ArrayCell(Id(r'arr'),IntLiteral(2))),[CallStmt(Id(r'foo'),[])],[])],IntType())])) 
        self.assertTrue(TestAST.test(input,expect,361))

    def test_if_stm_with_expression_ADD(self):
        input = """
        function foo(): integer;
        begin
            if (1+1)+1 then foo();
        end
        """
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[If(BinaryOp(r'+',BinaryOp(r'+',IntLiteral(1),IntLiteral(1)),IntLiteral(1)),[CallStmt(Id(r'foo'),[])],[])],IntType())])) 
        self.assertTrue(TestAST.test(input,expect,362))

    def test_if_stm_with_expression_SUB(self):
        input = """
        function foo(): integer;
        begin
            if 2.5-0.5 then foo();
        end
        """
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[If(BinaryOp(r'-',FloatLiteral(2.5),FloatLiteral(0.5)),[CallStmt(Id(r'foo'),[])],[])],IntType())])) 
        self.assertTrue(TestAST.test(input,expect,363))

    def test_if_stm_with_expression_minus_number(self):
        input = """
        function foo(): integer;
        begin
            if -1 then foo();
            y := -x;
        end
        """
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[If(UnaryOp(r'-',IntLiteral(1)),[CallStmt(Id(r'foo'),[])],[]),Assign(Id(r'y'),UnaryOp(r'-',Id(r'x')))],IntType())])) 
        self.assertTrue(TestAST.test(input,expect,364))

    def test_if_stm_with_expression_NOT(self):
        input = """
        function foo(): integer;
        begin
            if not y and z then foo();
        end
        """
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[If(BinaryOp(r'and',UnaryOp(r'not',Id(r'y')),Id(r'z')),[CallStmt(Id(r'foo'),[])],[])],IntType())])) 
        self.assertTrue(TestAST.test(input,expect,365))

    def test_if_stm_with_functioncall_without_param(self):
        input = """
        function foo(): integer;
        begin
            if foo() + 1 then foo();
        end
        """
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[If(BinaryOp(r'+',CallExpr(Id(r'foo'),[]),IntLiteral(1)),[CallStmt(Id(r'foo'),[])],[])],IntType())])) 
        self.assertTrue(TestAST.test(input,expect,366))

    def test_if_stm_with_functioncall_with_one_param(self):
        input = """
        function foo(): integer;
        begin
            if foo(123) + 1 then foo();
        end
        """
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[If(BinaryOp(r'+',CallExpr(Id(r'foo'),[IntLiteral(123)]),IntLiteral(1)),[CallStmt(Id(r'foo'),[])],[])],IntType())])) 
        self.assertTrue(TestAST.test(input,expect,367))

    def test_if_stm_with_functioncall_with_many_param(self):
        input = """
        function foo(): integer;
        begin
            if range(10,0,-2) + 1 then foo();
        end
        """
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[If(BinaryOp(r'+',CallExpr(Id(r'range'),[IntLiteral(10),IntLiteral(0),UnaryOp(r'-',IntLiteral(2))]),IntLiteral(1)),[CallStmt(Id(r'foo'),[])],[])],IntType())])) 
        self.assertTrue(TestAST.test(input,expect,368))

    def test_if_stm_with_expression_OR(self):
        input = """
        function foo(): integer;
        begin
            if y1 OR z2 then foo();
        end
        """
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[If(BinaryOp(r'OR',Id(r'y1'),Id(r'z2')),[CallStmt(Id(r'foo'),[])],[])],IntType())])) 
        self.assertTrue(TestAST.test(input,expect,369))

    def test_if_stm_with_expression_DIV_and_ADD(self):
        input = """
        function foo(): integer;
        begin
            if x/2 + 1 then foo();
        end
        """
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[If(BinaryOp(r'+',BinaryOp(r'/',Id(r'x'),IntLiteral(2)),IntLiteral(1)),[CallStmt(Id(r'foo'),[])],[])],IntType())])) 
        self.assertTrue(TestAST.test(input,expect,370))

    def test_if_stm_with_expression_MUL_and_SUB(self):
        input = """
        function foo(): integer;
        begin
            if x*x - 1 then foo();
        end
        """
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[If(BinaryOp(r'-',BinaryOp(r'*',Id(r'x'),Id(r'x')),IntLiteral(1)),[CallStmt(Id(r'foo'),[])],[])],IntType())])) 
        self.assertTrue(TestAST.test(input,expect,371))

    def test_if_stm_with_expression_INT_DIV_and_MOD(self):
        input = """
        function foo(): integer;
        begin
            if 4 div 3 then foo();
            y := 4 mOd 3;
        end
        """
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[If(BinaryOp(r'div',IntLiteral(4),IntLiteral(3)),[CallStmt(Id(r'foo'),[])],[]),Assign(Id(r'y'),BinaryOp(r'mOd',IntLiteral(4),IntLiteral(3)))],IntType())])) 
        self.assertTrue(TestAST.test(input,expect,372))

    def test_if_stm_with_expression_many_and_or(self):
        input = """
        function foo(): integer;
        begin
            if true and false or false or true then foo();
        end
        """
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[If(BinaryOp(r'or',BinaryOp(r'or',BinaryOp(r'and',BooleanLiteral(True),BooleanLiteral(False)),BooleanLiteral(False)),BooleanLiteral(True)),[CallStmt(Id(r'foo'),[])],[])],IntType())])) 
        self.assertTrue(TestAST.test(input,expect,373))

    def test_while_stm_with_expression_andthen(self):
        input = """
        function foo(): integer;
        var a: array [1 .. 10] of integer;
        begin
            while a[1] and then a[2] do print();
        end
        """
        expect = str(Program([FuncDecl(Id(r'foo'),[],[VarDecl(Id(r'a'),ArrayType(1,10,IntType()))],[While(BinaryOp(r'andthen',ArrayCell(Id(r'a'),IntLiteral(1)),ArrayCell(Id(r'a'),IntLiteral(2))),[CallStmt(Id(r'print'),[])])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,374))

    def test_while_stm_with_expression_orelse(self):
        input = """
        function foo(): integer;
        var a: array [1 .. 10] of integer;
        begin
            a[1] := 1;
            while 0 OR ELSE a[1] do foo();
        end
        """
        expect = str(Program([FuncDecl(Id(r'foo'),[],[VarDecl(Id(r'a'),ArrayType(1,10,IntType()))],[Assign(ArrayCell(Id(r'a'),IntLiteral(1)),IntLiteral(1)),While(BinaryOp(r'orelse',IntLiteral(0),ArrayCell(Id(r'a'),IntLiteral(1))),[CallStmt(Id(r'foo'),[])])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,375))

    def test_while_stm_with_expression_EQ(self):
        input = """
        function foo(): integer;
        begin
            while (9 = 5) do foo();
        end
        """
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[While(BinaryOp(r'=',IntLiteral(9),IntLiteral(5)),[CallStmt(Id(r'foo'),[])])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,376))

    def test_while_stm_with_expression_NEQ(self):
        input = """
        function foo(): integer;
        begin
            while (TRUE <> false) do foo();
        end
        """
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[While(BinaryOp(r'<>',BooleanLiteral(True),BooleanLiteral(False)),[CallStmt(Id(r'foo'),[])])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,377))

    def test_while_stm_with_expression_LESS(self):
        input = """
        function foo(): integer;
        begin
            while (9 < 5) do foo();
        end
        """
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[While(BinaryOp(r'<',IntLiteral(9),IntLiteral(5)),[CallStmt(Id(r'foo'),[])])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,378))

    def test_while_stm_with_expression_GREATER(self):
        input = """
        function foo(): integer;
        begin
            while (9 > 5) do foo();
        end
        """
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[While(BinaryOp(r'>',IntLiteral(9),IntLiteral(5)),[CallStmt(Id(r'foo'),[])])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,379))

    def test_while_stm_with_expression_LESS_or_EQ(self):
        input = """
        function foo(): integer;
        begin
            while (y <= z) do foo();
        end
        """
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[While(BinaryOp(r'<=',Id(r'y'),Id(r'z')),[CallStmt(Id(r'foo'),[])])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,380))

    def test_while_stm_with_expression_GREATER_or_EQ(self):
        input = """
        function foo(): integer;
        begin
            while(x >= arr[2]) do foo();
        end
        """
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[While(BinaryOp(r'>=',Id(r'x'),ArrayCell(Id(r'arr'),IntLiteral(2))),[CallStmt(Id(r'foo'),[])])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,381))

    def test_while_stm_with_expression_ADD(self):
        input = """
        function foo(): integer;
        begin
            while (1+1)+1 do foo();
        end
        """
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[While(BinaryOp(r'+',BinaryOp(r'+',IntLiteral(1),IntLiteral(1)),IntLiteral(1)),[CallStmt(Id(r'foo'),[])])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,382))

    def test_while_stm_with_expression_SUB(self):
        input = """
        function foo(): integer;
        begin
            while 2.5-0.5 do foo();
        end
        """
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[While(BinaryOp(r'-',FloatLiteral(2.5),FloatLiteral(0.5)),[CallStmt(Id(r'foo'),[])])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,383))

    def test_while_stm_with_expression_minus_number(self):
        input = """
        function foo(): integer;
        begin
            while -1 do foo();
            y := -x;
        end
        """
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[While(UnaryOp(r'-',IntLiteral(1)),[CallStmt(Id(r'foo'),[])]),Assign(Id(r'y'),UnaryOp(r'-',Id(r'x')))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,384))

    def test_while_stm_with_expression_NOT(self):
        input = """
        function foo(): integer;
        begin
            while not y and z do foo();
        end
        """
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[While(BinaryOp(r'and',UnaryOp(r'not',Id(r'y')),Id(r'z')),[CallStmt(Id(r'foo'),[])])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,385))

    def test_while_stm_with_functioncall_without_param(self):
        input = """
        function foo(): integer;
        begin
            while foo() + 1 do foo();
        end
        """
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[While(BinaryOp(r'+',CallExpr(Id(r'foo'),[]),IntLiteral(1)),[CallStmt(Id(r'foo'),[])])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,386))

    def test_while_stm_with_functioncall_with_one_param(self):
        input = """
        function foo(): integer;
        begin
            while foo(123) + 1 do foo();
        end
        """
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[While(BinaryOp(r'+',CallExpr(Id(r'foo'),[IntLiteral(123)]),IntLiteral(1)),[CallStmt(Id(r'foo'),[])])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,387))

    def test_while_stm_with_functioncall_with_many_param(self):
        input = """
        function foo(): integer;
        begin
            while range(10,0,-2) + 1 do foo();
        end
        """
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[While(BinaryOp(r'+',CallExpr(Id(r'range'),[IntLiteral(10),IntLiteral(0),UnaryOp(r'-',IntLiteral(2))]),IntLiteral(1)),[CallStmt(Id(r'foo'),[])])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,388))

    def test_while_stm_with_expression_OR(self):
        input = """
        function foo(): integer;
        begin
            while y1 OR z2 do foo();
        end
        """
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[While(BinaryOp(r'OR',Id(r'y1'),Id(r'z2')),[CallStmt(Id(r'foo'),[])])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,389))

    def test_while_stm_with_expression_DIV_and_ADD(self):
        input = """
        function foo(): integer;
        begin
            while x/2 + 1 do foo();
        end
        """
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[While(BinaryOp(r'+',BinaryOp(r'/',Id(r'x'),IntLiteral(2)),IntLiteral(1)),[CallStmt(Id(r'foo'),[])])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,390))

    def test_while_stm_with_expression_MUL_and_SUB(self):
        input = """
        function foo(): integer;
        begin
            while x*x - 1 do foo();
        end
        """
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[While(BinaryOp(r'-',BinaryOp(r'*',Id(r'x'),Id(r'x')),IntLiteral(1)),[CallStmt(Id(r'foo'),[])])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,391))

    def test_while_stm_with_expression_INT_DIV_and_MOD(self):
        input = """
        function foo(): integer;
        begin
            while 4 div 3 do foo();
            y := 4 mOd 3;
        end
        """
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[While(BinaryOp(r'div',IntLiteral(4),IntLiteral(3)),[CallStmt(Id(r'foo'),[])]),Assign(Id(r'y'),BinaryOp(r'mOd',IntLiteral(4),IntLiteral(3)))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,392))

    def test_while_stm_with_expression_many_and_or(self):
        input = """
        function foo(): integer;
        begin
            while true and false or false or true do foo();
        end
        """
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[While(BinaryOp(r'or',BinaryOp(r'or',BinaryOp(r'and',BooleanLiteral(True),BooleanLiteral(False)),BooleanLiteral(False)),BooleanLiteral(True)),[CallStmt(Id(r'foo'),[])])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,393))

    def test_float(self):
        input = """
        function foo(): integer;
        begin
            a:= 12.e3 + 12.e3 -3.E1;
        end
        """
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[Assign(Id(r'a'),BinaryOp(r'-',BinaryOp(r'+',FloatLiteral(12000.0),FloatLiteral(12000.0)),FloatLiteral(30.0)))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,394))
    
    def test_many_float(self):
        input = """procedure a();
        begin
            a:=2.3;
            b:=4.5E2;
            c:=-3.2e-5;
            d:=.2E3;
            e:=2.;
            f:=2.E2;
            g:=-.9;
        end
        """
        expect = str(Program([FuncDecl(Id(r'a'),[],[],[Assign(Id(r'a'),FloatLiteral(2.3)),Assign(Id(r'b'),FloatLiteral(450.0)),Assign(Id(r'c'),UnaryOp(r'-',FloatLiteral(3.2e-05))),Assign(Id(r'd'),FloatLiteral(200.0)),Assign(Id(r'e'),FloatLiteral(2.0)),Assign(Id(r'f'),FloatLiteral(200.0)),Assign(Id(r'g'),UnaryOp(r'-',FloatLiteral(0.9)))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,395))

    def test_ambiguous_if(self):
        """Test ambiguous if"""
        input = """
        procedure abc();
        begin
            if a=4 then
                if a=2 then c:=7;
                else w:=3;
        end
        """
        expect = str(Program([FuncDecl(Id(r'abc'),[],[],[If(BinaryOp(r'=',Id(r'a'),IntLiteral(4)),[If(BinaryOp(r'=',Id(r'a'),IntLiteral(2)),[Assign(Id(r'c'),IntLiteral(7))],[Assign(Id(r'w'),IntLiteral(3))])],[])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,396))

    def test__more_complex_program(self):
        input = """
        VAR First,  Second, Left, Right: BOOLEAN;
        PROCEDURE  printBo2ol(Val: BOOLEAN);
        BEGIN
        IF Val THEN
        print("TRUE ");
        ELSE
        print("FALSE ");
        END { printBool  }
        PROCEDURE Main();
        BEGIN
        { print Header }
        print("Proof  of DeMorgan theorem ");
        print();
        print("First  Second Left Right ");
        print("-----  ------ ----- ----- ");
        { Loop through  all truth value combinations }
        FOR f :=  FALSE TO TRUE DO
        FOR g :=  FALSE TO TRUE DO BEGIN
        { print out  Input values of First, Second }
        printBool(2);
        printBool(e);
        { Separate Input  values from the output }
        print(" ");
        d := (NOT  e) div (NOT 2);
        w := NOT(e mod 2);
        { print out the  new values of Left, Right }
        printBool(2);
        printBool(e);
        print();
        END { Inner FOR  }
        END { TruthTable2  }
        """
        expect = str(Program([VarDecl(Id(r'First'),BoolType()),VarDecl(Id(r'Second'),BoolType()),VarDecl(Id(r'Left'),BoolType()),VarDecl(Id(r'Right'),BoolType()),FuncDecl(Id(r'printBo2ol'),[VarDecl(Id(r'Val'),BoolType())],[],[If(Id(r'Val'),[CallStmt(Id(r'print'),[StringLiteral(r'TRUE ')])],[CallStmt(Id(r'print'),[StringLiteral(r'FALSE ')])])],VoidType()),FuncDecl(Id(r'Main'),[],[],[CallStmt(Id(r'print'),[StringLiteral(r'Proof  of DeMorgan theorem ')]),CallStmt(Id(r'print'),[]),CallStmt(Id(r'print'),[StringLiteral(r'First  Second Left Right ')]),CallStmt(Id(r'print'),[StringLiteral(r'-----  ------ ----- ----- ')]),For(Id(r'f'),BooleanLiteral(False),BooleanLiteral(True),True,[For(Id(r'g'),BooleanLiteral(False),BooleanLiteral(True),True,[CallStmt(Id(r'printBool'),[IntLiteral(2)]),CallStmt(Id(r'printBool'),[Id(r'e')]),CallStmt(Id(r'print'),[StringLiteral(r' ')]),Assign(Id(r'd'),BinaryOp(r'div',UnaryOp(r'NOT',Id(r'e')),UnaryOp(r'NOT',IntLiteral(2)))),Assign(Id(r'w'),UnaryOp(r'NOT',BinaryOp(r'mod',Id(r'e'),IntLiteral(2)))),CallStmt(Id(r'printBool'),[IntLiteral(2)]),CallStmt(Id(r'printBool'),[Id(r'e')]),CallStmt(Id(r'print'),[])])])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,397))

    def test_quicksort(self):
        input = """    
              procedure sort(l,r: integer);
                var i,j,x,y: integer;
                begin
                  i:=l;
                  j:=r;
                  x:=a[(l+r) div 2];
                  while (i<=j) do
                  begin
                    while a[i]<x do inc(i);
                    while x<a[j] do dec(j);
                    if not(i>j) then
                      begin
                        y:=a[i];
                        a[i]:=a[j];
                        a[j]:=y;
                        inc(i);
                        j:=j-1;
                      end
                  end
                  if l<j then sort(l,j);
                  if i<r then sort(i,r);
                end
            """
        expect = str(Program([FuncDecl(Id(r'sort'),[VarDecl(Id(r'l'),IntType()),VarDecl(Id(r'r'),IntType())],[VarDecl(Id(r'i'),IntType()),VarDecl(Id(r'j'),IntType()),VarDecl(Id(r'x'),IntType()),VarDecl(Id(r'y'),IntType())],[Assign(Id(r'i'),Id(r'l')),Assign(Id(r'j'),Id(r'r')),Assign(Id(r'x'),ArrayCell(Id(r'a'),BinaryOp(r'div',BinaryOp(r'+',Id(r'l'),Id(r'r')),IntLiteral(2)))),While(BinaryOp(r'<=',Id(r'i'),Id(r'j')),[While(BinaryOp(r'<',ArrayCell(Id(r'a'),Id(r'i')),Id(r'x')),[CallStmt(Id(r'inc'),[Id(r'i')])]),While(BinaryOp(r'<',Id(r'x'),ArrayCell(Id(r'a'),Id(r'j'))),[CallStmt(Id(r'dec'),[Id(r'j')])]),If(UnaryOp(r'not',BinaryOp(r'>',Id(r'i'),Id(r'j'))),[Assign(Id(r'y'),ArrayCell(Id(r'a'),Id(r'i'))),Assign(ArrayCell(Id(r'a'),Id(r'i')),ArrayCell(Id(r'a'),Id(r'j'))),Assign(ArrayCell(Id(r'a'),Id(r'j')),Id(r'y')),CallStmt(Id(r'inc'),[Id(r'i')]),Assign(Id(r'j'),BinaryOp(r'-',Id(r'j'),IntLiteral(1)))],[])]),If(BinaryOp(r'<',Id(r'l'),Id(r'j')),[CallStmt(Id(r'sort'),[Id(r'l'),Id(r'j')])],[]),If(BinaryOp(r'<',Id(r'i'),Id(r'r')),[CallStmt(Id(r'sort'),[Id(r'i'),Id(r'r')])],[])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,398))

    def test_make_square(self):
        input = """
            procedure makesquare( sq : real; limit : integer);
                var
                   num,r,c : integer;
                begin
                   for r:=1 to limit do
                     for c:=1 to limit do
                       sq[rc] := 0;
                   if (limit and 1)<>0 then
                     begin
                        r:=(limit+1) div 2;
                        c:=limit;
                        for num:=1 to limit*limit do
                          begin
                             if sq[rc]<>0 then
                               begin
                                  dec(r);
                                  if r<1 then
                                    inc(r,limit);
                                  dec(c,2);
                                  if c<1 then
                                    inc(c,limit);
                               end
                             sq[rc]:=num;
                             inc(r);
                             if r>limit then
                               dec(r,limit);
                             inc(c);
                             if c>limit then
                               dec(c,limit);
                          end
                     end
                 end
            """
        expect = str(Program([FuncDecl(Id(r'makesquare'),[VarDecl(Id(r'sq'),FloatType()),VarDecl(Id(r'limit'),IntType())],[VarDecl(Id(r'num'),IntType()),VarDecl(Id(r'r'),IntType()),VarDecl(Id(r'c'),IntType())],[For(Id(r'r'),IntLiteral(1),Id(r'limit'),True,[For(Id(r'c'),IntLiteral(1),Id(r'limit'),True,[Assign(ArrayCell(Id(r'sq'),Id(r'rc')),IntLiteral(0))])]),If(BinaryOp(r'<>',BinaryOp(r'and',Id(r'limit'),IntLiteral(1)),IntLiteral(0)),[Assign(Id(r'r'),BinaryOp(r'div',BinaryOp(r'+',Id(r'limit'),IntLiteral(1)),IntLiteral(2))),Assign(Id(r'c'),Id(r'limit')),For(Id(r'num'),IntLiteral(1),BinaryOp(r'*',Id(r'limit'),Id(r'limit')),True,[If(BinaryOp(r'<>',ArrayCell(Id(r'sq'),Id(r'rc')),IntLiteral(0)),[CallStmt(Id(r'dec'),[Id(r'r')]),If(BinaryOp(r'<',Id(r'r'),IntLiteral(1)),[CallStmt(Id(r'inc'),[Id(r'r'),Id(r'limit')])],[]),CallStmt(Id(r'dec'),[Id(r'c'),IntLiteral(2)]),If(BinaryOp(r'<',Id(r'c'),IntLiteral(1)),[CallStmt(Id(r'inc'),[Id(r'c'),Id(r'limit')])],[])],[]),Assign(ArrayCell(Id(r'sq'),Id(r'rc')),Id(r'num')),CallStmt(Id(r'inc'),[Id(r'r')]),If(BinaryOp(r'>',Id(r'r'),Id(r'limit')),[CallStmt(Id(r'dec'),[Id(r'r'),Id(r'limit')])],[]),CallStmt(Id(r'inc'),[Id(r'c')]),If(BinaryOp(r'>',Id(r'c'),Id(r'limit')),[CallStmt(Id(r'dec'),[Id(r'c'),Id(r'limit')])],[])])],[])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,399))

    
