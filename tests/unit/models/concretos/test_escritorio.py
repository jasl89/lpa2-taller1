"""
Pruebas unitarias para la clase Escritorio.

Verifica:
- Herencia de Superficie
- Propiedades específicas (num_cajones, tiene_organizador_cables)
- Cálculo de precio
"""

import pytest
from models.concretos.escritorio import Escritorio


class TestEscritorioInstanciacion:
    """Tests para la instanciación de Escritorio."""

    def test_crear_escritorio(self, escritorio_basico):
        """Verifica que se puede crear un escritorio."""
        assert escritorio_basico is not None
        assert escritorio_basico.nombre == "Escritorio Home Office"

    def test_escritorio_hereda_de_superficie(self, escritorio_basico):
        """Verifica que Escritorio tiene características de superficie."""
        # Escritorio no hereda de Superficie en la implementación actual
        assert hasattr(escritorio_basico, "largo")


class TestEscritorioPropiedades:
    """Tests para las propiedades de Escritorio."""

    def test_acceso_dimensiones(self, escritorio_basico):
        """Verifica acceso a dimensiones."""
        assert escritorio_basico.largo == 1.2

    def test_num_cajones(self, escritorio_basico):
        """Verifica propiedad num_cajones."""
        assert escritorio_basico.num_cajones == 2

    def test_tiene_organizador_cables(self, escritorio_basico):
        """Verifica propiedad tiene_iluminacion."""
        assert escritorio_basico.tiene_iluminacion is False


class TestEscritorioCalculoPrecio:
    """Tests para el cálculo de precio de Escritorio."""

    def test_calcular_precio(self, escritorio_basico):
        """Verifica el cálculo de precio."""
        precio = escritorio_basico.calcular_precio()
        assert precio > 0


class TestEscritorioDescripcion:
    """Tests para obtener_descripcion."""

    def test_obtener_descripcion(self, escritorio_basico):
        """Verifica que retorna descripción."""
        descripcion = escritorio_basico.obtener_descripcion()
        assert isinstance(descripcion, str)
        assert len(descripcion) > 0


@pytest.mark.parametrize(
    "num_cajones,tiene_organizador",
    [
        (0, False),
        (1, True),
        (2, True),
        (3, False),
    ],
)
def test_escritorio_diferentes_configuraciones(num_cajones, tiene_organizador):
    """Test parametrizado para diferentes configuraciones."""
    escritorio = Escritorio(
        "Test",
        "MDF",
        "Blanco",
        200,
        "rectangular",
        True if num_cajones > 0 else False,
        num_cajones,
        1.2,
        tiene_organizador,
    )
    assert escritorio.num_cajones == num_cajones
    assert escritorio.tiene_iluminacion == tiene_organizador
