# Copyright (c) 2021, Galois, Inc.
#
# All Rights Reserved
#
# This material is based upon work supported by the Defense Advanced Research
# Projects Agency (DARPA) under Contract No. FA8750-20-C-0203.
#
# Any opinions, findings and conclusions or recommendations expressed in this
# material are those of the author(s) and do not necessarily reflect the views
# of the Defense Advanced Research Projects Agency (DARPA).

from migration_helpers.name_space import rack
from ontology_changes import AtMost, ChangeCardinality, Commit, ChangePropertyIsATypeOf, SingleValue

PROV_S = rack("PROV-S")
REQUIREMENTS = rack("REQUIREMENTS")

commit = Commit(
    number="d8271d216704351cf0007a04abac47f4abc993ad",
    changes=[
        # REQUIREMENTS.sadl
        ChangeCardinality(
            name_space=REQUIREMENTS,
            class_id="REQUIREMENT",
            property_id="text",
            to_cardinality=SingleValue(),
        ),
        ChangeCardinality(
            name_space=REQUIREMENTS,
            class_id="REQUIREMENT",
            property_id="givenText",
            to_cardinality=AtMost(1),
        ),
        ChangeCardinality(
            name_space=REQUIREMENTS,
            class_id="REQUIREMENT",
            property_id="ifText",
            to_cardinality=AtMost(1),
        ),
        ChangeCardinality(
            name_space=REQUIREMENTS,
            class_id="REQUIREMENT",
            property_id="thenText",
            to_cardinality=AtMost(1),
        ),
        ChangeCardinality(
            name_space=REQUIREMENTS,
            class_id="DATA_DICTIONARY_TERM",
            property_id="text",
            to_cardinality=AtMost(1),
        ),
        ChangePropertyIsATypeOf(
            name_space=REQUIREMENTS,
            class_id="REQUIREMENT",
            property_id="governs",
            from_name_space=PROV_S,
            from_property_id="wasDerivedFrom",
            to_name_space=PROV_S,
            to_property_id="wasImpactedBy",
        ),
        ChangePropertyIsATypeOf(
            name_space=REQUIREMENTS,
            class_id="REQUIREMENT",
            property_id="satisfies",
            from_name_space=PROV_S,
            from_property_id="wasDerivedFrom",
            to_name_space=PROV_S,
            to_property_id="wasImpactedBy",
        ),
        ChangePropertyIsATypeOf(
            name_space=REQUIREMENTS,
            class_id="REQUIREMENT",
            property_id="mitigates",
            from_name_space=PROV_S,
            from_property_id="wasDerivedFrom",
            to_name_space=PROV_S,
            to_property_id="wasImpactedBy",
        ),
        ChangePropertyIsATypeOf(
            name_space=REQUIREMENTS,
            class_id="DATA_DICTIONARY_TERM",
            property_id="providedBy",
            from_name_space=PROV_S,
            from_property_id="wasDerivedFrom",
            to_name_space=PROV_S,
            to_property_id="wasImpactedBy",
        ),
        ChangePropertyIsATypeOf(
            name_space=REQUIREMENTS,
            class_id="DATA_DICTIONARY_TERM",
            property_id="consumedBy",
            from_name_space=PROV_S,
            from_property_id="wasDerivedFrom",
            to_name_space=PROV_S,
            to_property_id="wasImpactedBy",
        ),
    ],
)
