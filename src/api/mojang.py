"""
API oficial de Mojang.

Responsabilidades:
- Obtener versiones de Minecraft.
- Obtener información de una versión.
- Descargar el servidor Vanilla.
"""

import requests


class MojangAPI:
    VERSION_MANIFEST = (
        "https://piston-meta.mojang.com/mc/game/version_manifest_v2.json"
    )

    @classmethod
    def manifest(cls):
        """Obtiene el manifest oficial de Minecraft."""
        response = requests.get(cls.VERSION_MANIFEST)
        response.raise_for_status()
        return response.json()

    @classmethod
    def versions(cls, releases_only=True):
        """
        Devuelve una lista de versiones.

        releases_only=True -> solo versiones estables.
        """
        data = cls.manifest()

        versions = []

        for version in data["versions"]:
            if releases_only and version["type"] != "release":
                continue

            versions.append(version)

        return versions

    @classmethod
    def latest_release(cls):
        """Devuelve la última versión estable."""
        return cls.manifest()["latest"]["release"]

    @classmethod
    def version_info(cls, version_id):
        """Obtiene toda la información de una versión."""

        for version in cls.versions(False):
            if version["id"] == version_id:
                response = requests.get(version["url"])
                response.raise_for_status()
                return response.json()

        raise ValueError(f"No existe la versión {version_id}")

    @classmethod
    def server_download_url(cls, version_id):
        """Obtiene la URL del servidor Vanilla."""

        info = cls.version_info(version_id)

        return info["downloads"]["server"]["url"]

    @classmethod
    def java_version(cls, version_id):
        """Devuelve la versión de Java requerida."""

        info = cls.version_info(version_id)

        return info.get("javaVersion", {}).get("majorVersion", 21)
