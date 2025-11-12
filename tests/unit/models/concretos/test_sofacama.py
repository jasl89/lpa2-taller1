"""
Pruebas unitarias para la clase SofaCama.

Verifica:
- Herencia múltiple (Sofa y Cama)
- Propiedades de ambas clases padre
- Cálculo de precio combinado
- Conversión entre modos
"""

import pytest
from models.concretos.sofacama import SofaCama
from models.categorias.asientos import Asiento


class TestSofaCamaInstanciacion:
    """Tests para la instanciación de SofaCama."""

    def test_crear_sofacama(self, sofacama_estandar):
        """Verifica que se puede crear un sofá-cama."""
        assert sofacama_estandar is not None
        assert sofacama_estandar.nombre == "Sofá-Cama Multifuncional"

    def test_sofacama_hereda_de_asiento(self, sofacama_estandar):
        """Verifica que SofaCama hereda de Asiento."""
        assert isinstance(sofacama_estandar, Asiento)


class TestSofaCamaPropiedades:
    """Tests para las propiedades de SofaCama."""

    def test_num_puestos(self, sofacama_estandar):
        """Verifica propiedad num_puestos del sofá."""
        assert sofacama_estandar.num_puestos == 2

    def test_tamano_cama(self, sofacama_estandar):
        """Verifica propiedad tamano_cama."""
        assert sofacama_estandar.tamano_cama == "Matrimonial"


class TestSofaCamaCalculoPrecio:
    """Tests para el cálculo de precio de SofaCama."""

    def test_calcular_precio(self, sofacama_estandar):
        """Verifica el cálculo de precio."""
        precio = sofacama_estandar.calcular_precio()
        assert precio > 0

    def test_sofacama_mas_caro_que_sofa_simple(self):
        """Verifica que sofá-cama es más caro que sofá simple."""
        from models.concretos.sofa import Sofa

        sofa = Sofa(
            "Sofá", "Metal", "Gris", 500, material_tapizado="Tela", num_puestos=2
        )
        sofacama = SofaCama(
            "SofaCama",
            "Metal",
            "Gris",
            500,
            material_tapizado="Tela",
            num_puestos=2,
            tamano_cama="Matrimonial",
        )

        precio_sofa = sofa.calcular_precio()
        precio_sofacama = sofacama.calcular_precio()

        assert precio_sofacama > precio_sofa


class TestSofaCamaDescripcion:
    """Tests para obtener_descripcion."""

    def test_obtener_descripcion(self, sofacama_estandar):
        """Verifica que retorna descripción."""
        descripcion = sofacama_estandar.obtener_descripcion()
        assert isinstance(descripcion, str)
        assert len(descripcion) > 0


@pytest.mark.parametrize(
    "num_puestos,tamano_cama",
    [
        (2, "Individual"),
        (2, "Matrimonial"),
        (3, "Matrimonial"),
        (3, "Queen"),
    ],
)
def test_sofacama_diferentes_configuraciones(num_puestos, tamano_cama):
    """Test parametrizado para diferentes configuraciones."""
    sofacama = SofaCama(
        "Test",
        "Metal",
        "Gris",
        500,
        material_tapizado="Tela",
        num_puestos=num_puestos,
        tamano_cama=tamano_cama,
    )
    assert sofacama.num_puestos == num_puestos
    assert sofacama.tamano_cama == tamano_cama
