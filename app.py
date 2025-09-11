import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain.schema import HumanMessage, SystemMessage

load_dotenv()

llm = init_chat_model("llama-3.3-70b-versatile", model_provider="groq")

system_message = SystemMessage(
    content=(
        "🌸 **Instruções do personagem** 🌸\n\n"
        "Você é um(a) morador(a) da vila de **Animal Crossing**. Seu papel é:\n"
        "- Responder APENAS perguntas relacionadas a Animal Crossing.\n"
        "- Ser sempre **fofo(a), acolhedor(a) e caloroso(a)** nas respostas.\n\n"
        "**Formato da resposta (OBRIGATÓRIO):**\n"
        "\"Pergunta: ...\"\n"
        "\"Resposta: ...\"\n\n"
        "Se a pergunta não for sobre Animal Crossing, responda educadamente que só pode falar sobre esse tema."
        "Evite extender demais as respostas; seja breve e direto(a) ao ponto."
    )
)

def enviar_mensagem(mensagens_anteriores):
    ultima_mensagem = mensagens_anteriores[-1]  # pega só a última
    mensagens = [system_message, ultima_mensagem]
    resposta = llm.invoke(mensagens)
    return resposta.content


def gerar_resumo(mensagens):
    resumo_instrucao = HumanMessage(
        content=(
            "Faça um resumo amigável e organizado de todas as perguntas e respostas até agora, incluindo a última. Use uma linguagem clara, curta e fofa, adequada ao universo de Animal Crossing."
            "Não repita as perguntas e respostas no formato original."
            "O resumo deve ser apresentado diretamente, sem repetir instruções internas."
            "Ao terminar de responder, deixe claro que a  conversa acabou e o usuário pode digitar 'reset' para reiniciar a conversa ou 'sair' para encerrar."
            "Formato do resumo:\n\n"
            "Resumo: ...\n"
        )
    )
    mensagens_resumo = [system_message] + mensagens + [resumo_instrucao]
    resposta_resumo = llm.invoke(mensagens_resumo)
    return resposta_resumo.content

def chat():
    mensagem_inicial = "🌸🌻🐹 Chatbot Animal Crossing está pronto! Digite 'sair' para encerrar.🌸🌻"
    mensagens_anteriores = []
    contador_usuario = 0
    MAX_PERGUNTAS = 3

    print(mensagem_inicial)
    while True:
        entrada = input("Você: ")
        if entrada.lower() == 'sair':
            break
        if entrada.lower() == 'reset':
            mensagens_anteriores = []
            contador_usuario = 0
            print("🔄 Conversa reiniciada.\n" + mensagem_inicial)
            continue

        mensagens_anteriores.append(HumanMessage(content=entrada))
        contador_usuario += 1

        resposta = enviar_mensagem(mensagens_anteriores)
        print(f"\nBot:\n{resposta}\n")

        if contador_usuario == MAX_PERGUNTAS:
            resumo = gerar_resumo(mensagens_anteriores)
            print("📋 Resumo da conversa até agora:\n")
            print(resumo)

            while True:
                escolha = input("\n⚠️ Você atingiu o limite de 3 perguntas neste chat.\nDigite 'reset' para iniciar uma nova conversa ou 'sair' para encerrar: ")
                if escolha.lower() == 'reset':
                    mensagens_anteriores = []
                    contador_usuario = 0
                    print("🔄 Conversa reiniciada.\n" + mensagem_inicial)
                    break
                elif escolha.lower() == 'sair':
                    print("👋 Até logo, jogador(a)!")
                    return
                else:
                    print("❌ Opção inválida! Digite apenas 'reset' ou 'sair'.")

if __name__ == "__main__":
    chat()
