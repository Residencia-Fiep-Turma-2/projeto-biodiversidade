# Discussão sobre robustez, algoritmos, e qualidade de dados.

A importância da robustez dos algoritmos realizados é enfatizada conforme se testa diferentes bases de dados, sendo o algoritmo o responsável pelo tratamento dos dados
para que sua utilização seja menos dispendiosa. Erros referentes a dados faltantes e imprecisos são comumente encontrados em sistemas que não sejam amplamente testados 
em diversas condições.
Não diferente dos demais algoritmos que lidam com diferentes bases de dados e que não sejam de ampla utilização, os testes realizados sobre as funcionalidades propostas 
demonstram a fragilidade de algoritmos que precisam de software de terceiros cujo desenvolvedores não estão habituados, e também a escassez de dados obtidos de maneiras
não controladas.
Inicialmente, observando os dados faltantes e sua média por coluna fica claro como os dados tratados divergem entre si, obtendo médias 25% de dados faltantes por colunas,
afetando gravemente as funcionalidades propostas.
Campos obrigatórios ou automaticamente preenchidos levam a uma maior normalidade entre dados, como o observado no preenchimento taxonômico, não variando dentre as bases
de dados testadas. Filtros para dados também são afetados por dados faltantes podendo retornar menos valores do que o esperado, mas em situações controladas e conhecidas pelo desenvolvedor, 
resultados satisfatórios podem ser encontrados, como o foram em testes feitos para este caso.
Já a observação entre coordenadas dadas e a localização informada necessitou de software de terceiros para a obtenção da localização a partir dos dados de latitude e longitude,
retornando função com modelo próprio demonstra os problemas obtidos quando não se conhece muito bem os modelos utilizados. Situações de comparação demonstram problemas 
seja por cidades com nomes escritos de formas diferentes (Como por exemplo: Paraty e Parati) que fogem mesmo os tratamentos para pontuação diferentes. Outras situações como 
coordenadas inexistentes e até mesmo com caracteres não numéricos resultam em erros de sistema devido a dificuldade de se prever situações deste modo. 
Duas entre três bases de dados passaram com ressalvas (apenas situações de nomes divergentes para as mesmas cidades) nos testes para a observação de coordenadas, já o último caso
se encontra o único erro aferido durantes os testes devido a caracteres não numéricos presentes.
É então sugerido o tratamento desses dados para que este erro não ocorra futuramente.

