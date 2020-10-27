import lexer

terminales = {
    'Identificador':   lexer.Token(lexer.TokenKind.IDENTIFIER, ''),
    ':=':              lexer.Token(lexer.TokenKind.ASSIGNMENT, ':='),
    'si':              lexer.Token(lexer.TokenKind.IF, 'si'),
    'entonces':        lexer.Token(lexer.TokenKind.THEN, 'entonces'),
    'sino':            lexer.Token(lexer.TokenKind.ELSE, 'sino'),
    'mientras':        lexer.Token(lexer.TokenKind.WHILE, 'mientras'),
    'hacer':           lexer.Token(lexer.TokenKind.DO, 'hacer'),
    'Literal':         lexer.Token(lexer.TokenKind.LITERAL, ''),
    'Numero':          lexer.Token(lexer.TokenKind.NUMBER, ''),
    'aceptar':         lexer.Token(lexer.TokenKind.ACCEPT, 'aceptar'),
    'mostrar':         lexer.Token(lexer.TokenKind.PRINT, 'mostrar'),
    'op':              lexer.Token(lexer.TokenKind.OPERATOR, ''),
    '[':               lexer.Token(lexer.TokenKind.BRACKET_OPEN, '['),
    ']':               lexer.Token(lexer.TokenKind.BRACKET_CLOSE, ']'),
    '(':               lexer.Token(lexer.TokenKind.PARENTHESIS_OPEN, '('),
    ')':               lexer.Token(lexer.TokenKind.PARENTHESIS_CLOSE, ')'),
    ',':               lexer.Token(lexer.TokenKind.COMMA, ','),
    ';':               lexer.Token(lexer.TokenKind.SEMICOLON, ';')
}

producciones = {
    'Programa': [ 
        ['Declaracion',terminales[';'], 'Sentencia'],
        ['Sentencia']
    ],

    'Declaracion': [ 
        ['Sentencia', 'Declaracionp']
    ],

    'Declaracionp': [ 
        [terminales[';'], 'Declaracion', 'Declaracionp'],
        []
    ],

    'Sentencia': [ 
        [terminales['Identificador'], terminales[':='], 'Expresion', 'Sentenciap'],
        [terminales['si'], 'Expresion', terminales['entonces'], 'Sentencia', terminales['sino'], 'Sentencia', 'Sentenciap'],
        [terminales['si'], 'Expresion', terminales['entonces'], 'Sentencia', 'Sentenciap'],
        [terminales['mientras'], 'Expresion', terminales['hacer'], 'Sentencia', 'Sentenciap'],
    ],

    'Sentenciap': [ 
        [terminales[';'], 'Sentencia', 'Sentenciap'],
        []
    ],

    'Expresion': [ 
        [terminales['Literal'], 'Expresionp'],
        [terminales['Numero'], 'Expresionp'],
        [terminales['Identificador'], 'Expresionp'],
        [terminales['aceptar'], terminales['Literal'], terminales['Identificador'], 'Expresionp'],
        [terminales['mostrar'], terminales['Literal'], 'ListaIdentificadores', 'Expresionp']
    ],

    'Expresionp': [ 
        [terminales['op'], 'Expresion', 'Expresionp'],
        [terminales['['], 'Expresion', terminales[']'], 'Expresionp'],
        [terminales['('], 'Expresion', terminales[')'], 'Expresionp'],
        []
    ],

    'ListaIdentificadores': [ 
        [terminales['Identificador']],
        [terminales['Identificador'], terminales[','],'ListaIdentificadores']
    ],
}

no_terminales = [
	'Programa',
	'Declaracion',
	'Declaracionp',
	'Expresion',
	'Expresionp',
	'Sentencia',
	'Sentenciap',
	'ListaIdentificadores',
]

token123 = lexer.tokenize('id1 := \'string1\'; mientras id2 hacer id3 := 123')
