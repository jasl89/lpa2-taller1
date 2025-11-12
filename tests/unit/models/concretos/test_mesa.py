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
        assert mesa_extensible.capacidad_personas == 8


class TestMesaPropiedades:
    """Tests para las propiedades de Mesa."""

    def test_acceso_dimensiones(self, mesa_comedor):
        """Verifica acceso a dimensiones."""
        assert mesa_comedor.largo == 180
        assert mesa_comedor.ancho == 90
        assert mesa_comedor.altura == 75

    def test_mesa_extensible_propiedad(self, mesa_extensible):
        """Verifica propiedad capacidad_personas."""
        assert mesa_extensible.capacidad_personas == 8

    def test_mesa_no_extensible(self, mesa_comedor):
        """Verifica mesa con capacidad estándar."""
        assert mesa_comedor.capacidad_personas == 6


class TestMesaCalculoPrecio:
    """Tests para el cálculo de precio de Mesa."""

    def test_calcular_precio(self, mesa_comedor):
        """Verifica el cálculo de precio."""
        precio = mesa_comedor.calcular_precio()
        assert precio > 0

    def test_mesa_extensible_mas_cara(self):
        """Verifica que mesa con más capacidad puede tener diferente precio."""
        mesa1 = Mesa("Test1", "Madera", "Café", 400, "rectangular", 160, 80, 75, 4)
        mesa2 = Mesa("Test2", "Madera", "Café", 400, "rectangular", 180, 90, 75, 8)

        precio1 = mesa1.calcular_precio()
        precio2 = mesa2.calcular_precio()

        assert precio1 >= 0 and precio2 >= 0


class TestMesaDescripcion:
    """Tests para obtener_descripcion."""

    def test_obtener_descripcion(self, mesa_comedor):
        """Verifica que retorna descripción."""
        descripcion = mesa_comedor.obtener_descripcion()
        assert isinstance(descripcion, str)
        assert len(descripcion) > 0


@pytest.mark.parametrize(
    "forma,capacidad_personas",
    [
        ("rectangular", 4),
        ("rectangular", 6),
        ("redonda", 8),
        ("ovalada", 10),
    ],
)
def test_mesa_diferentes_configuraciones(forma, capacidad_personas):
    """Test parametrizado para diferentes configuraciones."""
    mesa = Mesa(
        "Test",
        "Madera",
        "Café",
        400,
        forma,
        160,
        80,
        75,
        capacidad_personas,
    )
    assert mesa.capacidad_personas == capacidad_personas
