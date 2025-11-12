"""
Pruebas unitarias para la clase Cama.

Verifica:
- Propiedades específicas (tamano, tiene_cabecera, incluye_colchon)
- Cálculo de precio según tamaño
- Validaciones de tamaño
"""

import pytest
from models.concretos.cama import Cama


class TestCamaInstanciacion:
    """Tests para la instanciación de Cama."""

    def test_crear_cama_individual(self, cama_individual):
        """Verifica que se puede crear una cama individual."""
        assert cama_individual is not None
        assert cama_individual.nombre == "Cama Individual"
        assert cama_individual.tamaño == "individual"

    def test_crear_cama_king(self, cama_king):
        """Verifica que se puede crear una cama King."""
        assert cama_king is not None
        assert cama_king.tamaño == "king"


class TestCamaPropiedades:
    """Tests para las propiedades de Cama."""

    def test_tamano(self, cama_individual):
        """Verifica propiedad tamano."""
        assert cama_individual.tamaño == "individual"

    def test_tiene_cabecera(self, cama_king):
        """Verifica propiedad tiene_cabecera."""
        assert cama_king.tiene_cabecera is True

    def test_incluye_colchon(self, cama_king):
        """Verifica propiedad incluye_colchon."""
        assert cama_king.incluye_colchon is True


class TestCamaCalculoPrecio:
    """Tests para el cálculo de precio de Cama."""

    def test_calcular_precio_individual(self, cama_individual):
        """Verifica el cálculo de precio para cama individual."""
        precio = cama_individual.calcular_precio()
        assert precio > 0

    def test_calcular_precio_king(self, cama_king):
        """Verifica el cálculo de precio para cama King."""
        precio = cama_king.calcular_precio()
        assert precio > 0

    def test_cama_king_mas_cara_que_individual(self):
        """Verifica que cama King es más cara que individual."""
        cama1 = Cama("individual", "Madera", "Natural", 300, "individual")
        cama2 = Cama("king", "Madera", "Natural", 300, "king")

        precio1 = cama1.calcular_precio()
        precio2 = cama2.calcular_precio()

        assert precio2 > precio1


class TestCamaDescripcion:
    """Tests para obtener_descripcion."""

    def test_obtener_descripcion(self, cama_individual):
        """Verifica que retorna descripción."""
        descripcion = cama_individual.obtener_descripcion()
        assert isinstance(descripcion, str)
        assert len(descripcion) > 0


@pytest.mark.parametrize(
    "tamano,tiene_cabecera,incluye_colchon",
    [
        ("individual", False, False),
        ("matrimonial", True, False),
        ("queen", True, True),
        ("king", True, True),
    ],
)
def test_cama_diferentes_configuraciones(tamano, tiene_cabecera, incluye_colchon):
    """Test parametrizado para diferentes configuraciones."""
    cama = Cama(
        f"Cama {tamano}",
        "Madera",
        "Natural",
        400,
        tamaño=tamano,
        tiene_cabecera=tiene_cabecera,
        incluye_colchon=incluye_colchon,
    )
    assert cama.tamaño == tamano
    assert cama.tiene_cabecera == tiene_cabecera
    assert cama.incluye_colchon == incluye_colchon
