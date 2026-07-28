from generators.iron_deficiency import generate_iron_deficiency
from generators.leukocytosis import generate_leukocytosis
from generators.leukopenia import generate_leukopenia
from generators.normal import generate_normal
from generators.thrombocytopenia import generate_thrombocytopenia
from generators.viral_infection import generate_viral_infection

GENERATOR_MAP = {

    "Normal": generate_normal,

    "Iron Deficiency": generate_iron_deficiency,

    "Leukocytosis": generate_leukocytosis,

    "Leukopenia": generate_leukopenia,

    "Viral Infection": generate_viral_infection,

    "Thrombocytopenia": generate_thrombocytopenia

}