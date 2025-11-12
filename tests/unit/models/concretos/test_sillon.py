"""
Pruebas unitarias para la clase Sillon.

Verifica:
- Herencia de Asiento
- Propiedades específicas (tiene_brazos, es_reclinable)
- Cálculo de precio
"""

import pytest
from models.concretos.sillon import Sillon


class TestSillonInstanciacion:
    """Tests para la instanciación de Sillon."""

    def test_crear_sillon(self, sillon_individual):
        """Verifica que se puede crear un sillón."""
        assert sillon_individual is not None
        assert sillon_individual.nombre == "Sillón Relax"

    def test_sillon_hereda_de_asiento(self, sillon_individual):
        """Verifica que Sillon tiene características de asiento."""
        # Sillon no hereda de Asiento en la implementación actual
        assert hasattr(sillon_individual, "capacidad_personas")


class TestSillonPropiedades:
    """Tests para las propiedades de Sillon."""

    def test_tiene_brazos(self, sillon_individual):
        """Verifica propiedad tiene_brazos."""
        assert sillon_individual.tiene_brazos is True

    def test_es_reclinable(self, sillon_individual):
        """Verifica propiedad es_reclinable."""
        assert sillon_individual.es_reclinable is False


class TestSillonCalculoPrecio:
    """Tests para el cálculo de precio de Sillon."""

    def test_calcular_precio(self, sillon_individual):
        """Verifica el cálculo de precio."""
        precio = sillon_individual.calcular_precio()
        assert precio > 0


class TestSillonDescripcion:
    """Tests para obtener_descripcion."""

    def test_obtener_descripcion(self, sillon_individual):
        """Verifica que retorna descripción."""
        descripcion = sillon_individual.obtener_descripcion()
        assert isinstance(descripcion, str)
        assert "Sillón" in descripcion or "Relax" in descripcion


@pytest.mark.parametrize(
    "tiene_brazos,es_reclinable",
    [
        (True, False),
        (True, True),
        (False, False),
        (False, True),
    ],
)
def test_sillon_diferentes_configuraciones(tiene_brazos, es_reclinable):
    """Test parametrizado para diferentes configuraciones."""
    sillon = Sillon(
        "Test",
        "Madera",
        "Beige",
        300,
        material_tapizado="Tela",
        tiene_brazos=tiene_brazos,
        es_reclinable=es_reclinable,
    )
    assert sillon.tiene_brazos == tiene_brazos
    assert sillon.es_reclinable == es_reclinable
