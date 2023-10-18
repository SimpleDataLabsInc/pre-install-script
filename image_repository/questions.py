import image_repository.consts as consts
import questionary
from  utils import state_or_defaults, update_and_persist, state_section

def AskImageRegistryQuestions(global_state):
    reg_state = state_section(global_state, consts.section_name)
    questions = [
        {
            'type': 'print',
            'message': consts.ImageRegistryText
        },
        {
            'type': 'confirm',
            'name': consts.IsPrivateImageRegistry,
            'message': consts.IsPrivateImageRegistryPromt
        },
        {
            'type': 'text',
            'name': consts.PrivateImageRegistry,
            'message': consts.PrivateImageRegistryPromt,
            'when': lambda st: st[consts.IsPrivateImageRegistry]
        },
        {
            'type': 'text',
            'name': consts.PrivateImageRegistrySecret,
            'message': consts.PrivateImageRegistrySecretPromt,
            'when': lambda st: st[consts.IsPrivateImageRegistry]
        }
    ]
    questions = state_or_defaults(reg_state, [], questions)
    r = questionary.unsafe_prompt(questions)
    update_and_persist(global_state, consts.section_name, r)

def GetFlagsFromResponse(global_state):
    flags = ""
    reg_state = state_section(global_state, consts.section_name)
    if reg_state[consts.IsPrivateImageRegistry]:
        flags = flags + " " + "--set global.prophecy.imagePullSecret=" + reg_state[consts.PrivateImageRegistrySecret]
        flags = flags + " " + "--set global.repository=" + reg_state[consts.PrivateImageRegistry]
    return flags
