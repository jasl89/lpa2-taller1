"""
Fixtures compartidos para todas las pruebas unitarias.
Permite reutilizar objetos comunes en múltiples tests.
"""

import pytest
from unittest.mock import Mock
from models.concretos.armario import Armario
from models.concretos.cajonera import Cajonera
from models.concretos.silla import Silla
from models.concretos.sillon import Sillon
from models.concretos.sofa import Sofa
from models.concretos.mesa import Mesa
from models.concretos.escritorio import Escritorio
from models.concretos.cama import Cama
from models.concretos.sofacama import SofaCama


@pytest.fixture
def armario_basico():
    """Fixture que retorna un armario básico para pruebas."""
    return Armario(
        nombre="Armario Clásico",
        material="Madera",
        color="Café",
        precio_base=500,
        num_puertas=2,
        num_cajones=0,
        tiene_espejos=False,
    )


@pytest.fixture
def armario_premium():
    """Fixture que retorna un armario premium con espejos."""
    return Armario(
        nombre="Armario Premium",
        material="Roble",
        color="Natural",
        precio_base=800,
        num_puertas=3,
        num_cajones=2,
        tiene_espejos=True,
    )


@pytest.fixture
def cajonera_pequena():
    """Fixture que retorna una cajonera pequeña."""
    return Cajonera(
        nombre="Cajonera Mini",
        material="Pino",
        color="Blanco",
        precio_base=150,
        num_cajones=3,
        profundidad=30,
    )


@pytest.fixture
def silla_simple():
    """Fixture que retorna una silla simple sin características especiales."""
    return Silla(
        nombre="Silla Estándar",
        material="Plástico",
        color="Negro",
        precio_base=50,
        tiene_respaldo=True,
        altura_regulable=False,
        tiene_ruedas=False,
    )


@pytest.fixture
def silla_oficina():
    """Fixture que retorna una silla de oficina con ruedas y altura regulable."""
    return Silla(
        nombre="Silla Ejecutiva",
        material="Cuero sintético",
        color="Negro",
        precio_base=150,
        tiene_respaldo=True,
        material_tapizado="Tela",
        altura_regulable=True,
        tiene_ruedas=True,
    )


@pytest.fixture
def sillon_individual():
    """Fixture que retorna un sillón individual."""
    return Sillon(
        nombre="Sillón Relax",
        material="Madera",
        color="Beige",
        precio_base=300,
        material_tapizado="Tela",
        tiene_apoyabrazos=True,
        es_reclinable=False,
    )


@pytest.fixture
def sofa_tres_puestos():
    """Fixture que retorna un sofá de tres puestos."""
    return Sofa(
        nombre="Sofá Moderno",
        material="Madera",
        color="Gris",
        precio_base=600,
        material_tapizado="Tela",
        num_puestos=3,
        es_modular=False,
    )


@pytest.fixture
def mesa_comedor():
    """Fixture que retorna una mesa de comedor."""
    return Mesa(
        nombre="Mesa Comedor 6p",
        material="Madera",
        color="Nogal",
        precio_base=400,
        largo=180,
        ancho=90,
        altura=75,
        es_extensible=False,
    )


@pytest.fixture
def mesa_extensible():
    """Fixture que retorna una mesa extensible."""
    return Mesa(
        nombre="Mesa Extensible",
        material="Madera",
        color="Blanco",
        precio_base=500,
        largo=160,
        ancho=80,
        altura=75,
        es_extensible=True,
        num_comensales=8,
    )


@pytest.fixture
def escritorio_basico():
    """Fixture que retorna un escritorio básico."""
    return Escritorio(
        nombre="Escritorio Home Office",
        material="MDF",
        color="Blanco",
        precio_base=200,
        largo=120,
        ancho=60,
        altura=75,
        num_cajones=2,
        tiene_organizador_cables=True,
    )


@pytest.fixture
def cama_individual():
    """Fixture que retorna una cama individual."""
    return Cama(
        nombre="Cama Individual",
        material="Madera",
        color="Natural",
        precio_base=300,
        tamano="Individual",
        tiene_cajones=False,
        incluye_colchon=False,
    )


@pytest.fixture
def cama_king():
    """Fixture que retorna una cama King size."""
    return Cama(
        nombre="Cama King",
        material="Roble",
        color="Nogal",
        precio_base=800,
        tamano="King",
        tiene_cajones=True,
        incluye_colchon=True,
    )


@pytest.fixture
def sofacama_estandar():
    """Fixture que retorna un sofá-cama estándar."""
    return SofaCama(
        nombre="Sofá-Cama Multifuncional",
        material="Metal",
        color="Gris",
        precio_base=500,
        material_tapizado="Tela",
        num_puestos=2,
        tamano_cama="Matrimonial",
    )


@pytest.fixture
def mock_mueble():
    """Fixture que retorna un mock de Mueble para pruebas de clases abstractas."""
    mock = Mock()
    mock.nombre = "Mueble Test"
    mock.material = "Material Test"
    mock.color = "Color Test"
    mock.precio_base = 100.0
    mock.calcular_precio.return_value = 100.0
    mock.obtener_descripcion.return_value = "Descripción mock"
    return mock


@pytest.fixture
def datos_mueble_validos():
    """Fixture que retorna datos válidos para crear un mueble."""
    return {
        "nombre": "Mueble Test",
        "material": "Madera",
        "color": "Café",
        "precio_base": 100.0,
    }


@pytest.fixture
def datos_mueble_invalidos():
    """Fixture que retorna datos inválidos para crear un mueble."""
    return {"nombre": "", "material": "", "color": "", "precio_base": -50.0}
