# 🧮 Matriz Inversa por Escalonamento e Solução de Sistemas via Inversa

![Python](https://img.shields.io/badge/Python-3-blue?logo=python&logoColor=white)
![Dependências](https://img.shields.io/badge/depend%C3%AAncias-nenhuma-brightgreen)
![Arquivo](https://img.shields.io/badge/arquivo%20%C3%BAnico-sim-informational)
![Documentação](https://img.shields.io/badge/coment%C3%A1rios-Doxygen-orange)

Projeto de **Álgebra Linear** que calcula a **inversa de uma matriz pelo método de escalonamento (Gauss-Jordan)** e usa essa inversa para **resolver sistemas lineares** da forma `A·x = b`.

Tudo em **um único arquivo Python**, sem bibliotecas externas, com código estrutural (apenas funções) e comentado no padrão **Doxygen**.

---

## 📑 Sumário

- [O que o programa faz](#-o-que-o-programa-faz)
- [Fundamentação teórica](#-fundamentação-teórica)
- [Como executar](#-como-executar)
- [Exemplo completo](#-exemplo-completo)
- [Estrutura do código](#-estrutura-do-código)
- [Casos de uso na vida real](#-casos-de-uso-na-vida-real)
- [Limitações e boas práticas](#-limitações-e-boas-práticas)
- [Testes realizados](#-testes-realizados)
- [Autor](#-autor)

---

## 🎯 O que o programa faz

1. Lê uma matriz quadrada **A** (n × n) e o vetor de termos independentes **b**.
2. Monta a matriz aumentada **[A | I]**.
3. Escalona até chegar em **[I | A⁻¹]** (Gauss-Jordan com pivoteamento parcial).
4. Calcula a solução do sistema: **x = A⁻¹ · b**.
5. **Verifica** o resultado: `A · A⁻¹ = I` e `A · x = b`.

Recursos extras:

- 🔍 **Passo a passo opcional:** mostra a matriz aumentada a cada operação, ideal para apresentar em sala.
- 🚫 **Detecção de matriz singular:** se `det(A) = 0`, avisa que não existe inversa, sem travar.
- ⌨️ **Entrada amigável:** aceita vírgula decimal (`1,5`) e pede o dado de novo se a entrada estiver errada.

---

## 📚 Fundamentação teórica

### Matriz inversa

A inversa de uma matriz quadrada **A** é a matriz **A⁻¹** tal que:

$$A \cdot A^{-1} = A^{-1} \cdot A = I$$

Ela só existe quando `det(A) ≠ 0` (matriz **invertível** ou **não singular**).

### Método de escalonamento (Gauss-Jordan)

A ideia é aplicar **operações elementares nas linhas** que transformam `A` em `I`. Aplicando exatamente as mesmas operações em `I`, ela se transforma em `A⁻¹`:

$$[\,A \mid I\,] \;\xrightarrow{\text{operações elementares}}\; [\,I \mid A^{-1}\,]$$

As operações permitidas são:

| Operação | Notação |
|---|---|
| Trocar duas linhas | `Li ↔ Lj` |
| Multiplicar uma linha por um número não nulo | `Li ← k·Li` |
| Somar a uma linha um múltiplo de outra | `Li ← Li + k·Lj` |

**Exemplo manual (2 × 2):** `A = [[2, 1], [5, 3]]`

```
[ 2  1 | 1  0 ]   L1 ← L1 / 2
[ 5  3 | 0  1 ]

[ 1  0,5 | 0,5  0 ]   L2 ← L2 − 5·L1
[ 5  3   | 0    1 ]

[ 1  0,5 |  0,5  0 ]   L2 ← L2 / 0,5
[ 0  0,5 | −2,5  1 ]

[ 1  0,5 |  0,5  0 ]   L1 ← L1 − 0,5·L2
[ 0  1   | −5    2 ]

[ 1  0 |  3  −1 ]
[ 0  1 | −5   2 ]      →   A⁻¹ = [[3, −1], [−5, 2]]
```

### Solução de sistemas via inversa

Dado o sistema `A·x = b`, se `A` é invertível, multiplicamos os dois lados por `A⁻¹`:

$$A\,x = b \;\Longrightarrow\; A^{-1}A\,x = A^{-1}b \;\Longrightarrow\; x = A^{-1}\,b$$

### Pivoteamento parcial

Em cada coluna, o programa escolhe como pivô o elemento de **maior valor absoluto** (da diagonal para baixo) e troca as linhas se necessário. Isso:

- evita dividir por zero quando há um zero na diagonal;
- reduz erros de arredondamento do ponto flutuante.

Se **todos** os candidatos a pivô forem (praticamente) zero, a matriz é singular.

---

## ▶️ Como executar

Requer apenas **Python 3**. Nenhuma instalação adicional.

```bash
git clone https://github.com/khaos77/Proj-Algebra-Linear-Inversa-Escalonamento.git
cd Proj-Algebra-Linear-Inversa-Escalonamento
python3 inversa_sistema.py
```

O programa pergunta, nesta ordem:

1. a **ordem** `n` da matriz;
2. as **linhas** da matriz A (valores separados por espaço);
3. o vetor **b**;
4. se você quer ver o **passo a passo** do escalonamento (`s` ou `n`).

---

## 💡 Exemplo completo

Sistema:

```
 2x +  y −  z =   8
−3x −  y + 2z = −11
−2x +  y + 2z =  −3
```

**Entrada:**

```
Ordem da matriz (n): 3

Digite a matriz A (3x3), uma linha por vez, valores separados por espaço:
  Linha 1: 2 1 -1
  Linha 2: -3 -1 2
  Linha 3: -2 1 2

Digite o vetor b (3 valores separados por espaço): 8 -11 -3

Mostrar passo a passo do escalonamento? (s/n): s
```

**Trecho final do passo a passo:**

```
Após zerar a coluna 2:
    1.0000    0.0000   -0.8000 |    0.0000   -0.2000   -0.2000
    0.0000    1.0000    0.4000 |    0.0000   -0.4000    0.6000
    0.0000    0.0000    0.2000 |    1.0000    0.8000   -0.2000

Após zerar a coluna 3:
    1.0000    0.0000    0.0000 |    4.0000    3.0000   -1.0000
    0.0000    1.0000    0.0000 |   -2.0000   -2.0000    1.0000
    0.0000    0.0000    1.0000 |    5.0000    4.0000   -1.0000
```

**Resultado:**

```
Matriz inversa A^-1:
    4.0000    3.0000   -1.0000
   -2.0000   -2.0000    1.0000
    5.0000    4.0000   -1.0000

Solução do sistema (x = A^-1 * b):
  x1 = 2.000000
  x2 = 3.000000
  x3 = -1.000000

Verificação A * A^-1 (deve ser a identidade):
    1.0000    0.0000    0.0000
    0.0000    1.0000   -0.0000
    0.0000   -0.0000    1.0000

Verificação A * x (deve ser igual a b):
  Linha 1: A*x = 8.000000   |   b = 8.000000
  Linha 2: A*x = -11.000000   |   b = -11.000000
  Linha 3: A*x = -3.000000   |   b = -3.000000
```

Solução: **x = 2, y = 3, z = −1** ✅

Matriz singular (sem inversa), por exemplo `A = [[1, 2], [2, 4]]`:

```
A matriz é SINGULAR (determinante = 0): não possui inversa.
Logo, o sistema não pode ser resolvido por este método.
```

---

## 🗂️ Estrutura do código

Tudo está em [`inversa_sistema.py`](inversa_sistema.py), organizado em funções:

| Função | Responsabilidade |
|---|---|
| `ler_matriz(n)` | Lê a matriz A do teclado, validando cada linha |
| `ler_vetor(n)` | Lê o vetor b, validando o tamanho |
| `imprimir_matriz(M, titulo, separador)` | Imprime matrizes (com barra `\|` na matriz aumentada) |
| `montar_matriz_aumentada(A)` | Constrói `[A \| I]` |
| `inversa_por_escalonamento(A, passo_a_passo)` | Gauss-Jordan com pivoteamento parcial; retorna `A⁻¹` ou `None` se singular |
| `multiplicar_matriz_vetor(M, v)` | Calcula `M · v` |
| `multiplicar_matrizes(A, B)` | Calcula `A · B` (usada na verificação) |
| `resolver_sistema_via_inversa(A_inv, b)` | Calcula `x = A⁻¹ · b` |
| `main()` | Fluxo principal: entrada, cálculo, saída e verificação |

Todas as funções têm documentação Doxygen (`@brief`, `@param`, `@return`).

---

## 🌍 Casos de uso na vida real

A inversa por escalonamento e a solução de sistemas aparecem sempre que várias grandezas se influenciam **ao mesmo tempo**. Os exemplos abaixo são didáticos, e você pode reproduzir cada um no programa.

### ⚡ 1. Circuitos elétricos (análise de malhas)

Pela Lei das Tensões de Kirchhoff, um circuito com 3 malhas gera `R · I = V`, onde `R` é a matriz de resistências (em Ω), `I` as correntes de malha e `V` as fontes de tensão.

```
Entrada:  A = [[ 10, −4, −2],     b = [18, 2, 6]
               [ −4, 12, −5],
               [ −2, −5, 11]]

Saída:    I = [3, 2, 2]   →   3 A, 2 A e 2 A nas malhas 1, 2 e 3
```

💡 Na diagonal fica a resistência total de cada malha, e fora dela, o negativo da resistência compartilhada entre malhas. **Vantagem da inversa:** se você trocar as fontes de tensão, não precisa escalonar de novo, basta multiplicar `R⁻¹` pelo novo `V`.

### 📈 2. Economia: modelo de insumo-produto de Leontief

Cada setor da economia consome produtos dos outros para produzir. Com a matriz de coeficientes técnicos `A` e a demanda final `d`, a produção necessária `x` satisfaz `(I − A)·x = d`.

```
Setor 1 (agricultura) e Setor 2 (indústria)

(I − A) = [[ 0,8, −0,3],     d = [60, 30]   (demanda final, em milhões)
           [−0,4,  0,9]]

Saída:   x = [105, 80]   →   produção total necessária de cada setor
```

💡 Aqui a própria **inversa** é o resultado de interesse (a "matriz de Leontief"):

```
(I − A)⁻¹ = [[1,500  0,500],
             [0,667  1,333]]
```

Ela diz quanto cada setor precisa produzir para atender **uma unidade** de demanda final de cada setor.

### 🥣 3. Nutrição e misturas (ração, ligas, fertilizantes)

Quanto usar de cada ingrediente para atingir uma meta de nutrientes? Cada coluna da matriz é um ingrediente (g de nutriente por 100 g) e `b` é a meta.

```
              Ingr. A  Ingr. B  Ingr. C
Proteína   [    40       10       20   ]       meta: 130 g
Carboidr.  [    30       60       10   ]       meta: 250 g
Gordura    [    10       20       50   ]       meta: 130 g

Saída:   x = [2, 3, 1]   →   200 g de A, 300 g de B e 100 g de C
```

### 🎮 4. Computação gráfica: desfazer uma transformação

Uma transformação linear 2D (escala, rotação, cisalhamento) leva o ponto original `p` até a tela: `q = M · p`. Para descobrir **qual ponto do objeto foi clicado** na tela, usamos `p = M⁻¹ · q`.

```
M = [[2, 1],        M⁻¹ = [[ 1, −1],
     [1, 1]]               [−1,  2]]

Clique na tela em q = (7, 4)   →   ponto original p = M⁻¹·q = (3, 1)
```

💡 Engines gráficas usam matrizes 4×4 em coordenadas homogêneas, mas a ideia é a mesma.

### 🚦 5. Tráfego: estimar fluxos que não se medem diretamente

Quando os sensores só medem **somas** de fluxos (por exemplo, o total que passa por pares de vias), é preciso desmembrar os valores individuais.

```
x₁ + x₂ = 800
     x₂ + x₃ = 900        A = [[1,1,0],[0,1,1],[1,0,1]]    b = [800, 900, 700]
x₁      + x₃ = 700

Saída:   x = [300, 500, 400] veículos/hora
```

### 🔧 Outras aplicações

- **Engenharia estrutural:** em treliças e vigas, `K·u = F` relaciona rigidez, deslocamentos e forças.
- **Regressão linear (mínimos quadrados):** os coeficientes saem de `β = (XᵀX)⁻¹·Xᵀy`.
- **Criptografia de Hill:** a mensagem é cifrada com uma matriz-chave e decifrada com a inversa dela (módulo 26, uma variação do conceito).

---

## ⚠️ Limitações e boas práticas

- **A matriz precisa ser quadrada e invertível.** Matrizes singulares (`det = 0`) são detectadas, e o programa avisa em vez de falhar.
- **Ponto flutuante:** matrizes muito mal condicionadas (determinante muito próximo de zero) podem dar resultados imprecisos. Pivôs com valor absoluto menor que `1e-12` são tratados como zero (constante `EPS`).
- **Custo computacional:** o método é O(n³). Para resolver **um único sistema**, eliminar diretamente é mais barato do que calcular a inversa, e bibliotecas profissionais (como `numpy.linalg.solve`) usam fatoração LU.
- **Quando a inversa compensa:** quando a mesma `A` é usada com **vários vetores `b`** diferentes (como no circuito), ou quando a própria `A⁻¹` é o que se quer (como em Leontief).

Este projeto tem objetivo **didático**: mostrar, passo a passo, como o método funciona por dentro.

---

## ✅ Testes realizados

O programa foi comparado com o `numpy` (usado só para conferir, não é dependência do projeto):

- matrizes **1×1**, **2×2** e identidade **4×4**;
- matriz com **zero na diagonal** (exige troca de linhas);
- matrizes **singulares** (linha dependente, linha de zeros, 2×2 e 3×3), todas detectadas corretamente;
- **300 matrizes aleatórias** de ordem 2 a 10, com inversa e solução do sistema iguais às do `numpy` (tolerância de 1e-6);
- entrada pelo terminal com vírgula decimal, quantidade errada de valores e texto no lugar de número.

---

## 👤 Autor

Feito por [**khaos77**](https://github.com/khaos77) para a disciplina de Álgebra Linear.
