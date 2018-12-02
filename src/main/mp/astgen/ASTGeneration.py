from MPVisitor import MPVisitor
from MPParser import MPParser
from AST import *

list_stmt = []
def ListDecl(lst:MPParser.Var_listContext,mtype:MPParser.Var_typeContext):
    VarList = []
    if mtype.INTEGER() is not None:
        returnType = IntType()
    elif mtype.REAL() is not None:
        returnType = FloatType()
    elif mtype.BOOLEAN() is not None:
        returnType = BoolType()
    elif mtype.STRING() is not None:
        returnType = StringType()
    else:
        mtype = mtype.array_type()
        up = str(mtype.upper_lower(0).getText())
        low = str(mtype.upper_lower(1).getText())
        if mtype.INTEGER() is not None:
            returnType = ArrayType(up,low,IntType())
        elif mtype.REAL() is not None:
            returnType = ArrayType(up,low,FloatType())
        elif mtype.BOOLEAN() is not None:
            returnType = ArrayType(up,low,BoolType())
        else:
            returnType = ArrayType(up,low,StringType())
    return VarDecl(Id(lst.ID().getText()), returnType)
class ASTGeneration(MPVisitor):
    # program: decl+ EOF;
    def visitProgram(self,ctx:MPParser.ProgramContext):
        return Program([self.visit(x) for x in ctx.decl()])

    # decl: var_decl | func_decl | proc_decl;
    def visitDecl(self,ctx:MPParser.DeclContext):
        return self.visit(ctx.getChild(0))

    # var_decl: VAR var_decl_list;
    def visitVar_decl(self,ctx:MPParser.Var_declContext):
        return self.visit(ctx.var_decl_list())
        
    # var_decl_list: one_line_decl var_decl_list?;
    # one_line_decl: var_list COLON var_type SEMI;
    # var_list: ID (COMMA var_list)?;
    def visitVar_decl_list(self,ctx:MPParser.Var_decl_listContext):
        result = ""
        getOneline = ctx
        getID = getOneline.one_line_decl().var_list()
        getType = getOneline.one_line_decl().var_type() 
        while(1):   # var_decl_list handle           
            while(1): # one_line_decl handle
                ele = str(ListDecl(getID,getType))
                result += "," + ele 
                if getID.var_list() is not None:
                    getID = getID.var_list()
                else:
                    break
            if getOneline.var_decl_list() is not None:
                getOneline = getOneline.var_decl_list()
                getID = getOneline.one_line_decl().var_list()
                getType = getOneline.one_line_decl().var_type()      
            else:
                break   
        return result[1:]
         
    # FUNCTION ID LB para_decl? RB COLON var_type SEMI var_decl? compound_stmt;
    def visitFunc_decl(self,ctx:MPParser.Func_declContext):
        return FuncDecl(Id(ctx.ID().getText()),
                        [self.visit(ctx.para_decl())] if ctx.para_decl() else [], #param
                        [self.visit(ctx.var_decl())] if ctx.var_decl() else [],   #local
                        self.visit(ctx.compound_stmt()) if ctx.compound_stmt() else [],                        #body
                        self.visit(ctx.var_type())
        )

    # PROCEDURE ID LB para_decl? RB SEMI var_decl? compound_stmt;
    def visitProc_decl(self,ctx:MPParser.Proc_declContext):
        return FuncDecl(Id(ctx.ID().getText()),
                        [self.visit(ctx.para_decl())] if ctx.para_decl() else [], #param
                        [self.visit(ctx.var_decl())] if ctx.var_decl() else [],   #local
                        self.visit(ctx.compound_stmt()) if ctx.compound_stmt() else [], #body
                        VoidType()
        )

    # para_decl: one_para_decl (SEMI para_decl)?;
    # one_para_decl: var_list COLON var_type;
    def visitPara_decl(self,ctx:MPParser.Para_declContext):
        result = ""
        getOneline = ctx
        getID = getOneline.one_para_decl().var_list()
        getType = getOneline.one_para_decl().var_type() 
        while(1):   # para_decl handle           
            while(1): # one_para_decl handle
                ele = str(ListDecl(getID,getType))
                result += "," + ele 
                if getID.var_list() is not None:
                    getID = getID.var_list()
                else:
                    break
            if getOneline.para_decl() is not None:
                getOneline = getOneline.para_decl()
                getID = getOneline.one_para_decl().var_list()
                getType = getOneline.one_para_decl().var_type()
            else:
                break   
        return result[1:]

    def visitStmt(self,ctx:MPParser.StmtContext):
        return self.visit(ctx.getChild(0))

    # compound_stmt: BEGIN stmt* END
    def visitCompound_stmt(self,ctx:MPParser.Compound_stmtContext):
        result = []
        for check_compound in ctx.stmt():
            x = self.visit(check_compound)
            if isinstance(x,list):
                result += x
            else:
                result.append(str(x))
        return result
        #return [j for i in ctx.stmt() for j in self.visit(i)]

    # assign_stmt: ((ids | index_exp) ASSIGN)+ exp;
    def visitAssign_stmt(self, ctx:MPParser.Assign_stmtContext):
        num_lhs = ctx.getChildCount() -1
        result = ""
        while num_lhs > 1:
            result += "," + str(Assign(self.visit(ctx.getChild(num_lhs-2)),
                                        self.visit(ctx.getChild(num_lhs)))
            )
            num_lhs -= 2
        return result[1:]

    # if_stmt: IF exp THEN stmt (ELSE stmt)?;
    def visitIf_stmt(self, ctx:MPParser.If_stmtContext):
        if ctx.stmt(0).compound_stmt() is None:
            then_body = [self.visit(ctx.stmt(0))]
        else:
            then_body = self.visit(ctx.stmt(0))
        if ctx.getChildCount() == 6:
            if ctx.stmt(1).compound_stmt() is None:
                else_body = [self.visit(ctx.stmt(1))]
            else:
                else_body = self.visit(ctx.stmt(1))
            return If(self.visit(ctx.exp()),
                        then_body,
                        else_body
            )
        else:
            return If(self.visit(ctx.exp()),
                        then_body,
                        []
            )

    # while_stmt: WHILE exp DO stmt;
    def visitWhile_stmt(self, ctx:MPParser.While_stmtContext):
        if ctx.stmt().compound_stmt() is None:
            while_body = [self.visit(ctx.stmt())]
        else:
            while_body = self.visit(ctx.stmt())
        return While(self.visit(ctx.exp()),
                    while_body
        )

    # for_stmt: FOR ID ASSIGN exp (TO | DOWNTO) exp DO stmt;
    def visitFor_stmt(self, ctx:MPParser.For_stmtContext):
        if ctx.TO():
            up = True
        elif ctx.DOWNTO():
            up = False
        if ctx.stmt().compound_stmt() is None:
            for_body = [self.visit(ctx.stmt())]
        else:
            for_body = self.visit(ctx.stmt())
        return For(Id(ctx.ID().getText()),
                    self.visit(ctx.exp(0)),
                    self.visit(ctx.exp(1)),
                    up,
                    for_body
        )

    # break_stmt: BREAK;
    def visitBreak_stmt(self, ctx:MPParser.Break_stmtContext):
        return Break()

    # continue_stmt: CONTINUE;
    def visitContinue_stmt(self,ctx:MPParser.Continue_stmtContext):
        return Continue()

    # return_stmt: RETURN exp?;
    def visitReturn_stmt(self, ctx:MPParser.Return_stmtContext):
        if ctx.exp():
            return Return(self.visit(ctx.exp()))
        else:
            return Return(None)

    # with_stmt: WITH var_decl_list DO stmt;
    def visitWith_stmt(self, ctx:MPParser.With_stmtContext):
        if ctx.stmt().compound_stmt() is None:
            with_body = [self.visit(ctx.stmt())]
        else:
            with_body = self.visit(ctx.stmt())
        return With([self.visit(ctx.var_decl_list())],
                    with_body
        )

    # call_stmt: ID LB exp_list? RB SEMI;
    def visitCall_stmt(self,ctx:MPParser.Call_stmtContext):
        return CallStmt(Id(ctx.ID().getText()),
                        self.visit(ctx.exp_list()) if ctx.exp_list() else []
        )

    # exp_list: exp (COMMA exp)*;
    def visitExp_list(self, ctx:MPParser.Exp_listContext):
        return [self.visit(x) for x in ctx.exp()]

    # exp: exp (AND THEN | OR ELSE) exp1
    #    | exp1;
    def visitExp(self, ctx:MPParser.ExpContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp1())
        else:
            if (ctx.AND() and ctx.THEN()):
                op = "andthen"       
            elif (ctx.OR() and ctx.ELSE()):
                op = "orelse"
            return BinaryOp(op,
                            self.visit(ctx.exp()),
                            self.visit(ctx.exp1())
                )

    # exp1: exp2 ((EQUAL | NOT_EQUAL | LESS | LE | GREATER | GE) exp2)?;
    def visitExp1(self, ctx:MPParser.Exp1Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp2(0))
        else:
            return BinaryOp (ctx.getChild(1).getText(),
                            self.visit(ctx.exp2(0)),
                            self.visit(ctx.exp2(1))
            )

    # exp2: exp2 (PLUS | SUBTRACTION | OR) exp3
    #     | exp3;
    def visitExp2(self, ctx:MPParser.Exp2Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp3())
        else:
            return BinaryOp (ctx.getChild(1).getText(),
                            self.visit(ctx.exp2()),
                            self.visit(ctx.exp3())
            )

    # exp3: exp3 (DIVISION | MULTIPLICATION | DIV | MOD | AND) exp4
    #     | exp4;
    def visitExp3(self, ctx:MPParser.Exp3Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp4())
        else:
            return BinaryOp (ctx.getChild(1).getText(),
                            self.visit(ctx.exp3()),
                            self.visit(ctx.exp4())
            )

    # exp4: (SUBTRACTION | NOT) exp4 | exp5;
    def visitExp4(self, ctx:MPParser.Exp4Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp5())
        else:
            return UnaryOp (ctx.getChild(0).getText(),
                            self.visit(ctx.exp4())
            )

    # exp5: exp6 (LS exp RS)*;
    def visitExp5(self, ctx:MPParser.Exp5Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp6())
        else:
            return ArrayCell(self.visit(ctx.exp6()),
                            self.visit(ctx.exp(0))
            )

    # exp6: (LB exp RB)+ | exp7;
    def visitExp6(self, ctx:MPParser.Exp6Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp7())
        else:
            return self.visit(ctx.exp())

    # exp7: operand | funcall;
    def visitExp7(self, ctx:MPParser.Exp7Context):
        return self.visit(ctx.getChild(0))

    # funcall: ID LB exp_list? RB;
    def visitFuncall(self,ctx:MPParser.FuncallContext):
        return CallExpr(Id(ctx.ID().getText()),
                        self.visit(ctx.exp_list()) if ctx.exp_list() else []
        )

    # operand: INTLIT | FLOATLIT | STRINGLIT | BOOLLIT | ID;
    def visitOperand(self, ctx:MPParser.OperandContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.INTLIT():
            return IntLiteral(int(ctx.INTLIT().getText()))
        elif ctx.FLOATLIT():
            return FloatLiteral(float(ctx.FLOATLIT().getText()))
        elif ctx.STRINGLIT():
            return StringLiteral(ctx.STRINGLIT().getText())
        else:
            #return BooleanLiteral(ctx.BOOLLIT().getText())
            return BooleanLiteral(False if ctx.BOOLLIT().getText()[0] in ["F","f"] else True)

    # index_exp: exp LS exp RS;
    def visitIndex_exp(self, ctx:MPParser.Index_expContext):
        return ArrayCell(self.visit(ctx.exp(0)),
                        self.visit(ctx.exp(1))
        )

    # ids: ID;
    def visitIds(self, ctx:MPParser.IdsContext):
        return Id(ctx.ID().getText())

    # var_type: INTEGER | REAL | BOOLEAN | STRING | array_type;
    def visitVar_type(self, ctx:MPParser.Var_typeContext):
        if ctx.INTEGER():
            return IntType()
        elif ctx.REAL():
            return FloatType()
        elif ctx.BOOLEAN():
            return BoolType()
        elif ctx.STRING():
            return StringType()
        else:
            return self.visit(ctx.array_type())

    # array_type:
    # ARRAY LS upper_lower DOUBLE_DOT upper_lower RS OF (
    #   BOOLEAN
    #   | INTEGER
    #   | REAL
    #   | STRING
    # );
    def visitArray_type(self, ctx:MPParser.Array_typeContext):
        if ctx.BOOLEAN():
            returnType = BoolType()
        elif ctx.INTEGER():
            returnType = IntType()
        elif ctx.REAL():
            returnType = FloatType()
        else:
            returnType = StringType()
        return ArrayType(self.visit(ctx.upper_lower(0)),
                        self.visit(ctx.upper_lower(1)),
                        returnType  
        )

    def visitUpper_lower(self,ctx:MPParser.Upper_lowerContext):
        result = int(str(ctx.INTLIT().getText()))
        return (result * -1 if ctx.SUBTRACTION() else result)