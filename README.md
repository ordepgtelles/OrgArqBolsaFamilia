Repositório criado para o trabalho de Organização e Estrutura de Arquivos, onde fará um arquivo hash de um arquivo da bolsa família e depois uma operação de conjuntos, nesse caso será realizada a diferença entre os arquivos referentes à Janeiro de 2019 e Dezembro de 2018.

Essa diferença pega as pessoas que tem somente no arquivo de Janeiro de 2019 e não tem no de Dezembro de 2018, ou seja, as pessoas que passaram a receber o auxílio bolsa família em Janeiro de 2019.

A chave do arquivo hash é o NIS.

Para executar o projeto:

  Baixe o arquivo bolsa neste link: http://www.portaltransparencia.gov.br/download-de-dados/bolsa-familia-pagamentos
  Importante: o nome dos arquivos devem ser bolsa-dez-2018.csv e bolsa-jan-2019.csv

  Compilar e executar : (DEVE SER SEGUIDO ESTA ORDEM EXATA)

    Primeiro execute o CriaIndice.py - Vai criar o arquivo de hash

    Depois execute o Diferenca.py - Vai comparar o arquivo de hash com o arquivo de pagamentos da bolsa
