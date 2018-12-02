import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_var_and_func_decl(self):
        input = """
        Var a,b:integer;
        sdsd:real;
        function test():integer;
        var x,y:real;
        begin
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))
    
    def test_procedure1(self):
        input=""" 
        procedure foo (a,b: integer;c: real);
        var x,y: real;
        begin
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,202))

    def test_foo(self):
        input=""" 
        procedure foo (a,b: integer);
        var x,y: real;
        begin
        end
        procedure main();
        //this is a comment
        var a,b: integer;
        begin
        foo();
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,203))

    def test_simple_program(self):
        input = """
        procedure foo (a,b: integer);
        var x,y: real;
        begin
        end
        procedure main();
        //this is a comment
        var a,b: integer;
        begin
            a:= 1;
            for i:=1 to 5 do
            begin
                pritnt(a);
                 foo(a,b);
            end                   
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,204))
        
    def test_whole_program(self):
        input = """
        procedure foo (a,b: integer);
        var x,y: real;
        begin
        end

        procedure main();
        //this is a comment
        var a,b: integer;
            c:array [1 .. 2] of real;
        begin
            a:= 1;
            if a>1 then
                foo(a,b);
            else 
                a := foo(a,b)+3;
            while a=1 do a:=c-b;
            for i:=1 to a*2 do foo(a,b);
            break;
            continue;
            return foo(a,b);
            with a:integer; b:real; do
            begin
                a:=foo(a,b);
                print(a);
            end

        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,205))

    def test_wrong_float(self):
        input = """
        procedure foo(a,b:integer);
        var x:real;
        begin
            for a:=1 to n do
            begin
                if x >= 4 or  x < 4 then
                begin
                    foo(3);
                    a:=1;
                end
                else 
                begin
                    foo(1.);
                    1l.2e-!2;
                end
            end
        end
        """
        expect = "Error on line 7 col 32: <"
        self.assertTrue(TestParser.test(input,expect,206))

    def test_semi_in_wrong_position(self):
        input = """
        procedure foo(a,b:integer);
        var x:real;
        begin
            for a:=1 to n do
            begin
                if x >= 4 or  x < 4 then
                begin
                    foo(3);
                    a:=1;
                end
                else 
                begin
                    foo(1.);
                    ;
                end
            end
        end
        """
        expect = "Error on line 7 col 32: <"
        self.assertTrue(TestParser.test(input,expect,207))

    def test_plus_is_not_unary(self):
        input = """
         procedure foo(a,b:integer);
        var x:real;
        begin
            foo(-+3);
        end
        """
        expect = "Error on line 5 col 17: +"
        self.assertTrue(TestParser.test(input,expect,208))

    def test_wrong_syntax_in_for(self):
        input = """
        procedure foo(a,b:integer);
        var x:real;
        begin
            for a:=1,b:=2 to n do foo(a,b);  
        end
        """
        expect = "Error on line 5 col 20: ,"
        self.assertTrue(TestParser.test(input,expect,209))

    def test_missing_id(self):
        input = """
        procedure foo(a,b:integer);
        var x:real;
        begin
            a:=1;
            x:= + 1;
        end
        """
        expect = "Error on line 6 col 16: +"
        self.assertTrue(TestParser.test(input,expect,210))

    def test_index_exp(self):
        input = """
        procedure foo(a,b:integer);
        var x:real;
        begin
            a[.2e+12 + 3] := 3;
        end

        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,211))

    def test_non_assoc(self):
        input = """
        procedure foo(a,b:integer);
        var x:real;
        begin
            a[.2e3 >= 5 < 12 + 3] := 3;
        end
        """
        expect = "Error on line 5 col 24: <"
        self.assertTrue(TestParser.test(input,expect,212))

    def test_floatlit_in_index(self):
        input = """
        procedure foo(a,b:integer);
        var x:real;
        begin
            a[.2e-----3 + 3] + 1 := 3;
        end
        """
        expect = "Error on line 5 col 16: e"
        self.assertTrue(TestParser.test(input,expect,213))

    def test_wrong_exp(self):
        input = """
        procedure foo(a,b:integer);
        var x:real;
        begin
           a[1] := 02_;
        end
        """
        expect = "Error on line 5 col 21: _"
        self.assertTrue(TestParser.test(input,expect,214))

    def test_negative_index(self):
        input = """
        procedure foo(a,b:integer);
        var x:real;
        begin
           a[-1] := 02;
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,215))

    def test_error_char(self):
        input = """
        procedure foo(a,b:integer);
        var x:real;
        begin
          a[#12] := 02;
        end
        """
        expect = "#"
        self.assertTrue(TestParser.test(input,expect,216))

    def test_unclosed_string(self):
        input = """
        procedure foo(a,b:integer);
        var x:real; s:string;
        begin
          s:="abc;
        end
        """
        expect = "abc;"
        self.assertTrue(TestParser.test(input,expect,217))

    def test_ID_is_keyword(self):
        input = """
        procedure foo(a,b:integer);
        var x:real; true:integer; 
        begin
            true:=1;
            s:="abc;
        end
        """
        expect = "Error on line 3 col 20: true"
        self.assertTrue(TestParser.test(input,expect,218))

    def test_semi_after_while(self):
        input = """
        procedure foo(a,b:integer);
        var x:real; 
        begin
            while ( a+b- not c );
            while ( b--not c) do
            foo();
        end
        """
        expect = "Error on line 5 col 32: ;"
        self.assertTrue(TestParser.test(input,expect,219))

    def test_wrong_while(self):
        input = """
        procedure foo(a,b:integer);
        var x:real; 
        begin
            while ( a+b- not c )
            while ( b--not c) do
            foo();
        end
        """
        expect = "Error on line 6 col 12: while"
        self.assertTrue(TestParser.test(input,expect,220))

    def test_subtraction(self):
        input = """procedure a();
        begin
            a:=a-5;
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,221))

    def test_tamgiac(self):
        input = """
        Var a,b,c,s,p: real;
        pROCEDURE main() ;
        Begin
            Clrscr();
            Writeln("BAI TOAN TAM GIAC:");
            Writeln("---------------------------------");
            Write("nhap a =");readln(a);
            Write("nhap b =");readln(b);
            Write("nhap c =");readln(c);
            If ((a+b)>c)and((b+c)>a)and((a+c)>b) then
                Begin
                    p:=(a+b+c)/2;
                    s:=sqrt(p*(p-a)*(p-b)*(p-c));
                    Writeln("Chu vi tam giac:",2*p);
                    Writeln("Dien tich tam giac:",s);
                End
            Else Writeln(a,", ", b,", ", c, " khong phai la ba canh cua tam giac");
            Readln();
        End
        """
        expect = "successful"     
        self.assertTrue(TestParser.test(input,expect,222))
    
    def test_phuongtrinh_bacnhat(self):
        input = """
        pROCEDURE main() ;
        Var a,b,x:real;
        Begin
            Clrscr();
            Writeln("GIAI PHUONG TRINH BAC NHAT: AX + B=0");
            Writeln("-------------------------------------------------------");
            Write ("Nhap a= "); readln(a);
            Write ("Nhap b= ");readln(b);
            If(a=0) then
                If(b=0) then Writeln(" Phuong trinh co vo so nghiem");
                Else writeln("Phuong tring vo nghiem");
            Else Writeln("Phuong trinh co nghiem x=",-b/a);
            Readln();
        End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,223))
    
    def test_hinhtron(self):
        input = """
        Var r,dt,cv:real;
        pROCEDURE main() ;
        Begin
            Clrscr();
            Writeln("TINH DIEN TICH & CHU VI HINH TRON:");
            Writeln("--------------------------------------------------");
            Write ("Nhap ban kinh R="); readln(r);
            dt:=pi*r*r;
            cv:=2*pi*r;
            Writeln("Dien tich hinh tron la:",dt);
            Writeln("Chu vi hinh tron la:",cv);
            Readln();
        End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,224))

    def test_ucln(self):
        input = """
        Function UCLN(m,n:integer):integer;
        Begin
            If(m=n) then RETURN m ;
            else
                If (m>n) then return UCLN(m-n,n);
                else return UCLN(m,n-m);
        End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,225)) 

    def test_daoso(self):
        input = """
        Procedure Daoso(n: integer);
        Begin
            Assign(f,fo);
            Rewrite(f);
            If n > 0 then
                Begin
                Write(f,n mod 10);
                Daoso(n div 10);
                End
            Close(f);
        End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,226))

    def test_copy(self):
        input = """
        function ok(i : integer):boolean;
        var k : integer;
        begin
            ok := true;
            for k := 2 to i div 2 do
                if copy(s,i-2*k+1,k) = copy(s,i-k+1,k) then
                begin
                    ok := false;
                    exit();
                end
        end 
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,227))

    def test_fibo(self):
        input = """
        function fibo(x: integer): integer;
        var f1,f2: integer;
        Begin
            if x<=2 then
                return 1;
            else
                return fibo(x-2)+ fibo(x-1);
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,228))

    def test_giai_thua(self):
        input = """
        function gt(x:integer):integer;
        begin
            if x = 0 then
                return 1;
            else
                return x*gt(x-1);
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,229))

    def test_chen_phantu(self):
        input = """
        Procedure ChenPhanTu(A:array[0 .. 10] of REAL;N: Integer; k, X:Integer);
        Var i :Integer;
        Begin
            For i:=N downto k+ 1 do
                A[i] := A[i-1];
            A[k] := X;
        End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,230))

    def test_capsocong(self):
        input = """
        Function KtraMangCapSoCong (A:Mang20;  N:Integer; k:Integer):Boolean;
        Var flag :boolean;
        i :Integer;
        Begin
            for i:=1 to N do
            if(A[i] <> A[i-1] + k) then
                flag:=false;     // Cham dut, ket qua: khong phai
            return flag; {Ket qua kiem tra la mang cap so cong}
        End
        """
        expect = "Error on line 2 col 38: Mang20"
        self.assertTrue(TestParser.test(input,expect,231))

    def test_mangtang(self):
        input = """
        Function KtraMangTang ( A:array[0 .. 10] of REAL; N :Integer) : Boolean;
        Var Flag : Boolean;
            i :Integer;
        Begin
            Flag := True;
            i:= 0;
            while(i<n) do begin
                If(A[i] < A[i-1]) Then
                    Flag :=False; { Cham dut kiem tra, ket qua qua trinh : khong tang }
                i:=i+1;
            end
            return Flag;
        End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,232))

    def test_doixung(self):
        input = """
        Function KtraDoiXung (A:array[0 .. 10] of REAL; N:Integer ) : Boolean;
        Var Flag:Boolean;
            i :Integer;
        Begin
            Flag:=True;
            For  i :=1 to N do
                If(A[i] <> A[N-i  +1]) Then
                    Flag :=False;       { Cham dut kiem tra, ket qua qua trinh : khong doi xung }
            return flag;
        End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,233))

    def test_thaythe_bangtong(self):
        input = """
        Procedure ThayTheBangTong(A:array[0 .. 10] of integer; N:Integer; X, Y:Integer);
        Var i,k:Integer;
        Begin
            For i:=0 to N do
                If( (A[i-1]+A[i]) mod 10 = 0) then
                    Begin
                        k := (A[i-1]+A[i]);
                        A[i-1] := k;
                        A[i] := k;
                    End
        End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,234))

    def test_thaythe(self):
        input = """
        Procedure ThayTheTatCa (A:array[0 .. 10] of integer;N, x,y:Integer);
        Var i:Integer;
        Begin
            For i:=0 to N do
                If(A[i] = x) then { Tim thay x ==> thay the thanh y }
            A[i] := y;
        End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,235))

    def test_dem_ptu(self):
        input = """
        Function DemPtuX(A:array[0 .. 10] of integer; N,X : Integer) : Integer;
        Var i , Count : Integer;
        Begin
            Count := 0;
            For i:=0 to N do
                If ( A[i] = X ) then
                    Count := Count + 1;
            return Count;
        End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,236))

    def test_so_nguyento(self):
        input = """
        Function LaSoNT(N:Integer) :Integer;
        Var i:Integer;
        Begin
            For i:=2 to N-1 do
                If(N mod i = 0) then
                    return 0;
            Else
                return 1;
        End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,237))

    def test_chiahet_5(self):
        input = """
        Function Tong_So_Chia_Het_Cho5(A:array[0 .. 10] of integer ; N:Integer):Integer;
        Var S,i :Integer;
        Begin
        	S:=0;
        	For i:=0 to N do
        	    If(A[i] mod 5=0) then
        	        S := S+A[i];
        	return S;
        End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,238))

    def test_array(self):
        input = """
        Procedure NhapMang1C(A : array[0 .. 10] of integer;N:Integer);
        Var i: Integer;
        Begin
        Write("So luong phan tu:");
        Readln( N);
        For i:=0 to N do
            Begin
                Write("Nhap phan tu thu", i," ");
                Readln( A[i] );
            End
        End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,239))

    def test_tong_array(self):
        input = """
        function sum_real_array(a: array[0 .. m-1] of real;n:integer):real;
        var i:integer;s:real;
        beGin
            s:=0.;
            for i:=n-1 doWnTO 0 do s:=s+a[i];
            reTuRn s;
        eND
        procedure main() ;
        var a: array[0 .. m-1] of real; n:integer;
        beGin
            Writeln("Sum of real array: "+sum_real_array(a,n));
        eND
        """
        expect = "Error on line 2 col 46: m"
        self.assertTrue(TestParser.test(input,expect,240))

    def test_sort_array(self):
        input = """
        procedure main() ;
        var a: array[0 .. m-1] of integer;
            i,j,temp: integer;
        beGin
            for i := 0 to n - 2 do
                for j:= i+1 to n-1 do
                    if(a[i]>a[j]) then beGin
                        temp := a[i];
                        a[i] := a[j];
                        a[j] := temp;
                    eND
            print(a);
        eND
        """
        expect = "Error on line 3 col 26: m"
        self.assertTrue(TestParser.test(input,expect,241))

    def test_assign11(self):
        input = """
        procedure main() ;
        beGin
            if a=b then if c = d then e := f;
            else i := 1;
            else x := 2 ;
        eND
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,242))

    def test_double_square(self):
        input = """
        procedure main() ;
        beGin
            a[b[2]] := 10;
            foo();
            return ;
        eND
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,243))

    def test_urname(self):
        input = """
        Var name, surname: String;
        Procedure Main();
        Begin
	        write("Nhap ten cua ban:");
	        readln(name);
	        write("Nhap ho cua ban:");
	        readln(surname);
	        writeln();(*new line*)
	        writeln();//new line}
	        writeln("Ten day du cua ban la : ",name," ",surname);
	        readln();
        End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,244))

    def test_putIntln(self):
        input = """
        var i: integer ;
        function f(): integer ;
        begin
	        return 200;
        end
        procedure main() ;
        var main: integer ;
        begin
	        main := f() ;
	        putIntLn(main);
	        with
                i: integer;
                main: integer;
                f: integer;
	        do begin
		        main := f := i:= 100;
		        putIntLn (i);
		        putIntLn (main );
		        putIntLn (f);
	        end
	        putIntLn (main);
        end
        var g: real ;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,245))

    def test_double_then(self):
        input = """
                procedure test2() ;
                begin
	               if a=b then if c=d then while (d=e) do
                   beGin
                   eND
               else c := 1;
                end
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,246))
  
    def test_where_is_equal(self):
        input = """
        procedure foo(a,b);
        begin
                if ( a+b-!-c )
                        int a = 0;
                if ( b-- <> c)
                        foo();
                else 
                        f(not a ----b >= !-3);        
        end
        """
        expect = "Error on line 2 col 25: )"
        self.assertTrue(TestParser.test(input,expect,247))

    def test_id_start_with_char(self):
        input = """
        procedure foo(a,b);
        begin
                if ( a+b-!-c )
                        int a = 0;
                if ( b--!c)
                        foo();
                else f(!!!a----b >= !-3);
                
        end
        """
        expect = "Error on line 2 col 25: )"
        self.assertTrue(TestParser.test(input,expect,248))

    def test_literal_not_in_funcdeclr(self):
        input = """
        procedure foo(int a[3] >= 1);
        begin
            if ( a+b-!-c )
                int a = 0;
                if ( b--!c)
                foo();
                else f(!!!a----b >= !-3);
                
        end
        """
        expect = "Error on line 2 col 26: a"
        self.assertTrue(TestParser.test(input,expect,249))

    def test_wrongtype_var(self):
        input = """
        procedure foo(a,b);
        begin
                float a;
                void foo(int a[])
                if ( x> 3 == c) a = 1; 
                return x == -!-!-!3 >= 3;
                void a,b[6];
                
        end
        """
        expect = "Error on line 2 col 25: )"
        self.assertTrue(TestParser.test(input,expect,250))

    def test_after_void_is_funcdeclr(self):
        input = """
        procedure foo(a,b);
        begin
                float a;
                void foo(int a[])
                if ( x> 3 == c) a[9] = 1;
                return x == -!-!-!3[0] >= 3;
                void a,b[6];
                
        end      
        """
        expect = "Error on line 2 col 25: )"
        self.assertTrue(TestParser.test(input,expect,251))

    def test_index(self):
        """Simple program: int main() {} """
        input = """
        procedurE foo (b : real) ;
            begin
             1[1] := 1;
             (1>=0)[2] := 2+a[1][1]+c+("abc"< 0);
             ahihi(1)[m+1] := 3;
             (1+a[1]+(1<0))[10] := 4;
            End 
            
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,252))

    def test_var(self):
        input = """
        PROCEDURE main() ;
        var a, b, c : integer ;
            d: array [1 .. 5] of integer ;
            e , f : real ;
        BEGIN
        END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,253))

    def test_function(self):
        input = """
        FUNcTION foo(a, b: integer ; c: real):array [1 .. 2] of integer ;
        var x,y: real ;
        BEGIN
        END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,254))

    def test_procedure2(self):
        input = """
        proCeduRe foo(a, b: integer ; c: real) ;
        var x,y: real ;
        BEGIN
        END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,255))

    def test_assign33(self):
        input = """
        proCeduRe foo(a, b: integer ; c: real) ;
        var x,y: real ;
        BEGIN
            a := 1;
            b := a[12] ;
        END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,256))

    def test_assign44(self):
        input = """
        proCeduRe foo() ;
        var x,y: real ;
        BEGIN
            a := "conga";
            b := func(1,a+1) ;
        END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,257))

    def test_assign22(self):
        input = """
        proCeduRe foo(c: real) ;
        var x,y: real ;
        BEGIN 
            1 := 1;
            c := a[12] ;
        END"""
        expect = "Error on line 5 col 14: :="
        self.assertTrue(TestParser.test(input,expect,258))

    def test_assign34(self):
        input = """
        function foo(c: real): real ;
        var x,y: array[m..n] of real;
        BEGIN
            a[m+n] := a[m+1] ;
            foo()[m*1] := a[a div 3] ;
        END"""
        expect = "Error on line 3 col 23: m"
        self.assertTrue(TestParser.test(input,expect,259))

    def test_assign43(self):
        input = """
        function foo(c: real): real ;
        var x: integer ;
        BEGIN
            a[m+n] := a[m+1] := foo()[m*1] := a[a div 3] := (a>m) and then (b<n);
        END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,260))

    def test_assign5(self):
        input = """function foo(c: real): real ; x:=a[1]"""
        expect = "Error on line 1 col 30: x"
        self.assertTrue(TestParser.test(input,expect,261))

    def test_if(self):
        input = """
        function foo(c: real): real ;
        var x:real ;
        BEGIN
            if(a>1) then a:=1 ;
        END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,262))

    def test_if2(self):
        input = """
        pROCEDURE foo(c: real) ;
        var x:real ;
        BEGIN
            if(a>1) then a:=1 ;
            else foo();
        END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,263))

    def test_if3(self):
        input = """
        pROCEDURE foo(c: real) ;
        var x:real ;
        BEGIN
            if(a>1) then a:=1 ;
            else if (1<2)<>(2<3) then x:=1 ;
            else foo(a+1,2);
        END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,264))

    def test_if4(self):
        input = """
        pROCEDURE foo(c: real) ;
        var x:real ;
        BEGIN
            if(a>1) then a:=1 ;
            if (1<2) then beGin x:=1 ; end
            else foo(a+1,2);
        END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,265))

    def test_while1(self):
        input = """
        pROCEDURE foo(c: real) ;
        var x:real ;
        BEGIN
            whILe(a<>1) do beGin end
        END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,266))

    def test_while2(self):
        input = """
        pROCEDURE foo(c: real) ;
        var x:real ;
        BEGIN
            whILe(a<>1) do beGin
                if(a=1) then x:=1;
                foo();
            end
        END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,267))

    def test_while3(self):
        input = """
        pROCEDURE foo(c: real) ;
        var x:real ;
        BEGIN
            whILe(a<>1) do beGin
                while(1) do x:=1;
            end
        END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,268))

    def test_while4(self):
        input = """
        pROCEDURE foo(c: real) ;
        BEGIN
            whILe(a<>1) do beGin
                while(1) do x:=1;
                if(a=1) then begin end
            end
        END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,269))

    def test_with1(self):
        input = """
        pROCEDURE foo(c: real) ;
        BEGIN
            with a , b : integer ; c : array [1 .. 2] of real ; do
            d := c [a] + b ;
        END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,270))

    def test_with2(self):
        input = """
        pROCEDURE foo(c: real) ;
        BEGIN
            with a , b : integer ; c : array [1 .. 2] of real ; do begin
            d := c [a] + b ;
            foo();foo1(a,b,c);
            end
        END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,271))

    def test_with3(self):
        input = """
        pROCEDURE foo(c: real) ;
        BEGIN
            with a , b : integer ; c : array [1 .. 2] of real ; do begin
            d := c [a] + b ;
            foo();foo1(a,b,c);
            with a , b : integer ; do begin
                foo2(a,b,"anc");
            end
            end
        END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,272))

    def test_with4(self):
        input = """
        function foo(c: real): sTRIng;
        BEGIN
            with c , d : integer ; c : array [1 .. 2] of real ; do
                with a , b : integer ; do
                    foo2(a,b,"anc");
        END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,273))

    def test_for1(self):
        input = """
        function foo(c: real): sTRIng;
        BEGIN
            FOR i:=1 to m+10 do 
                s := s + 1;
        END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,274))

    def test_for2(self):
        input = """
        function foo(c: real): sTRIng;
        BEGIN
            FOR i:=1 to m+10 do beGin
                s := s + 1;
                if(a=1) then s:=s-1;
            end
        END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,275))

    def test_for3(self):
        input = """
        function foo(c: real): sTRIng;
        BEGIN
            FOR i:=1 to m+10 do beGin
                for j:=m+1 doWnTO 100 do beGin
                    s := s + 1;
                    if(a=1) then s:=s-1;
                eND
            end
        END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,276))

    def test_for4(self):
        input = """
        pROCEDURE foo(c: real);
        BEGIN
        FOR i:=1 to m+10 do beGin
            while i>1 do
                FOR i:=m+1 doWnTO 10 do
                    while j>1 do x:=foo(10);
        end
        END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,277))

    def test_break(self):
        input = """
        pROCEDURE foo(c: real);
        BEGIN
        FOR i:=1 to m+10 do beGin
            brEaK;
        end
        END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,278))

    def test_continue(self):
        input = """
        pROCEDURE foo(c: real);
        BEGIN
            while (1) do continuE ;
        END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,279))

    def test_return1(self):
        input = """
        pROCEDURE foo(c: real);
        BEGIN
            while (1) do reTuRn ;
        END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,280))

    def test_return2(self):
        input = """
        function foo(c: real): integer;
        BEGIN
            while (1) do reTuRn foo(a+1);
        END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,281))

    def test_compound(self):
        input = """
        function foo(c: real): integer;
        BEGIN
            while (1=1) do begin eND
        END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,282))

    def test_call1(self):
        input = """
        function foo(c: real): integer;
        BEGIN
            foo (3,a+1);
            foo1();
        END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,283))

    def test_call2(self):
        input = """
        function foo(c: real): integer;
        BEGIN
            foo(3,a+1,a<>1,a[1]);
            return 1;
        END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,284))

    def test_call3(self):
        input = """
        function foo(c: real): integer;
        BEGIN
            foo(3,a+1,x and then y,a[1],foo(1,2)[m+1]);
            return foo2();
        END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,285))

    def test_program1(self):
        input = """
        procedurE foo () ;
            begin
            End           
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,286))

    def test_program2(self):
        input = """
        function main (): real ;
            begin
            End            
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,287))

    def test_program3(self):
        input = """
        var a, b, c : integer ;
                    d: array [1 .. 5] of integer ;
                    e , f : real ;
            
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,288))

    def test_more_complex_program1(self):
        input = """
            proceDure main ():  real ;BEGIN
            putIntLn(4);
            end
        """
        expect = "Error on line 2 col 29: :"
        self.assertTrue(TestParser.test(input,expect,289))
    
    def test_more_complex_program2(self):
        input = """
            function main () ;BEGIN
            return 0;
            end
        """
        expect = "Error on line 2 col 29: ;"
        self.assertTrue(TestParser.test(input,expect,290))

    def test_more_complex_program3(self):
        input = """proceDure main () ;
        var x,y: array [1 .. 5] of integer;
        BEGIN
            putIntLn(4);
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,291))

    def test_wrong_miss_close1(self):
        input = """proceDure main( beGin end"""
        expect = "Error on line 1 col 16: beGin"
        self.assertTrue(TestParser.test(input,expect,292))
    
    def test_wrong_miss_close2(self):
        input = """function main( beGin end"""
        expect = "Error on line 1 col 15: beGin"
        self.assertTrue(TestParser.test(input,expect,293))

    def test_if5(self):
        input = """
        function foo():real;
        begin
        if (color = red) then
            writeln("You have chosen a red car");
        else
            writeln("Please choose a color for your car");
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,294))

    def test_if6(self):
        input = """
        function foo():real;
        begin
        if( a < 20 ) then
            (* if condition is true then print the following *)
            writeln("a is less than 20" );
        
        else
            (* if condition is false then print the following *) 
            writeln("a is not less than 20" );
            writeln("value of a is : ", a);
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,295))

    def test_if7(self):
        input = """
        procedure main();
        var
            { local variable definition }
            a : integer;
        begin
        a := 100;
        (* check the boolean condition *)
        if( a < 20 ) then
            (* if condition is true then print the following *)
            writeln("a is less than 20" );
        
        else
            (* if condition is false then print the following *) 
            writeln("a is not less than 20" );
            writeln("value of a is : ", a);
        end     
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,296))

    def test_if8(self):
        input = """
        procedure main();
        begin
            if (a <= 20) then
            c:= c+1;
            else 
            begin end
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,297))

    def test_if9(self):
        input = """
        procedure main();
        begin
            if (a <= 20) then
            c:= c+1;
            else 
            else
            begin end
        end 
        """
        expect = "Error on line 7 col 12: else"
        self.assertTrue(TestParser.test(input,expect,298))

    def test_while5(self):
        input = """
        procedure main();
        begin
        a := 10;
        while  a < 20  do
            begin
                writeln("value of a: ", a);
                a := a + 1;
            end
        end
    
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,299))

    def test_while6(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,300))

    
    
    
    
    
    
    
    
    
    