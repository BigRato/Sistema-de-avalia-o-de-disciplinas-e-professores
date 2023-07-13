CREATE OR REPLACE FUNCTION 
	criar_avaliacoes()
RETURNS VOID AS $$

BEGIN
  -- Adição das avaliações dos professores
  INSERT INTO AVALIACAO_PROFESSOR (TEXTO, ESTUDANTE_ID, PROFESSOR_ID) VALUES
    ('Boa didática', 6, 6),
    ('Chega atrasado', 7, 7),
    ('Provas difíceis', 8, 8);

  -- Adição das avaliações das turmas 

  -- Turmas existentes
  -- (PROF, DISC, ANO, SEM, COD)
  -- (7, 10, 2020, 1, 'A'),  
  -- (8, 10, 2020, 2, 'B'),
  -- (7, 11, 2020, 1, 'A'),
  -- (8, 11, 2020, 2, 'B'),
  -- (7, 12, 2020, 1, 'A'),
  -- (8, 12, 2020, 2, 'B');

  INSERT INTO AVALIACAO_TURMA (TEXTO, ESTUDANTE_ID, TURMA_PROFESSOR_ID, TURMA_DISCIPLINA_ID, TURMA_ANO, TURMA_SEMESTRE, TURMA_CODIGO) VALUES
    ('Bem difícil', 9, 7, 10, 2020, 1, 'A'),
    ('Tem que se esforçar bastante', 10, 8, 10, 2020, 2, 'B'),
    ('Essencial para o curso', 11, 7, 12, 2020, 1, 'A');
    
END;
$$ LANGUAGE plpgsql;

