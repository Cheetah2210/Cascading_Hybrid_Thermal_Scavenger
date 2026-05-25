from variables.GEN_III_node_amplifiers import CHTSController

def test_four_stage_balance():
    # 0.185 + 0.140 + 0.071 + 0.05 = 0.446
    controller = CHTSController()
    result = controller.compute_cascaded_output(100.0)
    assert abs(result["total_output"] - 44.6) < 0.001
    assert "ads" in result["outputs"]
