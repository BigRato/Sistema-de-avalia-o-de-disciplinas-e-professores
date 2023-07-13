BEGIN TRANSACTION;

  SELECT criar_estudantes();
  SELECT criar_departamentos();
  SELECT criar_disciplinas();
  SELECT criar_professores();
  SELECT criar_turmas();
  SELECT criar_avaliacoes();
  SELECT criar_denuncias();
  

COMMIT;