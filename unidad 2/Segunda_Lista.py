lista_compras = []
print("🛒 Lista de Compras 🛒")
producto1 = input(" Agrega el primer producto: ")
lista_compras.append(producto1)
producto2 = input("Agrega el segundo producto: ")
lista_compras.append(producto2)
producto3 = input("Agrega el tercer producto: ")
lista_compras.append(producto3)
print("\n📌 Tu lista de compras es:")
for producto in lista_compras:
    print(f"- {producto}")
print("\n✅ ¡Lista creada con éxito!")
#https://www.webfx.com/tools/emoji-cheat-sheet/