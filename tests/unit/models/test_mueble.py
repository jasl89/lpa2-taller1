"""
Pruebas unitarias para la clase base abstracta Mueble.

Verifica que:
- No se puede instanciar directamente (es abstracta)
- Los métodos abstractos deben ser implementados
- Las validaciones de propiedades funcionan correctamente
- Los getters y setters funcionan como se espera
"""

import pytest
from models.mueble import Mueble


class MuebleConcreto(Mueble):
    """Clase concreta para poder testear la clase abstracta Mueble."""

    def calcular_precio(self) -> float:
        return self.precio_base

    def obtener_descripcion(self) -> str:
        return f"Mueble: {self.nombre}"


class TestMuebleInstanciacion:
    """Grupo de tests para verificar la instanciación de Mueble."""

    def test_no_se_puede_instanciar_directamente(self):
        """Verifica que Mueble no puede ser instanciada directamente."""
        with pytest.raises(TypeError):
            Mueble("Silla", "Madera", "Café", 100.0)

    def test_instanciar_clase_concreta_exitosamente(self):
        """Verifica que una clase concreta puede ser instanciada."""
        mueble = MuebleConcreto("Mesa", "Madera", "Blanco", 200.0)
        assert mueble is not None
        assert mueble.nombre == "Mesa"

    def test_valores_iniciales_correctos(self):
        """Verifica que los valores iniciales se asignan correctamente."""
        mueble = MuebleConcreto("Silla", "Plástico", "Negro", 50.0)
        assert mueble.nombre == "Silla"
        assert mueble.material == "Plástico"
        assert mueble.color == "Negro"
        assert mueble.precio_base == 50.0


class TestMueblePropiedadNombre:
    """Grupo de tests para la propiedad nombre."""

    def test_getter_nombre(self):
        """Verifica que el getter de nombre funciona."""
        mueble = MuebleConcreto("Escritorio", "Metal", "Gris", 300.0)
        assert mueble.nombre == "Escritorio"

    def test_setter_nombre_valido(self):
        """Verifica que se puede cambiar el nombre con un valor válido."""
        mueble = MuebleConcreto("Mesa", "Madera", "Café", 150.0)
        mueble.nombre = "Mesa Grande"
        assert mueble.nombre == "Mesa Grande"

    def test_setter_nombre_elimina_espacios(self):
        """Verifica que el setter elimina espacios al inicio y final."""
        mueble = MuebleConcreto("Mesa", "Madera", "Café", 150.0)
        mueble.nombre = "  Silla Nueva  "
        assert mueble.nombre == "Silla Nueva"

    def test_setter_nombre_vacio_lanza_excepcion(self):
        """Verifica que un nombre vacío lanza ValueError."""
        mueble = MuebleConcreto("Mesa", "Madera", "Café", 150.0)
        with pytest.raises(ValueError, match="El nombre no puede estar vacío"):
            mueble.nombre = ""

    def test_setter_nombre_solo_espacios_lanza_excepcion(self):
        """Verifica que un nombre con solo espacios lanza ValueError."""
        mueble = MuebleConcreto("Mesa", "Madera", "Café", 150.0)
        with pytest.raises(ValueError, match="El nombre no puede estar vacío"):
            mueble.nombre = "   "


class TestMueblePropiedadMaterial:
    """Grupo de tests para la propiedad material."""

    def test_getter_material(self):
        """Verifica que el getter de material funciona."""
        mueble = MuebleConcreto("Silla", "Cuero", "Negro", 200.0)
        assert mueble.material == "Cuero"

    def test_setter_material_valido(self):
        """Verifica que se puede cambiar el material con un valor válido."""
        mueble = MuebleConcreto("Mesa", "Madera", "Café", 150.0)
        mueble.material = "Metal"
        assert mueble.material == "Metal"

    def test_setter_material_elimina_espacios(self):
        """Verifica que el setter elimina espacios al inicio y final."""
        mueble = MuebleConcreto("Mesa", "Madera", "Café", 150.0)
        mueble.material = "  Vidrio  "
        assert mueble.material == "Vidrio"

    def test_setter_material_vacio_lanza_excepcion(self):
        """Verifica que un material vacío lanza ValueError."""
        mueble = MuebleConcreto("Mesa", "Madera", "Café", 150.0)
        with pytest.raises(ValueError, match="El material no puede estar vacío"):
            mueble.material = ""

    def test_setter_material_solo_espacios_lanza_excepcion(self):
        """Verifica que un material con solo espacios lanza ValueError."""
        mueble = MuebleConcreto("Mesa", "Madera", "Café", 150.0)
        with pytest.raises(ValueError, match="El material no puede estar vacío"):
            mueble.material = "   "


class TestMueblePropiedadColor:
    """Grupo de tests para la propiedad color."""

    def test_getter_color(self):
        """Verifica que el getter de color funciona."""
        mueble = MuebleConcreto("Sofá", "Tela", "Azul", 500.0)
        assert mueble.color == "Azul"

    def test_setter_color_valido(self):
        """Verifica que se puede cambiar el color con un valor válido."""
        mueble = MuebleConcreto("Mesa", "Madera", "Café", 150.0)
        mueble.color = "Rojo"
        assert mueble.color == "Rojo"

    def test_setter_color_elimina_espacios(self):
        """Verifica que el setter elimina espacios al inicio y final."""
        mueble = MuebleConcreto("Mesa", "Madera", "Café", 150.0)
        mueble.color = "  Verde  "
        assert mueble.color == "Verde"

    def test_setter_color_vacio_lanza_excepcion(self):
        """Verifica que un color vacío lanza ValueError."""
        mueble = MuebleConcreto("Mesa", "Madera", "Café", 150.0)
        with pytest.raises(ValueError, match="El color no puede estar vacío"):
            mueble.color = ""


class TestMueblePropiedadPrecio:
    """Grupo de tests para la propiedad precio_base."""

    def test_getter_precio_base(self):
        """Verifica que el getter de precio_base funciona."""
        mueble = MuebleConcreto("Cama", "Madera", "Natural", 600.0)
        assert mueble.precio_base == 600.0

    def test_setter_precio_base_valido(self):
        """Verifica que se puede cambiar el precio_base con un valor válido."""
        mueble = MuebleConcreto("Mesa", "Madera", "Café", 150.0)
        mueble.precio_base = 200.0
        assert mueble.precio_base == 200.0

    def test_setter_precio_base_cero_es_valido(self):
        """Verifica que un precio de 0 es válido."""
        mueble = MuebleConcreto("Mesa", "Madera", "Café", 150.0)
        mueble.precio_base = 0.0
        assert mueble.precio_base == 0.0

    def test_setter_precio_base_negativo_lanza_excepcion(self):
        """Verifica que un precio negativo lanza ValueError."""
        mueble = MuebleConcreto("Mesa", "Madera", "Café", 150.0)
        with pytest.raises(ValueError, match="El precio base no puede ser negativo"):
            mueble.precio_base = -50.0


class TestMuebleMetodosAbstractos:
    """Grupo de tests para verificar métodos abstractos."""

    def test_clase_sin_calcular_precio_no_se_puede_instanciar(self):
        """Verifica que una clase sin implementar calcular_precio no se puede instanciar."""
        with pytest.raises(TypeError):

            class MuebleIncompleto(Mueble):
                def obtener_descripcion(self) -> str:
                    return "Test"

            MuebleIncompleto("Test", "Test", "Test", 100.0)

    def test_clase_sin_obtener_descripcion_no_se_puede_instanciar(self):
        """Verifica que una clase sin implementar obtener_descripcion no se puede instanciar."""
        with pytest.raises(TypeError):

            class MuebleIncompleto(Mueble):
                def calcular_precio(self) -> float:
                    return 100.0

            MuebleIncompleto("Test", "Test", "Test", 100.0)

    def test_calcular_precio_implementado(self):
        """Verifica que calcular_precio se implementa correctamente."""
        mueble = MuebleConcreto("Mesa", "Madera", "Café", 150.0)
        precio = mueble.calcular_precio()
        assert precio == 150.0

    def test_obtener_descripcion_implementado(self):
        """Verifica que obtener_descripcion se implementa correctamente."""
        mueble = MuebleConcreto("Mesa", "Madera", "Café", 150.0)
        descripcion = mueble.obtener_descripcion()
        assert "Mesa" in descripcion


class TestMuebleMetodosEspeciales:
    """Grupo de tests para métodos especiales (__str__, __repr__)."""

    def test_str_contiene_informacion_basica(self):
        """Verifica que __str__ retorna información legible."""
        mueble = MuebleConcreto("Escritorio", "Metal", "Gris", 300.0)
        resultado = str(mueble)
        assert "Escritorio" in resultado
        assert "Metal" in resultado
        assert "Gris" in resultado

    def test_repr_contiene_informacion_tecnica(self):
        """Verifica que __repr__ retorna información técnica."""
        mueble = MuebleConcreto("Silla", "Plástico", "Negro", 50.0)
        resultado = repr(mueble)
        assert "Mueble" in resultado
        assert "Silla" in resultado
        assert "50.0" in resultado


@pytest.mark.parametrize(
    "nombre,material,color,precio",
    [
        ("Silla Moderna", "Plástico", "Blanco", 75.0),
        ("Mesa Clásica", "Madera", "Café", 250.0),
        ("Escritorio Pro", "Metal", "Negro", 400.0),
    ],
)
def test_mueble_con_diferentes_valores(nombre, material, color, precio):
    """Test parametrizado para verificar diferentes combinaciones de valores."""
    mueble = MuebleConcreto(nombre, material, color, precio)
    assert mueble.nombre == nombre
    assert mueble.material == material
    assert mueble.color == color
    assert mueble.precio_base == precio
