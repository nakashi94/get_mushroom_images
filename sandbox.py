# file = open("sample.txt", "w", encoding="utf-8")

# file.write("Hello python\n")
# file.write("Hello world!\n")
# file.write("Hi, Tanaka")

# file.close()

# file = open("sample.txt", "r", encoding="utf-8")

# content = file.read()
# print(content)
# print(type(content))

# file.close()

# with open("index.txt", "w", encoding="utf-8") as file:
#     file.write("Hello index")

names = ["Tanaka", "Suzuki", "Yamada"]

for i, name in enumerate(names):
    print(f"{i}:{name}")
