"""
Pruebas unitarias para la clase Cajonera.

Verifica:
- Instanciación correcta
- Cálculo de precio
- Propiedades específicas
- Métodos de descripción
"""

import pytest
from models.concretos.cajonera import Cajonera


class TestCajoneraInstanciacion:
    """Tests para la instanciación de Cajonera."""

    def test_crear_cajonera_basica(self, cajonera_pequena):
        """Verifica que se puede crear una cajonera."""
        assert cajonera_pequena is not None
        assert cajonera_pequena.nombre == "Cajonera Mini"
        assert cajonera_pequena.material == "Pino"
        assert cajonera_pequena.color == "Blanco"

    def test_crear_cajonera_con_parametros_personalizados(self):
        """Verifica creación con parámetros personalizados."""
        cajonera = Cajonera(
            nombre="Cajonera Grande",
            material="Roble",
            color="Nogal",
            precio_base=300,
            num_cajones=5,
            profundidad=40,
        )
        assert cajonera.nombre == "Cajonera Grande"
        assert cajonera.num_cajones == 5
        assert cajonera.profundidad == 40


class TestCajoneraPropiedades:
    """Tests para las propiedades de Cajonera."""

    def test_acceso_propiedades(self, cajonera_pequena):
        """Verifica el acceso a propiedades."""
        assert cajonera_pequena.num_cajones == 3
        assert cajonera_pequena.profundidad == 30
        assert cajonera_pequena.precio_base == 150


class TestCajoneraCalculoPrecio:
    """Tests para el cálculo de precio de Cajonera."""

    def test_calcular_precio_basico(self, cajonera_pequena):
        """Verifica el cálculo de precio básico."""
        precio = cajonera_pequena.calcular_precio()
        assert precio > 0
        assert isinstance(precio, (int, float))

    def test_precio_aumenta_con_mas_cajones(self):
        """Verifica que más cajones aumentan el precio."""
        caj1 = Cajonera("Test1", "Pino", "Blanco", 150, num_cajones=3, profundidad=30)
        caj2 = Cajonera("Test2", "Pino", "Blanco", 150, num_cajones=6, profundidad=30)

        precio1 = caj1.calcular_precio()
        precio2 = caj2.calcular_precio()

        assert precio2 > precio1


class TestCajoneraDescripcion:
    """Tests para el método obtener_descripcion."""

    def test_obtener_descripcion_contiene_informacion_basica(self, cajonera_pequena):
        """Verifica que la descripción contiene información básica."""
        descripcion = cajonera_pequena.obtener_descripcion()
        assert isinstance(descripcion, str)
        assert len(descripcion) > 0


@pytest.mark.parametrize(
    "num_cajones,profundidad",
    [
        (2, 25),
        (3, 30),
        (5, 35),
        (6, 40),
    ],
)
def test_cajonera_diferentes_configuraciones(num_cajones, profundidad):
    """Test parametrizado para diferentes configuraciones."""
    cajonera = Cajonera(
        nombre="Test",
        material="Pino",
        color="Blanco",
        precio_base=150,
        num_cajones=num_cajones,
        profundidad=profundidad,
    )
    assert cajonera.num_cajones == num_cajones
    assert cajonera.profundidad == profundidad
    precio = cajonera.calcular_precio()
    assert precio > 0
