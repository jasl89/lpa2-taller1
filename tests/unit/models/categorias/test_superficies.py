"""
Pruebas unitarias para la clase abstracta Superficie.

Verifica:
- Herencia de Mueble
- No se puede instanciar directamente
- Propiedades específicas de superficies (largo, ancho, altura)
- Validaciones de dimensiones
- Métodos de cálculo de área y factor de tamaño
"""

import pytest
from unittest.mock import Mock
from models.categorias.superficies import Superficie


class SuperficieConcreto(Superficie):
    """Clase concreta para testear Superficie."""

    def calcular_precio(self) -> float:
        return self.precio_base * self.calcular_factor_tamaño()

    def obtener_descripcion(self) -> str:
        return f"Superficie: {self.nombre}"


class TestSuperficieInstanciacion:
    """Tests para la instanciación de Superficie."""

    def test_no_se_puede_instanciar_directamente(self):
        """Verifica que Superficie no puede ser instanciada directamente."""
        with pytest.raises(TypeError):
            Superficie("Mesa", "Madera", "Café", 300.0, 120, 80, 75)

    def test_instanciar_clase_concreta_exitosamente(self):
        """Verifica que una clase concreta puede ser instanciada."""
        superficie = SuperficieConcreto(
            "Mesa Test", "Madera", "Blanco", 250.0, 150, 90, 75
        )
        assert superficie is not None
        assert superficie.nombre == "Mesa Test"
        assert superficie.largo == 150
        assert superficie.ancho == 90
        assert superficie.altura == 75

    def test_hereda_de_mueble(self):
        """Verifica que Superficie hereda de Mueble."""
        from models.mueble import Mueble

        assert issubclass(Superficie, Mueble)


class TestSuperficiePropiedades:
    """Tests para las propiedades de Superficie."""

    def test_getter_largo(self):
        """Verifica que el getter de largo funciona."""
        superficie = SuperficieConcreto("Test", "Madera", "Café", 200.0, 180, 90, 75)
        assert superficie.largo == 180

    def test_setter_largo_valido(self):
        """Verifica que se puede cambiar el largo."""
        superficie = SuperficieConcreto("Test", "Madera", "Café", 200.0, 150, 80, 75)
        superficie.largo = 200
        assert superficie.largo == 200

    def test_setter_largo_cero_lanza_excepcion(self):
        """Verifica que largo = 0 lanza ValueError."""
        superficie = SuperficieConcreto("Test", "Madera", "Café", 200.0, 150, 80, 75)
        with pytest.raises(ValueError, match="debe ser mayor a 0"):
            superficie.largo = 0

    def test_setter_largo_negativo_lanza_excepcion(self):
        """Verifica que largo negativo lanza ValueError."""
        superficie = SuperficieConcreto("Test", "Madera", "Café", 200.0, 150, 80, 75)
        with pytest.raises(ValueError, match="debe ser mayor a 0"):
            superficie.largo = -50

    def test_getter_ancho(self):
        """Verifica que el getter de ancho funciona."""
        superficie = SuperficieConcreto("Test", "Madera", "Café", 200.0, 150, 100, 75)
        assert superficie.ancho == 100

    def test_setter_ancho_valido(self):
        """Verifica que se puede cambiar el ancho."""
        superficie = SuperficieConcreto("Test", "Madera", "Café", 200.0, 150, 80, 75)
        superficie.ancho = 90
        assert superficie.ancho == 90

    def test_setter_ancho_cero_lanza_excepcion(self):
        """Verifica que ancho = 0 lanza ValueError."""
        superficie = SuperficieConcreto("Test", "Madera", "Café", 200.0, 150, 80, 75)
        with pytest.raises(ValueError, match="debe ser mayor a 0"):
            superficie.ancho = 0

    def test_setter_ancho_negativo_lanza_excepcion(self):
        """Verifica que ancho negativo lanza ValueError."""
        superficie = SuperficieConcreto("Test", "Madera", "Café", 200.0, 150, 80, 75)
        with pytest.raises(ValueError, match="debe ser mayor a 0"):
            superficie.ancho = -30

    def test_getter_altura(self):
        """Verifica que el getter de altura funciona."""
        superficie = SuperficieConcreto("Test", "Madera", "Café", 200.0, 150, 80, 85)
        assert superficie.altura == 85

    def test_setter_altura_valido(self):
        """Verifica que se puede cambiar la altura."""
        superficie = SuperficieConcreto("Test", "Madera", "Café", 200.0, 150, 80, 75)
        superficie.altura = 80
        assert superficie.altura == 80

    def test_setter_altura_cero_lanza_excepcion(self):
        """Verifica que altura = 0 lanza ValueError."""
        superficie = SuperficieConcreto("Test", "Madera", "Café", 200.0, 150, 80, 75)
        with pytest.raises(ValueError, match="debe ser mayor a 0"):
            superficie.altura = 0


class TestSuperficieMetodos:
    """Tests para los métodos de Superficie."""

    def test_calcular_area(self):
        """Verifica que calcular_area funciona correctamente."""
        superficie = SuperficieConcreto("Test", "Madera", "Café", 200.0, 100, 50, 75)
        area = superficie.calcular_area()
        assert area == 5000

    def test_calcular_area_con_diferentes_dimensiones(self):
        """Verifica el cálculo de área con diferentes dimensiones."""
        superficie = SuperficieConcreto("Test", "Madera", "Café", 200.0, 180, 90, 75)
        area = superficie.calcular_area()
        assert area == 16200

    def test_calcular_factor_tamano_superficie_pequena(self):
        """Verifica el factor de tamaño para superficie pequeña."""
        superficie = SuperficieConcreto("Test", "Madera", "Café", 200.0, 80, 60, 75)
        factor = superficie.calcular_factor_tamaño()
        assert factor >= 1.0

    def test_calcular_factor_tamano_superficie_grande(self):
        """Verifica que superficie más grande tiene mayor factor."""
        sup1 = SuperficieConcreto("Test1", "Madera", "Café", 200.0, 100, 60, 75)
        sup2 = SuperficieConcreto("Test2", "Madera", "Café", 200.0, 200, 100, 75)

        factor1 = sup1.calcular_factor_tamaño()
        factor2 = sup2.calcular_factor_tamaño()

        assert factor2 > factor1

    def test_obtener_info_superficie(self):
        """Verifica que obtener_info_superficie retorna información correcta."""
        superficie = SuperficieConcreto("Test", "Madera", "Café", 200.0, 120, 80, 75)
        info = superficie.obtener_info_superficie()
        assert "120" in info
        assert "80" in info
        assert "75" in info
        assert "9600" in info  # área

    def test_obtener_info_superficie_incluye_area(self):
        """Verifica que la información incluye el área calculada."""
        superficie = SuperficieConcreto("Test", "Madera", "Café", 200.0, 150, 90, 75)
        info = superficie.obtener_info_superficie()
        area = superficie.calcular_area()
        assert str(int(area)) in info


class TestSuperficieConMesa:
    """Tests usando la clase concreta Mesa."""

    def test_mesa_es_superficie(self, mesa_comedor):
        """Verifica que Mesa hereda de Superficie."""
        assert isinstance(mesa_comedor, Superficie)

    def test_mesa_tiene_dimensiones(self, mesa_comedor):
        """Verifica que Mesa tiene propiedades de Superficie."""
        assert hasattr(mesa_comedor, "largo")
        assert hasattr(mesa_comedor, "ancho")
        assert hasattr(mesa_comedor, "altura")


class TestSuperficieConEscritorio:
    """Tests usando la clase concreta Escritorio."""

    def test_escritorio_es_superficie(self, escritorio_basico):
        """Verifica que Escritorio hereda de Superficie."""
        assert isinstance(escritorio_basico, Superficie)

    def test_escritorio_calcula_area(self, escritorio_basico):
        """Verifica que Escritorio puede calcular su área."""
        area = escritorio_basico.calcular_area()
        assert area > 0


@pytest.mark.parametrize(
    "largo,ancho,area_esperada",
    [
        (100, 50, 5000),
        (120, 80, 9600),
        (180, 90, 16200),
        (200, 100, 20000),
    ],
)
def test_calcular_area_parametrizado(largo, ancho, area_esperada):
    """Test parametrizado para cálculo de área."""
    superficie = SuperficieConcreto("Test", "Madera", "Café", 200.0, largo, ancho, 75)
    area = superficie.calcular_area()
    assert area == area_esperada


@pytest.mark.parametrize(
    "largo,ancho,altura",
    [
        (0, 80, 75),
        (120, 0, 75),
        (120, 80, 0),
        (-100, 80, 75),
        (120, -50, 75),
        (120, 80, -10),
    ],
)
def test_dimensiones_invalidas_parametrizado(largo, ancho, altura):
    """Test parametrizado para validar dimensiones inválidas."""
    with pytest.raises(ValueError):
        SuperficieConcreto("Test", "Madera", "Café", 200.0, largo, ancho, altura)


def test_superficie_con_mock():
    """Test usando mock para verificar llamadas a métodos."""
    superficie = SuperficieConcreto("Test", "Madera", "Café", 200.0, 150, 80, 75)

    # Mock del método calcular_factor_tamaño
    superficie.calcular_factor_tamaño = Mock(return_value=1.25)

    precio = superficie.calcular_precio()
    superficie.calcular_factor_tamaño.assert_called_once()
    assert precio == 200.0 * 1.25


def test_factor_tamano_calculo_preciso():
    """Verifica el cálculo preciso del factor de tamaño."""
    superficie = SuperficieConcreto("Test", "Madera", "Café", 200.0, 100, 100, 75)
    # Área = 10000, factor = 1.0 + (10000/10000)*0.05 = 1.05
    factor = superficie.calcular_factor_tamaño()
    assert factor == 1.05


def test_modificar_dimensiones_actualiza_area():
    """Verifica que modificar dimensiones actualiza el área."""
    superficie = SuperficieConcreto("Test", "Madera", "Café", 200.0, 100, 100, 75)
    area_inicial = superficie.calcular_area()

    superficie.largo = 150
    area_nueva = superficie.calcular_area()

    assert area_nueva > area_inicial
    assert area_nueva == 15000
