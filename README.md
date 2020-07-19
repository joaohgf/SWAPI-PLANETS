# SWAPI-PLANETS-SQL

### Aplicação REST com banco SQL e autenticação JWT
Através dessa API você consegue criar planetas em um banco SQLite3

É necessário instalar os requirements:

```sh
$ pip install -r requirements.txt
```

Após isso é preciso setar 'FLASK_ENV':

```sh
$ export FLASK_ENV=development
```
#### Para rodar a aplicação:
```sh
$ flask run
```


#### Para consultar todos planetas criados é necessário fazer um GET na rota '/api/av1/planets/':

- Irá retornar um JSON com todos os planetas.


Para utilizar o criar os planetas, é preciso fazer login.
E para conseguir logar, você precisa criar um usuário.


#### Para isso vamos fazer um POST na rota '/api/av1/user/create/' com os seguintes dados:

```sh 
 {
  "login" : "teste", 
  "password": "teste"
 }
```

#### Então faremos login com um POST na rota  '/api/av1/user/login/':

```sh 
 {
  "login" : "teste", 
  "password": "teste"
 }
```
Após esse comando, irá retornar um JSON com um access_token, parecido com esse: 

```sh 
 {
  "acess_token" : "EXAMPLE"
 }
```

Só então iremos fazer um POST na rota  '/api/av1/planet/create/' com os dados, porém é necessario passar como parâmetro:
| Content-type| Authorization|
| ------ | ------ |
| application/json | Bearer 'acess_token'|


E no body:
```sh 
 {
  "name" : "Planeta1", 
  "climate": "Climate1",
  "terrain": "Terrain1"
 }
```
#### Para filtrar os planetas, pode-se fazer de duas maneiras:
- ID
- NAME

#### Para filtrar pelo ID usa-se a rota '/api/av1/planet/<planet_id>' e o 'planet_id' pode ser consultado através do GET em todos os planetas.

#### Para filtrar pelo NAME usa-se a rota '/api/av1/planet/name/<name_planet>' e sendo o 'name_planet' o nome do planeta inserido.


#### E para fazer logout precisa-se fazer um POST para rota '/api/av1/user/logout/' com o parâmetro:
 Authorization|
| ------ |
| Bearer 'acess_token'|



### Ferramentas 
- Linguagem: Python 3
- Biblioteca: Flask e SQLite

Feito por: João Freitas
