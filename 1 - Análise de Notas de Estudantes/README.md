# Análise de Desempenho Escolar - Dataset de Estudantes

Este projeto tem como objetivo realizar uma análise sobre o desempenho acadêmico de 2.392 estudantes do ensino médio, com base em fatores como hábitos de estudo, envolvimento dos pais, atividades extracurriculares, e características demográficas. O objetivo é entender como esses fatores influenciam o desempenho acadêmico e como podemos prever as classificações dos estudantes.

## Sobre o Dataset

O **School Performance Dataset** contém informações detalhadas sobre 2.392 estudantes de ensino médio. As variáveis incluem dados demográficos, hábitos de estudo, envolvimento dos pais, participação em atividades extracurriculares e desempenho acadêmico. A variável alvo, **GradeClass**, classifica as notas dos alunos em cinco categorias distintas, oferecendo um robusto conjunto de dados para pesquisa educacional, modelagem preditiva e análise estatística.

### Variáveis no Dataset

#### Informações do Estudante
- **StudentID**: Identificador único atribuído a cada aluno (1001 a 3392).

#### Detalhes Demográficos
- **Age**: A idade dos alunos varia de 15 a 18 anos.
- **Gender**: Gênero dos alunos, onde 0 representa Masculino e 1 representa Feminino.
- **Ethnicity**: Etnia dos alunos, codificada como:
  - 0: Caucasiano
  - 1: Afro-americano
  - 2: Asiático
  - 3: Outro
- **ParentalEducation**: Nível educacional dos pais, codificado como:
  - 0: Nenhum
  - 1: Ensino Médio
  - 2: Ensino Superior Incompleto
  - 3: Bacharelado
  - 4: Pós-graduação

#### Hábitos de Estudo
- **StudyTimeWeekly**: Tempo de estudo semanal em horas, variando de 0 a 20 horas.
- **Absences**: Número de faltas durante o ano letivo, variando de 0 a 30.
- **Tutoring**: Status de tutoria, onde 0 indica Não e 1 indica Sim.

#### Envolvimento Parental
- **ParentalSupport**: Nível de apoio dos pais, codificado como:
  - 0: Nenhum
  - 1: Baixo
  - 2: Moderado
  - 3: Alto
  - 4: Muito Alto

#### Atividades Extracurriculares
- **Extracurricular**: Participação em atividades extracurriculares, onde 0 indica Não e 1 indica Sim.
- **Sports**: Participação em esportes, onde 0 indica Não e 1 indica Sim.
- **Music**: Participação em atividades musicais, onde 0 indica Não e 1 indica Sim.
- **Volunteering**: Participação em voluntariado, onde 0 indica Não e 1 indica Sim.

#### Desempenho Acadêmico
- **GPA**: Média de notas (Grade Point Average) em uma escala de 2.0 a 4.0, influenciada por hábitos de estudo, envolvimento dos pais e atividades extracurriculares.

#### Variável Alvo: **GradeClass**
Classificação das notas dos estudantes com base no GPA:
- **0**: 'A' (GPA >= 3.5)
- **1**: 'B' (3.0 <= GPA < 3.5)
- **2**: 'C' (2.5 <= GPA < 3.0)
- **3**: 'D' (2.0 <= GPA < 2.5)
- **4**: 'F' (GPA < 2.0)

## Objetivos do Projeto

1. **Análise Descritiva**: Analisar a distribuição das notas e dos fatores que impactam o desempenho acadêmico, como gênero, etnia e nível educacional dos pais.
2. **Correlação entre Variáveis**: Explorar como fatores como tempo de estudo, envolvimento dos pais, e participação em atividades extracurriculares influenciam o GPA.
3. **Modelagem Preditiva**: Desenvolver modelos para prever a classificação do desempenho dos alunos com base em suas características.
4. **Visualização de Dados**: Criar gráficos para entender melhor as distribuições e correlações entre as variáveis.

## Ferramentas Utilizadas

- **Python**: Linguagem de programação utilizada para análise de dados.
- **Pandas**: Biblioteca para manipulação de dados.
- **Matplotlib e Seaborn**: Bibliotecas para visualizações estáticas de dados.
- **Plotly**: Biblioteca para visualizações interativas.
- **Scikit-learn**: Biblioteca para construção de modelos de aprendizado de máquina.

## Como Executar o Projeto

### Pré-requisitos

Certifique-se de ter as bibliotecas necessárias instaladas:

```bash
pip install pandas matplotlib seaborn plotly scikit-learn
