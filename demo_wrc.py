#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# ChEMBL webresource client examples

The library helps accessing ChEMBL data and cheminformatics tools from Python. You don't need to know how to write SQL. You don't need to know how to interact with REST APIs. You don't need to compile or install any cheminformatics frameworks. Results are cached.

The client handles interaction with the HTTPS protocol and caches all results in the local file system for faster retrieval. Abstracting away all network-related tasks, the client provides the end user with a convenient interface, giving the impression of working with a local resource. Design is based on the Django QuerySet interface. The client also implements lazy evaluation of results, which means it will only evaluate a request for data when a value is required. This approach reduces number of network requests and increases performance.


# ## Available data entities
# 
# You can list available data entities using the following code

# In[1]:


from chembl_webresource_client.new_client import new_client

available_resources = [resource for resource in dir(new_client) if not resource.startswith('_')]
print(available_resources)


# ## Available filters
# 
# The design of the client is based on Django QuerySet (https://docs.djangoproject.com/en/1.11/ref/models/querysets) and most important lookup types are supported. These are:
# 
# - exact
# - iexact
# - contains
# - icontains
# - in
# - gt
# - gte
# - lt
# - lte
# - startswith
# - istartswith
# - endswith
# - iendswith
# - range
# - isnull
# - regex
# - iregex

# ## Only operator
# 
# `only` is a special method allowing to limit the results to a selected set of fields. only should take a single argument: a list of fields that should be included in result. Specified fields have to exists in the endpoint against which only is executed. Using only will usually make an API call faster because less information returned will save bandwidth. The API logic will also check if any SQL joins are necessary to return the specified field and exclude unnecessary joins with critically improves performance.
# 
# Please note that only has one limitation: a list of fields will ignore nested fields i.e. calling only(['molecule_properties__alogp']) is equivalent to only(['molecule_properties']).
# 
# For many 2 many relationships only will not make any SQL join optimisation.

# # Molecules
# 
# Molecule records may be retrieved in a number of ways, such as lookup of single molecules using various identifiers or searching for compounds via similarity.

# ## Find a molecule by pref_name
# 

# In[2]:


from chembl_webresource_client.new_client import new_client

molecule = new_client.molecule
mols = molecule.filter(pref_name__iexact='aspirin')
mols


# ## Find a molecule by its synonyms
# 
# - in case it is not found by pref_name
# - Use the `only` method where you can specify fields you want to be included in response

# In[3]:


from chembl_webresource_client.new_client import new_client

molecule = new_client.molecule
mols = molecule.filter(molecule_synonyms__molecule_synonym__iexact='viagra').only('molecule_chembl_id')
mols


# ## Get a single molecule by ChEMBL id
# 
# All the main entities in the ChEMBL database have a ChEMBL ID. It is a stable identifier designed for straightforward lookup of data.

# In[4]:


from chembl_webresource_client.new_client import new_client

molecule = new_client.molecule
m1 = molecule.filter(chembl_id='CHEMBL192').only(['molecule_chembl_id', 'pref_name', 'molecule_structures'])
m1


# ## Get many molecules by id

# In[5]:


from chembl_webresource_client.new_client import new_client

molecule = new_client.molecule
mols = molecule.filter(molecule_chembl_id__in=['CHEMBL25', 'CHEMBL192', 'CHEMBL27']).only(['molecule_chembl_id', 'pref_name'])
mols


# ## Display a molecule image

# In[6]:


from chembl_webresource_client.new_client import new_client
from IPython.display import SVG

image = new_client.image
image.set_format('svg')
SVG(image.get('CHEMBL25'))


# ## Get a single molecule by standard inchi key

# In[7]:


from chembl_webresource_client.new_client import new_client

molecule = new_client.molecule
mol = molecule.filter(molecule_structures__standard_inchi_key='BSYNRYMUTXBXSQ-UHFFFAOYSA-N').only(['molecule_chembl_id', 'pref_name', 'molecule_structures'])
mol


# ## Find compounds similar to given SMILES query with similarity threshold of 70%

# In[8]:


from chembl_webresource_client.new_client import new_client

similarity = new_client.similarity
res = similarity.filter(smiles="CO[C@@H](CCC#C\C=C/CCCC(C)CCCCC=C)C(=O)[O-]", similarity=70).only(['molecule_chembl_id', 'similarity'])
for i in res:
    print(i)


# ## Find compounds similar to aspirin (CHEMBL25) with similarity threshold of 70%
# 

# In[9]:


from chembl_webresource_client.new_client import new_client

similarity = new_client.similarity
res = similarity.filter(chembl_id='CHEMBL25', similarity=70).only(['molecule_chembl_id', 'pref_name', 'similarity'])
res


# ## Find compounds with the same connectivity

# In[10]:


from chembl_webresource_client.new_client import new_client

molecule = new_client.molecule
res = molecule.filter(molecule_structures__canonical_smiles__connectivity='CN(C)C(=N)N=C(N)N').only(['molecule_chembl_id', 'pref_name'])
for i in res:
    print(i)


# ## Get all approved drugs
# 
# using `order_by` to sort them by molecular weight

# In[11]:


from chembl_webresource_client.new_client import new_client

molecule = new_client.molecule
approved_drugs = molecule.filter(max_phase=4).order_by('molecule_properties__mw_freebase')
approved_drugs


# ## Get approved drugs for lung cancer

# In[12]:


from chembl_webresource_client.new_client import new_client

drug_indication = new_client.drug_indication
molecules = new_client.molecule

lung_cancer_ind = drug_indication.filter(efo_term__icontains="LUNG CARCINOMA")
lung_cancer_mols = molecules.filter(
    molecule_chembl_id__in=[x['molecule_chembl_id'] for x in lung_cancer_ind])

len(lung_cancer_mols)


# ## Filter drugs by approval year and name

# In[13]:


from chembl_webresource_client.new_client import new_client

drug = new_client.drug
res = drug.filter(first_approval__gte=1980).filter(usan_stem="-azosin")
res


# ## Get all biotherapeutic molecules

# In[14]:


from chembl_webresource_client.new_client import new_client

molecule = new_client.molecule
biotherapeutics = molecule.filter(biotherapeutic__isnull=False)
len(biotherapeutics)


# ## Get molecules with molecular weight <= 300

# In[15]:


from chembl_webresource_client.new_client import new_client

molecule = new_client.molecule
light_molecules = molecule.filter(molecule_properties__mw_freebase__lte=300)

len(light_molecules)


# ## Get molecules with molecular weight <= 300 AND pref_name ending with nib

# In[16]:


from chembl_webresource_client.new_client import new_client

molecule = new_client.molecule
light_nib_molecules = molecule.filter(molecule_properties__mw_freebase__lte=300, pref_name__iendswith="nib").only(['molecule_chembl_id', 'pref_name'])

light_nib_molecules


# ## Get all molecules in ChEMBL with no Rule-of-Five violations

# In[17]:


from chembl_webresource_client.new_client import new_client

molecule = new_client.molecule
no_violations = molecule.filter(molecule_properties__num_ro5_violations=0)
len(no_violations)


# # Activities

# ## Get all IC50 activities related to the hERG target

# In[18]:


from chembl_webresource_client.new_client import new_client

target = new_client.target
activity = new_client.activity
herg = target.filter(pref_name__iexact='hERG').only('target_chembl_id')[0]
herg_activities = activity.filter(target_chembl_id=herg['target_chembl_id']).filter(standard_type="IC50")

len(herg_activities)


# ## Get all activities for a specific target with assay type B (binding):

# In[19]:


from chembl_webresource_client.new_client import new_client

activity = new_client.activity
res = activity.filter(target_chembl_id='CHEMBL3938', assay_type='B')

len(res)


# ## Get all activities with a pChEMBL value for a molecule

# In[20]:


from chembl_webresource_client.new_client import new_client

activities = new_client.activity
res = activities.filter(molecule_chembl_id="CHEMBL25", pchembl_value__isnull=False)

len(res)


# ## Search for ADMET-related inhibitor assays (type A)

# In[21]:


from chembl_webresource_client.new_client import new_client
assay = new_client.assay
res = assay.filter(description__icontains='inhibit', assay_type='A')
res


# # Tissues

# ## Get tissue by BTO ID

# In[22]:


from chembl_webresource_client.new_client import new_client

tissue = new_client.tissue
res = tissue.filter(bto_id="BTO:0001073")
res


# ## Get tissue by Caloha id

# In[23]:


from chembl_webresource_client.new_client import new_client

tissue = new_client.tissue
res = tissue.filter(caloha_id="TS-0490")
res


# ## Get tissue by Uberon id

# In[24]:


from chembl_webresource_client.new_client import new_client

tissue = new_client.tissue
res = tissue.filter(uberon_id="UBERON:0000173")
res


# ## Get tissue by name

# In[25]:


from chembl_webresource_client.new_client import new_client

tissue = new_client.tissue
res = tissue.filter(pref_name__istartswith='blood')
res


# # Cells

# ## Get cell line by cellosaurus id

# In[26]:


from chembl_webresource_client.new_client import new_client

cell_line = new_client.cell_line
res = cell_line.filter(cellosaurus_id="CVCL_0417")
res


# # Targets

# ## Find a target by gene name

# In[27]:


from chembl_webresource_client.new_client import new_client

target = new_client.target
gene_name = 'BRD4'
res = target.filter(target_synonym__icontains=gene_name).only(['organism', 'pref_name', 'target_type'])
for i in res:
    print(i)


# # References

# ## Find all PubMed IDs from a list that exist in the ChEMBL database.

# In[15]:


from chembl_webresource_client.new_client import new_client
ids = (27502541, 27584694, 27977190, 81377812)
pubmed_IDs = new_client.document
pm = pubmed_IDs.filter(pubmed_id__in=ids).only('pubmed_id')
pm


# ## Find all Datasets that were produced after 2021

# In[16]:


datasets = new_client.document
ds = datasets.filter(year__gte=2021, doc_type = 'DATASET')
ds


# # Sources

# ## Get the table of ChEMBL sources

# In[17]:


sources = new_client.source
sources


# # Utils

# ## Convert SMILES to CTAB

# In[28]:


from chembl_webresource_client.utils import utils

aspirin = utils.smiles2ctab('O=C(Oc1ccccc1C(=O)O)C')
aspirin


# ## Compute Maximal Common Substructure

# In[29]:


from chembl_webresource_client.utils import utils

smiles = ["O=C(NCc1cc(OC)c(O)cc1)CCCC/C=C/C(C)C",
          "CC(C)CCCCCC(=O)NCC1=CC(=C(C=C1)O)OC", "c1(C=O)cc(OC)c(O)cc1"]
mols = [utils.smiles2ctab(smile) for smile in smiles]
sdf = ''.join(mols)
result = utils.mcs(sdf)
result


# ## Compute various molecular descriptors

# In[30]:


from chembl_webresource_client.utils import utils
import json

aspirin = utils.smiles2ctab('O=C(Oc1ccccc1C(=O)O)C')
descs = json.loads(utils.chemblDescriptors(aspirin))[0]
descs


# ## Compute structural alerts

# In[31]:


from chembl_webresource_client.utils import utils

mol = utils.smiles2ctab("O=C(Oc1ccccc1C(=O)O)C")
alerts = json.loads(utils.structuralAlerts(mol))
for a in alerts[0]:
    print(a)


# ## Standardize a molecule

# In[32]:


from chembl_webresource_client.utils import utils
mol = utils.smiles2ctab("[Na]OC(=O)Cc1ccc(C[NH3+])cc1.c1nnn[n-]1.O")
st = json.loads(utils.standardize(mol))
st


# ## Calculate the parent molecule

# In[33]:


from chembl_webresource_client.utils import utils

mol = utils.smiles2ctab("[Na]OC(=O)Cc1ccc(C[NH3+])cc1.c1nnn[n-]1.[Na]")
par = json.loads(utils.getParent(mol))
par


# In[ ]:




