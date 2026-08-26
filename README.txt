requirements.txt

Como o projeto já terá essa dependência registrada, o arquivo pode conter inicialmente apenas:

Flask

Depois, na EC2:

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py

A aplicação ficará disponível em:

http://IP_PUBLICO_DA_EC2:5000

e os dois endpoints que os alunos poderão testar são:

/

e

/api/health

Além disso:

/about

Esse desenho é interessante para a disciplina porque a página não é apenas um "Hello World": ela já contém uma interface web, uma API REST mínima e uma operação de health check. Assim, quando chegarmos a Docker, Redis, banco de dados, autenticação, microsserviços e Load Balancer, podemos continuar evoluindo a mesma aplicação, em vez de abandonar o exemplo da primeira aula.