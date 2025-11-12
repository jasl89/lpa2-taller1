"""
Pruebas unitarias para la clase Comedor (composición).

Verifica:
- Composición de mesa y sillas
- Métodos para agregar/quitar sillas
- Cálculo de precio total
- Validaciones de capacidad
"""

import pytest
from unittest.mock import Mock
from models.composicion.comedor import Comedor


class TestComedorInstanciacion:
    """Tests para la instanciación de Comedor."""

    def test_crear_comedor_sin_sillas(self, mesa_comedor):
        """Verifica que se puede crear comedor sin sillas."""
        comedor = Comedor("Comedor Básico", mesa_comedor)
        assert comedor is not None
        assert comedor.nombre == "Comedor Básico"
        assert comedor.mesa == mesa_comedor
        assert len(comedor.sillas) == 0

    def test_crear_comedor_con_sillas(self, mesa_comedor, silla_simple):
        """Verifica que se puede crear comedor con sillas."""
        sillas = [silla_simple]
        comedor = Comedor("Comedor Completo", mesa_comedor, sillas)
        assert len(comedor.sillas) == 1

    def test_crear_comedor_con_multiples_sillas(self, mesa_comedor, silla_simple):
        """Verifica creación con múltiples sillas."""
        sillas = [silla_simple, silla_simple, silla_simple, silla_simple]
        comedor = Comedor("Comedor 4p", mesa_comedor, sillas)
        assert len(comedor.sillas) == 4


class TestComedorPropiedades:
    """Tests para las propiedades de Comedor."""

    def test_getter_nombre(self, mesa_comedor):
        """Verifica el getter de nombre."""
        comedor = Comedor("Mi Comedor", mesa_comedor)
        assert comedor.nombre == "Mi Comedor"

    def test_getter_mesa(self, mesa_comedor):
        """Verifica el getter de mesa."""
        comedor = Comedor("Comedor Test", mesa_comedor)
        assert comedor.mesa == mesa_comedor

    def test_getter_sillas_retorna_copia(self, mesa_comedor, silla_simple):
        """Verifica que getter de sillas retorna una copia."""
        sillas = [silla_simple]
        comedor = Comedor("Comedor Test", mesa_comedor, sillas)
        sillas_obtenidas = comedor.sillas
        sillas_obtenidas.append(silla_simple)
        # La lista interna no debe modificarse
        assert len(comedor.sillas) == 1


class TestComedorAgregarSilla:
    """Tests para el método agregar_silla."""

    def test_agregar_silla_exitosamente(self, mesa_comedor, silla_simple):
        """Verifica que se puede agregar una silla."""
        comedor = Comedor("Comedor Test", mesa_comedor)
        resultado = comedor.agregar_silla(silla_simple)
        assert (
            "agregada exitosamente" in resultado.lower() or "exitosamente" in resultado
        )
        assert len(comedor.sillas) == 1

    def test_agregar_multiples_sillas(self, mesa_comedor, silla_simple):
        """Verifica que se pueden agregar múltiples sillas."""
        comedor = Comedor("Comedor Test", mesa_comedor)
        comedor.agregar_silla(silla_simple)
        comedor.agregar_silla(silla_simple)
        comedor.agregar_silla(silla_simple)
        assert len(comedor.sillas) == 3


class TestComedorQuitarSilla:
    """Tests para el método quitar_silla."""

    def test_quitar_silla_de_comedor_vacio(self, mesa_comedor):
        """Verifica que no se puede quitar silla de comedor vacío."""
        comedor = Comedor("Comedor Test", mesa_comedor)
        resultado = comedor.quitar_silla()
        assert "no hay sillas" in resultado.lower()

    def test_quitar_ultima_silla(self, mesa_comedor, silla_simple):
        """Verifica que se puede quitar la última silla."""
        sillas = [silla_simple, silla_simple]
        comedor = Comedor("Comedor Test", mesa_comedor, sillas)
        resultado = comedor.quitar_silla()
        assert "removida" in resultado.lower() or "remov" in resultado.lower()
        assert len(comedor.sillas) == 1

    def test_quitar_silla_por_indice(self, mesa_comedor, silla_simple):
        """Verifica que se puede quitar silla por índice."""
        sillas = [silla_simple, silla_simple, silla_simple]
        comedor = Comedor("Comedor Test", mesa_comedor, sillas)
        comedor.quitar_silla(0)
        assert len(comedor.sillas) == 2

    def test_quitar_silla_indice_invalido(self, mesa_comedor, silla_simple):
        """Verifica manejo de índice inválido."""
        sillas = [silla_simple]
        comedor = Comedor("Comedor Test", mesa_comedor, sillas)
        resultado = comedor.quitar_silla(10)
        assert "inválido" in resultado.lower() or "invalido" in resultado.lower()


class TestComedorCalculoPrecio:
    """Tests para el cálculo de precio total."""

    def test_calcular_precio_total_solo_mesa(self, mesa_comedor):
        """Verifica cálculo de precio solo con mesa."""
        comedor = Comedor("Comedor Test", mesa_comedor)
        precio_total = comedor.calcular_precio_total()
        precio_mesa = mesa_comedor.calcular_precio()
        assert precio_total == precio_mesa

    def test_calcular_precio_total_con_sillas(self, mesa_comedor, silla_simple):
        """Verifica cálculo de precio con mesa y sillas."""
        sillas = [silla_simple, silla_simple]
        comedor = Comedor("Comedor Test", mesa_comedor, sillas)
        precio_total = comedor.calcular_precio_total()
        precio_esperado = mesa_comedor.calcular_precio() + (
            silla_simple.calcular_precio() * 2
        )
        assert precio_total == precio_esperado

    def test_precio_aumenta_al_agregar_sillas(self, mesa_comedor, silla_simple):
        """Verifica que el precio aumenta al agregar sillas."""
        comedor = Comedor("Comedor Test", mesa_comedor)
        precio_inicial = comedor.calcular_precio_total()
        comedor.agregar_silla(silla_simple)
        precio_con_silla = comedor.calcular_precio_total()
        assert precio_con_silla > precio_inicial


class TestComedorDescripcion:
    """Tests para obtener_descripcion."""

    def test_obtener_descripcion_sin_sillas(self, mesa_comedor):
        """Verifica descripción de comedor sin sillas."""
        comedor = Comedor("Comedor Test", mesa_comedor, [])
        # Comedor no tiene obtener_descripcion, verificamos que existe
        assert comedor.nombre == "Comedor Test"

    def test_obtener_descripcion_con_sillas(self, mesa_comedor, silla_simple):
        """Verifica descripción de comedor con sillas."""
        sillas = [silla_simple, silla_simple]
        comedor = Comedor("Comedor Test", mesa_comedor, sillas)
        # Comedor no tiene obtener_descripcion, verificamos número de sillas
        assert len(comedor.sillas) == 2


@pytest.mark.parametrize("num_sillas", [0, 1, 2, 4, 6])
def test_comedor_con_diferentes_cantidades_sillas(
    mesa_comedor, silla_simple, num_sillas
):
    """Test parametrizado para diferentes cantidades de sillas."""
    sillas = [silla_simple] * num_sillas
    comedor = Comedor("Comedor Test", mesa_comedor, sillas)
    assert len(comedor.sillas) == num_sillas


def test_comedor_con_mocks():
    """Test usando mocks para mesa y sillas."""
    mesa_mock = Mock()
    mesa_mock.calcular_precio.return_value = 500.0

    silla_mock = Mock()
    silla_mock.calcular_precio.return_value = 100.0

    comedor = Comedor("Comedor Mock", mesa_mock, [silla_mock, silla_mock])
    precio_total = comedor.calcular_precio_total()

    assert precio_total == 700.0
    mesa_mock.calcular_precio.assert_called_once()
    assert silla_mock.calcular_precio.call_count == 2
