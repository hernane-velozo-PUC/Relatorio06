import mysql.connector

# agora é necessário criar um objeto de conexão: encontra o MySQL e informa as credenciais para se conectar ao banco
con = mysql.connector.connect(host='localhost', database='mySQL',user='Hernane',password='IoT000#$$')

# verifique se a conexão ao BD foi realizada com sucesso
if con.is_connected():
    db_info = con.get_server_info()
    print("Conentado com sucesso ao Servidor ", db_info)

    # a partir de agora pode-se executar comandos SQL: para tanto é necessário criar um objeto tipo cursor
    # o cursor permite acesso aos elementos do BD
    cursor = con.cursor()
    # agora você pode executar o seu comando SQL. Por exemplo o comando "select database();" mostra o BD atual selecionado
    cursor.execute("select database();")
    # crio uma variável qualquer para receber o retorno do comando de execução
    linha = cursor.fetchone()
    print("Conectado ao DB", linha)

# ao final, encerre a conexão com o BD
if con.is_connected():
    cursor.close()
    con.close()
    print("Fim da conexão")

def print_hi(name):
    print(f'{name}')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('===> Script básico de acesso ao MySQL <===')
