"""
Pruebas unitarias para la clase Cama.

Verifica:
- Propiedades específicas (tamano, tiene_cajones, incluye_colchon)
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
        assert cama_individual.tamano == "Individual"

    def test_crear_cama_king(self, cama_king):
        """Verifica que se puede crear una cama King."""
        assert cama_king is not None
        assert cama_king.tamano == "King"


class TestCamaPropiedades:
    """Tests para las propiedades de Cama."""

    def test_tamano(self, cama_individual):
        """Verifica propiedad tamano."""
        assert cama_individual.tamano == "Individual"

    def test_tiene_cajones(self, cama_king):
        """Verifica propiedad tiene_cajones."""
        assert cama_king.tiene_cajones is True

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
        cama1 = Cama("Individual", "Madera", "Natural", 300, "Individual")
        cama2 = Cama("King", "Madera", "Natural", 300, "King")

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
    "tamano,tiene_cajones,incluye_colchon",
    [
        ("Individual", False, False),
        ("Matrimonial", True, False),
        ("Queen", True, True),
        ("King", True, True),
    ],
)
def test_cama_diferentes_configuraciones(tamano, tiene_cajones, incluye_colchon):
    """Test parametrizado para diferentes configuraciones."""
    cama = Cama(
        f"Cama {tamano}",
        "Madera",
        "Natural",
        400,
        tamano=tamano,
        tiene_cajones=tiene_cajones,
        incluye_colchon=incluye_colchon,
    )
    assert cama.tamano == tamano
    assert cama.tiene_cajones == tiene_cajones
    assert cama.incluye_colchon == incluye_colchon
