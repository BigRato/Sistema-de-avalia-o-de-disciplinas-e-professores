CREATE OR REPLACE FUNCTION 
	criar_turmas()
RETURNS VOID AS $$

BEGIN
  -- Adição das turmas  
  INSERT INTO TURMA (PROFESSOR_ID, DISCIPLINA_ID, ANO, SEMESTRE, CODIGO) VALUES
    -- professora (id=7): LAURA ANGELICA FERREIRA DARNET, 
    -- professor (id=8): MAURO GUILHERME MAIDANA CAPPELLARO
    -- disciplina (id=10): ALGORITMOS E PROGRAMAÇÃO DE COMPUTADORES, 
    -- disciplina (id=11): BANCOS DE DADOS
    -- disciplina (id=12): ESTRUTURAS DE DADOS
    (7, 10, 2020, 1, 'A'),  
    (8, 10, 2020, 2, 'B'),
    (7, 11, 2020, 1, 'A'),
    (8, 11, 2020, 2, 'B'),
    (7, 12, 2020, 1, 'A'),
    (8, 12, 2020, 2, 'B');
    
END;
$$ LANGUAGE plpgsql;