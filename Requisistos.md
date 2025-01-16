# Requisitos
# Regras de Negócio - Sistema de Gestão Financeira

## 1. Cadastro de Usuários
1. O sistema deve permitir o cadastro de novos usuários com os seguintes campos obrigatórios:
   - Nome completo
   - E-mail (deve ser único)
   - Senha (mínimo de 8 caracteres, incluindo uma letra maiúscula, um número e um caractere especial)
2. O e-mail deve ser validado antes de concluir o cadastro.
3. Senhas devem ser armazenadas de forma segura usando hash (ex.: bcrypt).

## 2. Controle de Receitas e Despesas
1. Cada usuário pode cadastrar receitas e despesas com as seguintes informações:
   - Tipo: Receita ou Despesa
   - Categoria (ex.: Alimentação, Transporte, Lazer)
   - Valor (positivo e maior que zero)
   - Data da transação
   - Descrição (opcional)
2. O sistema deve validar que o valor da transação seja positivo.
3. Transações podem ser editadas ou excluídas pelo usuário a qualquer momento.

## 3. Controle de Contas Bancárias
1. O usuário pode registrar múltiplas contas bancárias com:
   - Nome da conta (ex.: Conta Corrente, Poupança)
   - Saldo inicial
2. O saldo da conta deve ser atualizado automaticamente com base nas receitas e despesas associadas.
3. Não é permitido que o saldo de uma conta fique negativo.

## 4. Relatórios Financeiros
1. O sistema deve gerar relatórios financeiros com as seguintes opções:
   - Resumo mensal de receitas, despesas e saldo.
   - Comparativo entre meses (ex.: gastos por categoria).
   - Gráficos ilustrando a evolução financeira.
2. Relatórios devem ser filtráveis por:
   - Período (mês/ano)
   - Categoria
   - Conta bancária

## 5. Planejamento Financeiro
1. O usuário pode definir metas financeiras com:
   - Nome da meta
   - Valor-alvo
   - Data limite
   - Descrição (opcional)
2. O sistema deve calcular automaticamente o progresso da meta com base nas economias do usuário.

## 6. Segurança e Privacidade
1. Todos os dados do usuário devem ser armazenados de forma criptografada.
2. Somente o próprio usuário deve ter acesso às suas informações financeiras.
3. O sistema deve permitir que o usuário exclua sua conta e todos os dados associados.

## 7. Notificações
1. O sistema deve enviar notificações por e-mail para:
   - Avisos de metas próximas do vencimento.
   - Lembretes de transações recorrentes.
   - Alertas de saldo baixo em contas bancárias.

## 8. Transações Recorrentes
1. O usuário pode configurar transações recorrentes (ex.: aluguel, salário) com:
   - Frequência (diária, semanal, mensal, anual)
   - Data de início e fim (opcional)
2. O sistema deve criar automaticamente as transações com base na configuração definida.

## 9. Exportação de Dados
1. O usuário pode exportar seus dados financeiros em formatos:
   - CSV
   - PDF
2. A exportação deve incluir opções de filtro (ex.: por período, por categoria).

## 10. Multimoedas
1. O sistema deve permitir o registro de transações em diferentes moedas.
2. O sistema deve calcular automaticamente o valor equivalente na moeda principal do usuário com base na taxa de câmbio atual.

---

Essas regras podem ser ajustadas para atender a requisitos específicos. Caso precise de algo mais detalhado ou queira expandir funcionalidades, é só pedir!
