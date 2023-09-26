use SkillUp_GCOLIV1;
go

drop table projeto_ada_giuliano.clientes

alter schema projeto_ada_giuliano;
go
create table projeto_ada_giuliano.clientes 
	(cpf varchar(14) primary key not null, 
	nome varchar(255) not null, 
	rg varchar(12),
	nascimento date not null,
	cep varchar(9) not null,
	numero varchar(255),
	complemento varchar(255),
	logradouro varchar(255),
	bairro varchar(255),
	cidade varchar(255),
	uf varchar(2));
go

