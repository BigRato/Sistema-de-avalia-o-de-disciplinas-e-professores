#!/bin/bash

psql -U $POSTGRES_USER -d $POSTGRES_DB -a -f /scripts/functions/criar_estudantes.sql
psql -U $POSTGRES_USER -d $POSTGRES_DB -a -f /scripts/functions/criar_departamentos.sql
psql -U $POSTGRES_USER -d $POSTGRES_DB -a -f /scripts/functions/criar_disciplinas.sql
psql -U $POSTGRES_USER -d $POSTGRES_DB -a -f /scripts/functions/criar_professores.sql
psql -U $POSTGRES_USER -d $POSTGRES_DB -a -f /scripts/functions/criar_turmas.sql
psql -U $POSTGRES_USER -d $POSTGRES_DB -a -f /scripts/functions/criar_avaliacoes.sql
psql -U $POSTGRES_USER -d $POSTGRES_DB -a -f /scripts/functions/criar_denuncias.sql
psql -U $POSTGRES_USER -d $POSTGRES_DB -a -f /scripts/ddl.sql
psql -U $POSTGRES_USER -d $POSTGRES_DB -a -f /scripts/dml.sql
psql -U $POSTGRES_USER -d $POSTGRES_DB -a -f /scripts/functions/view_turmas.sql