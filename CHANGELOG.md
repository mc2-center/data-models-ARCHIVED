# Changelog

All notable changes to the CCKP data models will be documented in this file.

The format is based on [Keep a Changelog] and will adhere to [Semantic Versioning].

## [Unreleased]

Track upcoming/planned changes to the data models.
- ...

## [2.1.3](https://github.com/mc2-center/data-models/releases/tag/v2.1.3) - 2022-12-09

### Added
- "Antinomony" as a valid value for Tool Input/Output Format attributes.
- "Training Material" as valid value for Tool Input/Output Data attributes.
- "RDS' as valid value for Tool Input/Output Format attributes
- "Allograft" as Publication/Dataset Assay valid value
- "Isothermal Titration Calorimetry" as valid value for Publication/Dataset Assay attributes
- "Fruit Fly" to Dataset Species attribute

### Removed
- "Dataset Theme Name" and "Publication Theme Name" attributes from the Dataset and Publication components, respectively.
- Dataset, Publication, Tool, and Project "Consortium Name" attributes from their corresponding components.
- "Theme" and "Consortium" from DependsOnComponents and DependsOn for Datasets, Publications, Tools, and Projects
- Duplicated "SRA" value from dataset file formats

## [2.1.2](https://github.com/mc2-center/data-models/releases/tag/v2.1.2) - 2022-11-21

### Added
- "HDF" as valid value for Tool Input/Outpuf Format
- Grants: CA274494, CA267170, CA263001, CA264611, CA271273, CA275808, CA274492, CA274499, CA274502, CA274509 as valid values for Grant Number attributes in the "View" components.
- "Auburn University" as valid value for Grant Institution Name and "AU" as valid value for Grant Institution Alias
- "Oncogenic Stress" as theme name to "View" attribute valid values
- "Publication Abstract" as a required attribute for the Publicatoin and PublicationView components
- "Project Investigator" as an attribute for Project and Project View components.
- "Publication Accessibility" attribute with valid values of "Open Access" and "Restricted Access"
- "Sequence Composition Calculation" as valid value for Tool Operation
- "Sequence Features" as valid value for Tool Input/Output Data attributes
- "Metagenomics" as tool Topic valid value
- "Tissue Microarray" as valid value for Publication/Dataset Tissue
- "Clear Cell Renal Cell Carcinoma" as valid value for Publication/Datastet TumorType
- "Peritoneum" as valid value for Publication/Dataset Tissue attribute.

### Changed
- Capitlization of "Thyroid gland" to "Thyroid Gland" for publication/dataset tissue attributes. 

### Removed
- "Project Theme Name" from Project View component.
- "Colorectal Adenoma" from Publication/Dataset Assay and add as valid value for Publication/Dataset TumorType

### Fixed
- Valid values for attributes that use the same Grant Number values, File Format values, and Assay values so they match.

## [2.1.1](https://github.com/mc2-center/data-models/releases/tag/v2.1.1) - 2022-09-29

### Added
- "Tumor Progression" to list of valid values for Tool language attribute.
- "Nextflow" and "OpenEdge ABL" as valid values for Tool Language attribute
- "Mesenchyme" and "Sinonasal Tract" as valid values for "Publication Tissue" and "Dataset Tissue" attributes
- "In Vitro Translation" as assay valid value for Publication/Dataset Assay attributes
- "Proteomics" and "NPJ Regen Med" as Publication Journal Valid Values
- "LSM" as valid value for Tool Input/Output Format
- "CA224012" as Grant Number for View componenet valid value
- "Not Applicable" as valid values for Tool Input/Output Data
- "HDF", "JSON", "GCTx", "RTF", "GCT" and "HDF5" as valid values for File Format attribute
- "Modeling" as valid value for Publication/Dataset Assay attributes.
- "Atypical Teratoid/Rhabdoid Tumor" to tumor type valid value attributes 
- "Dataset File Formats" attribute with list of valid values (the same as File Format valid values).
- "Castration-Resistant Prostate Carcinoma" and "Primary Central Nervous System Lymphoma" as valid values for Publication/Dataset Tumor Type attributes
- "Lymph" as valid value for Publication/Dataset Tissue attributes.
- "Multiplexed Immunohistochemistry" as valid value for Publication/Dataset Assay.
- "Multiplexed Immunofluorescence", "3D Bioprinting" as valid values for Publication/Dataset Assay
- "De Novo Sequencing" as valid value for Tool Operation
- "Sequence Image" as valid value for Tool Input/Output Data attributes. 
- "FCS" as valid value for Dataset File Formats attribute
- "Nasopharyngeal Carcinoma" and "Retinoblastoma" as valid values for Dataset/Publication Tumor Type
- "Sinonasal Squamous Cell Carcinoma" as Dataset/Publication Tumor Type valid value
- url validation rule for url/homepage/website attributes
- int validation rule for Pubmed Id attributes.
- Unique validatrion rule of aliases and id attributes
- Regex validation rule for Grant Number and Orcid Id attributes
- Update View component Grant Number valid values with latest grant numbers

### Changed
- All "list" validation rules to "list like" because can have 0 or more values.

### Removed
- "Platform Development" duplicated valid value from Project Theme Name, Grant Theme Name, Dataset Theme Name, and Publication Theme Name
- Leading white space from "Adrenal Gland" valid value for Publication/Dataset Tissue attributes.
- Valid values from Publication Journal attribute. 

### Fixed
- Type in File Format valid values "SRA,TXT" to SRA, TXT - add in a white space

## [2.1.0](https://github.com/mc2-center/data-models/releases/tag/v2.1.0) - 2022-08-11

### Added
- "Project View" componenent that includes project attributes.
- Cancer Metab, Proc IEEE Int Conf Comput Vis, FASEB J, J Assist Reprod Genet, Phys Rev Res, Hematol Oncol, Cancer Biol Ther, IEEE/ACM Trans Comput Biol Bioinform, Molecules, Biostatistics, Eur Biophys J, Exp Hematol as Publication Journal Valid Values
- "Dataset Url" attribute and add to DependsOn for Dataset comonent and Dataset View component.
- "Data Index" as valid value for Tool Input/Output Data attributes
- "Chemical Data Format" as valid value for Tool Input/Output format attributes
- Comparative Genomics" as valid value for Tool Topic
- "Platform Development", "Immunotherapy", "Computational Model Development", "Experimental Model Development", "Method/Assay Development", "Platform Development", and "Mechano-resistance" as valid values for Publication View, Dataset View, Grant View, and Project View
- "University of Arizona" as valid value for Grant Instituion Name and "UA" as valid value for Grant Institution Alias
- "University of Chicago" as value value for Grant Instituion Name and "UChicago" as valid value for Grant Instituion Alias
- "University of Illinois" as valid value for Grant Institution Name and Grant Instituion Alias
- "University of Miami" and "U Miami" as valid values for Grant Instituion Name and Grant Instituion Alias, respectively.
- "University of New South Wales" and "UNSW" as valid values for Grant Instituion Name and Grant Instituion Alias, respectively.
- "CCBIR", "MetNet", "PDMC" as valid values to Tool Consortium Name, Publication Consortium Name, Dataset Consortium Name, Grant Consortium Name, and Project Consortium Name
- "University of Texas Southwestern Medical Center" as valid value for Grant Institution Name and "UT Southwestern" as valid value for Grant Institution Alias
- "Rockefeller University" as valid value for Grant Institution Name and Grant Instituion Alias
- "Cold Spring Harbor Laboratory" and Jackson Laboratory as valid values for Grant Institution Name and "CSHL" and "Jackson Laboratory" as valid values for Grant Instituion Alias
- "Lurie Children's Hospital" as valid value for Grant Institiion Name and Grant Insitution Alias
- "University of Alabama at Birmingham" as valid value for Grant Institution Alias and "UAB" as Grant Instition Alias valid value
- "University of Texas MD Anderson Cancer Center" as valid values for Grant Instituion Name and Grant Instituion Alias

### Changed
- Specify which components joined tables (e.g. Tool Grant dependsOn Tool and Grant) depend on in DependsOn column.

### Removed
- "Tool Id" attribute and remove from DependsOn for Tool Component, Tool Grant component, and Tool View Component
- "Tool Grant Id" attribute and remove from DependsOn for Tool Grant Component and update description to specify that Tool Grant table joins the tool and grant tables based on their uuids.
- "Publication Id" attribute and remove from DependsOn for Publication component, Publication Grant component, and Publication View component 
- "Publication Grant Id" attribute and remove from DependsOn for Publication Grant component and update description to specify that Publication Grant table joins the publication and grant tables based on their uuids.
- "Dataset Id" attribute and remove from DependsOn for Dataset component, Dataset Grant component, and Dataset View component.
-  "Dataset Grant Id" attribute and remove from DependsOn for Dataset Grant component and update description to specify that Dataset Grant table joins the dataset and grant tables based on their uuids.
- "Consortium Id" attribute and remove from DependsOn for Consortium component, Consortium Grant Component, and Person Consortium component
- "Consortium Grant Id" attribute and remove from DependsOn for Consoritum Grant component and update description to specify that Consortium Grant table joins the consortium and grant tables based on their uuids.
- "Grant Id" attribute and remove from DependsOn for cooresponding components.
- "Project Id" attribute and remove from DependsOn for Project component.
- "Person Id" attribute and remove from DependsOn for Person component, Person View component, and Person Consortium Component.
- "Person Consoritum" attribute and remove from Depends On for Person Consortium table and update description to specify that Person Consortium table joins the Person and Consortium tables based on their uuids.
- "Theme Id" attribute and remove from DependsOn for Theme componenet and Theme Grant Component.
- "Theme Grant Id" attribute and remove from Depends On for Theme Grant table and update description to specify that Theme Grant table joins the Theme and Grant tables based on their uuids.
- "Institution Id" attribute and remove from DependsOn for Instituion componenet and Institution Grant Component.
- "Institution Grant" attribute and remove from Depends On for Instituion Grant table and update description to specify that Instituion Grant table joins the Institution and Grant tables based on their uuids.
- "File Id" attribute and remove from DependsOn for File componenet, File View component, and File Grant component.
- "File Grant" attribute and remove from Depends On for File Grant table and update description to specify that File Grant table joins the File and Grant tables based on their uuids.
- "Publication Tool Name" from Publication View component. 
- "Tool Dataset Alias" from Tool View component. 
- "Dataset External Link" attribute.

### Fixed

## [2.0.1](https://github.com/mc2-center/data-models/releases/tag/v2.0.1) - 2022-07-01

### Added
- "NCI Clinical and Translational Exploratory/Developmental Studies" as a valid value for Consortium Name attributes.
- "Mechano-genetics" as a Theme Name valid value.
- "University of Texas at Austin" to Grant Institution Name and "UT Austin" to Grant Institution Alias
- "Stony Brook University" to Grant Institiuoin Name and "SBU" to Grant Institution Alias.
- "St. Jude Children's Research Hospital" to Grant Instituion Name and StJude to Grant Institution Alias
- CA260432 as a Grant Number valid value for View componenets

### Changed
- "New York University School of Medicine" to "New York University"
- "City Of Hope National Medical Center" to "City of Hope"
- "Not Associated" as a valid valued for Grant Number attributes to "Affiliated/Non-Grant Associated"
- Dataset Pubmed Id Required to TRUE

## [2.0.0](https://github.com/mc2-center/data-models/releases/tag/v2.0.0) - 2022-06-28

### Added
- Data input/output format, publication assay, dataset assay, publication tumor type, dataset tumor type, publication tissue, dataset species valid values with newly added cv terms. 
- Grant Number valid values for Publication View Grant Number, Person View Grant Number, Dataset View Grant Number, File View Grant Number, and Tool View Grant Number to account for all CSBC PS-ON grants.
- Files Component and attributes File Name, File Url, and File Format to allow for a files component in data model.
- File Grant Component and File Grant Id attribute to account for many-to-many relationship between files and grants.
- File View Component and File Grant Number attribute along with valid values and DependsOn attributes to create a user friendly single manifest for file metadata submission.
- Dataset Tissue attribute to Dataset component and Dataset View component. Since removing tissue from the files schema, it is necessary to include at dataset level since tumor type information is collected at the dataset level.
- "R21" as valid value for Grant Type attribute. 
- "Not Associated" to the valid values for View Grant Number attributes.
- "Protein-Protein Interactions" as valid value for working group participation attribute.
- "HTAN" as valid value for View Consortium Name attributes to capture cross network folks.
- List as validation rule for Dataset Assay, Dataset Species, Dataset tumorType, and Dataset Tissue to allow for multiple values.
- "Multiple values permitted, comma separated" to descriptions of all attributes with list as a validation rule to be clear about attribute cardinality. 
- Grant View component with corresponding Grant related attributes to make data model and manifests consistent until normalized tables are implemented.
- Add File Id as an attribute to allow for a unique identifier for the file component.
- Grant Investigator attribute to Grant View component.

### Changed
- Tool Operation valid values to reflect the cut down EDAM terminology.
- Tool Topic Valid Values to reflect the cut down EDAM terminology.
- Tool Input Data and Tool Output Data valid values to reflect the cut down EDAM terminology.
- Tool Input Format and Tool Output Format valid values to reflect the cut down EDAM terminology.
- File Format valid values to reflect the cut down terminology.
- "synapse entity id" in description of all ids to "unique identifier" and changed Required to FALSE for all since unique identifiers will replace dummy files in Synapse.
- Dataset External Link Required to False and update description to clarify that it will be autogenerated to clarify that collaborators do not need to fill out this attribute.

### Removed
- Name from valid value for Tool Input Data and Tool Output Data attributes because "Name" is an attribute name for the Person component, it cannot be used as a valid value for other attribues. This causes "Name" to be added as an attribute for the Tool and ToolView manifest since Tool Input Data and Tool Output Data (where "Name" is a valid value) dependsOn Tool.

### Fixed
- Typo in Grant Id description.

## [1.0.0] - 2022-05-09

### Added 
- Initial pages for the repo, including .gitignore, README, CHANGELOG
- Person Consortium Component, and Person Consortium Id, DependsOn Component Person and Consortium to account for many to many relationship between person and consortium.
- Consortium Grant component, Consortium Grant Id attribute, DependsOn Component Consortium and Grant to account for many to many relationship between consortium and grant.
- Publication Grant component, Publication Grant Id attribute, DependsOn Component Publiation and Grant to account for many to many relationship between publication and grant.
- Dataset Grant component, Dataset Grant Id attritube, DependsOn Component Dataset, Grant to account for many to many relationship between datasets and grant. 
- Tool Grant Component, Tool Grant Id attribute, and DependsOn Component Tool and Grant because in theory, many to many relationship between tools and grants. 
- Foreign key attributes to DependsOn columns for associative tables because these were not added when created.
- R01 and R37 Grant Type valid values. Were not initially included, but need to be.
- Portal Display to DependsOn for Person because it was missed in the DependsOn, so it was not showing up in the manifest. 
- Journal valid values for Publication component because we use shortened terms for the journal: to make consistent for portal searching.
- Insitution Location City and Institution Location State to DependsOn for Institution. Was missed and not showing up in the manifest.
- Tool View, Publication View, Dataset View, and Person view components and associated attributes to create denormalized and user friendly manifest for investigator submission.
- Publication Tool Name to Publication View Component to be able to associate tools with publications. 
- Example to Consortium Full Name attribute's description to be clear about what kinds of values we are looking for. 
- Information about Synapse Profile Id and where to find identifier in attribute description since it is not straightforward where to find Synapse Profile Id.
- Examples to description of Theme Name and Theme Display Name to be clear about what the difference is between the two attributes. 
- Examples to description of Institution Name and Institution Full Name attributes to be clear about what the difference is between the two attributes. 
- DependsOn Components for Views to show which components that views depend on. 
- Publication Dataset Alias and Publication Tool Name to the Publication View component to allow for a list of datasets and tools to be submitted along with a publication. 
- Tool Pubmed Id and Tool Dataset Alias to Tool View component to allow for a list of datasets to be submitted along with a tool. And to clarify in the description of the Tool Pubmed Id that it is the publication that references the development of the tool. 
- Dataset Pubmed Id as an attribute to the Dataset View component to clarify in the descripton of Dataset Pubmed Id to submit the publication associated with the development of the dataset. 
- Person Publications, Person Datasets, and Person Tools to the Person View Component to allow for lists of associated publications, datasets, and tools to be submitted with a person manifest. 
- New terms to valid values for Publication/Dataset Assay Tool Input/Output Format, Dataset/Publication Tumor Type, and Tool Type to update newly added terms from last batch annotation batch (April)
- "list" as validation rule for attributes under the view components (e.g. Publication Grant, Tool Consortium, etc.) to account for more than one.

### Changed
- Valid value for "Text" in data input/output to "Plain Text" because Schematic did not like "Text" because it clashes with a biothings namespace.
- Valid value for "Protein" in format input/output to "A protein" because Schematic did not like "Protein" because it clashes with a biothings namespace.
- Descriptions for various Name, Full Name, and Display name attributes to specify what we mean (e.g. Human readable, machine readable, etc.)
- Valid value for "Cell" in Publication Journal to "Cell (Jounral)" because Schematic did not like "Cell" because it clashes with biothings namespace.

### Removed
- Person Grant Table (Includes Person Grant Id attribute) because of unnecessary circular relationship because Person dependsOn Consoritum and Grant depends On Consortium. Person and Grant can be joined using the Consortium table.
- Consortium from DependsOn Component for Grant because new associative Consortium Grant table component accounts for this relationship.
- Consortium from DependsOn Component for Person because new associative Person Consortium component accounts for this relationship.
- Person Dataset Component because of unnecessary circular relationship because Person can be connected with Datasets through grant.
- Person Publication Component because of unnecessary circular relationshp because Person can be connected with Publication through grant.
- Person Tool Component because of unnecessary circular relationshp because Person can be connected with Tool through grant.
- Valid values for Consortium Id, Consortium Name, Consortium Dispaly Name, Consortium Full Name, Consortium Description because these are not necessary as these need to be free text fields in order to add a new consortium. 
- Valid values for Grant Id, Grant Name, and Grant Number because these were not necessary as these need to be free text fields in order to add a new grant. 
- Valid values for Project Id and Project Name because these were not necessary as these need to be free text fields in order to add a new project. 
- Valid values for Theme Id, Theme Name, Theme Display Name, and Theme Description because these were not necessary as these need to be free text fields in order to add a new theme. 
- Valid values for Institution Name, Institution Full Name, Instituion Alias, Institution Location City, Rorid because if submitting an institution manifest, it will be a new instititution and, thus, does not need already existing values. 
- Delete various Grant Name attributes for View components because we will be using Grant Number as key for the views. Grant Name is unecessary.

### Fixed
- Valid values for Publication Assay, Publication Tumor Type, and Publication Tissue. Values were missing or mismatched.

[Keep a Changelog]: https://keepachangelog.com/en/1.0.0/
[Semantic Versioning]: https://semver.org/
[Unreleased]: https://github.com/olivierlacan/keep-a-changelog/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/mc2-center/data-models/releases/tag/v1.0.0
