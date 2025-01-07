test_case_description = {
    "title" : "Guiding tests in PBRT",
    "short" : "Comparing path tracing with and without path guiding using PBRT's guidedvolpath integrator.",
    "long" : "This test compares ."
}

common_parameters = {
    "integrator": "guidedvolpathvspg",
    "maxdepth" : ["integer", 20],
    "minrrdepth" : ["integer", 20],
    "usenee" : ["bool", True],
    "surfaceguiding" : ["bool", False],
    "volumeguiding" : ["bool", False],
}

test_cases = {
    "volume_guiding" : {
        "parameters" : {
            "surfaceguiding" : ["bool", True],
            "volumeguiding" : ["bool", True],
            "storeISGBuffer" : ["bool", False],
            "vspguiding" : ["bool", False],
            "isgBufferFileName" : ["string", "$SCENE$-volume_guiding-vspgb.exr"],
        },
        "description" : "VSPG buffer calculation",
    },
    "vspg_guiding_contrib" : {
        "parameters" : {
            "surfaceguiding" : ["bool", True],
            "volumeguiding" : ["bool", True],
            "vspguiding" : ["bool", True],
            "vspsamplingmethod" : ["string", "Resampling"],
            "vspcriterion" : ["string", "Contribution"],
            "vspmisratio" : ["float", 0.75],
            "storeISGBuffer" : ["bool", True],
            "isgBufferFileName" : ["string", "$SCENE$-vspg_guiding_contrib-vspgb.exr"],
        },
        "description" : "VSPG buffer calculation",
    },
    "vspg_guiding_variance" : {
        "parameters" : {
            "surfaceguiding" : ["bool", True],
            "volumeguiding" : ["bool", True],
            "vspguiding" : ["bool", True],
            "vspsamplingmethod" : ["string", "Resampling"],
            "vspcriterion" : ["string", "Variance"],
            "vspmisratio" : ["float", 0.75],
            "storeISGBuffer" : ["bool", True],
            "isgBufferFileName" : ["string", "$SCENE$-vspg_guiding_variance-vspgb.exr"],
        },
        "description" : "VSPG buffer calculation",
    },
    "vspg_guiding_villemin_contrib" : {
        "parameters" : {
            "surfaceguiding" : ["bool", True],
            "volumeguiding" : ["bool", True],
            "vspguiding" : ["bool", True],
            "vspsamplingmethod" : ["string", "Villemin"],
            "vspcriterion" : ["string", "Contribution"],
            "vspmisratio" : ["float", 0.75],
            "storeISGBuffer" : ["bool", True],
            "isgBufferFileName" : ["string", "$SCENE$-vspg_guiding_villemin_contrib-vspgb.exr"],
        },
        "description" : "VSPG buffer calculation",
    },
    "vspg_guiding_villemin_variance" : {
        "parameters" : {
            "surfaceguiding" : ["bool", True],
            "volumeguiding" : ["bool", True],
            "vspguiding" : ["bool", True],
            "vspsamplingmethod" : ["string", "Villemin"],
            "vspcriterion" : ["string", "Variance"],
            "vspmisratio" : ["float", 0.75],
            "storeISGBuffer" : ["bool", True],
            "isgBufferFileName" : ["string", "$SCENE$-vspg_guiding_villemin_variance-vspgb.exr"],
        },
        "description" : "VSPG buffer calculation",
    }

}
