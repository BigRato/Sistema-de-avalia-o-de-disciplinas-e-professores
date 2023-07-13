CREATE VIEW view_turmas AS
SELECT
    p.nome as professor,
    d.nome as disciplina,
    t.ano,
    t.semestre,
    t.codigo
FROM
    TURMA t
    INNER JOIN PROFESSOR p ON p.id = t.professor_id
    INNER JOIN DISCIPLINA d ON d.id = t.disciplina_id 
