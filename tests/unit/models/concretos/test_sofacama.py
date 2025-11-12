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

    def test_capacidad_personas(self, sofacama_estandar):
        """Verifica propiedad capacidad_personas del sofá."""
        assert sofacama_estandar.capacidad_personas == 2

    def test_tamaño_cama(self, sofacama_estandar):
        """Verifica propiedad tamaño_cama."""
        assert sofacama_estandar.tamaño_cama == "matrimonial"


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
            "Sofá", "Metal", "Gris", 500, material_tapizado="Tela", capacidad_personas=2
        )
        sofacama = SofaCama(
            "SofaCama",
            "Metal",
            "Gris",
            500,
            material_tapizado="Tela",
            capacidad_personas=2,
            tamaño_cama="matrimonial",
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
    "capacidad_personas,tamaño_cama",
    [
        (2, "individual"),
        (2, "matrimonial"),
        (3, "matrimonial"),
        (3, "queen"),
    ],
)
def test_sofacama_diferentes_configuraciones(capacidad_personas, tamaño_cama):
    """Test parametrizado para diferentes configuraciones."""
    sofacama = SofaCama(
        "Test",
        "Metal",
        "Gris",
        500,
        material_tapizado="Tela",
        capacidad_personas=capacidad_personas,
        tamaño_cama=tamaño_cama,
    )
    assert sofacama.capacidad_personas == capacidad_personas
    assert sofacama.tamaño_cama == tamaño_cama
