class Utente:
    def __init__(self, numero, nome, prioridade, sala, medico, enfermeiro):
        self.numero = numero
        self.nome = nome
        self.prioridade = prioridade
        self.sala = sala
        self.medico = medico
        self.enfermeiro = enfermeiro 


class SistemaGestaoHospital:
    def __init__(self):
        self.fila_espera = []
        self.contador_atendimento = 1


        self.salas_disponiveis = {
            "Sala 1": {"medico": "Dr. António Silva", "enfermeiro": "Enf.ª Maria Santos"},
            "Sala 2": {"medico": "Dra. Joana Costa", "enfermeiro": "Enf. Pedro Luanda"},
            "Sala 3": {"medico": "Dr. Fernando Sousa", "enfermeiro": "Enf.ª Ana Paula"}
        }

    def registar_utente(self):
        print("\n--- REGISTO DE NOVO UTENTE ---")
        nome = input("Nome completo do utente: ")


        resp_prioridade = input(
            "Possui prioridade clínica ou legal (Grávidas, Idosos, Deficiência, Urgência)? (s/n): ").strip().lower()
        prioridade = True if resp_prioridade == 's' else False


        print("\nSalas e Equipas Disponíveis:")
        for sala, info in self.salas_disponiveis.items():
            print(f"- {sala} | Médico: {info['medico']} | Enfermeiro: {info['enfermeiro']}")

        sala_escolhida = input("Indique a sala de atendimento para o encaminhamento: ")

        if sala_escolhida in self.salas_disponiveis:
            medico = self.salas_disponiveis[sala_escolhida]["medico"]
            enfermeiro = self.salas_disponiveis[sala_escolhida]["enfermeiro"]
        else:

            sala_escolhida = "Sala 1"
            medico = self.salas_disponiveis["Sala 1"]["medico"]
            enfermeiro = self.salas_disponiveis["Sala 1"]["enfermeiro"]
            print("Sala inválida. Atribuída por defeito à Sala 1.")


        novo_utente = Utente(
            numero=self.contador_atendimento,
            nome=nome,
            prioridade=prioridade,
            sala=sala_escolhida,
            medico=medico,
            enfermeiro=enfermeiro
        )


        if prioridade:

            self.fila_espera.insert(0, novo_utente)
            print(f"\n[PRIORITÁRIO] Utente registado com sucesso! Senha atribuída: {self.contador_atendimento}")
        else:
            self.fila_espera.append(novo_utente)
            print(f"\nUtente registado com sucesso! Senha atribuída: {self.contador_atendimento}")

        self.contador_atendimento += 1

    def consultar_fila(self):
        print("\n--- ESTADO ATUAL DA FILA DE ESPERA ---")
        if not self.fila_espera:
            print("A fila de espera encontra-se vazia.")
            return

        for utente in self.fila_espera:
            tipo = "PRIORITÁRIO" if utente.prioridade else "Normal"
            print(
                f"Senha: {utente.numero} | Nome: {utente.nome} | Tipo: {tipo} | Encaminhado para: {utente.sala} (Médico: {utente.medico} | Enf.: {utente.enfermeiro})")

    def chamar_proximo(self):
        print("\n--- CHAMADA DE UTENTE ---")
        if not self.fila_espera:
            print("Não há utentes em espera.")
            return


        utente_chamado = self.fila_espera.pop(0)
        print(f"A chamar a senha {utente_chamado.numero}: {utente_chamado.nome}")
        print(f"Dirija-se à **{utente_chamado.sala}**")
        print(f"Equipa responsável -> Médico(a): {utente_chamado.medico} | Enfermeiro(a): {utente_chamado.enfermeiro}")



def main():
    sistema = SistemaGestaoHospital()

    while True:
        print("\n==========================================")
        print(" SISTEMA DE GESTÃO DE FILAS - HOSPITAL GERAL DO UÍGE")
        print("==========================================")
        print("1. Registar Novo Utente (Chegada)")
        print("2. Consultar Fila de Espera")
        print("3. Chamar Próximo Utente")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            sistema.registar_utente()
        elif opcao == '2':
            sistema.consultar_fila()
        elif opcao == '3':
            sistema.chamar_proximo()
        elif opcao == '4':
            print("A encerrar o sistema. Até breve!")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()