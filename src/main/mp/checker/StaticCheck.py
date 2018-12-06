
"""
 * @author nhphung
 * modified by Hoang Kim
"""
from AST import * 
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import *

checkType = None
class MType:
    def __init__(self,partype,rettype):
        self.partype = partype
        self.rettype = rettype
    def __str__(self):
        return 'MType([' + ','.join(str(i) for i in self.partype) + ']' + ',' + str(self.rettype) + ')'
     
class Symbol:
    def __init__(self,name,mtype,value = None):
        self.name = name
        self.mtype = mtype
        self.value = value
    def __str__(self):
        return 'Symbol(' + self.name + ',' + str(self.mtype) + ')'

class StaticChecker(BaseVisitor,Utils):
    global_envi = [
                Symbol("getInt",MType([],IntType())),
    			Symbol("putInt",MType([IntType()],VoidType())),
                Symbol("putIntLn",MType([IntType()],VoidType())),
                Symbol("getFloat",MType([],FloatType())),
                Symbol("putFloat",MType([FloatType()],VoidType())),
                Symbol("putFloatLn",MType([FloatType()],VoidType())),
                Symbol("putBool",MType([BoolType()],VoidType())),
                Symbol("putBoolLn",MType([BoolType()],VoidType())),
                Symbol("putString",MType([StringType()],VoidType())),
                Symbol("putStringLn",MType([StringType()],VoidType())),
                Symbol("putLn",MType([],VoidType()))
    ]
            
    def __init__(self,ast):
        self.ast = ast  

    def check(self):
        self.visit(self.ast,[StaticChecker.global_envi[:]])
        return []

    def checkRedeclared(self,sym,kind,env):
        if self.lookup(sym.name.lower(), env, lambda x:x.name.lower()):
            raise Redeclared(kind,sym.name)
        return sym

    def checkBreakContinue(self,_stmt):
        if type(_stmt) is If:
            for i in _stmt.thenStmt:
                if type(i) is Break:
                    raise BreakNotInLoop()
                elif type(i) is Continue:
                    raise ContinueNotInLoop()
            for i in _stmt.elseStmt:
                if type(i) is Break:
                    raise BreakNotInLoop()
                elif type(i) is Continue:
                    raise ContinueNotInLoop()
        elif type(_stmt) is With:
            for i in _stmt.stmt:
                if type(i) is Break:
                    raise BreakNotInLoop()
                elif type(i) is Continue:
                    raise ContinueNotInLoop()

    def checkCorrectReturn(self,retType,returnStmt,env):
        if type(retType) is VoidType:
            if not returnStmt.expr is None:
                raise TypeMismatchInStatement(returnStmt)
        else:
            if returnStmt.expr is None:
                raise TypeMismatchInStatement(returnStmt)
            else:
                exp_type = self.visit(returnStmt.expr,env)
                if type(exp_type) != type(retType):
                    if type(retType) is FloatType and type(exp_type) is IntType:
                        pass
                    else:
                        raise TypeMismatchInStatement(returnStmt)
                else:
                    if type(retType) is ArrayType:
                        if type(retType.eleType) == type(exp_type.eleType) and retType.lower == exp_type.lower and retType.upper == exp_type.upper:
                            pass
                        else:
                            raise TypeMismatchInStatement(returnStmt)

    def visitProgram(self,ast, c): 
        for x in ast.decl:
            if type(x) is VarDecl:
                c[0] += [self.visit(x,c[:])]
            else:
                c[0] += [self.checkRedeclared(Symbol(x.name.name,MType([i.varType for i in x.param],x.returnType)), Procedure() if type(x.returnType) is VoidType else Function(),c[0])]
        for i in ast.decl:
            if type(i) is FuncDecl:
                sym_main = self.lookup('main',c[0],lambda x:x.name.lower())
                if not sym_main or not type(sym_main.mtype) is MType or not type(sym_main.mtype.rettype) is VoidType or sym_main.mtype.partype != []:
                    raise NoEntryPoint()
                self.visit(i,c[:])

    # Decl
    def visitVarDecl(self,ast,c):
        # variable:Id
        # varType: Type
        return self.checkRedeclared(Symbol(ast.variable.name,ast.varType),Variable(),c[0])

    def visitFuncDecl(self, ast, c):
        #name: Id
        #param: list(VarDecl)
        #returnType: Type => VoidType for Procedure
        #local:list(VarDecl)
        #body: list(Stmt)
        global checkType
        checkType = ast.returnType
        c = [[]] + c
        lst_checkNotReturn = []
        gotReturn = False
        for x in ast.param:
            c[0] += [self.checkRedeclared(Symbol(x.variable.name,x.varType),Parameter(),c[0])]
        for x in ast.local:
            c[0] += [self.visit(x,c[:])]
        for x in ast.body:
            # Check Return trong Func trả về đúng kiểu 
            if type(x) is Return:
                gotReturn = True
                self.checkCorrectReturn(ast.returnType,x,c)
            else:
                if type(x) is Break:
                    raise BreakNotInLoop()
                elif type(x) is Continue:
                    raise ContinueNotInLoop()
                self.checkBreakContinue(x)
                # True khi Stmt có Return, False ngược lại 
                lst_checkNotReturn += [self.visit(x,c[:])]
        # Check FuncNotReturn
        if not type(ast.returnType) is VoidType:
            res = reduce(lambda x,y: x or y,lst_checkNotReturn,False)
            if res == False and not gotReturn:
                raise FunctionNotReturn(ast.name.name)
        checkType =None

    # Stmt
    def visitAssign(self,ast,c):
        #lhs:Expr
        #exp:Expr
        lhstype = self.visit(ast.lhs,c)
        exptype = self.visit(ast.exp,c)
        if type(lhstype) in [IntType,FloatType,BoolType]:
            if type(lhstype) == type(exptype):
                pass
            elif type(lhstype) is FloatType and type(exptype) is IntType:
                pass
            else:
                raise TypeMismatchInStatement(ast)
        else:
            raise TypeMismatchInStatement(ast)
        return False
 
    def visitIf(self,ast,c):
        #expr:Expr
        #thenStmt:list(Stmt)
        #elseStmt:list(Stmt)
        checkReturnThen = False
        checkReturnElse = False
        expr_type = self.visit(ast.expr,c)
        if not type(expr_type) is BoolType:
            raise TypeMismatchInStatement(ast)
        for x in ast.thenStmt:
            self.checkBreakContinue(x)
            resThen = self.visit(x,c[:])
            if resThen:
                checkReturnThen = True
        for x in ast.elseStmt:
            self.checkBreakContinue(x)
            resElse = self.visit(x,c[:])
            if resElse:
                checkReturnElse = True
        return checkReturnElse and checkReturnThen

    def visitWhile(self,ast,c):
        #exp: Expr
        #sl:list(Stmt)
        exp_type = self.visit(ast.exp,c)
        if not type(exp_type) is BoolType:
            raise TypeMismatchInStatement(ast)
        for x in ast.sl:
            self.visit(x,c[:])
        return False

    def visitFor(self,ast,c):
        #id:Id
        #expr1,expr2:Expr
        #loop:list(Stmt)
        #up:Boolean #True => increase; False => decrease
        for x in c:
            sym_id = self.lookup(ast.id.name.lower(),x,lambda x:x.name.lower())
            if sym_id:
                break
        if sym_id:
            id_type = sym_id.mtype
        else:
            raise Undeclared(Identifier(),ast.id.name)
        expr1_type = self.visit(ast.expr1,c)
        expr2_type = self.visit(ast.expr2,c)
        if not (type(id_type) is IntType and type(expr1_type) is IntType and type(expr2_type) is IntType):
            raise TypeMismatchInStatement(ast)
        for x in ast.loop:
            self.visit(x,c[:])
        return False

    def visitBreak(self,ast,c):
        return False

    def visitContinue(self,ast,c):
        return False

    def visitReturn(self,ast,c):
        #expr:Expr
        self.checkCorrectReturn(checkType,ast,c)
        return True
        
    def visitWith(self,ast,c):
        #decl:list(VarDecl)
        #stmt:list(Stmt)
        checkReturn = False
        c = [[]] + c
        for x in ast.decl:
            c[0] += [self.checkRedeclared(Symbol(x.variable.name,x.varType),Variable(),c[0])]
        for x in ast.stmt:
            self.checkBreakContinue(x)
            res = self.visit(x,c[:])
            if res:
                checkReturn = True
        return checkReturn

    def visitCallStmt(self, ast, c): 
        #method:Id
        #param:list(Expr)
        for x in c:
            sym = self.lookup(ast.method.name.lower(),x,lambda x: x.name.lower())
            if sym:
                break
        if not sym or not type(sym.mtype) is MType or not type(sym.mtype.rettype) is VoidType:
            raise Undeclared(Procedure(),ast.method.name)
        else:
            lst_param_actual = [self.visit(x,c) for x in ast.param]
            lst_param_formal = [x for x in sym.mtype.partype]
            if len(lst_param_actual) != len(lst_param_formal):
                raise TypeMismatchInStatement(ast)
            else:
                lst_compare = list(zip(lst_param_actual,lst_param_formal))
                for i in lst_compare:
                    if type(i[0]) != type(i[1]) :
                        if type(i[0]) is IntType and type(i[1]) is FloatType:
                            pass
                        else:
                            raise TypeMismatchInStatement(ast)
                    else:
                        if type(i[0]) is ArrayType:
                            if type(i[0].eleType) != type(i[1].eleType) or i[0].lower != i[1].lower or i[0].upper != i[1].upper:
                                raise TypeMismatchInStatement(ast)                  
        return False

    # Exp
    def visitId(self,ast,c):
        #name:string
        for x in c:
            sym = self.lookup(ast.name.lower(),x,lambda x:x.name.lower())
            if sym:
                break
        if sym:
            if type(sym.mtype) is MType:
                    return sym.mtype.rettype
            else:
                    return sym.mtype
        raise Undeclared(Identifier(),ast.name)
    
    def visitArrayCell(self,ast,c):
        #arr:Expr
        #idx:Expr
        arrtype = self.visit(ast.arr,c)
        idxtype = self.visit(ast.idx,c)
        if not type(arrtype) is ArrayType:
            raise TypeMismatchInExpression(ast)
        else:
            if not type(idxtype) is IntType:
                raise TypeMismatchInExpression(ast)
            # arr là ArrayType thì chỉ có thể là Id hoặc CallEpxr
            if type(ast.arr) is Id:
                for x in c:
                    sym_arr = self.lookup(ast.arr.name.lower(),x,lambda x:x.name.lower())
                    if sym_arr:
                        break
                if not sym_arr or type(sym_arr.mtype) is MType:
                    raise Undeclared(Identifier(),ast.arr.name)
                else:
                    return sym_arr.mtype.eleType
            elif type(ast.arr) is CallExpr:
                for x in c:
                    sym_arr = self.lookup(ast.arr.method.name.lower(),x,lambda x:x.name.lower())
                    if sym_arr:
                        break
                if not sym_arr or not type(sym_arr.mtype) is MType:
                    raise Undeclared(Function(),ast.arr.name)
                else:
                    return sym_arr.mtype.rettype.eleType
            
    def visitBinaryOp(self,ast,c):
        #op:string: AND THEN => andthen; OR ELSE => orelse; other => keep it
        #left:Expr
        #right:Expr
        lefttype = self.visit(ast.left, c)
        righttype = self.visit(ast.right,c)
        if type(lefttype) != type(righttype):
            if type(lefttype) in [IntType,FloatType] and type(righttype) in [IntType,FloatType]:
                if ast.op in ['+','-','*','/']:
                    return FloatType()
                elif ast.op in ['<','<=','>','>=','=','<>']:
                    return BoolType()
        elif type(lefttype) == type(righttype):
            if type(lefttype) is BoolType:
                if ast.op.lower() in ['and','andthen','or','orelse']:
                    return BoolType()
            elif type(lefttype) is IntType:
                if ast.op.lower() in ['+','-','*','div','mod']:
                    return IntType()
                elif ast.op.lower() in ['<','<=','>','>=','=','<>']:
                    return BoolType()
                elif ast.op == '/':
                    return FloatType()
            elif type(lefttype) is FloatType:
                if ast.op in ['+','-','*','/']:
                    return FloatType()
                elif ast.op in ['=','<>','<','<=','>','>=']:
                    return BoolType()
        raise TypeMismatchInExpression(ast)

    def visitUnaryOp(self,ast,c):
        #op:string
        #body:Expr
        bodytype = self.visit(ast.body,c)
        if ast.op.lower() == 'not':
            if type(bodytype) is BoolType:
                return BoolType()
        elif ast.op == '-':
            if type(bodytype) in [IntType,FloatType]:
                return bodytype
        raise TypeMismatchInExpression(ast) 

    def visitCallExpr(self,ast,c):
        #method:Id
        #param:list(Expr)
        for x in c:
            sym = self.lookup(ast.method.name.lower(),x,lambda x: x.name.lower())
            if sym:
                break
        if not sym or not type(sym.mtype) is MType or type(sym.mtype.rettype) is VoidType:
            raise Undeclared(Function(),ast.method.name)
        else:
            lst_param_actual = [self.visit(x,c) for x in ast.param]
            lst_param_formal = [x for x in sym.mtype.partype]
            if len(lst_param_actual) != len(lst_param_formal):
                raise TypeMismatchInExpression(ast)
            else:
                lst_compare = list(zip(lst_param_actual,lst_param_formal))
                for i in lst_compare:
                    if type(i[0]) != type(i[1]) :
                        if type(i[0]) is IntType and type(i[1]) is FloatType:
                            pass
                        else:
                            raise TypeMismatchInExpression(ast)
                    else:
                        if type(i[0]) is ArrayType:
                            if type(i[0].eleType) != type(i[1].eleType) or i[0].lower != i[1].lower or i[0].upper != i[1].upper:
                                raise TypeMismatchInExpression(ast)
            return sym.mtype.rettype
        
    def visitIntLiteral(self,ast, c): 
        return IntType()
    
    def visitFloatLiteral(self,ast, c): 
        return FloatType()

    def visitStringLiteral(self,ast, c): 
        return StringType()

    def visitBooleanLiteral(self,ast, c): 
        return BoolType()