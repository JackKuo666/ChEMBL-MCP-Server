from typing import Any, List, Dict
import asyncio
import logging
from mcp.server.fastmcp import FastMCP
import chembl_webresource_client
from chembl_webresource_client.new_client import new_client
from chembl_webresource_client.utils import utils

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Initialize FastMCP server
mcp = FastMCP("semanticscholar")


@mcp.tool()
async def example_activity(assay_chembl_id: str) -> List[Dict[str, Any]]:
    client = new_client
    activities = client.activity.filter(assay_chembl_id=assay_chembl_id)
    return list(activities)

@mcp.tool()
async def example_activity_supplementary_data_by_activity(activity_chembl_id: str) -> List[Dict[str, Any]]:
    client = new_client
    activity_supp_data = client.activity_supplementary_data_by_activity.filter(activity_chembl_id=activity_chembl_id)
    return list(activity_supp_data)

@mcp.tool()
async def example_assay(assay_type: str) -> List[Dict[str, Any]]:
    client = new_client
    assays = client.assay.filter(assay_type=assay_type)
    return list(assays)

@mcp.tool()
async def example_assay_class(assay_class_type: str) -> List[Dict[str, Any]]:
    client = new_client
    assay_classes = client.assay_class.filter(assay_class_type=assay_class_type)
    return list(assay_classes)

@mcp.tool()
async def example_atc_class(level1: str) -> List[Dict[str, Any]]:
    client = new_client
    atc_classes = client.atc_class.filter(level1=level1)
    return list(atc_classes)

@mcp.tool()
async def example_binding_site(site_name: str) -> List[Dict[str, Any]]:
    client = new_client
    binding_sites = client.binding_site.filter(site_name=site_name)
    return list(binding_sites)

@mcp.tool()
async def example_biotherapeutic(biotherapeutic_type: str) -> List[Dict[str, Any]]:
    client = new_client
    biotherapeutics = client.biotherapeutic.filter(biotherapeutic_type=biotherapeutic_type)
    return list(biotherapeutics)

@mcp.tool()
async def example_cell_line(cell_line_name: str) -> List[Dict[str, Any]]:
    client = new_client
    cell_lines = client.cell_line.filter(cell_line_name=cell_line_name)
    return list(cell_lines)

@mcp.tool()
async def example_chembl_id_lookup(available_type: str, q: str) -> List[Dict[str, Any]]:
    client = new_client
    chembl_ids = client.chembl_id_lookup.filter(available_type=available_type, q=q)
    return list(chembl_ids)

@mcp.tool()
async def example_chembl_release() -> List[Dict[str, Any]]:
    client = new_client
    chembl_releases = client.chembl_release.all()
    return list(chembl_releases)

@mcp.tool()
async def example_compound_record(compound_name: str) -> List[Dict[str, Any]]:
    client = new_client
    compound_records = client.compound_record.filter(compound_name=compound_name)
    return list(compound_records)

@mcp.tool()
async def example_compound_structural_alert(alert_name: str) -> List[Dict[str, Any]]:
    client = new_client
    structural_alerts = client.compound_structural_alert.filter(alert_name=alert_name)
    return list(structural_alerts)

@mcp.tool()
async def example_description(description_type: str) -> List[Dict[str, Any]]:
    client = new_client
    descriptions = client.description.filter(description_type=description_type)
    return list(descriptions)

@mcp.tool()
async def example_document(journal: str) -> List[Dict[str, Any]]:
    client = new_client
    documents = client.document.filter(journal=journal)
    return list(documents)

@mcp.tool()
async def example_drug(drug_type: str) -> List[Dict[str, Any]]:
    client = new_client
    drugs = client.drug.filter(drug_type=drug_type)
    return list(drugs)

@mcp.tool()
async def example_drug_indication(mesh_heading: str) -> List[Dict[str, Any]]:
    client = new_client
    drug_indications = client.drug_indication.filter(mesh_heading=mesh_heading)
    return list(drug_indications)

@mcp.tool()
async def example_drug_warning(meddra_term: str) -> List[Dict[str, Any]]:
    client = new_client
    drug_warnings = client.drug_warning.filter(meddra_term=meddra_term)
    return list(drug_warnings)

@mcp.tool()
async def example_go_slim(go_slim_term: str) -> List[Dict[str, Any]]:
    client = new_client
    go_slims = client.go_slim.filter(go_slim_term=go_slim_term)
    return list(go_slims)

@mcp.tool()
async def example_mechanism(mechanism_of_action: str) -> List[Dict[str, Any]]:
    client = new_client
    mechanisms = client.mechanism.filter(mechanism_of_action=mechanism_of_action)
    return list(mechanisms)

@mcp.tool()
async def example_molecule(molecule_type: str) -> List[Dict[str, Any]]:
    client = new_client
    molecules = client.molecule.filter(molecule_type=molecule_type)
    return list(molecules)

@mcp.tool()
async def example_molecule_form(form_description: str) -> List[Dict[str, Any]]:
    client = new_client
    molecule_forms = client.molecule_form.filter(form_description=form_description)
    return list(molecule_forms)

@mcp.tool()
async def example_organism(tax_id: int) -> List[Dict[str, Any]]:
    client = new_client
    organisms = client.organism.filter(tax_id=tax_id)
    return list(organisms)

@mcp.tool()
async def example_protein_classification(protein_class_name: str) -> List[Dict[str, Any]]:
    client = new_client
    protein_classifications = client.protein_classification.filter(protein_class_name=protein_class_name)
    return list(protein_classifications)

@mcp.tool()
async def example_source(source_description: str) -> List[Dict[str, Any]]:
    client = new_client
    sources = client.source.filter(source_description=source_description)
    return list(sources)

@mcp.tool()
async def example_target(target_type: str) -> List[Dict[str, Any]]:
    client = new_client
    targets = client.target.filter(target_type=target_type)
    return list(targets)

@mcp.tool()
async def example_target_component(component_type: str) -> List[Dict[str, Any]]:
    client = new_client
    target_components = client.target_component.filter(component_type=component_type)
    return list(target_components)

@mcp.tool()
async def example_target_relation(relationship_type: str) -> List[Dict[str, Any]]:
    client = new_client
    target_relations = client.target_relation.filter(relationship_type=relationship_type)
    return list(target_relations)

@mcp.tool()
async def example_tissue(tissue_name: str) -> List[Dict[str, Any]]:
    client = new_client
    tissues = client.tissue.filter(tissue_name=tissue_name)
    return list(tissues)

@mcp.tool()
async def example_xref_source(xref_name: str) -> List[Dict[str, Any]]:
    client = new_client
    xref_sources = client.xref_source.filter(xref_name=xref_name)
    return list(xref_sources)

@mcp.tool()
async def example_canonicalizeSmiles(smiles: str) -> str:
    canonical_smiles = utils.canonicalizeSmiles(smiles)
    return canonical_smiles

@mcp.tool()
async def example_chemblDescriptors(smiles: str) -> Dict[str, Any]:
    descriptors = utils.chemblDescriptors(smiles)
    return descriptors

@mcp.tool()
async def example_description_utils(chembl_id: str) -> str:
    description = utils.description(chembl_id)
    return description

@mcp.tool()
async def example_descriptors(smiles: str) -> Dict[str, Any]:
    descriptors = utils.descriptors(smiles)
    return descriptors

@mcp.tool()
async def example_getParent(chembl_id: str) -> str:
    parent = utils.getParent(chembl_id)
    return parent

@mcp.tool()
async def example_highlightSmilesFragmentSvg(smiles: str, fragment: str) -> str:
    highlighted_svg = utils.highlightSmilesFragmentSvg(smiles, fragment)
    return highlighted_svg

@mcp.tool()
async def example_inchi2inchiKey(inchi: str) -> str:
    inchi_key = utils.inchi2inchiKey(inchi)
    return inchi_key

@mcp.tool()
async def example_inchi2svg(inchi: str) -> str:
    inchi_svg = utils.inchi2svg(inchi)
    return inchi_svg
    # print("InChI SVG:", inchi_svg)  # Skipping printing SVG

@mcp.tool()
async def example_is3D(smiles: str) -> bool:
    is_3d = utils.is3D(smiles)
    return is_3d

@mcp.tool()
async def example_official_utils(chembl_id: str) -> str:
    official = utils.official(chembl_id)
    return official

@mcp.tool()
async def example_removeHs(smiles: str) -> str:
    smiles_no_h = utils.removeHs(smiles)
    return smiles_no_h

@mcp.tool()
async def example_smiles2inchi(smiles: str) -> str:
    smiles_inchi = utils.smiles2inchi(smiles)
    return smiles_inchi

@mcp.tool()
async def example_smiles2inchiKey(smiles: str) -> str:
    smiles_inchi_key = utils.smiles2inchiKey(smiles)
    return smiles_inchi_key

@mcp.tool()
async def example_smiles2svg(smiles: str) -> str:
    smiles_svg = utils.smiles2svg(smiles)
    return smiles_svg
    # print("SMILES SVG:", smiles_svg)  # Skipping printing SVG

@mcp.tool()
async def example_standardize(smiles: str) -> str:
    standardized_smiles = utils.standardize(smiles)
    return standardized_smiles

@mcp.tool()
async def example_status() -> Dict[str, Any]:
    status = utils.status()
    return status

@mcp.tool()
async def example_structuralAlerts(smiles: str) -> List[Dict[str, Any]]:
    alerts = utils.structuralAlerts(smiles)
    return alerts

if __name__ == "__main__":
    logging.info("Starting chembl MCP server")
    # Initialize and run the server
    mcp.run(transport='stdio')
