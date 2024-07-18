grammar WCPL;

program: statement+ ;

statement
    : classDef
    | functionDef
    | variableDef
    | ifStatement
    | forLoop
    | expression
    ;

classDef: 'beg class' IDENTIFIER classBody 'end' ;
classBody: (functionDef | variableDef)* ;

functionDef: 'beg def' IDENTIFIER '(' parameters? ')' block 'end' ;
parameters: IDENTIFIER (',' IDENTIFIER)* ;

variableDef: IDENTIFIER '=' expression ;
block: statement+ ;

ifStatement: 'beg if' expression block 'end' ;
forLoop: 'beg for' IDENTIFIER 'in' expression block 'end' ;

expression
    : STRING
    | NUMBER
    | IDENTIFIER
    | functionCall
    | '(' expression ')'
    ;

functionCall: 'open' IDENTIFIER '(' arguments? ')' ;
arguments: expression (',' expression)* ;

STRING: '"' .*? '"' ;
NUMBER: [0-9]+ ;
IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]* ;
WS: [ \t\r\n]+ -> skip ;
COMMENT: '**' ~[\r\n]* -> skip ;
