import mysql.connector

conexao = mysql.connector.connect(
	host='localhost',
	user='mysql_alfamed',
	password='alfamed',
	database='mybd',
)
cursor = conexao.cursor()

# CREATE 
#tabela cargo
id_cargo=3
descricao= "tenico de TI"
comando = f'insert into cargo(id_cargo, descricao) values ({id_cargo}, "{descricao}")'
conexao.commit() # edita o banco de dados
cursor.execute(comando)
#tabela funcionario
id_funcionario=2
nome="carlos"
cpf="765.875.898-99"
endereco="Av. Brasil, 100"
data_nasc="1985-02-14"
data_admissao="2021-07-01"
departamento_id_departamento=56
turnos_id_turnos=552
salario="4500.00'"
filial_id_filia=1
cargo_id_cargo=3
comando = f'INSERT INTO funcionario (id_funcionario, nome, cpf, endereco, data_nasc, data_admissao, departamento_id_departamento, turnos_id_turnos, salario, filial_id_filial, cargo_id_cargo) values ({id_funcionario},"{nome}","{cpf}","{endereco}","{data_nasc}","{data_admissao}",{departamento_id_departamento},{turnos_id_turnos},"{salario}",{filial_id_filia},{cargo_id_cargo} )'
conexao.commit() # edita o banco de dados
cursor.execute(comando)


# READ
#tabela cargo 
conmando= f'Select * from cargo'
resultado = cursor.fetchall()# ler o banco de dados
print(resultado)
cursor.execute(comando)
#tabela cliente
conmando= f'Select * from funcionario'
resultado = cursor.fetchall()# ler o banco de dados
print(resultado)
cursor.execute(comando)


# UPDATE
#tabela cargo
descricao="medico"
id_cargo=2
comando=f'update cargo set descricao="{descricao}" where id_cargo={id_cargo}'
conexao.commit() # edita o banco de dados
cursor.execute(comando)
#tabela funcionario
salario = '3500.00'
id_funcionario = 1
comando= f'UPDATE funcionario SET salario = "{salario}" WHERE id_funcionario ={id_funcionario}'
conexao.commit() # edita o banco de dados
cursor.execute(comando)


#DELETE
#Tabela cargo 
id_cargo=2
comando=f'delete from cargo where id_cargo={id_cargo}'
conexao.commit() # edita o banco de dados
cursor.execute(comando)
#tabela funcionario
id_cargo=1
comando=f'delete from funcionario where id_cargo={id_cargo}'
conexao.commit() # edita o banco de dados
cursor.execute(comando)


conexao.close()
cursor.closse()