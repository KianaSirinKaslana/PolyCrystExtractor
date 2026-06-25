"""
PolyCrystExtractor - Layer 2: Ontology Definition
定义聚合物晶体学的核心数据模型
"""
from chemdataextractor.model import BaseModel, StringType, ModelType, Compound, FloatType
from chemdataextractor.parse import R

class SpaceGroup(BaseModel):
    """
    空间群模型
    自带正则拦截器，用于捕获被 OCR 破坏或带有特殊变体的符号 (如 P2_1/c)
    """
    value = StringType(parse_expression=R('^[A-Za-z0-9_/\-\·]+$'))

class ChainConformation(BaseModel):
    """
    链构象模型 (聚合物特有)
    例如：planar zigzag, helix s*2/1, TGTG
    """
    value = StringType()

class ZValuePolymer(BaseModel):
    """
    聚合物单胞内链数/重复单元数 (Z/Zc)
    考虑到物理自洽校验，这里提取为浮点数，后续在校验层强制验证为整数
    """
    value = FloatType()

class UnitCellPolymer(BaseModel):
    """
    扩展版晶胞参数
    相比传统小分子，新增了聚合物的纤维周期 (Fiber Period)
    """
    a = FloatType()
    b = FloatType()
    c = FloatType()
    alpha = FloatType()
    beta = FloatType()
    gamma = FloatType()
    volume = FloatType()
    fiber_period = FloatType()  # 聚合物特有：c轴重复距离

class PhysicalProperties(BaseModel):
    """
    大分子物理属性
    提取结晶度、实测密度与分子量
    """
    density = FloatType()
    molecular_weight_Mn = FloatType()
    molecular_weight_Mw = FloatType()
    crystallinity = FloatType() # 结晶度 (Xc)

class PolymerCrystalRecord(BaseModel):
    """
    【顶层聚合模型】
    将所有 30+ 字段聚合在一处，作为最终落盘 JSON 的骨架
    """
    compound = ModelType(Compound, required=True)
    space_group = ModelType(SpaceGroup)
    unit_cell = ModelType(UnitCellPolymer)
    z_value = ModelType(ZValuePolymer)
    chain_conformation = ModelType(ChainConformation)
    properties = ModelType(PhysicalProperties)

    # 后续将继续补充 ThermalProperties(热力学性质), ProcessingHistory(加工历史) 等
