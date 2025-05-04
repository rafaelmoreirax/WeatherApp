# ☁️ Weather App (Clima via API) em Python

Uma aplicação simples de linha de comando feita em Python que busca e exibe o clima atual de uma cidade especificada pelo usuário, utilizando a API gratuita [wttr.in](https://wttr.in).

---

## 📌 Tópicos

- [🧠 Sobre o Projeto](#-sobre-o-projeto)
- [🖼️ Demonstração](#-demonstração)
- [🚀 Tecnologias Utilizadas](#-tecnologias-utilizadas)
- [⚙️ Como Executar](#️-como-executar)
- [🛠️ Funcionalidades](#️-funcionalidades)
- [📄 Licença](#-licença)
- [🤝 Contribuindo](#-contribuindo)

---

## 🧠 Sobre o Projeto

Este é um projeto simples de linha de comando em Python que permite ao usuário consultar a previsão do tempo de qualquer cidade utilizando a API pública `wttr.in`. Ele é ideal para quem está começando a aprender sobre requisições HTTP, consumo de APIs e manipulação de dados em JSON no Python.

---

## 🖼️ Demonstração

```bash
Digite o nome de uma cidade para ver o clima atual.
Para sair, digite 'q'.

Cidade: São Paulo

Tempo em São Paulo:
🌦️  Parcialmente nublado
🌡️  Temperatura: 22°C
💨  Vento: 15 km/h
```

---

## 🚀 Tecnologias Utilizadas

- Python 3.x
- Biblioteca [requests](https://pypi.org/project/requests/)

---

## ⚙️ Como Executar

1. **Clone o repositório:**

```bash
git clone https://github.com/rafaelmoreirax/weather-app-python.git
cd weather-app-python
```

2. **Instale as dependências:**

```bash
pip install requests
```

3. **Execute o script:**

```bash
python main.py
```

4. **Siga as instruções:**

- Digite o nome da cidade.
- Digite `q` para sair do programa.

---

## 🛠️ Funcionalidades

- [x] Busca do clima atual por nome da cidade
- [x] Suporte a múltiplas cidades
- [x] Interface simples via terminal
- [x] Utiliza dados em tempo real da API `wttr.in`
- [ ] Interface gráfica (em desenvolvimento)

---

## 📄 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---

## 🤝 Contribuindo

Contribuições são sempre bem-vindas!

1. Faça um fork do projeto
2. Crie uma branch para sua feature: `git checkout -b minha-feature`
3. Faça commit das suas alterações: `git commit -m 'feat: adiciona nova feature'`
4. Faça push para a branch: `git push origin minha-feature`
5. Abra um Pull Request

---

## 💡 Autor

Desenvolvido por [Rafael Moreira](https://github.com/rafaelmoreirax) ☀️
