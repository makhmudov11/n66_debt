from core.database_settings import execute_query

def print_menu():
    print("""
    1.Registratsiya
    2.Login
    """)
    choice = input("Tanlang: ")
    res = False
    if choice == '1':
        register()
        res = login()
    elif choice == '2':
        res = login()
    else:
        print("Invald choice.")
        return print_menu()




def register():
    print("Registratsiya sahifasi.")

    username = input("Username kiriting: ")
    password = input("Parolingizni kiriting: ")

    query1 = """
                SELECT * FROM users WHERE username = %s AND password = %s;
            """
    params1 = (username, password)
    user = execute_query(query=query1, params=params1, fetch='one')
    if len(user) != 0:
        print("Siz Avval royhatdan otkansiz.")
        return

    params = (username, password)
    query = """
        
        INSERT INTO users(username, password) VALUES (%s, %s);
    """

    execute_query(params=params, query=query)
    params1 = (username, password)
    user = execute_query(query=query1, params=params1)
    print("Endi login qiling.")
    return


def login():
    print("login sahifasi.")

    username = input("Username kiriting: ")
    password = input("Parolingizni kiriting: ")

    query = """
        SELECT * FROM users WHERE username = %s AND password = %s;
    """
    params = (username, password)
    user = execute_query(query=query, params=params, fetch='one')

    if user is None:
        return False
    return True