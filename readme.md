# Extract API

Este projeto é uma aplicação Python que extrai dados de uma API, transforma os dados em um formato estruturado e os salva em um arquivo CSV.

## Estrutura do Projeto

- **`api.py`**: Contém o código principal para extração, transformação e carregamento dos dados.
- **`products.csv`**: Arquivo CSV gerado contendo os dados extraídos e transformados.
- **`readme.md`**: Este arquivo, com informações sobre o projeto.

## Funcionalidades

1. **Extração de Dados**: Os dados são extraídos de uma API pública usando a biblioteca `requests`.
2. **Transformação de Dados**: Os dados são processados e estruturados em um DataFrame usando a biblioteca `pandas`.
3. **Carregamento de Dados**: Os dados transformados são salvos em um arquivo CSV.

## Requisitos

- Python 3.7 ou superior
- Bibliotecas Python:
  - `requests`
  - `pandas`

## Como Executar

1. Instale as dependências necessárias:
   ```bash
   pip install requests pandas

2. Execute o script principal:
python api.py

3. Após a execução, o arquivo `products.csv` será gerado com os dados extraídos e transformados.

## Estrutura do CSV

O arquivo `products.csv` contém as seguintes colunas:

- `id`: Identificador único do produto.  
- `title`: Nome do produto.  
- `price`: Preço do produto.  
- `description`: Descrição do produto.  
- `discountPercentage`: Percentual de desconto aplicado ao produto.  
- `rating`: Avaliação média do produto.  
- `stock`: Quantidade em estoque.  
- `brand`: Marca do produto.  
- `category`: Categoria do produto.  
- `thumbnail`: URL da imagem do produto.  

## Exemplo de Uso

Este projeto pode ser usado para extrair dados de APIs públicas e salvá-los em um formato estruturado para análise ou integração com outros sistemas.

## Melhorias Futuras

- Adicionar suporte para mais campos da API.  
- Implementar tratamento de erros mais robusto.  
- Adicionar testes automatizados para validação do código.  

## Licença

Este projeto é de uso livre e aberto para modificações.