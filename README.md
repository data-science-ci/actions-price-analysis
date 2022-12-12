## Stock value forecasts (EN)

### Data analysts:
- Walker Teotônio Correia de Barros
- Maria Luiza Leite dos Santos
- Benn Arthur de Souza Fonseca Amaral
- Kennyo Wescley Elias Cavalcante

### We want to answer the following questions
 - Which company has the highest probability of return in a one-month period?
 - What are the differences in PETRE and COGNE stocks?
 - Which company had the highest rate of change in price in the last trade?

### Data used:

#### B3 Data
https://www.b3.com.br/pt_br/market-data-e-indices/servicos-de-dados/market-data/historico/mercado-a-vista/series-historicas/

#### Preprocessing

##### Structuring

###### Column naming
To obtain the data needed for the sample analysis, it was necessary to use some data preprocessing techniques. As our sample was derived from a txt file, and the columns were not named, it was necessary to do this manually using the .columns attribute, and to adjust the values with commas.

###### Correcting the data types
The second step was to adjust the data types to the needs of our sample

#### Removing Noisy Data 
During pre-processing, we also found data that did not make sense for analysis, or that were absurdly discrepant from the context of the application, probably caused by errors in the collection, so it was necessary to eliminate records that could cause problems in the measurements obtained
-------------------------------------------------------------------------
#### Column Analysis
Columns with large numbers of errors in the records that were not relevant to the sample were removed. These columns were identified based on analysis of their central tendency measures

#### Conclusions

##### Results

##### Limitations 

##### Future work
 - Anapy Module

##### Improvements

Translated with www.DeepL.com/Translator (free version)
# Previsões de valor de ações (PT-BR)

### Analistas de dados:
- Walker Teotônio Correia de Barros
- Maria Luiza Leite dos Santos
- Benn Arthur de Souza Fonseca Amaral
- Kennyo Wescley Elias Cavalcante

### Queremos responder as perguntas a seguir
 -  Qual a empresa com maior probabilidade de retorno no período de um mês?
 -  Quais as diferenças nas ações da PETRE e da COGNE?
 -  Qual empresa teve a maior taxa de variação no preço do último negócio?

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

#### Análise de Colunas
Colunas com grandes números de erros nos registros e que não eram relevantes para a amostra, foram removidas. Essas colunas foram identificadas com base na análise da medidas de tedência central das mesmas

#### Conclusões

##### Resultados

##### Limitações 

##### Trabalhos futuros
 - Módulo Anapy

##### Melhorias
