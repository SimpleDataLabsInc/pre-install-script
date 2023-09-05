import image_repository.consts as consts
import questionary


def AskImageRegistryQuestions(cloud=None):
    result = {}
    questions = [
        {
            'type': 'confirm',
            'name': consts.IsPrivateImageRegistry,
            'message': consts.IsPrivateImageRegistryPromt
        },
    ]

    print(consts.ImageRegistryText)
    r = questionary.prompt(questions)
    result.update(r)

    if r[consts.IsPrivateImageRegistry]:
        questions = [
            {
                'type': 'text',
                'name': consts.PrivateImageRegistry,
                'message': consts.PrivateImageRegistryPromt
            },
            {
                'type': 'text',
                'name': consts.PrivateImageRegistrySecret,
                'message': consts.PrivateImageRegistrySecretPromt
            }

        ]
        r = questionary.prompt(questions)
        result.update(r)
        return result

    return result

def GetFlagsFromResponse(response):
    flags = ""
    if response[consts.IsPrivateImageRegistry]:
        flags = flags + " " + "--set global.prophecy.imagePullSecret=" + response[consts.PrivateImageRegistrySecret]
        flags = flags + " " + "--set global.repository=" + response[consts.PrivateImageRegistry]
    return flags
