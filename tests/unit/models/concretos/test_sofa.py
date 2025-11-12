"""
Pruebas unitarias para la clase Sofa.

Verifica:
- Herencia de Asiento
- Propiedades específicas (capacidad_personas, es_modular)
- Cálculo de precio
"""

import pytest
from models.concretos.sofa import Sofa
from models.categorias.asientos import Asiento


class TestSofaInstanciacion:
    """Tests para la instanciación de Sofa."""

    def test_crear_sofa(self, sofa_tres_puestos):
        """Verifica que se puede crear un sofá."""
        assert sofa_tres_puestos is not None
        assert sofa_tres_puestos.nombre == "Sofá Moderno"

    def test_sofa_hereda_de_asiento(self, sofa_tres_puestos):
        """Verifica que Sofa hereda de Asiento."""
        assert isinstance(sofa_tres_puestos, Asiento)


class TestSofaPropiedades:
    """Tests para las propiedades de Sofa."""

    def test_capacidad_personas(self, sofa_tres_puestos):
        """Verifica propiedad capacidad_personas."""
        assert sofa_tres_puestos.capacidad_personas == 3

    def test_es_modular(self, sofa_tres_puestos):
        """Verifica propiedad es_modular."""
        assert sofa_tres_puestos.es_modular is False


class TestSofaCalculoPrecio:
    """Tests para el cálculo de precio de Sofa."""

    def test_calcular_precio(self, sofa_tres_puestos):
        """Verifica el cálculo de precio."""
        precio = sofa_tres_puestos.calcular_precio()
        assert precio > 0


class TestSofaDescripcion:
    """Tests para obtener_descripcion."""

    def test_obtener_descripcion(self, sofa_tres_puestos):
        """Verifica que retorna descripción."""
        descripcion = sofa_tres_puestos.obtener_descripcion()
        assert isinstance(descripcion, str)
        assert "Sofá" in descripcion or "Moderno" in descripcion


@pytest.mark.parametrize(
    "capacidad_personas,es_modular",
    [
        (2, False),
        (3, False),
        (3, True),
        (4, True),
    ],
)
def test_sofa_diferentes_configuraciones(capacidad_personas, es_modular):
    """Test parametrizado para diferentes configuraciones."""
    sofa = Sofa(
        "Test",
        "Madera",
        "Gris",
        600,
        material_tapizado="Tela",
        capacidad_personas=capacidad_personas,
        es_modular=es_modular,
    )
    assert sofa.capacidad_personas == capacidad_personas
    assert sofa.es_modular == es_modular
