CREATE OR REPLACE FUNCTION 
	criar_denuncias()
RETURNS VOID AS $$

BEGIN
  -- Adição das denuncias de avaliações de professores
  INSERT INTO DENUNCIA_AVALIACAO_PROFESSOR (AVALIACAO_PROFESSOR_ID, ESTUDANTE_ID) VALUES
    (1, 4),
    (2, 5),
    (3, 6);


  -- Adição das denuncias de avaliações das turmas
  INSERT INTO DENUNCIA_AVALIACAO_TURMA (AVALIACAO_TURMA_ID, ESTUDANTE_ID) VALUES
    (1, 7),
    (2, 8),
    (3, 9);
    
END;
$$ LANGUAGE plpgsql;