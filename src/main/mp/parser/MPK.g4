// Lê Hoàng Kim 1611712 
grammar MP;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

program: decl+ EOF;

decl: func_decl | proc_decl | var_decl;
//Var
var_decl: VAR var_decl_list;

var_decl_list: one_line_decl var_decl_list?;

one_line_decl: var_list COLON var_type SEMI;

var_list: ID (COMMA var_list)?;
//Function
func_decl: FUNCTION ID LB para_decl? RB COLON var_type SEMI var_decl? compound_stmt;
//Procedure
proc_decl: PROCEDURE ID LB para_decl? RB SEMI var_decl? compound_stmt;

para_decl: one_para_decl (SEMI para_decl)?;

one_para_decl: var_list COLON var_type;

stmt: (	(
			assign_stmt
			| break_stmt
			| continue_stmt
			| return_stmt
		) SEMI
	)
	| (
		if_stmt
		| for_stmt
		| with_stmt
		| while_stmt
		| compound_stmt
		| call_stmt
	);

assign_stmt: ((ids | index_exp) ASSIGN)+ exp;

ids: ID;

index_exp: exp LS exp RS;

if_stmt: IF exp THEN stmt (ELSE stmt)?;

while_stmt: WHILE exp DO stmt;

for_stmt: FOR ID ASSIGN exp (TO | DOWNTO) exp DO stmt;

break_stmt: BREAK;

continue_stmt: CONTINUE;

return_stmt: RETURN exp?;

with_stmt: WITH var_decl_list DO stmt;

call_stmt: ID LB exp_list? RB SEMI;

funcall: ID LB exp_list? RB;

compound_stmt: BEGIN stmt* END;

expression_stmt: exp SEMI;

exp: exp (AND THEN | OR ELSE) exp1
	| exp1;

exp1: exp2 ((EQUAL | NOT_EQUAL | LESS | LE | GREATER | GE) exp2)?;

exp2: exp2 (PLUS | SUBTRACTION | OR) exp3
	| exp3;

exp3: exp3 (DIVISION | MULTIPLICATION | DIV | MOD | AND) exp4
	| exp4;

exp4: (SUBTRACTION | NOT) exp4 | exp5;

exp5: exp6 (LS exp RS)*;

exp6: LB exp RB | exp7;

exp7: operand | funcall;

exp_list: exp (COMMA exp)*;

operand: INTLIT | FLOATLIT | STRINGLIT | BOOLLIT | ID;

//condition_exp: NOT* exp ((AND | OR) condition_exp)*;

var_type: INTEGER | REAL | BOOLEAN | STRING | array_type;

array_type:
	ARRAY LS upper_lower DOUBLE_DOT upper_lower RS OF (
		BOOLEAN
		| INTEGER
		| REAL
		| STRING
	);

upper_lower: SUBTRACTION? INTLIT;

//Comments
COMMENT_1: '(*' .*? ')' -> skip;

COMMENT_2: '{' .*? '}' -> skip;

COMMENT_3: '//' ~[\r\n]* -> skip;

//Keywords
WITH: W I T H;

BREAK: B R E A K;

CONTINUE: C O N T I N U E;

FOR: F O R;

TO: T O;

DOWNTO: D O W N T O;

DO: D O;

IF: I F;

THEN: T H E N;

ELSE: E L S E;

RETURN: R E T U R N;

WHILE: W H I L E;

BEGIN: B E G I N;

END: E N D;

FUNCTION: F U N C T I O N;

PROCEDURE: P R O C E D U R E;

VAR: V A R;

ARRAY: A R R A Y;

OF: O F;

REAL: R E A L;

BOOLEAN: B O O L E A N;

INTEGER: I N T E G E R;

STRING: S T R I N G;

NOT: N O T;

AND: A N D;

OR: O R;

DIV: D I V;

MOD: M O D;

//Operators
PLUS: '+';

SUBTRACTION: '-';

MULTIPLICATION: '*';

DIVISION: '/';

NOT_EQUAL: '<>';

EQUAL: '=';

LESS: '<';

GREATER: '>';

LE: '<=';

GE: '>=';

ASSIGN: ':=';

//Boolean type 
BOOLLIT: T R U E | F A L S E;

//Identifiers
ID: ('_' | LETTER) (('_' | LETTER | DIGIT)+)?;

//Seperators
LB: '(';

RB: ')';

LS: '[';

RS: ']';

COLON: ':';

SEMI: ';';

DOUBLE_DOT: '..';

COMMA: ',';

//Integer literal
INTLIT: DIGIT;

//Floating-point literal
FLOATLIT: (DIGIT (('.' DIGIT? EXPONENT?)? | EXPONENT))
	| ('.' DIGIT EXPONENT?);

//String literal
STRINGLIT:
	'"' ('\\' [bfnrt"'\\] | ~[\b\f\n\r\t"'\\])* '"' {
	    self.text = self.text[1:len(self.text)-1]};
WS: [ \f\t\r\n]+ -> skip; // skip spaces, tabs, newlines
ILLEGAL_ESCAPE:
	'"' ('\\' [bfnrt"'\\] | ~[\b\f\n\r\t"'\\])* ('\\' ~[bfnrt"'\\] | [\b\f\t"'\\]) {
		raise IllegalEscape(self.text[1:])};

UNCLOSE_STRING:
	'"' ('\\' [bfnrt"'\\] | ~[\b\f\n\r\t"'\\])* {
	    raise UncloseString(self.text[1:])};
ERROR_CHAR:
	.{
        raise ErrorToken(self.text)};
//Alphabet Set
fragment A: 'a' | 'A';
fragment B: 'b' | 'B';
fragment C: 'c' | 'C';
fragment D: 'd' | 'D';
fragment E: 'e' | 'E';
fragment F: 'f' | 'F';
fragment G: 'g' | 'G';
fragment H: 'h' | 'H';
fragment I: 'i' | 'I';
fragment J: 'j' | 'J';
fragment K: 'k' | 'K';
fragment L: 'l' | 'L';
fragment M: 'm' | 'M';
fragment N: 'n' | 'N';
fragment O: 'o' | 'O';
fragment P: 'p' | 'P';
fragment Q: 'q' | 'Q';
fragment R: 'r' | 'R';
fragment S: 's' | 'S';
fragment T: 't' | 'T';
fragment U: 'u' | 'U';
fragment V: 'v' | 'V';
fragment W: 'w' | 'W';
fragment X: 'x' | 'X';
fragment Y: 'y' | 'Y';
fragment Z: 'z' | 'Z';
//All other fragments
fragment DIGIT: [0-9]+;
fragment LETTER: [a-zA-Z]+;
fragment EXPONENT: [eE][+-]? DIGIT;