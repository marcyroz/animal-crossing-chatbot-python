# 🏝️🐹 Chatbot Animal Crossing
<img width="1880" height="863" alt="image" src="https://github.com/user-attachments/assets/6bad6bfc-da0f-4d0d-abaa-10bf101cdfb8" />

Um chatbot fofinho baseado em **LangChain** e **Groq LLaMA 3.3** que responde apenas sobre o universo de **Animal Crossing**.  
Ele tem um limite de **3 perguntas por sessão**, gera um **resumo amigável** ao final e permite **resetar** ou **encerrar** a conversa.  

---

## ✨ Funcionalidades

- 🌸 Responde **somente** perguntas sobre **Animal Crossing**.  
- 📝 Mantém o formato de resposta fixo:

```

Pergunta: ...
Resposta: ...

```

- 📋 Ao final de 3 perguntas, gera um **resumo fofo e organizado**.  
- 🔄 Opções de **resetar** a conversa ou **encerrar** o chat.  
- ⚠️ Se o usuário digitar algo inválido no menu final, o chatbot pede uma opção correta.  

---

## 🛠️ Tecnologias usadas

- [Python 3.10+](https://www.python.org/)  
- [LangChain](https://www.langchain.com/)  
- [Groq API](https://groq.com/)  
- [python-dotenv](https://pypi.org/project/python-dotenv/)  

---

## 📦 Instalação

1. Clone este repositório:

```

git clone [https://github.com/marcyroz/animal-crossing-chatbot-python.git](https://github.com/marcyroz/animal-crossing-chatbot-python.git)
cd animal-crossing-chatbot-python

```

2. Crie e ative um ambiente virtual (opcional, mas recomendado):

```

python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

```

3. Instale as dependências:

```

pip install -r requirements.txt

```

4. Altere o nome do ".env.example" para ".env" e adicione sua chave da api do Groq:

```

GROQ_API_KEY="sua_chave_aqui"

```

---

## ▶️ Como usar

1. Execute o chatbot:

```

python app.py
ou
py app.py

```

2. Interaja com o bot:

```

🌸🌻🐹 Chatbot Animal Crossing está pronto! Digite 'sair' para encerrar.🌸🌻

Você: Quem é a Isabelle?
Bot:
Pergunta: Quem é a Isabelle?
Resposta: Isabelle é uma adorável secretária que ajuda na administração da sua ilha!

Você: ...

```

3. Após 3 perguntas, o bot gera um resumo:

```

📋 Resumo da conversa até agora:
Resumo: Você perguntou sobre Isabelle e outros personagens da vila.
Eu respondi com carinho e dicas úteis sobre Animal Crossing!

⚠️ Você atingiu o limite de 3 perguntas neste chat.
Digite 'reset' para iniciar uma nova conversa ou 'sair' para encerrar.

```

---

## 📂 Estrutura do projeto

```

chatbot-animal-crossing/
│── app.py           # Código principal do chatbot
│── .env             # Variável de ambiente (não subir para o GitHub!)
│── requirements.txt # Dependências do projeto
│── README.md        # Documentação do projeto

```

---

## 📜 Regras do bot

- Responde apenas sobre **Animal Crossing**.
- Sempre usa o formato definido:

```

Pergunta: ...
Resposta: ...

```

- É sempre **fofo(a), acolhedor(a) e caloroso(a)**.
- Se o usuário falar de outro assunto → responde que só pode falar de Animal Crossing.
- Nunca estende demais as respostas.

---

## 👩‍💻 Autora

Feito com carinho para o universo de **Animal Crossing** 🌸✨
