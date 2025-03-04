import renderer.pbrt.PBRTRenderer as PBRTRenderer
import utils.TestCaseHelper as TestCaseHelper
import utils.SceneHelper as SceneHelper

import utils.ResultsViewer as ResultsViewer

# path to the PBRT installation (e.g., folder or a soft link to it)
pbrt_dir = "./pbrt-renderer/"

# name of the experiment and the folders
experiment_name = 'vspg-equal-spp'

# path to store the results
results_dir = "./pbrt-results/" + experiment_name

# path to store the post-processed results and the HTML viewer
viewer_output_dir = "./pbrt-viewers/"  + experiment_name

# Loading the test case descriptions from a file
testCases = TestCaseHelper.loadTestCases("pbrt-testcases/vspg")
testCaseDescription = TestCaseHelper.loadTestCaseDescription("pbrt-testcases/vspg")

# Loading the scenes to run the test cases (e.g., pbrt-scenes can be a folder or a soft link to it)
[scenes, scenes_dir] = SceneHelper.loadScenes("pbrt-scenes/scenesconfig") 

# Setup the PBRT renderer
pbrt = PBRTRenderer.PBRTRenderer(pbrt_dir, results_dir, scenes_dir)

# equal-spp experiments, the spp for all renderings
spp = 32

#for each scene and each scene variant
for scene, scene_config in scenes:
    resolution = scene_config["resolution"]
    for variant in scene_config["variants"]:
        #run each test case defined in the test cases file
        for testCase in testCases:    
            pbrt.runTestCase(scene, variant, resolution, testCase, budget = spp, equal_spp = True, stats = True, usedGuidedGBuffer = False)
#after running all test cases for all scenes prepare the results in an interactive HTML viewer 
viewer = ResultsViewer.ResultsViewer("./utils/webviewer")
viewer.generateHTMLS(viewer_output_dir, results_dir, scenes_dir, scenes, testCaseDescription, testCases, showReference=True, referenceTag="_ref_depth15", referenceSubFolder="reference", perScene=True, errors=["relMSE","SMAPE"])