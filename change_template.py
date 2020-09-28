class Templates():
    master_files = [
        'CER - Rules',
        'VCG - Grouper',
        'HFR - Registry'
    ]

    template = {
        'CER': {
            'title':'Update Rule',
            'ini':['CER'],
            'rsn':'Update criteria/logic of rule',
            'plan':'Update the rule',
            'backout':'Undo the change',
            'test':'Verify rule passes as expected',

            },
        'VCG': {
            'title':'Update Grouper',
            'ini':['VCG'],
            'rsn':'Add/remove records from grouper',
            'plan':'Update the grouper',
            'backout':'Undo the change',
            'test':'Verify grouper has correct records'
        },
        'HFR': {
            'title':'Update Registry',
            'ini':['HFR','VCG','CER'],
            'rsn':'Update registry rules and groupers',
            'plan':'Update the registry inclusion rule and/or metrics',
            'backout':'Undo the change',
            'test':"""Move to SUP.\nVerify configuration.\nProcess registry and/or metrics.\nVerify metric data is correct"""
        }
    }
