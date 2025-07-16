# Bot de Cadastro de Produtos - Hashtag Intensivão

Este bot automatiza o processo de cadastro de produtos no formulário do curso Intensivão de Python da Hashtag.

## Funcionalidades

- Abre o navegador e acessa o formulário online.
- Preenche os campos com base em um arquivo `produtos.csv`.
- Envia os dados automaticamente para cada linha da planilha.

## Requisitos

- Python 3
- Bibliotecas:
  - `pyautogui`
  - `pandas`

## Como usar

1. Instale as dependências:
pip install pyautogui pandas


2. Prepare um arquivo `produtos.csv` com as colunas:
- `codigo`, `marca`, `tipo`, `categoria`, `preco_unitario`, `custo`, `obs`

3. Execute o script




⚠️ **Atenção:** Verifique e ajuste as coordenadas `x` e `y` dos `pyautogui.click()` para sua tela.

## Autor

Desenvolvido por Guilherme Santos Pereira durante os estudos com a Hashtag Treinamentos.

