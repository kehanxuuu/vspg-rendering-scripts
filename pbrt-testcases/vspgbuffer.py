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
    "vspg_buffer" : {
        "parameters" : {
            "surfaceguiding" : ["bool", True],
            "volumeguiding" : ["bool", True],
            "storeVSPBuffer" : ["bool", True],
            "vspBufferFileName" : ["string", "$SCENE$-vspg_buffer-vspg-buffer.exr"],
        },
        "description" : "VSPG buffer calculation",
    },
    "vspg_guiding" : {
        "parameters" : {
            "surfaceguiding" : ["bool", True],
            "volumeguiding" : ["bool", True],
            "vspprimaryguiding" : ["bool", True],
            "vspsecondaryguiding" : ["bool", True],
            "vspresampling" : ["bool", True],
            "storeVSPBuffer" : ["bool", True],
            "vspBufferFileName" : ["string", "$SCENE$-vspg_guiding-vspg-buffer.exr"],
        },
        "description" : "VSPG buffer calculation",
    }
}
