CREATE OR REPLACE FUNCTION 
	criar_disciplinas()
RETURNS VOID AS $$

BEGIN
  -- Adição das disciplinas  
  INSERT INTO DISCIPLINA (NOME, DEPARTAMENTO_ID) VALUES
    ('BARRAGENS', 1),
    ('DINÂMICA DAS ESTRUTURAS 2', 1),
    ('EQUAÇÕES DIFERENCIAIS ORDINÁRIAS 2', 1),

    ('ELABORAÇAO DE PROJETOS EM TURISMO', 2),
    ('ENOTURISMO', 2),
    ('ESTRUTURAÇÃO E PROMOÇÃO DE DESTINOS', 2),
    
    ('INTRODUÇÃO AO PLANEJAMENTO', 3),
    ('INTRODUÇÃO AS TEORIAS DA COMUNICAÇÃO', 3),
    ('LINGUAGENS DA COMUNICAÇÃO 1', 3),

    ('ALGORITMOS E PROGRAMAÇÃO DE COMPUTADORES', 4),
    ('BANCOS DE DADOS', 4),
    ('ESTRUTURAS DE DADOS', 4);


END;
$$ LANGUAGE plpgsql;