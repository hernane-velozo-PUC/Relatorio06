#By Hernane Velozo - IoT I - PUCMinas / 01/2022
#Query para visualizar dados recebidos pelo broker

#Seleciona como default o banco mySQL criado no script Python
USE mySQL;

# Com o comando SELECT abaixo, podemos visualizar os dados armazenados na tabela "dadosIoT".
SELECT * FROM dadosIoT;
