CREATE TABLE cliente(
    cli_id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY, -- Boa prática para IDs sequenciais
    cli_nome VARCHAR(255) NOT NULL,
    cli_cpf VARCHAR(14) UNIQUE,
    cli_cnpj VARCHAR(18) UNIQUE,
    cli_rg VARCHAR(20),
    cli_dtnsc DATE,
    cli_end VARCHAR(255),
    cli_end_num VARCHAR(10),
    cli_end_cid VARCHAR(100),
    cli_end_bairro VARCHAR(100),
    cli_tel VARCHAR(20),
    cli_cel VARCHAR(20),
    cli_email VARCHAR(100),
    cli_tipo VARCHAR(20)
);

CREATE TABLE material(
	mat_cod INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
	mat_desc VARCHAR(255),
	mat_etq INT,
	mat_preco_unit DECIMAL(10, 4),
	mat_fne VARCHAR(200),
	mat_dt_aqui DATE,
	mat_obs TEXT
);

CREATE TABLE funcionario(
	func_id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
	func_nome VARCHAR(255) NOT NULL,
	func_cpf VARCHAR(14) UNIQUE,
	func_rg VARCHAR(20),
	func_tel VARCHAR(20),
	func_cel VARCHAR(20),
	func_email VARCHAR(100),
	func_cargo VARCHAR(100)
);

CREATE TABLE usuario (
    usr_id INT PRIMARY KEY,
    usr_username VARCHAR(100) NOT NULL UNIQUE,
    usr_password_hash VARCHAR(255) NOT NULL,
    usr_salt VARCHAR(64) NOT NULL,
    usr_email VARCHAR(255) UNIQUE,
    usr_created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    usr_func_id INT,
    CONSTRAINT fk_usuario_funcionario FOREIGN KEY (usr_func_id) REFERENCES funcionario(func_id)
);

CREATE TABLE servico(
	ser_id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
	ser_cli_id INT,
	ser_usr_id INT,
	ser_desc TEXT,
	ser_tipo_servico CHAR(1),
	ser_preco_total DECIMAL(10, 4) NOT NULL,
	CONSTRAINT fk_cliente_servico FOREIGN KEY (ser_cli_id) REFERENCES cliente(cli_id),
	CONSTRAINT fk_usuario_servico FOREIGN KEY (ser_usr_id) REFERENCES usuario(usr_id)
);

CREATE TABLE servico_material (
    ser_id INT REFERENCES servico(ser_id),
    mat_cod INT REFERENCES material(mat_cod),
    quantidade INT NOT NULL DEFAULT 1,
    PRIMARY KEY (ser_id, mat_cod)
);