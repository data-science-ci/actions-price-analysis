# Stock price forecasts

### Data Scientists:
- Walker Teotônio Correia de Barros
- Maria Luiza Leite dos Santos
- Benn Arthur de Souza Fonseca Amaral
- Kennyo Wescley Elias Cavalcante


#### B3 Data
https://www.b3.com.br/pt_br/market-data-e-indices/servicos-de-dados/market-data/historico/mercado-a-vista/


### We want to answer the following questions:
 - Is there a best month to invest in the asset?
 - On which day did the stock change the most?
 - What was the stock's biggest rally for the month and how long did it hold?



# Previsões de valor de ações (PT-BR)

### Analistas de dados:
- Walker Teotônio Correia de Barros
- Maria Luiza Leite dos Santos
- Benn Arthur de Souza Fonseca Amaral
- Kennyo Wescley Elias Cavalcante

### Queremos responder as perguntas a seguir
 - Existe um melhor mês para investir no ativo?
 - Qual o dia que a ação mais variou?
 - Qual foi o maior topo da ação no mês e por quanto tempo ele se manteve?

### Dados utilizados:

#### B3 Dados
https://www.b3.com.br/pt_br/market-data-e-indices/servicos-de-dados/market-data/historico/mercado-a-vista/series-historicas/

#### Pré-processamento

##### Estruturação

###### Nomeação de colunas
Para obter os dados necessários para a análise da amostra, foi necessário utilizar algumas técnicas de pré-processamento dos dados. Como nossa amostra deriva de um arquivo do tipo txt, e as colunas não estavam nomeadas, foi necessários fazer isso manualmente utilizando o atributo .columns, além disso, foi necessário ajustar os valores com vírgula.

###### Correção dos tipos de dados
O segundo passo foi adequar os tipos de dados as necessidades da nossa amostra

#### Remoção de Dados Ruídosos 

Durante o pré-processamento, também foram encontrados dados que não fazem sentido para análise, ou que estavam absurdamente discrepantes do contexto da aplicação, causado provavelmente por erros na coleta, dessa forma, foi necessário eliminar registros que poderiam causar problemas nas medidas obtidas
-------------------------------------------------------------------------
#### Análise de Colunas
Colunas com grandes números de erros nos registros e que não eram relevantes para a amostra, foram removidas. Essas colunas foram identificadas com base na análise da medidas de tedência central das mesmas

#### Conclusões

##### Resultados

##### Limitações 

##### Trabalhos futuros
 - Módulo Anapy

##### Melhorias
