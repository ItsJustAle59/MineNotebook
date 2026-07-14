from src.api.mojang import MojangAPI

print("Última versión:")
print(MojangAPI.latest_release())

print()

print("Primeras 10 versiones:")
for version in MojangAPI.versions()[:10]:
    print("-", version["id"])

print()

print("Java para 1.21.1:")
print(MojangAPI.java_version("1.21.1"))

print()

print("URL del servidor:")
print(MojangAPI.server_download_url("1.21.1"))
