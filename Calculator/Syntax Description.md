## Syntax Description

```BNF
<statement> ::= print <expression> | var <assignment>
<assignment> ::= <identifier> = <expression>  
                | <identifier> = { <expression_list> } 
                | <identifier> = ( <expression_list> ) 
                | <identifier> = <matrix>
<expression_list> ::= <expression> | <expression_list> , <expression>
<matrix> ::= [ <row_list> ]
<row_list> ::= <row> | <row_list> , <row>
<row> ::= [ <expression_list> ]
<expression> ::= <term> | <term> + <expression> | <term> - <expression>
<term> ::= <factor> | <factor> * <term> | <factor> / <term>
<factor> ::= <unary> | <unary> ^ <unary>
<unary> ::= <primary> | + <primary> | - <primary>
<primary> ::= ( <expression> ) | <number> | <identifier> | <built-in> ( <expression_list> )
<number> ::= real number
<identifier> ::= string of length > 0
<built-in> ::= list of built-in functions
```