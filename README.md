# 🖼️ PDI Studio — Sistema Interativo de Processamento e Análise de Imagens

O **PDI Studio** é uma aplicação desktop educacional desenvolvida em **Python** com **Tkinter**, baseada nos princípios de **Programação Orientada a Objetos (POO)** e no padrão de arquitetura **MVC (Model-View-Controller)**.

O objetivo do projeto é oferecer aos estudantes um ambiente prático e interativo para experimentar conceitos fundamentais da disciplina de **Processamento Digital de Imagens (PDI)**, permitindo visualizar transformações e analisar resultados em tempo real.

---

## 🎯 Sobre o Projeto

O software funciona como uma mini-suíte de laboratório de PDI, cobrindo:
* **Gerenciamento de Imagens:** Carregamento de imagens em múltiplos formatos (`.png`, `.jpg`, `.jpeg`, `.bmp`), exportação dos resultados e restauração da imagem original a qualquer momento.
* **Espaços e Modelos de Cores:** Conversão de BGR/RGB para Tons de Cinza, HSV, LAB, RGBA e CMYK.
* **Análise de Histograma:** Visualização gráfica da distribuição de intensidades de pixels (monocromático ou por canais R, G, B) em janela dedicada via **Matplotlib** e equalização de histograma.
* **Limiarização e Segmentação:** Técnicas de binarização e segmentação incluindo limiarização global, método automático de **Otsu**, limiarização adaptativa e multissegmentação (quantização em níveis).
* **Painel de Auditoria e Logs:** Histórico em tempo real de todas as ações e transformações realizadas na sessão.

---

## 🏗️ Arquitetura do Software (MVC)

O projeto é estruturado para ensinar boas práticas de engenharia de software e separação de responsabilidades:

```
pdi_studio/
├── main.py                     # Ponto de entrada (execução principal)
├── requirements.txt            # Dependências externas do projeto
├── README.md                   # Manual de instalação e documentação
├── .gitignore                  # Arquivos desconsiderados no versionamento
│
├── controllers/
│   └── controller.py           # Controlador principal: orquestra a View e o Model
│
├── models/
│   ├── model.py                # Modelo central: gerencia o estado da imagem atual
│   ├── color_model.py          # Módulo de conversão entre espaços de cores
│   ├── histogram_model.py      # Módulo de cálculo e equalização de histogramas
│   ├── threshold_model.py      # Módulo de algoritmos de limiarização e segmentação
│   └── utils.py                # Funções utilitárias e conversões para Tkinter
│
└── views/
    ├── view.py                 # Janela principal que agrega os componentes visuais
    ├── menu_bar.py             # Barra de menus superior (Arquivo, Cores, Histograma, etc.)
    ├── image_panel.py          # Área central de exibição da imagem
    ├── control_panel.py        # Painel lateral com o histórico de logs
    └── histogram_canvas.py     # Componente gráfico com Matplotlib embutido no Tkinter
```

---

## 🛠️ Pré-requisitos

Antes de iniciar, certifique-se de ter instalado em sua máquina:
* **Python 3.10 ou superior** ([Download do Python oficial](https://www.python.org/downloads/))
* **Pip** (gerenciador de pacotes do Python, já incluso na maioria das instalações)

> [!IMPORTANT]
> **Atenção para usuários de Linux (Ubuntu/Debian e derivados):**
> O módulo gráfico `tkinter` requer a biblioteca do sistema instalada. Se necessário, instale com o comando:
> ```bash
> sudo apt update && sudo apt install python3-tk
> ```

---

## 🚀 Guia Passo a Passo de Instalação para o Aluno

Siga os passos abaixo no terminal do seu sistema operacional (Linux, macOS ou Windows):

### 1. Clonar ou Baixar o Projeto
Abra o terminal na pasta onde deseja salvar o projeto:
```bash
git clone https://github.com/Prof-Saulo-Santos/pdi-studio.git
cd pdi_studio
```
*(Caso tenha baixado o arquivo `.zip`, descompacte-o e abra o terminal dentro da pasta `pdi_studio`)*.

---

### 2. Criar um Ambiente Virtual (Recomendado)
O ambiente virtual isola as bibliotecas do projeto para não haver conflitos com outros pacotes do seu computador.

* **No Linux / macOS:**
  ```bash
  python3 -m venv .venv
  ```

* **No Windows:**
  ```powershell
  python -m venv .venv
  ```

---

### 3. Ativar o Ambiente Virtual

* **No Linux / macOS:**
  ```bash
  source .venv/bin/activate
  ```

* **No Windows (PowerShell):**
  ```powershell
  .venv\Scripts\Activate.ps1
  ```
  *(Se o PowerShell bloquear a execução de scripts, execute uma vez como Administrador: `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`)*

* **No Windows (Prompt de Comando / CMD):**
  ```cmd
  .venv\Scripts\activate.bat
  ```

> Você saberá que o ambiente está ativo quando o prefixo `(.venv)` aparecer no início da linha do terminal.

---

### 4. Instalar as Dependências

Com o ambiente virtual ativado, instale os pacotes listados no `requirements.txt`:
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

As seguintes bibliotecas serão instaladas automaticamente:
* `opencv-python`: Algoritmos de processamento digital de imagens.
* `Pillow`: Manipulação e compatibilidade de imagens para o Tkinter.
* `numpy`: Operações numéricas e matriciais de alta performance.
* `matplotlib`: Criação e plotagem dos gráficos de histograma.

---

### 5. Executar a Aplicação

Com as dependências instaladas, execute o arquivo principal:

* **No Linux / macOS:**
  ```bash
  python3 main.py
  ```

* **No Windows:**
  ```powershell
  python main.py
  ```

---

## 📖 Como Usar o Sistema

1. **Abrir Imagem:** No menu superior, clique em **Arquivo → Abrir...** e escolha uma imagem (`.jpg`, `.png`, `.bmp`).
2. **Aplicar Filtros e Transformações:**
   * **Cores:** Converta a imagem para *Tons de Cinza*, *Espaço HSV* ou *Espaço LAB*.
   * **Histograma:** Clique em *Visualizar Histograma* para abrir a análise gráfica detalhada ou em *Equalizar Histograma* para melhorar o contraste.
   * **Limiarização:** Selecione *Otsu*, *Adaptativa* ou *Multissegmentação* para binarizar e segmentar objetos.
3. **Restaurar Original:** Caso queira desfazer as transformações e voltar à imagem inicial, vá em **Arquivo → Restaurar Original**.
4. **Salvar Resultado:** Quando concluir o experimento, clique em **Arquivo → Salvar como...**.
5. **Histórico:** Observe o painel direito da interface, onde cada operação aplicada é registrada cronologicamente.

---

## ❓ Resolução de Problemas Frequentes

* **Erro: `ModuleNotFoundError: No module named 'tkinter'` (Linux):**
  Instale o pacote do sistema: `sudo apt install python3-tk`.
* **Erro: `pip: command not found`:**
  Certifique-se de que o Python foi adicionado ao PATH do sistema durante a instalação.
* **A imagem não carrega:**
  Verifique se o caminho da imagem não contém caracteres especiais incompatíveis e se o formato do arquivo é `.png`, `.jpg`, `.jpeg` ou `.bmp`.
