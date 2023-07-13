CREATE OR REPLACE FUNCTION 
	criar_estudantes()
RETURNS VOID AS $$

BEGIN
  -- Adição dos estudantes  
  INSERT INTO ESTUDANTE (NOME, EMAIL, MATRICULA, SENHA, ADM) VALUES
    ('Débora', 'debora@email.com', 201, '123', true),
    ('João', 'joao@email.com', 202, '123', true),
    ('Maria', 'maria@email.com', 203, '123', true),
    ('Pedro', 'pedro@email.com', 204, '123', true),
    ('Ana', 'ana@email.com', 205, '123', true),
    ('Carlos', 'carlos@email.com', 206, '123', false),
    ('Julia', 'julia@email.com', 207, '123', false),
    ('Rafael', 'rafael@email.com', 208, '123', false),
    ('Camila', 'camila@email.com', 209, '123', false),
    ('Fernando', 'fernando@email.com', 210, '123', false),
    ('Isabela', 'isabela@email.com', 211, '123', false),
    ('Lucas', 'lucas@email.com', 212, '123', false);

END;
$$ LANGUAGE plpgsql;