import sqlite3
import sys

def buscar_usuario_vulneravel(username):
    # ❌ VULNERÁVEL: Concatenação direta de input do usuário
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    # SQL Injection - usando f-string com input do usuário
    query = f"SELECT * FROM usuarios WHERE username = '{username}'"
    cursor.execute(query)
    
    return cursor.fetchall()

def deletar_usuario_vulneravel(user_id):
    # ❌ VULNERÁVEL: Concatenação com operador +
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    # SQL Injection - concatenação direta
    query = "DELETE FROM usuarios WHERE id = " + user_id
    cursor.execute(query)
    conn.commit()
    
def atualizar_email_vulneravel(email, user_id):
    # ❌ VULNERÁVEL: Usando % formatting
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    # SQL Injection - % formatting
    query = "UPDATE usuarios SET email = '%s' WHERE id = %s" % (email, user_id)
    cursor.execute(query)
    conn.commit()

# Simulando entrada do usuário (para CodeQL detectar o fluxo)
if __name__ == "__main__":
    # Entrada vinda de argumentos da linha de comando (fonte externa)
    if len(sys.argv) > 1:
        user_input = sys.argv[1]
        buscar_usuario_vulneravel(user_input)
        deletar_usuario_vulneravel(user_input)
        atualizar_email_vulneravel(user_input, "1")