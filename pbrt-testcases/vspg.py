test_case_description = {
    "paper" : "Volume Scattering Probability Guiding",
    "title" : "Evaluation of Volume Scattering Probability Guiding (VSPG).",
    "short" : "Evalaution of our Volume Scattering Probability Guiding (VSPG) framework and our VSP-driven distance sampling algorithm.",
    "long" : "The results show the outcomes for different volume rendering algorithms without (e.g., No Guiding and Dir. Guiding) \
                and with using our volume scattering probability guiding (VSPG) framework (e.g., Dir. + VSPG ...), as well as, multiple distance sampling stategies to guided the VSP (e.g., NDS, NDS+, Resampling).\
                For these rendering the maximum path length is set to 15 and stochastic path termination via Russian roulette is disabled.",
}

common_parameters = {
    "integrator": "guidedvolpathvspg",
    "maxdepth" : ["integer", 15],
    "minrrdepth" : ["integer", 15],
    "usenee" : ["bool", True],
    "surfaceguiding" : ["bool", False],
    "volumeguiding" : ["bool", False],
    "vspguiding" : ["bool", False],
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
        "skipViewer" : True,
        "skipErrorStats" : True,
        "description" : "generate transmittance buffer to use for NDS+",
    },
    
    "delta_tracking" : {
        "parameters" : {
            "surfaceguiding" : ["bool", False],
            "volumeguiding" : ["bool", False],
            "vspguiding" : ["bool", False],
        },
        "label" : "No Guiding",
        "description" : "delta tracking",
    },
    
    "directional_guiding" : {
        "parameters" : {
            "surfaceguiding" : ["bool", True],
            "volumeguiding" : ["bool", True],
            "vspguiding" : ["bool", False],
        },
        "label" : "Dir. Guiding",
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
        "label" : "Dir. + VSPG (NDS) Var.",
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
        "label" : "Dir. + VSPG (NDS+) Var.",
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
            # "storeISGBuffer" : ["bool", True],
            # "isgBufferFileName" : ["string", "$SCENE$-buffer-vspg_resampling_contrib.exr"],
        },
        "label" : "Dir. + VSPG (Resampling) Contrib.",
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
            # "storeISGBuffer" : ["bool", True],
            # "isgBufferFileName" : ["string", "$SCENE$-buffer-vspg_resampling_variance.exr"],
        },
        "label" : "Dir. + VSPG (Resampling) Var.",
        "description" : "volume scattering probability guiding with the resampling method for distance sampling, variance-based criterion",
    }

}
