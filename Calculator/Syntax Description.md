## Syntax Description

```BNF
<statement> ::= print <expression> | var <assignment>
<assignment> ::= <identifier> = <expression> 
                | <identifier> ( <var_list> ) = <expression> 
                | <identifier> = { <expression_list> } 
                | <identifier> = ( <expression_list> ) 
                | <identifier> = <row>
                | <identifier> = <matrix>
<expression_list> ::= <expression> | <expression_list> , <expression>
<var_list> ::= <var> | <var_list> , <var>
<var> ::= x | y | z | t
<row> ::= [ <expression_list> ]
<matrix> ::= [ <row_list> ]
<row_list> ::= <row> | <row_list> , <row>
<expression> ::= <term> | <term> + <expression> | <term> - <expression>
<term> ::= <factor> | <factor> * <term> | <factor> / <term>
<factor> ::= <unary> | <unary> ^ <exp>
<unary> ::= <primary> | + <primary> | - <primary>
<exp> ::= <expprimary> | + <expprimary> | - <expprimary>
<primary> ::= ( <expression> ) | <number> | <identifier> | <var>
<expprimary> ::= ( <expression> ) | <number> | <identifier>
<number> ::= real number
<identifier> ::= string of length > 0
```