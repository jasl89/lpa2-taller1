"""
Pruebas unitarias para la clase Silla.

Verifica:
- Herencia de Asiento
- Propiedades específicas (altura_regulable, tiene_ruedas)
- Cálculo de precio
- Métodos específicos (regular_altura, es_silla_oficina)
"""

import pytest
from models.concretos.silla import Silla
from models.categorias.asientos import Asiento


class TestSillaInstanciacion:
    """Tests para la instanciación de Silla."""

    def test_crear_silla_simple(self, silla_simple):
        """Verifica que se puede crear una silla simple."""
        assert silla_simple is not None
        assert silla_simple.nombre == "Silla Estándar"
        assert silla_simple.capacidad_personas == 1

    def test_crear_silla_oficina(self, silla_oficina):
        """Verifica que se puede crear una silla de oficina."""
        assert silla_oficina is not None
        assert silla_oficina.altura_regulable is True
        assert silla_oficina.tiene_ruedas is True

    def test_silla_hereda_de_asiento(self, silla_simple):
        """Verifica que Silla hereda de Asiento."""
        assert isinstance(silla_simple, Asiento)

    def test_silla_capacidad_siempre_uno(self):
        """Verifica que las sillas siempre tienen capacidad de 1 persona."""
        silla = Silla("Test", "Madera", "Café", 100, altura_regulable=True)
        assert silla.capacidad_personas == 1


class TestSillaPropiedades:
    """Tests para las propiedades de Silla."""

    def test_altura_regulable_getter(self, silla_oficina):
        """Verifica el getter de altura_regulable."""
        assert silla_oficina.altura_regulable is True

    def test_altura_regulable_setter(self, silla_simple):
        """Verifica el setter de altura_regulable."""
        assert silla_simple.altura_regulable is False
        silla_simple.altura_regulable = True
        assert silla_simple.altura_regulable is True

    def test_tiene_ruedas_getter(self, silla_oficina):
        """Verifica el getter de tiene_ruedas."""
        assert silla_oficina.tiene_ruedas is True

    def test_tiene_ruedas_setter(self, silla_simple):
        """Verifica el setter de tiene_ruedas."""
        assert silla_simple.tiene_ruedas is False
        silla_simple.tiene_ruedas = True
        assert silla_simple.tiene_ruedas is True


class TestSillaCalculoPrecio:
    """Tests para el cálculo de precio de Silla."""

    def test_calcular_precio_silla_simple(self, silla_simple):
        """Verifica el cálculo de precio para silla simple."""
        precio = silla_simple.calcular_precio()
        assert precio > 0
        assert isinstance(precio, float)

    def test_calcular_precio_silla_oficina_mas_caro(self, silla_simple, silla_oficina):
        """Verifica que silla de oficina es más cara."""
        precio_simple = silla_simple.calcular_precio()
        precio_oficina = silla_oficina.calcular_precio()
        # La silla de oficina tiene mayor precio base y características adicionales
        assert precio_oficina > precio_simple

    def test_precio_incluye_costo_altura_regulable(self):
        """Verifica que altura regulable aumenta el precio."""
        silla1 = Silla("Test", "Plástico", "Negro", 100, altura_regulable=False)
        silla2 = Silla("Test", "Plástico", "Negro", 100, altura_regulable=True)

        precio1 = silla1.calcular_precio()
        precio2 = silla2.calcular_precio()

        assert precio2 > precio1

    def test_precio_incluye_costo_ruedas(self):
        """Verifica que las ruedas aumentan el precio."""
        silla1 = Silla("Test", "Plástico", "Negro", 100, tiene_ruedas=False)
        silla2 = Silla("Test", "Plástico", "Negro", 100, tiene_ruedas=True)

        precio1 = silla1.calcular_precio()
        precio2 = silla2.calcular_precio()

        assert precio2 > precio1


class TestSillaMetodos:
    """Tests para métodos específicos de Silla."""

    def test_regular_altura_silla_no_regulable(self, silla_simple):
        """Verifica que no se puede regular altura en silla no regulable."""
        resultado = silla_simple.regular_altura(60)
        assert "no tiene altura regulable" in resultado

    def test_regular_altura_valor_valido(self, silla_oficina):
        """Verifica que se puede regular la altura con valor válido."""
        resultado = silla_oficina.regular_altura(60)
        assert "ajustada" in resultado.lower() or "60" in resultado

    def test_regular_altura_valor_muy_bajo(self, silla_oficina):
        """Verifica que altura muy baja es rechazada."""
        resultado = silla_oficina.regular_altura(30)
        assert "entre 40 y 100" in resultado

    def test_regular_altura_valor_muy_alto(self, silla_oficina):
        """Verifica que altura muy alta es rechazada."""
        resultado = silla_oficina.regular_altura(110)
        assert "entre 40 y 100" in resultado

    def test_es_silla_oficina_verdadero(self, silla_oficina):
        """Verifica que silla con ruedas y altura regulable es de oficina."""
        assert silla_oficina.es_silla_oficina() is True

    def test_es_silla_oficina_falso(self, silla_simple):
        """Verifica que silla simple no es de oficina."""
        assert silla_simple.es_silla_oficina() is False

    def test_es_silla_oficina_solo_ruedas(self):
        """Verifica que solo ruedas no hace silla de oficina."""
        silla = Silla(
            "Test", "Metal", "Gris", 80, altura_regulable=False, tiene_ruedas=True
        )
        assert silla.es_silla_oficina() is False

    def test_es_silla_oficina_solo_altura_regulable(self):
        """Verifica que solo altura regulable no hace silla de oficina."""
        silla = Silla(
            "Test", "Metal", "Gris", 80, altura_regulable=True, tiene_ruedas=False
        )
        assert silla.es_silla_oficina() is False


class TestSillaDescripcion:
    """Tests para el método obtener_descripcion."""

    def test_obtener_descripcion_contiene_nombre(self, silla_simple):
        """Verifica que la descripción contiene el nombre."""
        descripcion = silla_simple.obtener_descripcion()
        assert "Silla Estándar" in descripcion

    def test_obtener_descripcion_contiene_material(self, silla_simple):
        """Verifica que la descripción contiene el material."""
        descripcion = silla_simple.obtener_descripcion()
        assert "Plástico" in descripcion

    def test_obtener_descripcion_muestra_precio(self, silla_simple):
        """Verifica que la descripción muestra el precio."""
        descripcion = silla_simple.obtener_descripcion()
        assert "Precio" in descripcion or "$" in descripcion


@pytest.mark.parametrize(
    "altura_regulable,tiene_ruedas,es_oficina",
    [
        (False, False, False),
        (True, False, False),
        (False, True, False),
        (True, True, True),
    ],
)
def test_es_silla_oficina_parametrizado(altura_regulable, tiene_ruedas, es_oficina):
    """Test parametrizado para determinar si es silla de oficina."""
    silla = Silla(
        "Test",
        "Metal",
        "Negro",
        100,
        altura_regulable=altura_regulable,
        tiene_ruedas=tiene_ruedas,
    )
    assert silla.es_silla_oficina() == es_oficina


@pytest.mark.parametrize(
    "altura,es_valida",
    [
        (30, False),
        (40, True),
        (50, True),
        (75, True),
        (100, True),
        (110, False),
    ],
)
def test_regular_altura_parametrizado(altura, es_valida, silla_oficina):
    """Test parametrizado para regular altura."""
    resultado = silla_oficina.regular_altura(altura)
    if es_valida:
        assert "ajustada" in resultado.lower() or str(altura) in resultado
    else:
        assert "entre 40 y 100" in resultado
