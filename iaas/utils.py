import consts
from ..utils import state_section

def is_azure(global_state):
    iaas_state = state_section(global_state, consts.section_name)
    return iaas_state[consts.IaaS] == consts.Azure

def is_aws(global_state):
    iaas_state = state_section(global_state, consts.section_name)
    return iaas_state[consts.IaaS] == consts.AWS

def is_gcp(global_state):
    iaas_state = state_section(global_state, consts.section_name)
    return iaas_state[consts.IaaS] == consts.GCP