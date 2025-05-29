
from core.table_queries import initializing_tables
from login_register import print_menu, register


def main():
    print("""
    1. Mening qarzlarim (kimdan qachon qancha)
    2. Men bergan qarzlar (kimga, qachon, qancha)
    3. Olgan qarzlarim summasi(tolangan, tolanmagan)
    4. Bergan qarzlarim summasi(tolangan, tolanmagan)
    5. Qarzlarni to'las
    6. Chiqish
    """)

    choice = input("Enter your choice: ")
    if choice == "1":
        pass
    elif choice == "2":
        pass
    elif choice == "3":
        pass
    elif choice == '4':
        pass
    elif choice == '5':
        pass
    elif choice == '6':
        print("Goodbye")
    else:
        print("Invalid choice")
    main()


if __name__ == '__main__':
    initializing_tables()
    if print_menu():
        main()
    else:
        print("siz royhatdan otishingiz kerak.")
        register()
