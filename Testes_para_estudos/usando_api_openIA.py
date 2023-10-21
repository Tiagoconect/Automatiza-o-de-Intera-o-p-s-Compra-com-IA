import openai

# Configuração da chave de API
openai.api_key = "<YOUR_API_KEY>"

# Função para enviar uma mensagem ao ChatGPT
def enviar_mensagem(texto):
    resposta = openai.Completion.create(
        engine="davinci",
        prompt=texto,
        max_tokens=50  # Ajuste o limite de tokens conforme necessário
    )
    return resposta.choices[0].text.strip()

# Função para lidar com respostas após uma compra
def responder_apos_compra(id_compra, perguntas):
    respostas = []
    
    for pergunta in perguntas:
        resposta = enviar_mensagem(pergunta)
        respostas.append(resposta)
    
    # Envie as respostas para o cliente ou faça algo com elas, como armazená-las em um sistema de suporte.
    enviar_respostas_a_cliente(id_compra, respostas)

# Função de exemplo para enviar respostas ao cliente (substitua por sua própria lógica)
def enviar_respostas_a_cliente(id_compra, respostas):
    # Neste exemplo, supomos que estamos apenas imprimindo as respostas
    print(f"Respostas para a compra {id_compra}:")
    for i, resposta in enumerate(respostas, start=1):
        print(f"Pergunta {i}: {resposta}")

if __name__ == "__main__":
    id_compra = 12345
    perguntas = ["Qual é o status da minha compra?", "Quando meu pedido será entregue?"]
    responder_apos_compra(id_compra, perguntas)
