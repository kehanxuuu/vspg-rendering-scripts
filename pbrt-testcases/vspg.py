test_case_description = {
    "title" : "VSPG tests in PBRT",
    "short" : "Generate the transmittance buffer and compare between multiple VSPG algrithms.",
    "long" : "This test generates the transmittance buffer first for later use in NDS+, then runs multiple VSPG algrithms for comparison"
}

common_parameters = {
    "integrator": "guidedvolpathvspg",
    "maxdepth" : ["integer", 15],
    "minrrdepth" : ["integer", 15],
    "usenee" : ["bool", True],
    "surfaceguiding" : ["bool", False],
    "volumeguiding" : ["bool", False],
}

test_cases = {
    "tr_buffer_generation" : {
        "parameters" : {
            "surfaceguiding" : ["bool", True],
            "volumeguiding" : ["bool", True],
            "vspsamplingmethod" : ["string", "resampling"],
            "storeTrBuffer" : ["bool", True],
            "trBufferFileName" : ["string", "$SCENE$-stored-tr-buffer.exr"],
        },
        "description" : "generate transmittance buffer to use for NDS+",
    },
    
    "delta_tracking" : {
        "parameters" : {
            "surfaceguiding" : ["bool", False],
            "volumeguiding" : ["bool", False],
        },
        "description" : "delta tracking",
    },
    
    "directional_guiding" : {
        "parameters" : {
            "surfaceguiding" : ["bool", True],
            "volumeguiding" : ["bool", True],
        },
        "description" : "directional guiding for surface and volume",
    },
    
    "VSPG_NDS_variance" : {
        "parameters" : {
            "surfaceguiding" : ["bool", True],
            "volumeguiding" : ["bool", True],
            "vspguiding" : ["bool", True],
            "vspsamplingmethod" : ["string", "nds"],
            "collisionProbabilityBias" : ["bool", False],
            "vspmisratio" : ["float", 0.75],
            "vspcriterion" : ["string", "variance"],
            # "storeISGBuffer" : ["bool", True],
            # "isgBufferFileName" : ["string", "$SCENE$-buffer-VSPG_NDS_variance.exr"],
        },
        "description" : "volume scattering probability guiding with normalized distance sampling, variance-based criterion",
    },
    
    "VSPG_NDS+_variance" : {
        "parameters" : {
            "surfaceguiding" : ["bool", True],
            "volumeguiding" : ["bool", True],
            "vspguiding" : ["bool", True],
            "vspsamplingmethod" : ["string", "nds"],
            "collisionProbabilityBias" : ["bool", True],
            "vspmisratio" : ["float", 0.75],
            "vspcriterion" : ["string", "variance"],
            "loadTrBuffer" : ["bool", True],
            "trBufferFileName" : ["string", "$SCENE$-stored-tr-buffer.exr"],
            # "storeISGBuffer" : ["bool", True],
            # "isgBufferFileName" : ["string", "$SCENE$-buffer-VSPG_NDS+_variance.exr"],
        },
        "description" : "volume scattering probability guiding with improved version of normalized distance sampling, variance-based criterion",
    },
    
    "vspg_resampling_contrib" : {
        "parameters" : {
            "surfaceguiding" : ["bool", True],
            "volumeguiding" : ["bool", True],
            "vspguiding" : ["bool", True],
            "vspsamplingmethod" : ["string", "resampling"],
            "vspmisratio" : ["float", 0.75],
            "vspcriterion" : ["string", "contribution"],
            "vspmisratio" : ["float", 0.75],
            # "storeISGBuffer" : ["bool", True],
            # "isgBufferFileName" : ["string", "$SCENE$-buffer-vspg_resampling_contrib.exr"],
        },
        "description" : "volume scattering probability guiding with the resampling method for distance sampling, contribution-based criterion",
    },
    
    "vspg_resampling_variance" : {
        "parameters" : {
            "surfaceguiding" : ["bool", True],
            "volumeguiding" : ["bool", True],
            "vspguiding" : ["bool", True],
            "vspsamplingmethod" : ["string", "resampling"],
            "vspmisratio" : ["float", 0.75],
            "vspcriterion" : ["string", "variance"],
            "vspmisratio" : ["float", 0.75],
            # "storeISGBuffer" : ["bool", True],
            # "isgBufferFileName" : ["string", "$SCENE$-buffer-vspg_resampling_variance.exr"],
        },
        "description" : "volume scattering probability guiding with the resampling method for distance sampling, variance-based criterion",
    }

}
