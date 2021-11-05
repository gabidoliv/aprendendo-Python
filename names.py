from name_function import get_formatted_name

print("Pressione 'q' para sair.")
while True:
    first = input("\nForneça seu primeiro nome por gentileza: ")
    if first =='q':
        break
    last = input("Forneça seu segundo nome por gentileza: ")
    if last =='q':
        break

    formatted_name = get_formatted_name(first,last)
    print("\tSeu nome editado corretamente: " + formatted_name + ".")