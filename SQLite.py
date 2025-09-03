
import sqlite3
try:
    con = sqlite3.connect("meu_banco.db")
    cur = con.cursor()

    cur.execute("CREATE TABLE pessoa(id, nome, idade, cpf)")
    con.commit()
    #res = cur.execute("SELECT * FROM pessoa")
    #pessoas = res.fetchone()
    #cur.execute("CREATE TABLE consulta("id PRIMARY KEY ASC AUTOINCREMENT","data_consulta DATETIME","horario DATETIME","id_pessoa INTEGER,"FOREIGN KEY (id_pessoa) REFERENCES PESSOAS(id)")

    #print(pessoas)

    cur.close()
    con.close()

except ConnectionRefusedError as c:
    print('Erro de conexão com o banco')


