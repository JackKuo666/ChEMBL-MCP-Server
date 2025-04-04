from typing import Any, List, Dict, Callable, TypeVar, Optional
import asyncio
import logging
import functools
import time
from mcp.server.fastmcp import FastMCP
import chembl_webresource_client
from chembl_webresource_client.new_client import new_client
from chembl_webresource_client.utils import utils

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Initialize FastMCP server
mcp = FastMCP("chembl")

# 定义返回类型变量
T = TypeVar('T')

# 异步超时装饰器
def async_timeout(seconds: int):
    def decorator(func):
        @functools.wraps(func)
        async def wrapper(*args, **kwargs):
            try:
                return await asyncio.wait_for(func(*args, **kwargs), timeout=seconds)
            except asyncio.TimeoutError:
                logging.error(f"函数 {func.__name__} 执行超时 (超过 {seconds} 秒)")
                raise TimeoutError(f"函数执行超过 {seconds} 秒")
        return wrapper
    return decorator

# 错误处理装饰器
def error_handler(func):
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            start_time = time.time()
            result = await func(*args, **kwargs)
            end_time = time.time()
            logging.info(f"{func.__name__} 执行时间: {end_time - start_time:.2f}秒")
            return result
        except TimeoutError as e:
            logging.error(f"{func.__name__} 超时错误: {str(e)}")
            raise
        except Exception as e:
            logging.error(f"{func.__name__} 执行错误: {str(e)}")
            raise
    return wrapper


@mcp.tool()
@error_handler
@async_timeout(10)
async def example_activity(assay_chembl_id: str) -> List[Dict[str, Any]]:
    """获取指定assay_chembl_id的活性数据
    
    Args:
        assay_chembl_id: ChEMBL assay ID
        
    Returns:
        活性数据列表
    """
    client = new_client
    activities = client.activity.filter(assay_chembl_id=assay_chembl_id)
    return list(activities)

@mcp.tool()
@error_handler
@async_timeout(10)
async def example_activity_supplementary_data_by_activity(activity_chembl_id: str) -> List[Dict[str, Any]]:
    """获取指定activity_chembl_id的活性补充数据
    
    Args:
        activity_chembl_id: ChEMBL活性ID
        
    Returns:
        活性补充数据列表
    """
    client = new_client
    activity_supp_data = client.activity_supplementary_data_by_activity.filter(activity_chembl_id=activity_chembl_id)
    return list(activity_supp_data)

@mcp.tool()
@error_handler
@async_timeout(10)
async def example_assay(assay_type: str) -> List[Dict[str, Any]]:
    """获取指定类型的测定数据
    
    Args:
        assay_type: 测定类型
        
    Returns:
        测定数据列表
    """
    client = new_client
    assays = client.assay.filter(assay_type=assay_type)
    return list(assays)

@mcp.tool()
@error_handler
@async_timeout(10)
async def example_assay_class(assay_class_type: str) -> List[Dict[str, Any]]:
    """获取指定类型的测定分类数据
    
    Args:
        assay_class_type: 测定分类类型
        
    Returns:
        测定分类数据列表
    """
    client = new_client
    assay_classes = client.assay_class.filter(assay_class_type=assay_class_type)
    return list(assay_classes)

@mcp.tool()
@error_handler
@async_timeout(10)
async def example_atc_class(level1: str) -> List[Dict[str, Any]]:
    """获取指定level1的ATC分类数据
    
    Args:
        level1: ATC分类的level1值
        
    Returns:
        ATC分类数据列表
    """
    client = new_client
    atc_classes = client.atc_class.filter(level1=level1)
    return list(atc_classes)

@mcp.tool()
@error_handler
@async_timeout(10)
async def example_binding_site(site_name: str) -> List[Dict[str, Any]]:
    """获取指定名称的结合位点数据
    
    Args:
        site_name: 结合位点名称
        
    Returns:
        结合位点数据列表
    """
    client = new_client
    binding_sites = client.binding_site.filter(site_name=site_name)
    return list(binding_sites)

@mcp.tool()
@error_handler
@async_timeout(10)
async def example_biotherapeutic(biotherapeutic_type: str) -> List[Dict[str, Any]]:
    """获取指定类型的生物治疗数据
    
    Args:
        biotherapeutic_type: 生物治疗类型
        
    Returns:
        生物治疗数据列表
    """
    client = new_client
    biotherapeutics = client.biotherapeutic.filter(biotherapeutic_type=biotherapeutic_type)
    return list(biotherapeutics)

@mcp.tool()
@error_handler
@async_timeout(10)
async def example_cell_line(cell_line_name: str) -> List[Dict[str, Any]]:
    """获取指定名称的细胞系数据
    
    Args:
        cell_line_name: 细胞系名称
        
    Returns:
        细胞系数据列表
    """
    client = new_client
    cell_lines = client.cell_line.filter(cell_line_name=cell_line_name)
    return list(cell_lines)

@mcp.tool()
@error_handler
@async_timeout(10)
async def example_chembl_id_lookup(available_type: str, q: str) -> List[Dict[str, Any]]:
    """查找指定类型和查询的ChEMBL ID
    
    Args:
        available_type: 可用类型
        q: 查询字符串
        
    Returns:
        ChEMBL ID列表
    """
    client = new_client
    chembl_ids = client.chembl_id_lookup.filter(available_type=available_type, q=q)
    return list(chembl_ids)

@mcp.tool()
@error_handler
@async_timeout(10)
async def example_chembl_release() -> List[Dict[str, Any]]:
    """获取所有ChEMBL发布版本信息
    
    Returns:
        ChEMBL发布版本信息列表
    """
    client = new_client
    chembl_releases = client.chembl_release.all()
    return list(chembl_releases)

@mcp.tool()
@error_handler
@async_timeout(10)
async def example_compound_record(compound_name: str) -> List[Dict[str, Any]]:
    """获取指定名称的化合物记录
    
    Args:
        compound_name: 化合物名称
        
    Returns:
        化合物记录列表
    """
    client = new_client
    compound_records = client.compound_record.filter(compound_name=compound_name)
    return list(compound_records)

@mcp.tool()
@error_handler
@async_timeout(10)
async def example_compound_structural_alert(alert_name: str) -> List[Dict[str, Any]]:
    """获取指定名称的化合物结构警报
    
    Args:
        alert_name: 警报名称
        
    Returns:
        化合物结构警报列表
    """
    client = new_client
    structural_alerts = client.compound_structural_alert.filter(alert_name=alert_name)
    return list(structural_alerts)

@mcp.tool()
@error_handler
@async_timeout(10)
async def example_description(description_type: str) -> List[Dict[str, Any]]:
    """获取指定类型的描述数据
    
    Args:
        description_type: 描述类型
        
    Returns:
        描述数据列表
    """
    client = new_client
    descriptions = client.description.filter(description_type=description_type)
    return list(descriptions)

@mcp.tool()
@error_handler
@async_timeout(10)
async def example_document(journal: str) -> List[Dict[str, Any]]:
    """获取指定期刊的文档数据
    
    Args:
        journal: 期刊名称
        
    Returns:
        文档数据列表
    """
    client = new_client
    documents = client.document.filter(journal=journal)
    return list(documents)

@mcp.tool()
@error_handler
@async_timeout(10)
async def example_drug(drug_type: str) -> List[Dict[str, Any]]:
    """获取指定类型的药物数据
    
    Args:
        drug_type: 药物类型
        
    Returns:
        药物数据列表
    """
    client = new_client
    drugs = client.drug.filter(drug_type=drug_type)
    return list(drugs)

@mcp.tool()
@error_handler
@async_timeout(10)
async def example_drug_indication(mesh_heading: str) -> List[Dict[str, Any]]:
    """获取指定MeSH标题的药物适应症数据
    
    Args:
        mesh_heading: MeSH标题
        
    Returns:
        药物适应症数据列表
    """
    client = new_client
    drug_indications = client.drug_indication.filter(mesh_heading=mesh_heading)
    return list(drug_indications)

@mcp.tool()
@error_handler
@async_timeout(10)
async def example_drug_warning(meddra_term: str) -> List[Dict[str, Any]]:
    """获取指定MedDRA术语的药物警告数据
    
    Args:
        meddra_term: MedDRA术语
        
    Returns:
        药物警告数据列表
    """
    client = new_client
    drug_warnings = client.drug_warning.filter(meddra_term=meddra_term)
    return list(drug_warnings)

@mcp.tool()
@error_handler
@async_timeout(10)
async def example_go_slim(go_slim_term: str) -> List[Dict[str, Any]]:
    """获取指定GO Slim术语的数据
    
    Args:
        go_slim_term: GO Slim术语
        
    Returns:
        GO Slim数据列表
    """
    client = new_client
    go_slims = client.go_slim.filter(go_slim_term=go_slim_term)
    return list(go_slims)

@mcp.tool()
@error_handler
@async_timeout(10)
async def example_mechanism(mechanism_of_action: str) -> List[Dict[str, Any]]:
    """获取指定作用机制的数据
    
    Args:
        mechanism_of_action: 作用机制
        
    Returns:
        作用机制数据列表
    """
    client = new_client
    mechanisms = client.mechanism.filter(mechanism_of_action=mechanism_of_action)
    return list(mechanisms)

@mcp.tool()
@error_handler
@async_timeout(10)
async def example_molecule(molecule_type: str) -> List[Dict[str, Any]]:
    """获取指定类型的分子数据
    
    Args:
        molecule_type: 分子类型
        
    Returns:
        分子数据列表
    """
    client = new_client
    molecules = client.molecule.filter(molecule_type=molecule_type)
    return list(molecules)

@mcp.tool()
@error_handler
@async_timeout(10)
async def example_molecule_form(form_description: str) -> List[Dict[str, Any]]:
    """获取指定描述的分子形式数据
    
    Args:
        form_description: 形式描述
        
    Returns:
        分子形式数据列表
    """
    client = new_client
    molecule_forms = client.molecule_form.filter(form_description=form_description)
    return list(molecule_forms)

@mcp.tool()
@error_handler
@async_timeout(10)
async def example_organism(tax_id: int) -> List[Dict[str, Any]]:
    """获取指定分类ID的生物体数据
    
    Args:
        tax_id: 分类ID
        
    Returns:
        生物体数据列表
    """
    client = new_client
    organisms = client.organism.filter(tax_id=tax_id)
    return list(organisms)

@mcp.tool()
@error_handler
@async_timeout(10)
async def example_protein_classification(protein_class_name: str) -> List[Dict[str, Any]]:
    """获取指定蛋白质分类名称的数据
    
    Args:
        protein_class_name: 蛋白质分类名称
        
    Returns:
        蛋白质分类数据列表
    """
    client = new_client
    protein_classifications = client.protein_classification.filter(protein_class_name=protein_class_name)
    return list(protein_classifications)

@mcp.tool()
@error_handler
@async_timeout(10)
async def example_source(source_description: str) -> List[Dict[str, Any]]:
    """获取指定描述的数据源信息
    
    Args:
        source_description: 数据源描述
        
    Returns:
        数据源信息列表
    """
    client = new_client
    sources = client.source.filter(source_description=source_description)
    return list(sources)

@mcp.tool()
@error_handler
@async_timeout(10)
async def example_target(target_type: str) -> List[Dict[str, Any]]:
    """获取指定类型的靶点数据
    
    Args:
        target_type: 靶点类型
        
    Returns:
        靶点数据列表
    """
    client = new_client
    targets = client.target.filter(target_type=target_type)
    return list(targets)

@mcp.tool()
@error_handler
@async_timeout(10)
async def example_target_component(component_type: str) -> List[Dict[str, Any]]:
    """获取指定类型的靶点组件数据
    
    Args:
        component_type: 组件类型
        
    Returns:
        靶点组件数据列表
    """
    client = new_client
    target_components = client.target_component.filter(component_type=component_type)
    return list(target_components)

@mcp.tool()
@error_handler
@async_timeout(10)
async def example_target_relation(relationship_type: str) -> List[Dict[str, Any]]:
    """获取指定关系类型的靶点关系数据
    
    Args:
        relationship_type: 关系类型
        
    Returns:
        靶点关系数据列表
    """
    client = new_client
    target_relations = client.target_relation.filter(relationship_type=relationship_type)
    return list(target_relations)

@mcp.tool()
@error_handler
@async_timeout(10)
async def example_tissue(tissue_name: str) -> List[Dict[str, Any]]:
    """获取指定名称的组织数据
    
    Args:
        tissue_name: 组织名称
        
    Returns:
        组织数据列表
    """
    client = new_client
    tissues = client.tissue.filter(tissue_name=tissue_name)
    return list(tissues)

@mcp.tool()
@error_handler
@async_timeout(10)
async def example_xref_source(xref_name: str) -> List[Dict[str, Any]]:
    """获取指定名称的交叉引用源数据
    
    Args:
        xref_name: 交叉引用源名称
        
    Returns:
        交叉引用源数据列表
    """
    client = new_client
    xref_sources = client.xref_source.filter(xref_name=xref_name)
    return list(xref_sources)

@mcp.tool()
@error_handler
@async_timeout(5)
async def example_canonicalizeSmiles(smiles: str) -> str:
    """将SMILES字符串转换为规范形式
    
    Args:
        smiles: SMILES字符串
        
    Returns:
        规范化的SMILES字符串
    """
    canonical_smiles = utils.canonicalizeSmiles(smiles)
    return canonical_smiles

@mcp.tool()
@error_handler
@async_timeout(5)
async def example_chemblDescriptors(smiles: str) -> Dict[str, Any]:
    """获取SMILES字符串的ChEMBL描述符
    
    Args:
        smiles: SMILES字符串
        
    Returns:
        ChEMBL描述符字典
    """
    descriptors = utils.chemblDescriptors(smiles)
    return descriptors

@mcp.tool()
@error_handler
@async_timeout(5)
async def example_description_utils(chembl_id: str) -> str:
    """
    获取ChEMBL ID的描述信息
    
    Args:
        chembl_id: ChEMBL ID
        
    Returns:
        描述信息
    """
    description = utils.description(chembl_id)
    return description

@mcp.tool()
@error_handler
@async_timeout(5)
async def example_descriptors(smiles: str) -> Dict[str, Any]:
    """
    获取SMILES字符串的描述符
    
    Args:
        smiles: SMILES字符串
        
    Returns:
        描述符字典
    """
    descriptors = utils.descriptors(smiles)
    return descriptors

@mcp.tool()
@error_handler
@async_timeout(5)
async def example_getParent(chembl_id: str) -> str:
    """
    获取ChEMBL ID的父级ID
    
    Args:
        chembl_id: ChEMBL ID
        
    Returns:
        父级ChEMBL ID
    """
    parent = utils.getParent(chembl_id)
    return parent

@mcp.tool()
@error_handler
@async_timeout(5)
async def example_highlightSmilesFragmentSvg(smiles: str, fragment: str) -> str:
    """
    生成高亮显示片段的SMILES SVG图像
    
    Args:
        smiles: SMILES字符串
        fragment: 要高亮的片段
        
    Returns:
        SVG图像字符串
    """
    highlighted_svg = utils.highlightSmilesFragmentSvg(smiles, fragment)
    return highlighted_svg

@mcp.tool()
@error_handler
@async_timeout(5)
async def example_inchi2inchiKey(inchi: str) -> str:
    """
    将InChI转换为InChI Key
    
    Args:
        inchi: InChI字符串
        
    Returns:
        InChI Key
    """
    inchi_key = utils.inchi2inchiKey(inchi)
    return inchi_key

@mcp.tool()
@error_handler
@async_timeout(5)
async def example_inchi2svg(inchi: str) -> str:
    """
    将InChI转换为SVG图像
    
    Args:
        inchi: InChI字符串
        
    Returns:
        SVG图像字符串
    """
    inchi_svg = utils.inchi2svg(inchi)
    return inchi_svg
    # print("InChI SVG:", inchi_svg)  # Skipping printing SVG

@mcp.tool()
@error_handler
@async_timeout(5)
async def example_is3D(smiles: str) -> bool:
    """
    检查SMILES字符串是否表示3D结构
    
    Args:
        smiles: SMILES字符串
        
    Returns:
        是否为3D结构
    """
    is_3d = utils.is3D(smiles)
    return is_3d

@mcp.tool()
@error_handler
@async_timeout(5)
async def example_official_utils(chembl_id: str) -> str:
    """
    获取ChEMBL ID的官方名称
    
    Args:
        chembl_id: ChEMBL ID
        
    Returns:
        官方名称
    """
    official = utils.official(chembl_id)
    return official

@mcp.tool()
@error_handler
@async_timeout(5)
async def example_removeHs(smiles: str) -> str:
    """
    从SMILES字符串中移除氢原子
    
    Args:
        smiles: SMILES字符串
        
    Returns:
        移除氢原子后的SMILES字符串
    """
    smiles_no_h = utils.removeHs(smiles)
    return smiles_no_h

@mcp.tool()
@error_handler
@async_timeout(5)
async def example_smiles2inchi(smiles: str) -> str:
    """
    将SMILES字符串转换为InChI
    
    Args:
        smiles: SMILES字符串
        
    Returns:
        InChI字符串
    """
    smiles_inchi = utils.smiles2inchi(smiles)
    return smiles_inchi

@mcp.tool()
@error_handler
@async_timeout(5)
async def example_smiles2inchiKey(smiles: str) -> str:
    """
    将SMILES字符串转换为InChI Key
    
    Args:
        smiles: SMILES字符串
        
    Returns:
        InChI Key
    """
    smiles_inchi_key = utils.smiles2inchiKey(smiles)
    return smiles_inchi_key

@mcp.tool()
@error_handler
@async_timeout(5)
async def example_smiles2svg(smiles: str) -> str:
    """
    将SMILES字符串转换为SVG图像
    
    Args:
        smiles: SMILES字符串
        
    Returns:
        SVG图像字符串
    """
    smiles_svg = utils.smiles2svg(smiles)
    return smiles_svg
    # print("SMILES SVG:", smiles_svg)  # Skipping printing SVG

@mcp.tool()
@error_handler
@async_timeout(5)
async def example_standardize(smiles: str) -> str:
    """
    标准化SMILES字符串
    
    Args:
        smiles: SMILES字符串
        
    Returns:
        标准化的SMILES字符串
    """
    standardized_smiles = utils.standardize(smiles)
    return standardized_smiles

@mcp.tool()
@error_handler
@async_timeout(5)
async def example_status() -> Dict[str, Any]:
    """
    获取ChEMBL Web服务的状态信息
    
    Returns:
        状态信息字典
    """
    status = utils.status()
    return status

@mcp.tool()
@error_handler
@async_timeout(5)
async def example_structuralAlerts(smiles: str) -> List[Dict[str, Any]]:
    """
    获取SMILES字符串的结构警报
    
    Args:
        smiles: SMILES字符串
        
    Returns:
        结构警报列表
    """
    alerts = utils.structuralAlerts(smiles)
    return alerts

if __name__ == "__main__":
    import argparse
    
    # 命令行参数解析
    parser = argparse.ArgumentParser(description='ChEMBL FastMCP服务器')
    parser.add_argument('--host', type=str, default='127.0.0.1', help='服务器主机地址')
    parser.add_argument('--port', type=int, default=8000, help='服务器端口')
    parser.add_argument('--transport', type=str, default='http', choices=['http', 'stdio'], help='传输方式')
    parser.add_argument('--log-level', type=str, default='INFO', choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'], help='日志级别')
    
    args = parser.parse_args()
    
    # 设置日志级别
    logging.getLogger().setLevel(getattr(logging, args.log_level))
    
    logging.info(f"启动ChEMBL MCP服务器 (传输方式: {args.transport})")
    
    # FastMCP只支持'stdio'作为transport参数
    if args.transport == 'http':
        logging.info(f"HTTP服务器将在 {args.host}:{args.port} 上运行")
        logging.warning("FastMCP不支持http传输方式，将使用stdio传输方式代替")
        # 由于缺少fastapi模块或FastMCP不支持http，使用stdio作为备选方案
        mcp.run(transport='stdio')
    else:
        logging.info("使用stdio传输方式")
        mcp.run(transport='stdio')
