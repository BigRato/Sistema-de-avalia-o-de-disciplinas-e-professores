CREATE OR REPLACE FUNCTION 
	criar_departamentos()
RETURNS VOID AS $$

BEGIN
  -- Adição dos departamentos  
  INSERT INTO DEPARTAMENTO (NOME) VALUES
    ('DECANATO DE PÓS-GRADUAÇÃO / DPG - BRASÍLIA'),
    ('CENTRO DE EXCELÊNCIA EM TURISMO - BRASÍLIA'),
    ('DEPARTAMENTO DE COMUNICAÇÃO ORGANIZACIONAL/COM - BRASÍLIA'),
    ('DEPTO CIÊNCIAS DA COMPUTAÇÃO - BRASÍLIA');

END;
$$ LANGUAGE plpgsql;