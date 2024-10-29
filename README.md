# Atividade Pontuada

### Objetivo:
Em até 3 componentes, crie um software com 5 funcionalidades para um dos sistemas de gestão listados abaixo:

- Banco ESCOLHIDO(PORFAVOR LER A BAIXO DETALHES)
- Biblioteca
- Vendas
- RH (Recursos Humanos)
- Estoque

Cada um dos participantes deve escrever o código necessário para as funcionalidades usando funções, listas e aplicando as boas práticas para nomear variáveis e funções no código.

### Tecnologias:
- Linguagem de programação: Python
- Versionamento: Git

### Observações:
- Não devem ser realizados commits na branch main
- A branch main deve receber apenas merge
- Todos devem criar uma branch para adicionar funcionalidades
- As branches devem ser deletadas após realizar merge

ALUNOS: Matheus Gabriel, Iury Alves e Gabriel Neves
  
  BANCO CAIXA:
  LOGIN: Matheus Gabriel, Senha: caixa@1234, saldo inicial é 2100

  EXPLICAÇAO DA OPÇAO 5(Consulta de Rendimento):
  A consulta de rendimento é uma simulação que calcula quanto o saldo atual de uma conta bancaria poderia render em um período específico, usando uma taxa de rendimento fixa. Esse tipo de funcionalidade é útil para simular os ganhos em uma aplicação financeira, como uma conta de poupança ou um fundo de investimento.

  Como Funciona a Consulta de Rendimento
Taxa de Rendimento: Na função consultar_rendimento, usamos uma taxa de rendimento de 0,5% (0.005) para simular o ganho. Isso significa que, com esse rendimento, o saldo aumentaria 0,5% sobre o valor atual.

Por exemplo, se a taxa de rendimento fosse mensal, esse cálculo mostraria quanto seu saldo renderia em um mês.
Cálculo do Rendimento: O rendimento é calculado multiplicando o saldo atual pela taxa de rendimento.

Fórmula: rendimento = saldo * taxa_rendimento
Suponha que o saldo seja R$ 2.100,00 e a taxa seja 0,5%. Nesse caso, o rendimento seria:

rendimento = 2100 × 0.005 = 10.50

Então, para um saldo de R$ 2.100, o usuário veria um rendimento estimado de R$ 10,50.
Apresentação do Resultado: Após o cálculo, o programa exibe uma mensagem com o saldo atual e o rendimento calculado. Esse valor é apenas ilustrativo e ajuda o usuário a ter uma ideia de quanto seu saldo poderia crescer com base na taxa informada.

Limitações e Simplificações
Essa consulta é uma simulação com algumas simplificações:

Taxa Fixa: Estamos usando uma taxa fixa de 0,5%, mas no mercado financeiro, as taxas de rendimento variam.
Não considera Impostos ou Taxas: Na prática, rendimentos sobre aplicações financeiras podem estar sujeitos a impostos, como o Imposto de Renda, que não são considerados aqui.
Em resumo, essa consulta serve como uma ferramenta educativa e ilustrativa, que permite ao usuário visualizar um potencial crescimento do saldo em um determinado período, usando uma taxa de rendimento fixa.
