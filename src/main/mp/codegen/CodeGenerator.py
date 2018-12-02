'''
 *   @author Nguyen Hua Phung
 *   @version 1.0
 *   23/10/2015
 *   This file provides a simple version of code generator
 *
'''
from Utils import *
from StaticCheck import *
from StaticError import *
from Emitter import Emitter
from Frame import Frame
from abc import ABC, abstractmethod
from ASTGeneration import ASTGeneration

class CodeGenerator(Utils):
    def __init__(self):
        self.libName = "io"

    def init(self):
        return [Symbol("getInt", MType(list(), IntType()), CName(self.libName)),
                    Symbol("putInt", MType([IntType()], VoidType()), CName(self.libName)),
                    Symbol("putIntLn", MType([IntType()], VoidType()), CName(self.libName)),
                    Symbol("getFloat",MType([],FloatType()), CName(self.libName)),
                    Symbol("putFloat",MType([FloatType()],VoidType()), CName(self.libName)),
                    Symbol("putFloatLn",MType([FloatType()],VoidType()), CName(self.libName)),
                    Symbol("putBool",MType([BoolType()],VoidType()), CName(self.libName)),
                    Symbol("putBoolLn",MType([BoolType()],VoidType()), CName(self.libName)),
                    Symbol("putString",MType([StringType()],VoidType()),CName(self.libName) ),
                    Symbol("putStringLn",MType([StringType()],VoidType()), CName(self.libName)),
                    Symbol("putLn",MType([],VoidType()), CName(self.libName))
                    ]

    def gen(self, ast, dir_):
        #ast: AST
        #dir_: String

        gl = self.init()
        gc = CodeGenVisitor(ast, gl, dir_)
        gc.visit(ast, None)

# class StringType(Type):
    
#     def __str__(self):
#         return "StringType"

#     def accept(self, v, param):
#         return None

class ArrayPointerType(Type):
    def __init__(self, ctype):
        #cname: String
        self.eleType = ctype

    def __str__(self):
        return "ArrayPointerType({0})".format(str(self.eleType))

    def accept(self, v, param):
        return None

class ClassType(Type):
    def __init__(self,cname):
        self.cname = cname
    def __str__(self):
        return "Class({0})".format(str(self.cname))
    def accept(self, v, param):
        return None
        
class SubBody():
    def __init__(self, frame, sym):
        #frame: Frame
        #sym: List[Symbol]

        self.frame = frame
        self.sym = sym

class Access():
    def __init__(self, frame, sym, isLeft, isFirst):
        #frame: Frame
        #sym: List[Symbol]
        #isLeft: Boolean
        #isFirst: Boolean

        self.frame = frame
        self.sym = sym
        self.isLeft = isLeft
        self.isFirst = isFirst

class Val(ABC):
    pass

class Index(Val):
    def __init__(self, value):
        #value: Int

        self.value = value

class CName(Val):
    def __init__(self, value):
        #value: String

        self.value = value

class CodeGenVisitor(BaseVisitor, Utils):
    def __init__(self, astTree, env, dir_):
        #astTree: AST
        #env: List[Symbol]
        #dir_: File

        self.astTree = astTree
        self.env = env
        self.className = "MPClass"
        self.path = dir_
        self.emit = Emitter(self.path + "/" + self.className + ".j")

    def visitProgram(self, ast, c):
        #ast: Program
        #c: Any
        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))
        for x in ast.decl:
            if type(x) is VarDecl:
                self.env += [Symbol(x.variable.name,x.varType, CName(self.className))]
                self.emit.printout(self.emit.emitATTRIBUTE(x.variable.name, x.varType,False,""))
            else:
                self.env += [Symbol(x.name.name,MType([i.varType for i in x.param ] if len(x.param)>0 else [],x.returnType), CName(self.className))]
        #e = SubBody(None, self.env)
        for x in ast.decl:
            self.visit(x, SubBody(None,self.env[:]))
        # generate default constructor
        a = self.genMETHOD(FuncDecl(Id("<init>"), list(), list(), list(),None), c, Frame("<init>", VoidType))
        self.emit.emitEPILOG()
        return c

    def genMETHOD(self, consdecl, o, frame):
        #consdecl: FuncDecl
        #o: Any
        #frame: Frame
        isInit = consdecl.returnType is None
        isMain = consdecl.name.name == "main" and len(consdecl.param) == 0 and type(consdecl.returnType) is VoidType
        returnType = VoidType() if isInit else consdecl.returnType
        methodName = "<init>" if isInit else consdecl.name.name
        intype = [ArrayPointerType(StringType())] if isMain else [x.varType for x in consdecl.param]
        mtype = MType(intype, returnType)

        a =  self.emit.emitMETHOD(methodName, mtype, not isInit, frame)
        self.emit.printout(a)
        frame.enterScope(True)

        # Generate code for parameter declarations
        if isInit:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(self.className), frame.getStartLabel(), frame.getEndLabel(), frame))
        else:
            glenv = o.sym
            if isMain: self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayPointerType(StringType()), frame.getStartLabel(), frame.getEndLabel(), frame))
            else:
                for x in consdecl.param:
                    idx = frame.getNewIndex()
                    glenv += [Symbol(x.variable.name, x.varType, Index(idx))]
                    c = self.emit.emitVAR(idx,x.variable.name,x.varType,frame.getStartLabel(), frame.getEndLabel(),frame)
                    self.emit.printout(c)
                    #idx += 1
            for x in consdecl.local:
                idx = frame.getNewIndex()
                glenv += [Symbol(x.variable.name, x.varType, Index(idx))]
                d = self.emit.emitVAR(idx,x.variable.name,x.varType,frame.getStartLabel(), frame.getEndLabel(),frame)
                self.emit.printout(d)
                #idx += 1

        body = consdecl.body
        b = self.emit.emitLABEL(frame.getStartLabel(), frame)
        self.emit.printout(b)

        # Generate code for statements
        if isInit:
            self.emit.printout(self.emit.emitREADVAR("this", ClassType(self.className), 0, frame))
            self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
        for x in body:
            self.visit(x, SubBody(frame, glenv))

        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        if type(returnType) is VoidType:
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()

    def visitFuncDecl(self, ast, o):
        subctxt = o
        frame = Frame(ast.name, ast.returnType)
        self.genMETHOD(ast, subctxt, frame)
        return o
        #return SubBody(None, [Symbol(ast.name.name, MType([i for i in ast.param], ast.returnType), CName(self.className))]+ o.sym[1])

    def visitVarDecl(self,ast,o):
        vtype = ast.varType
        if type(vtype) is ArrayType: raise Exception("No Array Pls")
        #self.emit.printout(self.emit.emitATTRIBUTE(ast.variable.name,vtype,False,""))
        #return None 
        return SubBody(None,[Symbol(ast.variable.name,vtype,CName(self.className))]+o.sym)

    def visitAssign(self,ast,o):
        rc, rt = self.visit(ast.exp,Access(o.frame,o.sym,False,True))
        lc,lt = self.visit(ast.lhs,Access(o.frame,o.sym,True,False))
        if type(lt) is FloatType and type(rt) is IntType:
            self.emit.printout(rc + self.emit.emitI2F(None) +lc)
            #self.emit.emitI2F(None)
        else:
            self.emit.printout(rc+lc)
        pass

    def visitCallStmt(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        sym = self.lookup(ast.method.name.lower(), nenv, lambda x: x.name.lower())
        cname = sym.value.value
    
        ctype = sym.mtype

        in_ = ("", list())
        for idx, val in enumerate(ast.param):
            str1, typ1 = self.visit(val, Access(frame, nenv, False, True))
            in_ = (in_[0] + str1, in_[1] + [typ1])
            if type(sym.mtype.partype[idx]) is FloatType and type(in_[1][idx]) is IntType:
                in_ = (in_[0] + self.emit.emitI2F(frame), in_[1])
            
        #self.emit.printout(in_[0])
        #checkPrintIntWithPutFloat = (cname + "/" + sym.name)
        #if checkPrintIntWithPutFloat in ['io/putFloat','io/putFloatLn'] and type(in_[1][0]) is IntType:
        #    buonNgu = self.emit.emitI2F(frame)
        #else:
        #    buonNgu = ""
        self.emit.printout(in_[0] + self.emit.emitINVOKESTATIC(cname + "/" + sym.name, ctype, frame))
        
    def visitIf(self,ast,o):
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym

        checkReturnAtTheEndThen = False
        
        expc, expt = self.visit(ast.expr,Access(frame,nenv,False,True))
        self.emit.printout(expc)
        falseLabel = frame.getNewLabel()
        endLabel = frame.getNewLabel()
        self.emit.printout(self.emit.emitIFFALSE(falseLabel,frame))
        if ast.thenStmt == []: 
            self.emit.printout(self.emit.emitGOTO(endLabel,frame))
        for x in ast.thenStmt: self.visit(x,SubBody(frame,nenv))
        if len(ast.thenStmt) > 0 and not type(ast.thenStmt[-1]) is Return:
            self.emit.printout(self.emit.emitGOTO(endLabel,frame))
        self.emit.printout(self.emit.emitLABEL(falseLabel,frame))
        for x in ast.elseStmt:
            self.visit(x,SubBody(frame,nenv))
        self.emit.printout(self.emit.emitLABEL(endLabel,frame))
        pass

    def visitWhile(self,ast,o):
        ctxt =o
        frame = ctxt.frame
        nenv = o.sym

        startLabel = frame.getNewLabel()
        endLabel = frame.getNewLabel()
        frame.brkLabel.append(endLabel)
        frame.conLabel.append(startLabel)

        self.emit.printout(self.emit.emitLABEL(startLabel,frame))
        expc, expt = self.visit(ast.exp,Access(frame,nenv,False,True))
        self.emit.printout(expc)
        self.emit.printout(self.emit.emitIFFALSE(endLabel,frame))
        for x in ast.sl:
            self.visit(x,SubBody(frame,nenv))
        self.emit.printout(self.emit.emitGOTO(startLabel,frame))
        self.emit.printout(self.emit.emitLABEL(endLabel,frame))
        
        frame.brkLabel = frame.brkLabel[:-1]
        frame.conLabel = frame.conLabel[:-1]
        pass

    def visitFor(self,ast,o):
        ctxt = o
        frame = ctxt.frame
        nenv = o.sym

        loopLable = frame.getNewLabel()
        endLabel = frame.getNewLabel()
        increaseLabel = frame.getNewLabel()
        frame.brkLabel.append(endLabel)
        frame.conLabel.append(increaseLabel)

        exp1c, exp1t = self.visit(ast.expr1,Access(frame,nenv,False,True))
        self.emit.printout(exp1c)
        idc, idt = self.visit(ast.id,Access(frame,nenv,True,False))
        self.emit.printout(idc)
        self.emit.printout(self.emit.emitLABEL(loopLable,frame))
        idc1, idt1 = self.visit(ast.id,Access(frame,nenv,False,True))
        self.emit.printout(idc1)
        exp2c, exp2t = self.visit(ast.expr2,Access(frame,nenv,False,True))
        self.emit.printout(exp2c)
        if ast.up: 
            incrcode = "\tiadd\n"
            self.emit.printout(self.emit.emitIFICMPGT(endLabel,frame))
        else:
            incrcode = "\tisub\n"
            self.emit.printout(self.emit.emitIFICMPLT(endLabel,frame))
        for x in ast.loop:
            self.visit(x,SubBody(frame,nenv))
        #self.emit.printout(self.emit.emitLABEL(loopLable,frame))
        idc2, idt2 = self.visit(ast.id,Access(frame,nenv,False,True))
        self.emit.printout(self.emit.emitLABEL(increaseLabel,frame))
        self.emit.printout(idc2 + "\ticonst_1\n" + incrcode)
        idc3, idt3 = self.visit(ast.id,Access(frame,nenv,True,False))
        self.emit.printout(idc3)
        self.emit.printout(self.emit.emitGOTO(loopLable,frame))
        self.emit.printout(self.emit.emitLABEL(endLabel,frame))

        frame.brkLabel = frame.brkLabel[:-1]
        frame.conLabel = frame.conLabel[:-1]
        pass

    def visitWith(self,ast,o):
        ctxt = o
        frame = ctxt.frame
        nenv = o.sym[:]

        frame.enterScope(False)
        startLabel = frame.getNewLabel()
        endLabel = frame.getNewLabel()
        for x in ast.decl:
            idx = frame.getNewIndex()
            self.emit.printout(self.emit.emitVAR(idx,x.variable.name,x.varType,startLabel,endLabel,frame))
            nenv += [Symbol(x.variable.name, x.varType, Index(idx))]
        self.emit.printout(self.emit.emitLABEL(startLabel,frame))
        for x in ast.stmt:
            self.visit(x,SubBody(frame,nenv))
        self.emit.printout(self.emit.emitLABEL(endLabel,frame))
        frame.exitScope()
        pass    

    def visitReturn(self,ast,o):
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        if ast.expr:
            exp_c, exp_t = self.visit(ast.expr,Access(frame,nenv,False,True))
            self.emit.printout(exp_c)
            if type(frame.returnType) is FloatType and type(exp_t) is IntType:
                self.emit.printout(self.emit.emitI2F(frame))
                exp_t = frame.returnType
            self.emit.printout(self.emit.emitRETURN(exp_t,frame))
        else:
            self.emit.printout(self.emit.emitRETURN(VoidType(),frame))
        pass

    def visitBreak(self,ast,o):
        frame = o.frame
        #self.emit.printout(self.emit.emitLABEL(frame.getBreakLabel(),frame))
        self.emit.printout(self.emit.emitGOTO(frame.getBreakLabel(),frame))
        pass

    def visitContinue(self,ast,o):
        frame = o.frame
        self.emit.printout(self.emit.emitGOTO(frame.getContinueLabel(),frame))

    def visitBinaryOp(self,ast,o):
        ctxt = o
        frame = ctxt.frame
        op = ast.op

        if op in ['andthen','orelse']:
            outLabel = frame.getNewLabel()
            falseLabel = frame.getNewLabel()
            trueLabel = frame.getNewLabel()

            lcode, ltype = self.visit(ast.left,Access(frame,o.sym,False,True))
            self.emit.printout(lcode)
            if op == 'andthen':
                self.emit.printout(self.emit.emitIFFALSE(falseLabel,frame))
                rcode, rtype = self.visit(ast.right,Access(frame,o.sym,False,True))
                self.emit.printout(rcode)
                self.emit.printout(self.emit.emitGOTO(outLabel,frame))
                self.emit.printout(self.emit.emitLABEL(falseLabel,frame))
                self.emit.printout("\ticonst_0\n")
                self.emit.printout(self.emit.emitLABEL(outLabel,frame))
            else:
                self.emit.printout(self.emit.emitIFTRUE(trueLabel,frame))
                rcode, rtype = self.visit(ast.right,Access(frame,o.sym,False,True))
                self.emit.printout(rcode)
                self.emit.printout(self.emit.emitGOTO(outLabel,frame))
                self.emit.printout(self.emit.emitLABEL(trueLabel,frame))
                self.emit.printout("\ticonst_1\n")
                self.emit.printout(self.emit.emitLABEL(outLabel,frame))
            return "",BoolType()
        else:
            lcode, ltype = self.visit(ast.left,Access(frame,o.sym,False,True))
            rcode, rtype = self.visit(ast.right,Access(frame,o.sym,False,True))
            if type(ltype) != type(rtype):
                if type(ltype) is IntType:
                    lcode += self.emit.emitI2F(frame)
                    ltype = FloatType()
                else:
                    rcode += self.emit.emitI2F(frame)
                    rtype = FloatType()
            if op in ['+','-']:
                opcode = self.emit.emitADDOP(op,ltype,frame)
            elif op in ['*','/']:
                if op == '/' and type(ltype) is IntType and type(rtype) is IntType:
                    lcode += self.emit.emitI2F(frame)
                    rcode += self.emit.emitI2F(frame)
                    ltype = FloatType()
                    rtype = FloatType()
                opcode = self.emit.emitMULOP(op,ltype,frame)
            elif op.lower() == 'and':
                opcode = self.emit.emitANDOP(frame)
            elif op.lower() == 'or':
                opcode = self.emit.emitOROP(frame)
            elif op.lower() == 'div':
                opcode = self.emit.emitDIV(frame)
            elif op.lower() == 'mod':
                opcode = self.emit.emitMOD(frame)
            else:
                if type(ltype) is FloatType:
                    falseLabel = frame.getNewLabel()
                    outLabel = frame.getNewLabel()
                    if op == '=': code = "\tifne Label" 
                    elif op == '<>': code = "\tifeq Label" 
                    elif op == '>': code = "\tifle Label" 
                    elif op == '<': code = "\tifge Label" 
                    elif op == '>=': code = "\tiflt Label" 
                    elif op == '<=': code = "\tifgt Label" 
                    opcode = "\tfcmpl\n" + code + str(falseLabel) + "\n" + "\ticonst_1\n" + self.emit.emitGOTO(outLabel,frame) + self.emit.emitLABEL(falseLabel,frame) + "\ticonst_0\n" + self.emit.emitLABEL(outLabel,frame)
                    ltype = BoolType()
                else:
                    opcode = self.emit.emitREOP(op,ltype,frame)
                    ltype = BoolType()
            #sef.emit.printout(lcode + rcode + opcode)
            return lcode + rcode + opcode,ltype

    def visitUnaryOp(self,ast,o):
        ctxt = o
        frame = ctxt.frame
        op = ast.op

        expc, expt = self.visit(ast.body,Access(frame,o.sym,False,True))
        if op == '-':
            opcode = self.emit.emitNEGOP(expt,frame)
        elif op == "not":
            opcode = self.emit.emitNOT(expt,frame)
        return expc + opcode, expt

    def visitId(self,ast,o):
        sym = self.lookup(ast.name.lower(),o.sym[::-1],lambda x:x.name.lower())
        if o.isLeft:
            if type(sym.value) is CName:
                res = self.emit.emitPUTSTATIC(sym.value.value + "/" + sym.name, sym.mtype, o.frame)
                #self.emit.printout(res)
                return res,sym.mtype
            elif type(sym.value) is Index:
                res = self.emit.emitWRITEVAR(sym.name,sym.mtype,sym.value.value,o.frame)
                #self.emit.printout(res)
                return res,sym.mtype
            else:
                return "",VoidType()
        else:
            if type(sym.value) is CName:
                res = self.emit.emitGETSTATIC(sym.value.value + "/" + sym.name, sym.mtype, o.frame)
                #self.emit.printout(res)
                return res,sym.mtype
            elif type(sym.value) is Index:
                res = self.emit.emitREADVAR(sym.name,sym.mtype,sym.value.value,o.frame)
                #self.emit.printout(res)
                return res,sym.mtype
            else:
                return "",VoidType()

    def visitCallExpr(self,ast,o):
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        sym = self.lookup(ast.method.name.lower(), nenv, lambda x: x.name.lower())
        cname = sym.value.value
        ctype = sym.mtype
        in_ = ("", [])
        for idx, val in enumerate(ast.param):
            str1, typ1 = self.visit(val, Access(frame, nenv, False, True))
            in_ = (in_[0] + str1, in_[1] + [typ1])
            if type(sym.mtype.partype[idx]) is FloatType and type(in_[1][idx]) is IntType:
                in_ = (in_[0] + self.emit.emitI2F(frame), in_[1])
        res = in_[0] + self.emit.emitINVOKESTATIC(cname + "/" + sym.name, ctype, frame)
        #self.emit.printout(res)
        return res,ctype.rettype 

    def visitArrayCell(self,ast,o):
        raise Exception("Array Cant visit that shit")

    def visitIntLiteral(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        res = self.emit.emitPUSHICONST(ast.value, frame)
        #self.emit.printout(res)
        return res,IntType()

    def visitFloatLiteral(self,ast,o):
        ctxt = o
        frame = ctxt.frame
        res = self.emit.emitPUSHFCONST(str(ast.value),frame)
        #self.emit.printout(res)
        return res,FloatType()

    def visitBooleanLiteral(self,ast,o):
        ctxt = o
        frame = ctxt.frame
        res = self.emit.emitPUSHICONST(str(ast.value),frame)
        #self.emit.printout(res)
        return res,BoolType()

    def visitStringLiteral(self,ast,o):
        ctxt = o
        frame = ctxt.frame
        res = self.emit.emitPUSHCONST(str(ast.value),StringType(),frame)
        #self.emit.printout(res)
        return res,StringType()