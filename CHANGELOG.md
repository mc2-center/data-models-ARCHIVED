# Changelog

All notable changes to the CCKP data models will be documented in this file.

The format is based on [Keep a Changelog] and will adhere to [Semantic Versioning].

## [Unreleased]

Track upcoming/planned changes to the data models.
- ...

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

## [2.0.0] - 2022-06-28

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

[Keep a Changelog]: https://keepachangelog.com/en/1.0.0/
[Semantic Versioning]: https://semver.org/
[Unreleased]: https://github.com/olivierlacan/keep-a-changelog/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/mc2-center/data-models/releases/tag/v1.0.0
