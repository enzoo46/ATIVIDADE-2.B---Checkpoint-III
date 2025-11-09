from datetime import datetime

class Mensagem:
    def __init__(self, texto):
        self.texto = texto
        self.data_envio = datetime.now()

    def enviar(self, canal):
        print(f"Enviando mensagem pelo {canal.nome}: {self.texto}")


class MensagemTexto(Mensagem):
    pass


class MensagemFoto(Mensagem):
    def __init__(self, texto, arquivo, formato):
        super().__init__(texto)
        self.arquivo = arquivo
        self.formato = formato


class MensagemVideo(Mensagem):
    def __init__(self, texto, arquivo, formato, duracao):
        super().__init__(texto)
        self.arquivo = arquivo
        self.formato = formato
        self.duracao = duracao


class MensagemArquivo(Mensagem):
    def __init__(self, texto, arquivo, formato):
        super().__init__(texto)
        self.arquivo = arquivo
        self.formato = formato


class Canal:
    def __init__(self, nome):
        self.nome = nome

    def enviar_mensagem(self, mensagem, destino):
        print(f"\n[{self.nome}] Enviando para {destino}...")
        mensagem.enviar(self)


class WhatsApp(Canal):
    def __init__(self):
        super().__init__("WhatsApp")


class Telegram(Canal):
    def __init__(self):
        super().__init__("Telegram")


class Facebook(Canal):
    def __init__(self):
        super().__init__("Facebook")


class Instagram(Canal):
    def __init__(self):
        super().__init__("Instagram")



if __name__ == "__main__":
    Criar as mensagens:
    msg1 = MensagemTexto("Olá! Tudo bem?")
    msg2 = MensagemFoto("Confira essa foto!", "foto.jpg", "jpg")
    msg3 = MensagemVideo("Veja este vídeo!", "video.mp4", "mp4", "00:30")

    Criar os Canais:
    whatsapp = WhatsApp()
    telegram = Telegram()
    facebook = Facebook()

   Envio de mensagens:
    whatsapp.enviar_mensagem(msg1, "+55 11 99999-9999")
    telegram.enviar_mensagem(msg2, "@usuario123")
    facebook.enviar_mensagem(msg3, "user.fb")
