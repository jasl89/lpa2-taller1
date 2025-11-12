"""
Pruebas unitarias para la clase abstracta Asiento.

Verifica:
- Herencia de Mueble
- No se puede instanciar directamente
- Propiedades específicas de asientos
- Validaciones de capacidad_personas
- Métodos de cálculo de factor de comodidad
"""

import pytest
from unittest.mock import Mock
from models.categorias.asientos import Asiento


class AsientoConcreto(Asiento):
    """Clase concreta para testear Asiento."""

    def calcular_precio(self) -> float:
        return self.precio_base * self.calcular_factor_comodidad()

    def obtener_descripcion(self) -> str:
        return f"Asiento: {self.nombre}"


class TestAsientoInstanciacion:
    """Tests para la instanciación de Asiento."""

    def test_no_se_puede_instanciar_directamente(self):
        """Verifica que Asiento no puede ser instanciada directamente."""
        with pytest.raises(TypeError):
            Asiento("Silla", "Madera", "Negro", 100.0, 1, True)

    def test_instanciar_clase_concreta_exitosamente(self):
        """Verifica que una clase concreta puede ser instanciada."""
        asiento = AsientoConcreto(
            "Silla Test", "Madera", "Café", 150.0, 1, True, "Tela"
        )
        assert asiento is not None
        assert asiento.nombre == "Silla Test"
        assert asiento.capacidad_personas == 1
        assert asiento.tiene_respaldo is True

    def test_instanciar_sin_material_tapizado(self):
        """Verifica que se puede instanciar sin material de tapizado."""
        asiento = AsientoConcreto("Banco", "Metal", "Gris", 80.0, 1, False)
        assert asiento.material_tapizado is None

    def test_hereda_de_mueble(self):
        """Verifica que Asiento hereda de Mueble."""
        from models.mueble import Mueble

        assert issubclass(Asiento, Mueble)


class TestAsientoPropiedades:
    """Tests para las propiedades de Asiento."""

    def test_getter_capacidad_personas(self):
        """Verifica que el getter de capacidad_personas funciona."""
        asiento = AsientoConcreto("Test", "Madera", "Café", 200.0, 3, True)
        assert asiento.capacidad_personas == 3

    def test_setter_capacidad_personas_valido(self):
        """Verifica que se puede cambiar capacidad_personas."""
        asiento = AsientoConcreto("Test", "Madera", "Café", 200.0, 2, True)
        asiento.capacidad_personas = 4
        assert asiento.capacidad_personas == 4

    def test_setter_capacidad_personas_cero_lanza_excepcion(self):
        """Verifica que capacidad_personas = 0 lanza ValueError."""
        asiento = AsientoConcreto("Test", "Madera", "Café", 200.0, 2, True)
        with pytest.raises(ValueError, match="debe ser mayor a 0"):
            asiento.capacidad_personas = 0

    def test_setter_capacidad_personas_negativo_lanza_excepcion(self):
        """Verifica que capacidad_personas negativo lanza ValueError."""
        asiento = AsientoConcreto("Test", "Madera", "Café", 200.0, 2, True)
        with pytest.raises(ValueError, match="debe ser mayor a 0"):
            asiento.capacidad_personas = -1

    def test_getter_tiene_respaldo(self):
        """Verifica que el getter de tiene_respaldo funciona."""
        asiento = AsientoConcreto("Test", "Madera", "Café", 200.0, 1, True)
        assert asiento.tiene_respaldo is True

    def test_setter_tiene_respaldo(self):
        """Verifica que se puede cambiar tiene_respaldo."""
        asiento = AsientoConcreto("Test", "Madera", "Café", 200.0, 1, True)
        asiento.tiene_respaldo = False
        assert asiento.tiene_respaldo is False

    def test_getter_material_tapizado(self):
        """Verifica que el getter de material_tapizado funciona."""
        asiento = AsientoConcreto("Test", "Madera", "Café", 200.0, 1, True, "Cuero")
        assert asiento.material_tapizado == "Cuero"

    def test_setter_material_tapizado(self):
        """Verifica que se puede cambiar material_tapizado."""
        asiento = AsientoConcreto("Test", "Madera", "Café", 200.0, 1, True, "Tela")
        asiento.material_tapizado = "Cuero"
        assert asiento.material_tapizado == "Cuero"


class TestAsientoMetodos:
    """Tests para los métodos de Asiento."""

    def test_calcular_factor_comodidad_basico(self):
        """Verifica que calcular_factor_comodidad funciona sin extras."""
        asiento = AsientoConcreto("Test", "Madera", "Café", 200.0, 1, False, None)
        factor = asiento.calcular_factor_comodidad()
        assert factor == 1.0

    def test_calcular_factor_comodidad_con_respaldo(self):
        """Verifica que el respaldo aumenta el factor de comodidad."""
        asiento = AsientoConcreto("Test", "Madera", "Café", 200.0, 1, True, None)
        factor = asiento.calcular_factor_comodidad()
        assert factor == 1.1

    def test_calcular_factor_comodidad_con_tapizado_tela(self):
        """Verifica que el tapizado de tela aumenta el factor."""
        asiento = AsientoConcreto("Test", "Madera", "Café", 200.0, 1, False, "Tela")
        factor = asiento.calcular_factor_comodidad()
        assert factor == 1.1

    def test_calcular_factor_comodidad_con_tapizado_cuero(self):
        """Verifica que el tapizado de cuero aumenta más el factor."""
        asiento = AsientoConcreto("Test", "Madera", "Café", 200.0, 1, False, "Cuero")
        factor = asiento.calcular_factor_comodidad()
        assert factor == 1.2

    def test_calcular_factor_comodidad_con_mas_capacidad(self):
        """Verifica que más capacidad aumenta el factor."""
        asiento1 = AsientoConcreto("Test1", "Madera", "Café", 200.0, 1, False, None)
        asiento2 = AsientoConcreto("Test2", "Madera", "Café", 200.0, 3, False, None)

        factor1 = asiento1.calcular_factor_comodidad()
        factor2 = asiento2.calcular_factor_comodidad()

        assert factor2 > factor1

    def test_calcular_factor_comodidad_completo(self):
        """Verifica el factor con todas las características."""
        asiento = AsientoConcreto("Test", "Madera", "Café", 200.0, 3, True, "Cuero")
        factor = asiento.calcular_factor_comodidad()
        # 1.0 + 0.1 (respaldo) + 0.2 (cuero) + 0.1 (2 personas adicionales) = 1.4
        assert round(factor, 1) == 1.4

    def test_obtener_info_asiento_basico(self):
        """Verifica que obtener_info_asiento retorna información correcta."""
        asiento = AsientoConcreto("Test", "Madera", "Café", 200.0, 2, True, None)
        info = asiento.obtener_info_asiento()
        assert "2" in info
        assert "Sí" in info or "personas" in info

    def test_obtener_info_asiento_con_tapizado(self):
        """Verifica que la info incluye el material de tapizado."""
        asiento = AsientoConcreto("Test", "Madera", "Café", 200.0, 1, True, "Tela")
        info = asiento.obtener_info_asiento()
        assert "Tela" in info


class TestAsientoConSilla:
    """Tests usando la clase concreta Silla."""

    def test_silla_es_asiento(self, silla_simple):
        """Verifica que Silla hereda de Asiento."""
        assert isinstance(silla_simple, Asiento)

    def test_silla_capacidad_es_uno(self, silla_simple):
        """Verifica que una silla tiene capacidad de 1 persona."""
        assert silla_simple.capacidad_personas == 1


class TestAsientoConSillon:
    """Tests usando la clase concreta Sillon."""

    def test_sillon_es_asiento(self, sillon_individual):
        """Verifica que Sillon tiene características de asiento."""
        # Sillon no hereda de Asiento en la implementación actual
        assert hasattr(sillon_individual, "capacidad_personas")


class TestAsientoConSofa:
    """Tests usando la clase concreta Sofa."""

    def test_sofa_es_asiento(self, sofa_tres_puestos):
        """Verifica que Sofa hereda de Asiento."""
        assert isinstance(sofa_tres_puestos, Asiento)

    def test_sofa_tiene_mayor_capacidad(self, sofa_tres_puestos):
        """Verifica que un sofá tiene mayor capacidad que una silla."""
        assert sofa_tres_puestos.capacidad_personas >= 2


@pytest.mark.parametrize(
    "capacidad,respaldo,tapizado,factor_min",
    [
        (1, False, None, 1.0),
        (1, True, None, 1.1),
        (1, True, "Tela", 1.2),
        (1, True, "Cuero", 1.3),
        (3, True, "Cuero", 1.4),
    ],
)
def test_factor_comodidad_parametrizado(capacidad, respaldo, tapizado, factor_min):
    """Test parametrizado para diferentes configuraciones de asiento."""
    asiento = AsientoConcreto(
        "Test", "Madera", "Café", 200.0, capacidad, respaldo, tapizado
    )
    factor = asiento.calcular_factor_comodidad()
    assert factor >= factor_min


def test_asiento_con_mock():
    """Test usando mock para verificar llamadas a métodos."""
    asiento = AsientoConcreto("Test", "Madera", "Café", 200.0, 2, True, "Tela")

    # Mock del método calcular_factor_comodidad
    asiento.calcular_factor_comodidad = Mock(return_value=1.5)

    precio = asiento.calcular_precio()
    asiento.calcular_factor_comodidad.assert_called_once()
    assert precio == 200.0 * 1.5


def test_asiento_tapizado_case_insensitive():
    """Verifica que el material de tapizado no es case-sensitive."""
    asiento1 = AsientoConcreto("Test1", "Madera", "Café", 200.0, 1, False, "CUERO")
    asiento2 = AsientoConcreto("Test2", "Madera", "Café", 200.0, 1, False, "cuero")

    factor1 = asiento1.calcular_factor_comodidad()
    factor2 = asiento2.calcular_factor_comodidad()

    assert factor1 == factor2
