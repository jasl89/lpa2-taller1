"""
Pruebas unitarias para la clase Armario.

Verifica:
- Instanciación correcta
- Cálculo de precio con diferentes configuraciones
- Propiedades específicas del armario
- Métodos de descripción
"""

import pytest
from models.concretos.armario import Armario


class TestArmarioInstanciacion:
    """Tests para la instanciación de Armario."""

    def test_crear_armario_basico(self, armario_basico):
        """Verifica que se puede crear un armario básico."""
        assert armario_basico is not None
        assert armario_basico.nombre == "Armario Clásico"
        assert armario_basico.material == "Madera"
        assert armario_basico.color == "Café"
        assert armario_basico.precio_base == 500

    def test_crear_armario_con_parametros_personalizados(self):
        """Verifica creación con parámetros personalizados."""
        armario = Armario(
            nombre="Armario Custom",
            material="Metal",
            color="Blanco",
            precio_base=600,
            num_puertas=4,
            num_cajones=3,
            tiene_espejos=True,
        )
        assert armario.nombre == "Armario Custom"
        assert armario.num_puertas == 4
        assert armario.num_cajones == 3
        assert armario.tiene_espejos is True

    def test_crear_armario_valores_por_defecto(self):
        """Verifica que los valores por defecto se aplican correctamente."""
        armario = Armario(
            nombre="Armario Simple", material="Madera", color="Natural", precio_base=400
        )
        assert armario.num_puertas == 2
        assert armario.num_cajones == 0
        assert armario.tiene_espejos is False


class TestArmarioPropiedades:
    """Tests para las propiedades del Armario."""

    def test_acceso_propiedades_basicas(self, armario_basico):
        """Verifica el acceso a propiedades básicas."""
        assert armario_basico.num_puertas == 2
        assert armario_basico.num_cajones == 0
        assert armario_basico.tiene_espejos is False

    def test_armario_premium_tiene_espejos(self, armario_premium):
        """Verifica que el armario premium tiene espejos."""
        assert armario_premium.tiene_espejos is True
        assert armario_premium.num_puertas == 3
        assert armario_premium.num_cajones == 2


class TestArmarioCalculoPrecio:
    """Tests para el cálculo de precio del Armario."""

    def test_calcular_precio_basico(self, armario_basico):
        """Verifica el cálculo de precio básico."""
        precio = armario_basico.calcular_precio()
        # 500 + (2*50) + (0*30) + 0 = 600
        assert precio == 600

    def test_calcular_precio_con_puertas(self):
        """Verifica que cada puerta añade 50 al precio."""
        armario = Armario("Test", "Madera", "Café", 500, num_puertas=3)
        precio = armario.calcular_precio()
        # 500 + (3*50) = 650
        assert precio == 650

    def test_calcular_precio_con_cajones(self):
        """Verifica que cada cajón añade 30 al precio."""
        armario = Armario("Test", "Madera", "Café", 500, num_puertas=2, num_cajones=3)
        precio = armario.calcular_precio()
        # 500 + (2*50) + (3*30) = 690
        assert precio == 690

    def test_calcular_precio_con_espejos(self):
        """Verifica que los espejos añaden 100 al precio."""
        armario = Armario(
            "Test", "Madera", "Café", 500, num_puertas=2, tiene_espejos=True
        )
        precio = armario.calcular_precio()
        # 500 + (2*50) + 100 = 700
        assert precio == 700

    def test_calcular_precio_premium_completo(self, armario_premium):
        """Verifica el cálculo de precio para armario premium."""
        precio = armario_premium.calcular_precio()
        # 800 + (3*50) + (2*30) + 100 = 1110
        assert precio == 1110

    def test_precio_es_entero(self, armario_basico):
        """Verifica que el precio retornado es un entero."""
        precio = armario_basico.calcular_precio()
        assert isinstance(precio, int)


class TestArmarioDescripcion:
    """Tests para el método obtener_descripcion."""

    def test_obtener_descripcion_contiene_nombre(self, armario_basico):
        """Verifica que la descripción contiene el nombre."""
        descripcion = armario_basico.obtener_descripcion()
        assert "Armario Clásico" in descripcion

    def test_obtener_descripcion_contiene_material(self, armario_basico):
        """Verifica que la descripción contiene el material."""
        descripcion = armario_basico.obtener_descripcion()
        assert "Madera" in descripcion

    def test_obtener_descripcion_contiene_color(self, armario_basico):
        """Verifica que la descripción contiene el color."""
        descripcion = armario_basico.obtener_descripcion()
        assert "Café" in descripcion

    def test_obtener_descripcion_contiene_puertas(self, armario_basico):
        """Verifica que la descripción contiene número de puertas."""
        descripcion = armario_basico.obtener_descripcion()
        assert "2" in descripcion

    def test_obtener_descripcion_espejos_si(self, armario_premium):
        """Verifica que muestra 'Sí' cuando tiene espejos."""
        descripcion = armario_premium.obtener_descripcion()
        assert "Sí" in descripcion

    def test_obtener_descripcion_espejos_no(self, armario_basico):
        """Verifica que muestra 'No' cuando no tiene espejos."""
        descripcion = armario_basico.obtener_descripcion()
        assert "No" in descripcion


@pytest.mark.parametrize(
    "num_puertas,num_cajones,tiene_espejos,precio_esperado",
    [
        (2, 0, False, 600),  # 500 + 100 + 0 + 0
        (3, 0, False, 650),  # 500 + 150 + 0 + 0
        (2, 2, False, 660),  # 500 + 100 + 60 + 0
        (2, 0, True, 700),  # 500 + 100 + 0 + 100
        (3, 2, True, 810),  # 500 + 150 + 60 + 100
    ],
)
def test_calcular_precio_parametrizado(
    num_puertas, num_cajones, tiene_espejos, precio_esperado
):
    """Test parametrizado para diferentes configuraciones de armario."""
    armario = Armario(
        nombre="Test",
        material="Madera",
        color="Café",
        precio_base=500,
        num_puertas=num_puertas,
        num_cajones=num_cajones,
        tiene_espejos=tiene_espejos,
    )
    precio = armario.calcular_precio()
    assert precio == precio_esperado


def test_armario_con_precio_base_none():
    """Verifica el manejo de precio_base None."""
    armario = Armario(
        nombre="Test", material="Madera", color="Café", precio_base=None, num_puertas=2
    )
    precio = armario.calcular_precio()
    # Si precio_base es None, se convierte a 0
    assert precio == 100  # 0 + (2*50)
