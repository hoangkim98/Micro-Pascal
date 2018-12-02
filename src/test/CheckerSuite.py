import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    def test_redeclared_global_var_var(self):
        input = """var a:integer;
        procedure main();
        begin
        end
        var A: array[1 .. 3] of real;
        """
        expect = "Redeclared Variable: A"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_redeclared_global_var_proc(self):
        input = """var a:integer;
        procedure a();
        begin end
        procedure main();
        begin
        end
        """
        expect = "Redeclared Procedure: a"
        self.assertTrue(TestChecker.test(input,expect,401))

    def test_redeclared_global_var_func(self):
        input = """var a:integer;
        function a():real;
        begin 
            return 1;
        end
        procedure main();
        begin
        end
        """
        expect = "Redeclared Function: a"
        self.assertTrue(TestChecker.test(input,expect,402))

    def test_redeclared_global_proc_var(self):
        input = """var a:integer;
        procedure b();
        begin end
        var b:integer;
        procedure main();
        begin
        end
        """
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input,expect,403))

    def test_redeclared_param_proc(self):
        input = """var a:integer;
        procedure foo(b,b:integer);
        begin end
        procedure main();
        begin
        end
        """
        expect = "Redeclared Parameter: b"
        self.assertTrue(TestChecker.test(input,expect,404))

    def test_redeclared_param_local_proc(self):
        input = """var a:integer;
        procedure foo(b:integer);
        var b:real;
        begin 
        end
        procedure main();
        begin
        end
        """
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input,expect,405))

    def test_redeclared_local_local_func(self):
        input = """var a:integer;
        procedure foo();
        var b,b:real;
        begin end
        procedure main();
        begin
        end
        """
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input,expect,406))

    def test_redeclared_global_proc_func(self):
        input = """var a:integer;
        procedure foo();
        begin end
        function foo():real;
        begin return 1; end
        procedure main();
        begin
        end
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,407))

    def test_redeclared_global_func_proc(self):
        input = """var a:integer;
        function foo():real;
        begin return 1; end
        procedure foo();
        begin end
        procedure main();
        begin
        end
        """
        expect = "Redeclared Procedure: foo"
        self.assertTrue(TestChecker.test(input,expect,408))

    def test_redeclared_decl_with(self):
        input = """
        procedure foo();
        begin 
            with a,b:real;a:string; do a:= a+1;
        end
        procedure main();
        begin
        end
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,409))

    def test_undeclared_id_proc(self):
        input = """
        procedure main();
        begin
            foo();
        end
        """
        expect = "Undeclared Procedure: foo"
        self.assertTrue(TestChecker.test(input,expect,410))

    def test_undeclared_id_expr(self):
        input = """
        var a:real;
        procedure main();
        begin
            a:= foo();
        end
        """
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,411))

    def test_undeclared_binary_func(self):
        input = """
        var a:real;
        procedure main();
        begin
            a := 1 + foo();
        end
        """
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,412))

    def test_undeclared_unary_func(self):
        input = """
        var a:real;
        procedure main();
        begin
            a := not foo();
        end
        """
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,413))

    def test_undeclared_id_ident(self):
        input = """
        procedure main();
        begin
            a :=1;
        end
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input,expect,414))

    def test_undeclared_arraycell(self):
        input = """
        procedure main();
        begin
            a[1] := 3;
        end
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input,expect,415))
    
    def test_redeclared_with_with(self):
        input = """var a,b:integer;
                procedure main();
                var b,c:real;
                begin
                    with a,b:array[1 .. 3] of string; do
                        with a, b: integer; a:string; do
                            begin
                            end
                end
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,416))
    
    def test_type_mismatch_expr_string(self):
        input = """var a:string;
        procedure main();
        begin
            if true aNd a then foo(); 
        end
        procedure foo();
        begin end
        """
        expect = "Type Mismatch In Expression: BinaryOp(aNd,BooleanLiteral(True),Id(a))"
        self.assertTrue(TestChecker.test(input,expect,417))
    
    def test_type_mismatch_expr_array(self):
        input = """var a:array[1 .. 6] of real;
        procedure main();
        begin
            if true aNd a then foo(); 
        end
        procedure foo();
        begin end
        """
        expect = "Type Mismatch In Expression: BinaryOp(aNd,BooleanLiteral(True),Id(a))"
        self.assertTrue(TestChecker.test(input,expect,418))

    def test_type_mismatch_expr_boolean(self):
        input = """
        procedure main();
        begin
            if true + false then foo(); 
        end
        procedure foo();
        begin end
        """
        expect = "Type Mismatch In Expression: BinaryOp(+,BooleanLiteral(True),BooleanLiteral(False))"
        self.assertTrue(TestChecker.test(input,expect,419))

    def test_type_mismatch_expr_int(self):
        input = """var a:integer;
        procedure main();
        begin
            if a aNd 1 then foo(); 
        end
        procedure foo();
        begin end
        """
        expect = "Type Mismatch In Expression: BinaryOp(aNd,Id(a),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,420))

    def test_type_mismatch_expr_float(self):
        input = """var a:real;
        procedure main();
        begin
            if a and THEN 1.4 then foo(); 
        end
        procedure foo();
        begin end
        """
        expect = "Type Mismatch In Expression: BinaryOp(andthen,Id(a),FloatLiteral(1.4))"
        self.assertTrue(TestChecker.test(input,expect,421))

    def test_type_mismatch_expr_diff_type(self):
        input = """var a:real;
        procedure main();
        begin
            if a and tRue then foo(); 
        end
        procedure foo();
        begin end
        """
        expect = "Type Mismatch In Expression: BinaryOp(and,Id(a),BooleanLiteral(True))"
        self.assertTrue(TestChecker.test(input,expect,422))

    def test_type_mismatch_expr_coercion(self):
        input = """var a:real;
        procedure main();
        begin
            if a and 3 then foo(); 
        end
        procedure foo();
        begin end
        """
        expect = "Type Mismatch In Expression: BinaryOp(and,Id(a),IntLiteral(3))"
        self.assertTrue(TestChecker.test(input,expect,423))

    def test_type_mismatch_expr_not(self):
        input = """var a:array[1 .. 5] of real;
        procedure main();
        begin
            if not 1 then foo(); 
        end
        procedure foo();
        begin end
        """
        expect = "Type Mismatch In Expression: UnaryOp(not,IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,424))

    def test_type_mismatch_expr_subOP(self):
        input = """var a:string;
        procedure main();
        begin
            if - a then foo(); 
        end
        procedure foo();
        begin end
        """
        expect = "Type Mismatch In Expression: UnaryOp(-,Id(a))"
        self.assertTrue(TestChecker.test(input,expect,425))

    def test_type_mismatch_expr_arraycell_arr(self):
        input = """var a:array[1 .. 7] of real;b:real;
        procedure main();
        begin
            if b[1] + 1 then foo(); 
        end
        procedure foo();
        begin end
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(b),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,426))

    def test_type_mismatch_expr_arraycell_idx(self):
        input = """var a:array[1 .. 9] of real;
        procedure main();
        begin
            if a[1.5] + 1 then foo(); 
        end
        procedure foo();
        begin end
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(a),FloatLiteral(1.5))"
        self.assertTrue(TestChecker.test(input,expect,427))

    def test_type_mismatch_expr_plus(self):
        input = """var a:array[1 .. 9] of real;
        procedure main();
        begin
            if foo() + foo() then foo(); 
        end
        function foo():real;
        begin end
        """
        expect = "Type Mismatch In Statement: If(BinaryOp(+,CallExpr(Id(foo),[]),CallExpr(Id(foo),[])),[CallStmt(Id(foo),[])],[])"
        self.assertTrue(TestChecker.test(input,expect,428))

    def test_type_mismatch_stmt_unaOP_if(self):
        input = """var a:array[1 .. 9] of real;
        procedure main();
        begin
            if -3 then foo(); 
        end
        procedure foo();
        begin end
        """
        expect = "Type Mismatch In Statement: If(UnaryOp(-,IntLiteral(3)),[CallStmt(Id(foo),[])],[])"
        self.assertTrue(TestChecker.test(input,expect,429))

    def test_type_mismatch_stmt_binOP_diff_if(self):
        input = """var a: real;
        procedure main();
        begin
            if a + 1 then foo(); 
        end
        procedure foo();
        begin end
        """
        expect = "Type Mismatch In Statement: If(BinaryOp(+,Id(a),IntLiteral(1)),[CallStmt(Id(foo),[])],[])"
        self.assertTrue(TestChecker.test(input,expect,430))

    def test_type_mismatch_stmt_binOP_int_if(self):
        input = """var a:integer;
        procedure main();
        begin
            if a dIV 3 then foo(); 
        end
        procedure foo();
        begin end
        """
        expect = "Type Mismatch In Statement: If(BinaryOp(dIV,Id(a),IntLiteral(3)),[CallStmt(Id(foo),[])],[])"
        self.assertTrue(TestChecker.test(input,expect,431))

    def test_type_mismatch_stmt_binOP_float_if(self):
        input = """var a:real;
        procedure main();
        begin
            if a / 3.5 then foo(); 
        end
        procedure foo();
        begin end
        """
        expect = "Type Mismatch In Statement: If(BinaryOp(/,Id(a),FloatLiteral(3.5)),[CallStmt(Id(foo),[])],[])"
        self.assertTrue(TestChecker.test(input,expect,432))

    def test_type_mismatch_stmt_arraycell_if(self):
        input = """var a:array[1 .. 9] of real;
        procedure main();
        begin
            if a[1] then foo(); 
        end
        procedure foo();
        begin end
        """
        expect = "Type Mismatch In Statement: If(ArrayCell(Id(a),IntLiteral(1)),[CallStmt(Id(foo),[])],[])"
        self.assertTrue(TestChecker.test(input,expect,433))

    def test_type_mismatch_stmt_id_if(self):
        input = """var a:real;
        procedure main();
        begin
            if a then foo(); 
        end
        procedure foo();
        begin end
        """
        expect = "Type Mismatch In Statement: If(Id(a),[CallStmt(Id(foo),[])],[])"
        self.assertTrue(TestChecker.test(input,expect,434))

    def test_type_mismatch_stmt_callexp_if(self):
        input = """var a:real;
        procedure main();
        begin
            if bar() then foo(); 
        end
        function bar():real;
        begin  return 1; end
        procedure foo();
        begin end
        """
        expect = "Type Mismatch In Statement: If(CallExpr(Id(bar),[]),[CallStmt(Id(foo),[])],[])"
        self.assertTrue(TestChecker.test(input,expect,435))

    def test_type_mismatch_stmt_unaOP_while(self):
        input = """var a:array[1 .. 9] of real;
        procedure main();
        begin
            while -3 do foo(); 
        end
        procedure foo();
        begin end
        """
        expect = "Type Mismatch In Statement: While(UnaryOp(-,IntLiteral(3)),[CallStmt(Id(foo),[])])"
        self.assertTrue(TestChecker.test(input,expect,436))

    def test_type_mismatch_stmt_binOP_diff_while(self):
        input = """var a: real;
        procedure main();
        begin
            while a + 1 do foo(); 
        end
        procedure foo();
        begin end
        """
        expect = "Type Mismatch In Statement: While(BinaryOp(+,Id(a),IntLiteral(1)),[CallStmt(Id(foo),[])])"
        self.assertTrue(TestChecker.test(input,expect,437))

    def test_type_mismatch_stmt_binOP_int_while(self):
        input = """var a:integer;
        procedure main();
        begin
            while a dIV 3 do foo(); 
        end
        procedure foo();
        begin end
        """
        expect = "Type Mismatch In Statement: While(BinaryOp(dIV,Id(a),IntLiteral(3)),[CallStmt(Id(foo),[])])"
        self.assertTrue(TestChecker.test(input,expect,438))

    def test_type_mismatch_stmt_binOP_float_while(self):
        input = """var a:real;
        procedure main();
        begin
            while a / 3.5 do foo(); 
        end
        procedure foo();
        begin end
        """
        expect = "Type Mismatch In Statement: While(BinaryOp(/,Id(a),FloatLiteral(3.5)),[CallStmt(Id(foo),[])])"
        self.assertTrue(TestChecker.test(input,expect,439))

    def test_type_mismatch_stmt_arraycell_while(self):
        input = """var a:array[1 .. 9] of real;
        procedure main();
        begin
            while a[1] do foo(); 
        end
        procedure foo();
        begin end
        """
        expect = "Type Mismatch In Statement: While(ArrayCell(Id(a),IntLiteral(1)),[CallStmt(Id(foo),[])])"
        self.assertTrue(TestChecker.test(input,expect,440))

    def test_type_mismatch_stmt_id_while(self):
        input = """var a:real;
        procedure main();
        begin
            while a do foo(); 
        end
        procedure foo();
        begin end
        """
        expect = "Type Mismatch In Statement: While(Id(a),[CallStmt(Id(foo),[])])"
        self.assertTrue(TestChecker.test(input,expect,441))

    def test_type_mismatch_stmt_callexp_while(self):
        input = """var a:real;
        procedure main();
        begin
            while bar() do foo(); 
        end
        function bar():real;
        begin return 1; end
        procedure foo();
        begin end
        """
        expect = "Type Mismatch In Statement: While(CallExpr(Id(bar),[]),[CallStmt(Id(foo),[])])"
        self.assertTrue(TestChecker.test(input,expect,442))

    def test_type_mismatch_stmt_id_for(self):
        input = """var a:boolean;
        procedure main();
        var a:real;
        begin
            for a :=1 to 10 do foo(); 
        end
        procedure foo();
        begin end
        """
        expect = "Type Mismatch In Statement: For(Id(a)IntLiteral(1),IntLiteral(10),True,[CallStmt(Id(foo),[])])"
        self.assertTrue(TestChecker.test(input,expect,443))

    def test_undeclared_id_for(self):
        input = """//var a:boolean;
        procedure main();
        //var a:real;
        begin
            for a :=1 to 10 do foo(); 
        end
        procedure foo();
        begin end
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input,expect,444))

    def test_type_mismatch_stmt_expr_for(self):
        input = """var a:boolean;
        procedure main();
        var a:real;
        begin
            for a :=1 to 10.4 do foo(); 
        end
        procedure foo();
        begin end
        """
        expect = "Type Mismatch In Statement: For(Id(a)IntLiteral(1),FloatLiteral(10.4),True,[CallStmt(Id(foo),[])])"
        self.assertTrue(TestChecker.test(input,expect,445))

    def test_type_mismatch_stmt_lhs_string_assign(self):
        input = """var a:string;
        procedure main();
        begin
            a := "1";
        end
        procedure foo();
        begin end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(a),StringLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,446))

    def test_type_mismatch_stmt_lhs_array_assign(self):
        input = """var a:array [1 .. 9] of real;
        procedure main();
        begin
            a := 1; 
        end
        procedure foo();
        begin end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(a),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,447))

    def test_type_mismatch_stmt_difftype_assign(self):
        input = """var a:real;
        procedure main();
        begin
            a:= tRuE; 
        end
        procedure foo();
        begin end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(a),BooleanLiteral(True))"
        self.assertTrue(TestChecker.test(input,expect,448))

    def test_type_mismatch_stmt_return_proc(self):
        input = """var a:real;
        procedure main();
        begin
            return a; 
        end
        procedure foo();
        begin end
        """
        expect = "Type Mismatch In Statement: Return(Some(Id(a)))"
        self.assertTrue(TestChecker.test(input,expect,449))

    def test_type_mismatch_stmt_return_func(self):
        input = """var a:real;
        procedure main();
        begin
        end
        function foo():real;
        begin 
            return ;
        end
        """
        expect = "Type Mismatch In Statement: Return(None)"
        self.assertTrue(TestChecker.test(input,expect,450))

    def test_type_mismatch_stmt_diff_return_func(self):
        input = """var a:real;
        procedure main();
        begin
        end
        function foo():real;
        begin 
            return "hello";
            //return b;
        end
        """
        expect = "Type Mismatch In Statement: Return(Some(StringLiteral(hello)))"
        self.assertTrue(TestChecker.test(input,expect,451))

    def test_type_mismatch_stmt_return_array_eleType_func(self):
        input = """var a:array[1 .. 10] of integer;
        procedure main();
        begin
        end
        function foo():array[1 .. 10] of real;
        begin
            return a;
        end
        """
        expect = "Type Mismatch In Statement: Return(Some(Id(a)))"
        self.assertTrue(TestChecker.test(input,expect,452))

    def test_type_mismatch_stmt_return_array_uplow_func(self):
        input = """var a:array[3 .. 10] of real;b:real;
        procedure main();
        begin
        end
        function foo():array[1 .. 10] of real;
        begin
            if a[1] > 3 then b:=1;
            return a;
        end
        """
        expect = "Type Mismatch In Statement: Return(Some(Id(a)))"
        self.assertTrue(TestChecker.test(input,expect,453))

    def test_redeclared_global_envi_variable(self):
        input = """var putIntLn:real;
        procedure main();
        begin
        end
        procedure foo();
        begin end
        """
        expect = "Redeclared Variable: putIntLn"
        self.assertTrue(TestChecker.test(input,expect,454))

    def test_redeclared_global_envi_func(self):
        input = """var a:real;
        procedure main();
        begin
        end
        procedure putLn();
        begin end
        """
        expect = "Redeclared Procedure: putLn"
        self.assertTrue(TestChecker.test(input,expect,455))

    def test_undeclared_param_callstmt(self):
        input = """var a:array[1 .. 10] of real;
        procedure main();
        begin
            foo(c,d);
        end
        procedure foo(a,b:real);
        begin
        end
        """
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input,expect,456))

    def test_type_mismatch_stmt_param_less_callstmt(self):
        input = """var a:array[1 .. 10] of real;
        procedure main();
        var b:real;
        begin
            foo(b);
        end
        procedure foo(a,b:real);
        begin
        end
        """
        expect = "Type Mismatch In Statement: CallStmt(Id(foo),[Id(b)])"
        self.assertTrue(TestChecker.test(input,expect,457))

    def test_type_mismatch_stmt_param_string_callstmt(self):
        input = """var a:string;
        procedure main();
        var b:real;
        begin
            foo(a,b,"1");
        end
        procedure foo(a:string;b:real);
        begin
        end
        """
        expect = "Type Mismatch In Statement: CallStmt(Id(foo),[Id(a),Id(b),StringLiteral(1)])"
        self.assertTrue(TestChecker.test(input,expect,458))

    def test_type_mismatch_stmt_param_compare_callstmt(self):
        input = """var c:real;
        procedure main();
        var d:real;
        begin
            foo(c,d);
        end
        procedure foo(a:integer;b:real);
        begin
        end
        """
        expect = "Type Mismatch In Statement: CallStmt(Id(foo),[Id(c),Id(d)])"
        self.assertTrue(TestChecker.test(input,expect,459))

    def test_type_mismatch_stmt_array_eleType_callstmt(self):
        input = """var c:array[1 .. 10] of integer;
        procedure main();
        var d:real;
        begin
            foo(d,c);
        end
        procedure foo(b:real;a:array[1 .. 10] of real);
        begin
        end
        """
        expect = "Type Mismatch In Statement: CallStmt(Id(foo),[Id(d),Id(c)])"
        self.assertTrue(TestChecker.test(input,expect,460))

    def test_type_mismatch_stmt_array_uplow_callstmt(self):
        input = """var c:array[1 .. 10] of integer;
        procedure main();
        var d:real;
        begin
            foo(d,c);
        end
        procedure foo(b:real;a:array[1 .. 9] of integer);
        begin
        end
        """
        expect = "Type Mismatch In Statement: CallStmt(Id(foo),[Id(d),Id(c)])"
        self.assertTrue(TestChecker.test(input,expect,461))
    
    def test_undeclared_param_callexpr(self):
        input = """var a: real;
        procedure main();
        begin
            a:= foo(c,d);
        end
        function foo(a,b:real):real;
        begin
            return 1;
        end
        """
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input,expect,462))

    def test_type_mismatch_expr_param_less_callexpr(self):
        input = """var a:array[1 .. 10] of real;
        procedure main();
        var b:real;
        begin
            b:=foo(b);
        end
        function foo(a,b:real):real;
        begin
            return 1;
        end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[Id(b)])"
        self.assertTrue(TestChecker.test(input,expect,463))

    def test_type_mismatch_expr_param_string_callexpr(self):
        input = """var a:string;
        procedure main();
        var b:real;
        begin
            b:=foo(a,b,"1");
        end
        function foo(a:string;b:real):real;
        begin
            return 1;
        end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[Id(a),Id(b),StringLiteral(1)])"
        self.assertTrue(TestChecker.test(input,expect,464))

    def test_type_mismatch_expr_param_compare_callexpr(self):
        input = """var c:real;
        procedure main();
        var d:real;
        begin
            d:=foo(c,d);
        end
        function foo(a:integer;b:real):real;
        begin
            return 1;
        end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[Id(c),Id(d)])"
        self.assertTrue(TestChecker.test(input,expect,465))

    def test_type_mismatch_expr_array_eleType_callexpr(self):
        input = """var c:array[1 .. 10] of integer;
        procedure main();
        var d:real;
        begin
            d:=foo(d,c);
        end
        function foo(b:real;a:array[1 .. 10] of real):real;
        begin
            return 1;
        end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[Id(d),Id(c)])"
        self.assertTrue(TestChecker.test(input,expect,466))

    def test_type_mismatch_expr_array_uplow_callexpr(self):
        input = """var c:array[1 .. 10] of integer;
        procedure main();
        var d:real;
        begin
            d:=foo(d,c);
        end
        function foo(b:real;a:array[1 .. 9] of integer):real;
        begin
            return 1;
        end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[Id(d),Id(c)])"
        self.assertTrue(TestChecker.test(input,expect,467))

    def test_undeclared_arraycell_callexpr(self):
        input = """var a: integer;
        procedure main();
        var a:integer;
        begin
            a:=foo()[a];
        end
        {function foo():real;
        begin
            return 1;
        end}
        """
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,468))

    def test_type_mismatch_expr_arraycell_arr_callexpr(self):
        input = """var a: integer;
        procedure main();
        var a:integer;
        begin
            a:=foo()[a];
        end
        function foo():real;
        begin
            return 1;
        end
        """
        expect = "Type Mismatch In Expression: ArrayCell(CallExpr(Id(foo),[]),Id(a))"
        self.assertTrue(TestChecker.test(input,expect,469))

    def test_type_mismatch_expr_arraycell_binOP(self):
        input = """var a: integer;
        procedure main();
        var a:integer;
        begin
            a:=(1+1)[a];
        end
        function foo():real;
        begin
            return 1;
        end
        """
        expect = "Type Mismatch In Expression: ArrayCell(BinaryOp(+,IntLiteral(1),IntLiteral(1)),Id(a))"
        self.assertTrue(TestChecker.test(input,expect,470))

    def test_no_entry(self):
        input = """var a:array[1 .. 10] of integer;
        function foo(): real;
        begin
            return 1;
        end
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input,expect,471))

    def test_no_entry_fake_function(self):
        input = """var a:array[1 .. 10] of integer;
        function main():real;
        begin
        end
        function foo():real;
        begin
            return 1;
        end
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input,expect,472))

    def test_no_entry_fake_variable(self):
        input = """var main: integer;
        function foo():real;
        begin
            return 1;
        end
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input,expect,473))

    def test_no_entry_param(self):
        input = """
        procedure main(a:real);
        begin end
        function foo():real;
        begin
            return 1;
        end
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input,expect,474))

    def test_break_in_func(self):
        input = """
        procedure main();
        begin
        end
        function foo(): real;
        begin
            break;
            return 1;
        end
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,475))
    
    def test_continue_in_proc(self):
        input = """
        procedure main();
        begin
        end
        procedure foo();
        begin
            continue;
            return ;
        end
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,476))

    def test_break_in_if_then(self):
        input = """
        procedure main();
        begin
        end
        procedure foo();
        begin
            if true then break;
            return ;
        end
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,477))

    def test_continue_in_if_else(self):
        input = """
        procedure main();
        begin
        end
        procedure foo();
        begin
            if true then foo(); else continue;
            return ;
        end
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,478))

    def test_break_with(self):
        input = """
        procedure main();
        begin
        end
        procedure foo();
        begin
            with a:real; do 
            begin
                continue;
            end
            return ;
        end
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,479))

    def test_break_if_if(self):
        input = """var a: integer;
        procedure main();
        var a:integer;
        begin
            if a>1 then 
                if a>1 then break;
        end
        function foo():real;
        begin
            return 1;
        end
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,480))

    def test_break_with_with(self):
        input = """var a: integer;
        procedure main();
        var a:integer;
        begin
            with a:real; do 
            begin
                //while a>1 do
                with a:real; do 
                begin
                    break;
                end
            end
        end
        function foo():real;
        begin
            return 1;
        end
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,481))

    def test_func_not_return_then_if(self):
        input = """var a:integer;
        procedure main();
        begin
        end
        function foo():real;
        begin
            a := 1;
            if true then 
            begin
                a := 1 ;
                return a;
            end
            else begin
                a :=3;
                //return a;
            end
        end
        """
        expect = "Function fooNot Return "
        self.assertTrue(TestChecker.test(input,expect,482))
    
    def test_func_not_return_else_if(self):
        input = """var a:integer;
        procedure main();
        begin
        end
        function foo():real;
        begin
            //return 1;
            a := 1;
            if true then 
            begin
                a := 1 ;
                //return a;
            end
            else begin
                a :=3;
                return a;
            end
            //return 1;
        end
        """
        expect = "Function fooNot Return "
        self.assertTrue(TestChecker.test(input,expect,483))

    def test_func_not_return_with_with(self):
        input = """var a:integer;
        procedure main();
        begin
        end
        function foo():real;
        begin
            //return 1;
            a := 1;
            with a:real; do
            begin
                //return 1;
                with a:integer; do
                begin
                    //return 3;
                end
            end
            //return 1;
        end
        """
        expect = "Function fooNot Return "
        self.assertTrue(TestChecker.test(input,expect,484))

    def test_func_not_return_if_with(self):
        input = """var a:integer;
        procedure main();
        begin
        end
        function foo():real;
        begin
            //return 1;
            a := 1;
            if true then 
            begin
                a := 1 ;
                with a:real; do 
                begin
                    //return 3;
                end
                //return a;
            end
            else 
            begin
                a :=3;
                //return a;
            end
            //return 1;
        end
        """
        expect = "Function fooNot Return "
        self.assertTrue(TestChecker.test(input,expect,485))
    
    def test_func_not_return_if_if(self):
        input = """var a:integer;
        procedure main();
        begin
        end
        function foo():real;
        begin
            //return 1;
            a := 1;
            if true then 
            begin
                a := 1 ;
                if a>3 then 
                begin
                    return a;
                end
                //return a;
            end
            else 
            begin
                a :=3;
                return a;
            end
            //return 1;
        end
        """
        expect = "Function fooNot Return "
        self.assertTrue(TestChecker.test(input,expect,486))

    def test_type_mismatch_stmt_return_if_func(self):
        input = """var a:integer;
        function foo():real;
        begin
            a:=1;
            if a>3 then return true;
            else return 1;
        end
        procedure main();
        begin
        end
        """
        expect = "Type Mismatch In Statement: Return(Some(BooleanLiteral(True)))"
        self.assertTrue(TestChecker.test(input,expect,487))

    def test_type_mismatch_stmt_return_with_func(self):
        input = """var a:integer;
        function foo():real;
        begin
            a:=1;
            with b:real; do
            begin
                a:=1;
                return false;
            end
        end
        procedure main();
        begin
        end
        """
        expect = "Type Mismatch In Statement: Return(Some(BooleanLiteral(False)))"
        self.assertTrue(TestChecker.test(input,expect,488))

    def test_type_mismatch_stmt_return_with_proc(self):
        input = """var a:integer;
        procedure foo();
        begin
            a:=1;
            with b:real; do
            begin
                a:=1;
                return truE;
            end
        end
        procedure main();
        begin
        end
        """
        expect = "Type Mismatch In Statement: Return(Some(BooleanLiteral(True)))"
        self.assertTrue(TestChecker.test(input,expect,489))

    def test_random1(self):
        input = """
        var a: real;
        procedure main();
        var a: real;
        i,j:integer;
        begin
            for i := 1 to 10 do begin
                for j := i downto 1 do
                    if (i + j) mod foo() = 1 then break;
            end
        end
            """
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,490))

    def test_type_mismatch_stmt_return_if_if(self):
        input = """var a:integer;
        function foo():boolean;
        begin
            if a>1 then
                if true then
                    begin a:=1;return 1;end
                else return true;
                {with a:real; do
                    begin
                        return 1;
                    end
                }
            else return true; 
            //return 1;
        end
        procedure main();
        begin
        end
        """
        expect = "Type Mismatch In Statement: Return(Some(IntLiteral(1)))"
        self.assertTrue(TestChecker.test(input,expect,491))

    def test_random_hai(self):
        input = """
        var a: real;
        procedure main();
        var i,j:real;
        k:boolean;
        a:string;
        b:array[1 .. 5] of integer;
        d:string;
        begin
        i := foo(a,b,b);
        end
        function foo(a:string;b,c:array[1 .. 5] of integer):integer;
        var d:array[1 .. 5] of integer;
        begin
            with a:integer; do
            begin 
                if a < 3 then a:=4 ;
                else begin 
                    for a := 1 to a do break;
                end                            
            end
        end
        function bar(a:string;b,c:array[1 .. 5] of integer):integer;
        var a:array[1 .. 5] of integer;
        begin
            with a:integer; do
            begin 
                if a < 3 then a:=4 ;
                else begin 
                    for a := 1 to a do break;
                end                            
            end
        end
        """
        expect = "Function fooNot Return "
        self.assertTrue(TestChecker.test(input, expect, 492))

    def test_random3(self):
        input = """
        var a: real;
        procedure main();
        var j:real;
        i:integer;
        k:boolean;
        a:string;
        b:array[1 .. 5] of integer;
        d:string;
        begin
        if false then i:=1;
        while false do if true then return; else bar(3);
        while true do i:= 1;
        with a:integer; do
            a:= foo(a);
        end
        procedure bar(a:integer);
        begin 
        if false then return ;
        end
        function foo(a:integer):integer;
        begin 
        if false then return 4;
        else if true then if true then return 3;
        end
            """
        expect = "Function fooNot Return "
        self.assertTrue(TestChecker.test(input, expect, 493))

    def test_random4(self):
        input = """
        var a: real;
        procedure main();
        var i,j:real;
        k:boolean;
        a:string;
        b:array[1 .. 5] of integer;
        d:string;
        begin
            foo(b[10]);
        end
        procedure foo(b:integer);
        var a:array[1 .. 5] of integer;
        begin
        end
        procedure foo(b:integer);
        var a:array[1 .. 5] of integer;
        begin
        end
        """
        expect = "Redeclared Procedure: foo"
        self.assertTrue(TestChecker.test(input, expect, 494))

    def test_random5(self):
        input = """
        var a: real;
        procedure main();
        var i,j:real;
        k:boolean;
        a:string;
        b:array[1 .. 5] of integer;
        d:string;
        begin
        i := foo(b[10]);
        end
        function foo(b:integer):integer;
        var a:array[1 .. 5] of integer;
        begin
            if b>3 then 
            begin
                with a,b:integer;do 
                begin
                    if b < 4 then return foo(3);
                    else 
                    begin
                        if b > 5 then return 3;
                    end
                end
            end
            else return 1;
        end
        """
        expect = "Function fooNot Return "
        self.assertTrue(TestChecker.test(input, expect, 495))

    def test_random6(self):
        input = """
        var x4:integer;

        procedure x6(a:integer; x2:string);
        begin
            if true then
            begin
                a := a + 1;
                return 6;
            end
            else
                return;
        end

        procedure main(); 
        var x1:integer;
            x2:real;
            x3:string;
        begin
            x6(1,"a");
            return;
        end
        """
        expect = "Type Mismatch In Statement: Return(Some(IntLiteral(6)))"
        self.assertTrue(TestChecker.test(input,expect,496))

    def test_random7(self):
        input = """
        var x4:integer;

        function x3(x1:string; x2:integer):integer;
        begin
            return x6(1, "x");
        end

        function x6(x2:integer; x2:string):integer;
        begin
            return 100;
        end

        procedure main(); 
        var x1:integer;
            x2:real;
            x3:string;
        begin
            x1:= x3("a",2);
            x2:= x6(2,"2");
            return;
        end
        """
        expect = "Redeclared Parameter: x2"
        self.assertTrue(TestChecker.test(input,expect,497))

    def test_random8(self):
        input = """
        var a: string;
        var k:string;
        var b:real;
        procedure main();
        var i,j:real;
        K:boolean;
        A:string;
        B:array[1 .. 5] of integer;
        d:integer;
        begin
            i := j := b[1];
        end
        function foo(a:integer):integer;
        var B:string;
        begin
            if true then
            begin
                if false then return 0.5;
                else return 3;
            end
            else return 1;
        end
            """
        expect = "Type Mismatch In Statement: Return(Some(FloatLiteral(0.5)))"
        self.assertTrue(TestChecker.test(input, expect, 498))

    def test_random9(self):
        input = """
        var a: real;
        procedure main();
        var j:real;
        i:integer;
        k:boolean;
        a:string;
        A:real;
        b:array[1 .. 5] of integer;
        d:string;
        begin
        if false then i:=1;
        while false do if true then return; else bar(3);
        while true do 
        begin 
            for I:= 4 to i+1 do
            begin
                with a:integer; do
                    a:= Foo1(a);
            end
        end
        wITH A:integer; do
            a:= foo(a);
        end
        procedure bar(a:integer);
        begin 
        if False then return ;
        end
        function foo1(a:integer):integer;
        begin 
        if false then return 4;
        end
        function foo(a:integer):integer;
        begin 
        if false then return 4;
        end
        """
        expect = "Redeclared Variable: A"
        self.assertTrue(TestChecker.test(input, expect, 499))
    

    
    
    