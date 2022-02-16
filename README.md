# Identificação de imóveis para compra e revenda - House Rocket Company
 
![alt text](https://github.com/laaisfmaia/Projeto-Insights-House-Rocket/blob/main/cursoDS/forsale.jpg)

## 1. Objetivo do Projeto

A base de dados analisada contém preços de venda de casas localizadas em King County, que abrange Seattle. O dataset inclui casas vendidas entre maio de 2014 e maio de 2015.

O objetivo do projeto é gerar insight acerca das melhores oportunidades de compra e revenda dos imóveis disponíveis no dataset através da análise e manipulação de dados para auxiliar a tomada de decisão do time de negócio. 

## 2. Questão de negócio

As principais questões de negócio são: 

- Quais são os imóveis devem ser comprados e por qual preço?
- Uma vez o imóvel comprado, qual o melhor momento para vendê-lo e por qual preço? Quando ele deve ser vendido para ter a maximização do lucro?

## 3. Premissas do negócio

- A média do preço das casas na região de Seattle é de U$300.000,00.
- Os imóveis do portfólio apresentam diferentes condições de uso.

## 4. Planejamento da solução

- Coletar os dados do site Kaggle;
- Entender qual vai ser o produto entregue;
- Decidir quais ferramentas vão ser usadas para análise;
- Tratar os dados para identificar possíveis outliers;
- Agrupar os dados para uma melhor análise;
- Fazer uma análise descritiva;
- Responder as perguntas de negócio.

## 5. Principais Insights

**Hipótese 1 -** Imóveis que possuem vista para água, são 3x mais caros, na média.

![H1.png](https://github.com/laaisfmaia/Projeto-Insights-House-Rocket/blob/main/cursoDS/H1.png)

A média de preços dos imóveis SEM VISTA para o água é de aproximadamente U$531.563,60. E a média de preços dos imóveis COM VISTA para a água é de U$1.661.876,02.

Dessa forma, nota-se que a Hipótese 1 é VERDADEIRA e os imóveis com vista para o água são cerca de 3x mais caros.

**Hipótese 2 -** Imóveis com data de construção menor que 1955, são na média 50% mais baratos.

![H2.png](https://github.com/laaisfmaia/Projeto-Insights-House-Rocket/blob/main/cursoDS/H2.png)

Nota-se que a Hipótese 2 de que Imóveis com data de construção menor que 1955 são na média 50% mais baratos é FALSA, visto que foi constatado que os valores médios dos preços são praticamente os mesmos, variando cerca de 1%.

**Hipótese 3 -** Imóveis sem porão possuem área total (sqft_lot) 40% maior do que os imóveis com porão.

![H3.png](https://github.com/laaisfmaia/Projeto-Insights-House-Rocket/blob/main/cursoDS/H3.png)

Nota-se que a Hipótese 3 de que Imóveis sem porão possuem área total 40% maior do que os imóveis com porão é FALSA, visto que a área total dos imóveis sem porão é cerca de 20% maior dos que os imóveis com porão.

**Hipótese 4 -** O crescimento do preço dos imóveis YoY ( Year over Year ) é de 10%

Os imóveis disponíveis no Dataset foram adiquiridos entre maio de 2014 e maio de 2015. Dessa forma, foi feito a comparação dos valores referentes a maio/2014 com maio/2015.

![H4.png](https://github.com/laaisfmaia/Projeto-Insights-House-Rocket/blob/main/cursoDS/H4.png)

Nota-se que a Hipótese 4 de que o crescimento do preço dos imóveis YoY (Year over Year - comparação ano a ano) é de 10% é FALSA, visto que os valores médios dos preços entre os dois anos variam cerca de 2%.

**Hipótese 5 -** Imóveis com 3 banheiros tem um crescimento MoM ( Month over Month ) de 15%

Média do preço dos imóveis por mês no ano:

![H5.1.png](https://github.com/laaisfmaia/Projeto-Insights-House-Rocket/blob/main/cursoDS/H5.1.png)

Nota-se que o crescimento do preço dos imóveis varia de mês em mês. Podendo chegar a um acréscimo de cerca de 12% assim como uma diminuição de 12%. Dessa forma, percebe-se que a Hipótese 5 de que os Imóveis com 3 banheiros tem um crescimento MoM ( Month over Month - comparação mês a mês ) de 15% é FALSA, sendo que a porcentagem média de acréscimo durante o período contabilizado é de cerca de 0.23%.

![H5.2.png](https://github.com/laaisfmaia/Projeto-Insights-House-Rocket/blob/main/cursoDS/H5.2.png)

[Acesso ao código](https://github.com/laaisfmaia/Projeto-Insights-House-Rocket/blob/main/cursoDS/Parte%2010%20-%20Hip%C3%B3teses%20sobre%20o%20neg%C3%B3cio.ipynb)

## 6. Resultados financeiros

A partir da análise dos dados foi feita uma sugestão de compra dos imóveis. Tal sugestão está relacionada com a região, uma vez que a região interfere significativamente no preço, com a condição da casa e com a característica de ter vista para a água.

O imóvel foi sugerido para compra se:

- seu preço estiver abaixo da mediana da região;
- se a condição da casa estiver boa e
- se tiver vista para a água.

Tabela com os imóveis sugeridos para a compra:
|       |         id |   zipcode |   price |   price_median |   condition |   waterfront | status   |
|------:|-----------:|----------:|--------:|---------------:|------------:|-------------:|:---------|
| 10674 | 7631800110 |     98166 |  380000 |         390000 |           3 |            1 | Compra   |
| 11189 | 2123039032 |     98070 |  369900 |         463750 |           5 |            1 | Compra   |
| 11193 | 3523029041 |     98070 |  290000 |         463750 |           4 |            1 | Compra   |
| 11207 | 8550001515 |     98070 |  429592 |         463750 |           5 |            1 | Compra   |
| 11224 |  222029026 |     98070 |  340000 |         463750 |           5 |            1 | Compra   |
| 11237 |  221029019 |     98070 |  400000 |         463750 |           3 |            1 | Compra   |
| 11285 | 2923039243 |     98070 |  340000 |         463750 |           3 |            1 | Compra   |
| 11295 | 2781600195 |     98070 |  285000 |         463750 |           3 |            1 | Compra   |
| 11300 | 5216200090 |     98070 |  385000 |         463750 |           4 |            1 | Compra   |

Além da região, outro aspecto que influencia no preço dos imóveis é a sazonalidade. Um exemplo é que no verão os imóveis mais próximas de lagos tem uma alta de preço, já que a procura por esse tipo de estabelecimento aumenta nessa época.

Dessa forma, foi criado uma recomendação de venda dos imóveis com base na mediana dos preços em relação a região e sazonalidade. E, a partir dessa análise, foi calculada a margem de lucro obtida em cada revenda, que apresentou um montante de **U$2.016.458.904,40**

Condições de venda:

- Se o preço da compra for maior que a mediana da região + sazonalidade:
    - O preço da venda será igual ao preço da compra + 10%
- Se o preço da compra for menor que a mediana da região + sazonalidade:
    - O preço da venda será igual ao preço da compra + 30%

Tabela com os preços sugeridos para venda dos 20 primeiros imóveis:

|    |         id |   zipcode | season   |   price |   price_median |   price_sale | % de lucro   |   lucro |
|---:|-----------:|----------:|:---------|--------:|---------------:|-------------:|:-------------|--------:|
|  0 | 7129300520 |     98178 | autumn   |  221900 |         290500 |       288470 | +30%         |   66570 |
|  1 | 2976800796 |     98178 | autumn   |  236000 |         290500 |       306800 | +30%         |   70800 |
|  2 | 1180003090 |     98178 | autumn   |  190000 |         290500 |       247000 | +30%         |   57000 |
|  3 | 2171400197 |     98178 | autumn   |  350000 |         290500 |       385000 | +10%         |   35000 |
|  4 | 1180002378 |     98178 | autumn   |  299000 |         290500 |       328900 | +10%         |   29900 |
|  5 | 1180500070 |     98178 | autumn   |  335000 |         290500 |       368500 | +10%         |   33500 |
|  6 |  179000350 |     98178 | autumn   |  194000 |         290500 |       252200 | +30%         |   58200 |
|  7 | 3810000202 |     98178 | autumn   |  251700 |         290500 |       327210 | +30%         |   75510 |
|  8 | 4058802105 |     98178 | autumn   |  150000 |         290500 |       195000 | +30%         |   45000 |
|  9 | 7878400135 |     98178 | autumn   |  355000 |         290500 |       390500 | +10%         |   35500 |
| 10 | 7887200390 |     98178 | autumn   |  294000 |         290500 |       323400 | +10%         |   29400 |
| 11 |  179003055 |     98178 | autumn   |  210000 |         290500 |       273000 | +30%         |   63000 |
| 12 | 8073000495 |     98178 | autumn   |  700000 |         290500 |       770000 | +10%         |   70000 |
| 13 | 7813200115 |     98178 | autumn   |  100000 |         290500 |       130000 | +30%         |   30000 |
| 14 | 4058801240 |     98178 | autumn   |  330000 |         290500 |       363000 | +10%         |   33000 |
| 15 | 3352402250 |     98178 | autumn   |  119900 |         290500 |       155870 | +30%         |   35970 |
| 16 |  399000195 |     98178 | autumn   |  200000 |         290500 |       260000 | +30%         |   60000 |
| 17 | 8073000265 |     98178 | autumn   |  360000 |         290500 |       396000 | +10%         |   36000 |
| 18 | 1180500100 |     98178 | autumn   |  353000 |         290500 |       388300 | +10%         |   35300 |
| 19 |  185000161 |     98178 | autumn   |  261000 |         290500 |       339300 | +30%         |   78300 |

[Clique aqui](https://github.com/laaisfmaia/Projeto-Insights-House-Rocket/blob/main/cursoDS/sugestao_pre%C3%A7o_venda.csv) para visualizar o arquivo .csv completo

[Acesso ao código](https://github.com/laaisfmaia/Projeto-Insights-House-Rocket/blob/main/cursoDS/Parte%209%20-%20Resultados%20financeiros%20-%20ETL.py)

## 7. Conclusão

- A análise permitiu encontrar 9 casas que estão aptas para a compra.
- A utilização dessa metodologia no auxílio na tomada de decisão para definição do preço de compra e revenda dos imóveis do portfólio proporcionará um lucro de **U$2.016.458.904,40**
- [Clique aqui](https://analytics-house-rocket-lais.herokuapp.com/) para acessar o relatório completo.

## 8. Próximos passos

- Analisar os imóveis que podem ser aptos para uma reforma e posterior revenda.
- Criação de um modelo de Machine Learning para otimização do método.

## 9. Extra

- Para acessar outras análises e maninupalações de dados feitas com esse dataset acesse os [notebooks 1 ao 10](https://github.com/laaisfmaia/Projeto-Insights-House-Rocket/tree/main/cursoDS) 
- Para acessar o código completo [clique aqui](https://github.com/laaisfmaia/Projeto-Insights-House-Rocket/blob/main/cursoDS/Parte%208%20-%20C%C3%B3digo%20para%20produ%C3%A7%C3%A3o.py)


