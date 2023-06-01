%{
  #include <stdio.h>
%}
%%
#.+ {printf("%s is a header file declaration", yytext);}
^(int|char|float|double).+; {printf("%s is a declaration statement", yytext);}
[a-zA-Z_][a-zA-Z_0-9]*=.+;x {printf("%s is an assignment statement", yytext);}
%%
int main() {
  FILE *f;
  f = fopen("input.c", "r");
  yyin = f;
  yylex();
  return 0;
}
int yywrap() {return 1;}
