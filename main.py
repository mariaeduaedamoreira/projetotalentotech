from gerenciador_tarefas import GerenciadorTarefas
from utilitarios import obter_inteiro_valido, obter_string_nao_vazia

def main():
    gerenciador = GerenciadorTarefas()

    while True:
        print("\n--- Gerenciador de Tarefas ---")
        print("1. Adicionar Tarefa")
        print("2. Visualizar Tarefas")
        print("3. Editar Tarefa")
        print("4. Excluir Tarefa")
        print("5. Sair")

        opcao = obter_inteiro_valido("Escolha uma opção: ")

        if opcao == 1:
            titulo = obter_string_nao_vazia("Título da tarefa: ")
            descricao = obter_string_nao_vazia("Descrição da tarefa: ")
            tarefa = gerenciador.adicionar_tarefa(titulo, descricao)
            print(f"Tarefa adicionada: {tarefa}")
        elif opcao == 2:
            tarefas = gerenciador.listar_tarefas()
            if tarefas:
                for tarefa in tarefas:
                    print(tarefa)
            else:
                print("Nenhuma tarefa encontrada.")
        elif opcao == 3:
            id = obter_inteiro_valido("ID da tarefa a ser editada: ")
            novo_titulo = obter_string_nao_vazia("Novo título: ")
            nova_descricao = obter_string_nao_vazia("Nova descrição: ")
            tarefa = gerenciador.editar_tarefa(id, novo_titulo, nova_descricao)
            if tarefa:
                print(f"Tarefa atualizada: {tarefa}")
            else:
                print("Tarefa não encontrada.")
        elif opcao == 4:
            id = obter_inteiro_valido("ID da tarefa a ser excluída: ")
            tarefa = gerenciador.excluir_tarefa(id)
            if tarefa:
                print(f"Tarefa excluída: {tarefa}")
            else:
                print("Tarefa não encontrada.")
        elif opcao == 5:
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
