import speech_recognition as sr
import pyttsx3
import csv

# Configuração do reconhecimento de voz
r = sr.Recognizer()
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)

# Configuração do sintetizador de voz
engine = pyttsx3.init()

# Função para ler os dados do usuário
def get_user_data():
    name = ''
    cpf = ''
    phone = ''

    # Obtém o nome do usuário
    while not name:
        engine.say('Olá, qual é o seu nome?')
        engine.runAndWait()
        try:
            with sr.Microphone() as source:
                audio = r.listen(source)
            name = r.recognize_google(audio, language='pt-BR')
        except:
            engine.say('Desculpe, não entendi. Por favor, repita.')
            engine.runAndWait()

    # Obtém o CPF do usuário
    while not cpf:
        engine.say(f'Ok, {name}, qual é o seu CPF?')
        engine.runAndWait()
        try:
            with sr.Microphone() as source:
                audio = r.listen(source)
            cpf = r.recognize_google(audio, language='pt-BR')
        except:
            engine.say('Desculpe, não entendi. Por favor, repita.')
            engine.runAndWait()

    # Obtém o número de telefone do usuário
    while not phone:
        engine.say(f'Ótimo, agora me diga o seu número de telefone.')
        engine.runAndWait()
        try:
            with sr.Microphone() as source:
                audio = r.listen(source)
            phone = r.recognize_google(audio, language='pt-BR')
        except:
            engine.say('Desculpe, não entendi. Por favor, repita.')
            engine.runAndWait()

    # Salva os dados do usuário em um arquivo CSV
    with open('user_data.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, cpf, phone])
        engine.say(f'{name}, seu cadastro foi realizado com sucesso!')
        engine.runAndWait()

# Executa a função principal
get_user_data()
