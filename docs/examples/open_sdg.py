"""
This is an example of converting CSV data and YAML metadata into the JSON output
suitable for the Open SDG reporting platform.
"""

import os
import sdg

# Input data from CSV files matching this pattern: tests/data/*-*.csv
data_pattern = os.path.join('tests', 'data', '*-*.csv')
data_input = sdg.inputs.InputCsvData(path_pattern=data_pattern)

# Input metadata from YAML files matching this pattern: tests/meta/*-*.md
meta_pattern = os.path.join('tests', 'meta', '*-*.md')
meta_input = sdg.inputs.InputYamlMdMeta(path_pattern=meta_pattern)

# Combine these inputs into one list.
inputs = [data_input, meta_input]

# Use a Prose.io file for the metadata schema.
schema_path = os.path.join('tests', '_prose.yml')
schema = sdg.schemas.SchemaInputOpenSdg(schema_path=schema_path)

# Validate the metadata. (This could also be done in a separate script.)
validator = sdg.Validator(inputs=inputs, schema=schema)
validation_successful = validator.execute()

# Abort if validation failed.
if not validation_successful:
    raise Exception('Aborting build because validation failed.')

# Create an "output" from these inputs and schema, for JSON for Open SDG.
opensdg_output = sdg.outputs.OutputOpenSdg(inputs, schema, output_folder='_site')

# Finally, perform the build.
opensdg_output.execute()
