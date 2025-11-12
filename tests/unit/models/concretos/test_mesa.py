"""
Pruebas unitarias para la clase Mesa.

Verifica:
- Herencia de Superficie
- Propiedades específicas (es_extensible, num_comensales)
- Cálculo de precio y capacidad
"""

import pytest
from models.concretos.mesa import Mesa
from models.categorias.superficies import Superficie


class TestMesaInstanciacion:
    """Tests para la instanciación de Mesa."""

    def test_crear_mesa_basica(self, mesa_comedor):
        """Verifica que se puede crear una mesa."""
        assert mesa_comedor is not None
        assert mesa_comedor.nombre == "Mesa Comedor 6p"

    def test_mesa_hereda_de_superficie(self, mesa_comedor):
        """Verifica que Mesa hereda de Superficie."""
        assert isinstance(mesa_comedor, Superficie)

    def test_crear_mesa_extensible(self, mesa_extensible):
        """Verifica que se puede crear mesa extensible."""
        assert mesa_extensible.es_extensible is True


class TestMesaPropiedades:
    """Tests para las propiedades de Mesa."""

    def test_acceso_dimensiones(self, mesa_comedor):
        """Verifica acceso a dimensiones."""
        assert mesa_comedor.largo == 180
        assert mesa_comedor.ancho == 90
        assert mesa_comedor.altura == 75

    def test_mesa_extensible_propiedad(self, mesa_extensible):
        """Verifica propiedad es_extensible."""
        assert mesa_extensible.es_extensible is True

    def test_mesa_no_extensible(self, mesa_comedor):
        """Verifica mesa no extensible."""
        assert mesa_comedor.es_extensible is False


class TestMesaCalculoPrecio:
    """Tests para el cálculo de precio de Mesa."""

    def test_calcular_precio(self, mesa_comedor):
        """Verifica el cálculo de precio."""
        precio = mesa_comedor.calcular_precio()
        assert precio > 0

    def test_mesa_extensible_mas_cara(self):
        """Verifica que mesa extensible es más cara."""
        mesa1 = Mesa("Test1", "Madera", "Café", 400, 160, 80, 75, es_extensible=False)
        mesa2 = Mesa("Test2", "Madera", "Café", 400, 160, 80, 75, es_extensible=True)

        precio1 = mesa1.calcular_precio()
        precio2 = mesa2.calcular_precio()

        assert precio2 > precio1


class TestMesaDescripcion:
    """Tests para obtener_descripcion."""

    def test_obtener_descripcion(self, mesa_comedor):
        """Verifica que retorna descripción."""
        descripcion = mesa_comedor.obtener_descripcion()
        assert isinstance(descripcion, str)
        assert len(descripcion) > 0


@pytest.mark.parametrize(
    "es_extensible,num_comensales",
    [
        (False, 4),
        (False, 6),
        (True, 8),
        (True, 10),
    ],
)
def test_mesa_diferentes_configuraciones(es_extensible, num_comensales):
    """Test parametrizado para diferentes configuraciones."""
    mesa = Mesa(
        "Test",
        "Madera",
        "Café",
        400,
        160,
        80,
        75,
        es_extensible=es_extensible,
        num_comensales=num_comensales,
    )
    assert mesa.es_extensible == es_extensible
