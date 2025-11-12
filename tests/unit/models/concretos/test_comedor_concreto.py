"""
Pruebas unitarias para la clase Comedor concreto.

Verifica:
- Instanciación del comedor
- Manejo de mesa y sillas
- Cálculo de precio
"""

import pytest
from models.concretos.comedor import Comedor


class TestComedorConcretoInstanciacion:
    """Tests para la instanciación del Comedor concreto."""

    def test_crear_comedor_con_mesa(self, mesa_comedor):
        """Verifica que se puede crear comedor con mesa."""
        comedor = Comedor(mesa_comedor)
        assert comedor is not None
        assert comedor.mesa == mesa_comedor

    def test_crear_comedor_sin_sillas(self, mesa_comedor):
        """Verifica que comedor inicia sin sillas."""
        comedor = Comedor(mesa_comedor)
        assert len(comedor.sillas) == 0

    def test_crear_comedor_con_sillas(self, mesa_comedor, silla_simple):
        """Verifica creación con lista de sillas."""
        sillas = [silla_simple, silla_simple]
        comedor = Comedor(mesa_comedor, sillas)
        assert len(comedor.sillas) == 2


class TestComedorConcretoMetodos:
    """Tests para los métodos del Comedor concreto."""

    def test_agregar_silla(self, mesa_comedor, silla_simple):
        """Verifica que se puede agregar silla."""
        comedor = Comedor(mesa_comedor)
        comedor.agregar_silla(silla_simple)
        assert len(comedor.sillas) == 1

    def test_quitar_silla_existente(self, mesa_comedor, silla_simple):
        """Verifica que se puede quitar silla existente."""
        comedor = Comedor(mesa_comedor, [silla_simple])
        comedor.quitar_silla(silla_simple)
        assert len(comedor.sillas) == 0

    def test_quitar_silla_no_existente(self, mesa_comedor, silla_simple, silla_oficina):
        """Verifica que quitar silla no existente no afecta."""
        comedor = Comedor(mesa_comedor, [silla_simple])
        comedor.quitar_silla(silla_oficina)
        assert len(comedor.sillas) == 1

    def test_cantidad_sillas(self, mesa_comedor, silla_simple):
        """Verifica el método cantidad_sillas."""
        comedor = Comedor(mesa_comedor, [silla_simple, silla_simple, silla_simple])
        cantidad = comedor.cantidad_sillas()
        assert cantidad == 3


class TestComedorConcretoCalculoPrecio:
    """Tests para el cálculo de precio del Comedor concreto."""

    def test_calcular_precio_total_solo_mesa(self, mesa_comedor):
        """Verifica cálculo con solo mesa."""
        comedor = Comedor(mesa_comedor)
        precio_total = comedor.calcular_precio_total()
        precio_mesa = mesa_comedor.calcular_precio()
        assert precio_total == precio_mesa

    def test_calcular_precio_total_con_sillas(self, mesa_comedor, silla_simple):
        """Verifica cálculo con mesa y sillas."""
        comedor = Comedor(mesa_comedor, [silla_simple, silla_simple])
        precio_total = comedor.calcular_precio_total()
        precio_esperado = mesa_comedor.calcular_precio() + (
            silla_simple.calcular_precio() * 2
        )
        assert precio_total == precio_esperado


class TestComedorConcretoDescripcion:
    """Tests para el método descripcion."""

    def test_descripcion_sin_sillas(self, mesa_comedor):
        """Verifica descripción sin sillas."""
        comedor = Comedor(mesa_comedor)
        desc = comedor.descripcion()
        assert isinstance(desc, str)
        assert len(desc) > 0

    def test_descripcion_con_sillas(self, mesa_comedor, silla_simple):
        """Verifica descripción con sillas."""
        comedor = Comedor(mesa_comedor, [silla_simple, silla_simple])
        desc = comedor.descripcion()
        assert "2" in desc


@pytest.mark.parametrize("num_sillas", [0, 1, 2, 4, 6])
def test_comedor_concreto_diferentes_cantidades(mesa_comedor, silla_simple, num_sillas):
    """Test parametrizado para diferentes cantidades de sillas."""
    sillas = [silla_simple] * num_sillas
    comedor = Comedor(mesa_comedor, sillas)
    assert comedor.cantidad_sillas() == num_sillas
