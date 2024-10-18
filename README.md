# Python judge

Python judge é um simples sistema de testes de arquivos baseados em input e output, sendo possível verificar a saída produzida por programas e comparar com a saída esperada. O sistema segue o mesmo propósito de algoritmos de judges online, utilizados em sites de programação como Codeforces e Beecrowd.

## Instalação

```
git clone https://github.com/victorrschmidt/python_judge.git
```

## Configuração

- Crie um arquivo de submissão Python na pasta `submissions`. No momento, somente arquivos Python são compatíveis.
- Coloque na pasta `io` os arquivos de entrada e saída, que devem estar na extensão `.in` e `.sol`, respectivamente. Os arquivos de entrada e saída de um mesmo caso de teste devem ter o mesmo nome.

## Executando

Para executar o arquivo desejado, digite o comando:

```
py main.py arquivo.py
```

## Configuração adicional

Você pode definir um tempo limite de execução (em segundos) no arquivo `main.py`, na constante `TIME_LIMIT`.
